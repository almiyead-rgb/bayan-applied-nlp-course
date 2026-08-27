from bayan.tokenization import corpus_fertility, token_fertility, truncation_rate


def toy_tokenize(text: str) -> list[str]:
    return text.replace("الخدمة", "ال خدمة").split()


def test_fertility():
    assert token_fertility("الخدمة ممتازة", toy_tokenize) == 1.5
    assert corpus_fertility(["الخدمة ممتازة", "سريع"], toy_tokenize) == 1.25


def test_truncation_rate_reserves_special_tokens():
    texts = ["a b", "a b c d"]
    assert truncation_rate(texts, str.split, max_length=5, special_tokens=2) == 0.5
