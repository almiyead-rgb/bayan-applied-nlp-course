"""Validate the published learner content, separately from ML/runtime testing.

Usage: python tools/test_portal_content_contract.py _site/index.html \
    --report _site/content-contract.json
This checks the generated site. It does not grade students, verify authorship,
or establish the scientific correctness of model outputs.
"""
from __future__ import annotations

import argparse
import ast
import base64
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_data = False
        self.data_parts: list[str] = []
        self.images: list[str] = []
        self.python_blocks: list[str] = []
        self.code_parts: list[str] | None = None
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag == 'script' and a.get('id') == 'portal-data':
            self.in_data = True
        if tag == 'img' and 'brand-image' in (a.get('class') or '').split():
            self.images.append(a.get('src') or '')
        if tag == 'code' and 'language-python' in (a.get('class') or '').split():
            self.code_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == 'script':
            self.in_data = False
        if tag == 'code' and self.code_parts is not None:
            self.python_blocks.append(''.join(self.code_parts))
            self.code_parts = None

    def handle_data(self, data: str) -> None:
        if self.in_data:
            self.data_parts.append(data)
        if self.code_parts is not None:
            self.code_parts.append(data)
        self.text_parts.append(data)


def check_site(path: Path) -> dict:
    source = path.read_text(encoding='utf-8')
    page = PageParser()
    page.feed(source)
    payload = json.loads(''.join(page.data_parts))
    course = payload['course']
    records = payload['documents']
    docs = {item['path']: item for item in records}
    checks: list[str] = []

    def require(condition: bool, name: str) -> None:
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    rubric = course['rubric']
    totals = {category: sum(row['points'] for row in rubric if row['category'] == category)
              for category in ('administrative', 'technical', 'presentation')}
    require(totals == {'administrative': 20, 'technical': 70, 'presentation': 10}
            and sum(totals.values()) == 100,
            '100_total_including_10_presentation_points')
    require(len({row['id'] for row in rubric}) == len(rubric)
            and all(sum(item['points'] for item in row['items']) == row['points'] for row in rubric),
            'unique_rubric_ids_and_item_totals')

    days = course['days']
    require([day['id'] for day in days] == [1, 2, 3, 4], 'four_ordered_days')
    require(all(len(day['topics']) >= 3 and len(day['architecture']) >= 3
                and all(all(isinstance(topic.get(key), list) and len(topic[key]) == 2
                            and all(isinstance(value, str) and value.strip() for value in topic[key])
                            for key in ('title', 'explanation', 'example')) for topic in day['topics'])
                for day in days), 'bilingual_daily_topics_examples_and_architecture')

    required = {
        'docs/project-walkthrough.md', 'docs/presentation-guide.md',
        'docs/learner-workflow.md', 'docs/pre-submission-checklist.md',
        'docs/policies/assessment-and-completion.md',
        'docs/policies/submission.md', 'docs/policies/integrity-and-privacy.md',
    }
    require(required <= docs.keys(), 'scenario_presentation_workflow_and_policy_guides_present')

    text_docs: dict[str, str] = {}
    parsed_docs: dict[str, PageParser] = {}
    for name, doc in docs.items():
        parsed = PageParser()
        parsed.feed(doc['html'])
        parsed_docs[name] = parsed
        text_docs[name] = ' '.join(parsed.text_parts)
    protected_pages = required | {'README.md', 'COURSE_GUIDE.md', 'docs/04-delivery-plan.md'}
    protected_pages |= {f'day-0{i}/README.md' for i in range(1, 5)}
    old_weights = re.compile(r'\b(?:35|15|40)\s*[%٪]')
    require(not any(old_weights.search(text_docs[name]) for name in protected_pages),
            'no_superseded_assessment_percentages')
    timed_pages = {'docs/04-delivery-plan.md'} | {f'day-0{i}/README.md' for i in range(1, 5)}
    clock = re.compile(r'(?<!\d)(?:0?[1-9]|1\d|2[0-3]):[0-5]\d(?!\d)')
    require(not any(clock.search(text_docs[name]) for name in timed_pages),
            'narrative_days_without_clock_schedules')

    require(len(page.images) == 1 and page.images[0].startswith('data:image/png;base64,'),
            'owner_brand_image_embedded_for_offline_use')
    image = base64.b64decode(page.images[0].split(',', 1)[1], validate=True)
    require(hashlib.sha256(image).hexdigest() ==
            '82323ee87fa0510bd5c01c631716d2e2458b79b49179de227821b016594aa9bf',
            'owner_brand_image_matches_supplied_asset')

    workflow = text_docs['docs/learner-workflow.md']
    require(all(value in workflow for value in
                ('Save a copy in Drive', 'Run all', '.ipynb', 'README.md',
                 'SDAIAAcademy', 'submission-v1.0', 'FINAL_COMMIT_SHA')),
            'beginner_run_export_readme_attribution_and_final_revision_steps')
    blocks = parsed_docs['docs/learner-workflow.md'].python_blocks
    require(len(blocks) >= 3, 'runnable_python_guidance_blocks_present')
    for number, block in enumerate(blocks, 1):
        ast.parse(block, filename=f'learner-workflow-block-{number}')
    checks.append('learner_workflow_python_syntax')

    require('one final assessment' in source.lower()
            and 'no edited replacement' in source.lower()
            and 'similarity percentage alone' in source.lower(),
            'one_shot_policy_with_evidence_based_integrity_notice')
    require('file:///C:' not in source and 'AppData/Local/Temp' not in source,
            'no_machine_specific_student_links')
    return {'result': 'PORTAL_CONTENT_CONTRACT_PASS', 'count': len(checks),
            'checks': checks, 'rubric_totals': totals,
            'scope': 'Learner content and syntax only; no grading, authorship inference or ML rerun.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    report = check_site(args.site)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output + '\n', encoding='utf-8')
    print(output)


if __name__ == '__main__':
    main()
