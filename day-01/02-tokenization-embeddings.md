# 2. Tokenisation وEmbeddings  
# From Tokens to Vectors

## الفكرة في جملة

النموذج لا يقرأ الكلمات مباشرة. tokenizer يحول النص إلى وحدات وIDs، ثم embedding layer تحول كل ID إلى متجه قابل للتعلم.

```text
"الخدمة ممتازة"
→ ["[CLS]", "الخدمة", "ممتاز", "##ة", "[SEP]"]
→ [101, ..., 102]
→ matrix: sequence_length × hidden_size
```

القيم أعلاه توضيحية `EXAMPLE` وليست output ثابتًا؛ IDs تعتمد على checkpoint.

## 2.1 ما هو Token؟

Token وحدة في vocabulary. قد يكون:

- كلمة كاملة.
- جزء كلمة `subword`.
- حرفًا أو byte.
- punctuation.
- special token مثل `[CLS]` أو `[SEP]` أو `[PAD]`.

**لا تساوي:** token ≠ كلمة بالضرورة، وtoken ID ≠ embedding.

## 2.2 لماذا Subwords؟

لو اعتمد tokenizer كلمات كاملة فقط، تصبح الكلمات الجديدة خارج المفردات. subwords تسمح بتركيب كلمات نادرة من أجزاء معروفة. المقابل: قد تنقسم العربية إلى وحدات أكثر بسبب اللصائق والتنوع الكتابي، فتستهلك سياقًا وحوسبة.

أشهر العائلات:

| العائلة | الفكرة المبسطة |
|---|---|
| WordPiece | يختار أجزاء من vocabulary لتغطية الكلمة |
| BPE | يدمج أزواجًا شائعة تدريجيًا |
| Unigram | يبدأ بمرشحين ويختار segmentation احتمالية |
| Byte-level | ينطلق من bytes لتقليل unknowns |

لا تختَر العائلة بالاسم؛ اختبر tokenizer الفعلي على corpus المهمة.

## 2.3 tokenizer وcheckpoint زوج واحد

IDs لا تحمل معنى عالميًا. الرقم 1000 في vocabulary نموذج قد يعني وحدة مختلفة تمامًا في نموذج آخر. لذلك:

```python
from transformers import AutoTokenizer

MODEL_ID = "google-bert/bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
```

النموذج المرجعي متعدد اللغات دُرب على 104 لغات حسب [بطاقة النموذج](https://huggingface.co/google-bert/bert-base-multilingual-cased). نستخدم tokenizer للمقارنة الثنائية، لا كادعاء أنه أفضل نموذج عربي.

## 2.4 قياس Fertility

نعرفه في الدورة:

[
	ext{fertility} =
rac{	ext{عدد model tokens دون special tokens}}
{	ext{عدد الكلمات المفصولة بالمسافة}}
]

```python
from src.bayan.tokenization import token_fertility

value = token_fertility(
    "الخدمة ممتازة",
    tokenizer.tokenize,
)
print(value)
```

### لماذا يهم؟

ارتفاع fertility قد يعني:

- طولًا أكبر وحوسبة أكثر.
- وصولًا أسرع إلى maximum context.
- truncation أكبر.
- محاذاة أصعب في NER.
- تمثيلًا أكثر تجزؤًا لبعض اللغات.

لكنه ليس مقياس جودة منفردًا؛ tokenizer ذو fertility أقل ليس أفضل تلقائيًا.

## 2.5 Padding وTruncation

الجمل في batch أطوالها مختلفة، بينما tensor مستطيل. [توثيق Hugging Face](https://huggingface.co/docs/transformers/main_classes/tokenizer) يوضح استراتيجيات padding وtruncation.

```python
batch = tokenizer(
    ["الخدمة ممتازة", "The service is excellent"],
    padding=True,
    truncation=True,
    max_length=32,
    return_tensors="pt",
)
print(batch["input_ids"].shape)
print(batch["attention_mask"].shape)
```

- `padding=True`: الحشو إلى أطول مثال في batch.
- `truncation=True`: قص ما يتجاوز الحد.
- `attention_mask=1`: token حقيقي غالبًا.
- `attention_mask=0`: padding غالبًا.

**قاعدة:** لا تختَر `max_length` من الذاكرة؛ قس distribution للطول ومعدل truncation على corpus.

## 2.6 من ID إلى Embedding

Embedding table مصفوفة:

[
E in mathbb{R}^{|V| 	imes d}
]

- (|V|): حجم vocabulary.
- (d): embedding dimension.
- اختيار ID يعني أخذ صف من المصفوفة.

```python
import numpy as np

rng = np.random.default_rng(42)
vocab_size, embedding_dim = 20, 4
embedding_table = rng.normal(size=(vocab_size, embedding_dim))

token_ids = np.array([2, 7, 5])
vectors = embedding_table[token_ids]

print(vectors.shape)  # (3, 4)
```

هذا المثال static lookup. داخل BERT تصبح المخرجات **contextual** بعد طبقات encoder: تمثيل كلمة «عين» يختلف بين «عين الماء» و«عين الإنسان».

## 2.7 ثلاثة أشياء لا تخلط بينها

| العنصر | مثال | هل يحمل متجهًا متعلمًا؟ |
|---|---|---|
| Token | `##ة` | لا، هو نص الوحدة |
| Token ID | `1842` | لا، هو فهرس |
| Embedding | `[0.12, -0.44, ...]` | نعم |

## نشاط القياس

قارن:

- `الخدمة ممتازة في الرياض`
- `وبالخدمة الإلكترونية الجديدة`
- `The service is excellent in Riyadh`

سجّل:

| النص | whitespace words | model tokens | fertility | ملاحظة |
|---|---:|---:|---:|---|

ثم أجب: هل الفرق سببه اللغة، اللصيقة، طول الكلمة، أم vocabulary؟ قد توجد أكثر من علة؛ لا تقفز إلى حكم جودة.

## أخطاء شائعة

- عدّ special tokens ضمن fertility دون التصريح.
- مقارنة tokenizers على نصين مختلفين.
- نسيان padding tokens عند pooling.
- استخدام raw pretrained `[CLS]` كـsentence similarity بلا تدريب مخصص.
- قص النص قبل قياس ما فُقد.
- تحميل tokenizer من checkpoint والنموذج من آخر.

## English recap

Tokenisation maps text to checkpoint-specific units and IDs. Fertility measures token fragmentation, padding creates rectangular batches, truncation can remove evidence, and embeddings map IDs to vectors. Always keep tokenizer and model checkpoint aligned.
