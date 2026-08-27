# تقرير تقييم بيان | Bayan Evaluation Report

> انسخ هذا الملف إلى جذر مستودعك باسم `EVALUATION_REPORT.md`، ثم احذف التعليمات بين الأقواس واستبدل كل `TODO` بدليلك الفعلي.

## 1. نطاق التقرير

- تاريخ التشغيل: `TODO`
- commit SHA: `TODO`
- runtime/device: `TODO`
- data version/hash: `TODO`
- preprocessing profile/version/backend: `TODO`
- model/checkpoint IDs: `TODO`
- نوع الأرقام: `MEASURED_SMOKE / MEASURED / COURSE_FIXTURE` — اختر بدقة.

## 2. العقود قبل القياس

| العقد | الدليل | الحالة |
|---|---|---|
| لا PII حقيقية | `TODO` | PASS/PENDING |
| train/validation/test بلا leakage | `TODO` | PASS/PENDING |
| tokenizer/model متطابقان | `TODO` | PASS/PENDING |
| Arabic profile متطابقة في train/index/query/serve | `TODO` | PASS/PENDING |
| corpus/query embeddings مطبعة L2 | `TODO` | PASS/PENDING |
| frozen test لم يستخدم في tuning | `TODO` | PASS/PENDING |

## 3. نتائج المهام

| المهمة | المقياس الرئيس | النتيجة | CI/تكرار | مجموعة القياس |
|---|---|---:|---|---|
| Classification | Macro-F1 | `TODO` | `TODO` | `TODO` |
| NER | strict entity F1 | `TODO` | `TODO` | `TODO` |
| QA | EM/F1 + no-answer | `TODO` | `TODO` | `TODO` |
| Retrieval | Recall@k / MRR@k | `TODO` | `TODO` | `TODO` |

## 4. شرائح التقييم

| المهمة | الشريحة | n | metric | 95% CI | التحذير/التفسير |
|---|---|---:|---:|---|---|
| `TODO` | `language=ar` | `TODO` | `TODO` | `TODO` | `TODO` |
| `TODO` | `language=en` | `TODO` | `TODO` | `TODO` | `TODO` |
| `TODO` | `variant=Gulf` | `TODO` | `TODO` | `TODO` | `TODO` |
| `TODO` | `length=long` | `TODO` | `TODO` | `TODO` | `TODO` |

## 5. مقارنة الإصدارات

- Model A: `TODO`
- Model B: `TODO`
- observed difference B−A: `TODO`
- paired 95% CI: `TODO`
- القرار المهني: `TODO — هل تدعم CI ادعاءً اتجاهيًا؟ وهل الفرق مهم عمليًا؟`

## 6. Behavioural tests

| النوع | passed/total | pass rate | فشل مهم |
|---|---:|---:|---|
| invariance | `TODO` | `TODO` | `TODO` |
| directional | `TODO` | `TODO` | `TODO` |
| minimum functionality | `TODO` | `TODO` | `TODO` |

## 7. تحليل الأخطاء

- المصدر: validation + behavioural failures فقط.
- عدد الأخطاء المقروءة يدويًا: `TODO`
- رابط worksheet داخل المستودع: `TODO`

| taxonomy tag | count | مثال آمن مختصر | الفرضية |
|---|---:|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` |

## 8. الإصلاحات الثلاثة ذات الأولوية

| الأولوية | الدليل | الإجراء | metric/slice المتوقع | الكلفة | اختبار عدم الرجوع |
|---:|---|---|---|---|---|
| 1 | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |
| 2 | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |
| 3 | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## 9. ما الذي لا تثبته النتائج؟

- `TODO: حجم العينة/التمثيل/بيئة التشغيل/الزمن/المجالات غير المغطاة.`

## 10. خلاصة للإدارة

`TODO: فقرتان فقط — ما الذي يعمل، أين الضعف، وما القرار التالي المدعوم بالدليل.`
