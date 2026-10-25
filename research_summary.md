# Research Summary (DRAFT: replace bracketed parts after your own research)

**Audience:** third-year CSE students new to NLP.
**Tools to compare (use at least 2):** e.g. ChatGPT, Gemini, Claude, DeepSeek, NotebookLM. Ask each the same questions (see `prompt_library.md`) and record differences.

## 1. Text preprocessing
Lowercasing, tokenisation and vectorisation turn text into numbers. For sentiment, removing stop words is risky because negations ("not", "never") matter. TF-IDF weights words by how distinctive they are; n-grams (e.g. "not good") recover a little word order. [Add 2 lines from the scikit-learn TfidfVectorizer docs.]

## 2. Sentiment classification
- **Classic:** TF-IDF + Logistic Regression: fast, interpretable (inspect coefficients), weak on context and sarcasm.
- **Pre-trained transformer:** understands context better, but was trained on other data (domain shift) and is a black box. [Add 2 lines from the Hugging Face pipelines docs and the model card.]

## 3. Evaluation metrics
Accuracy, precision, recall, F1 (macro), confusion matrix. Always evaluate on held-out data and report sample size. [Add 2 lines from scikit-learn model evaluation docs.]

## 4. Where AI tools disagreed
[Table: question | Tool A answer | Tool B answer | which was correct after checking the docs]

## 5. Sources (verify each link opens and says what you claim)
- scikit-learn documentation: TfidfVectorizer, LogisticRegression, classification metrics
- Hugging Face documentation: Transformers pipelines; dataset card for amazon_polarity; model card for distilbert-base-uncased-finetuned-sst-2-english
- McAuley and Leskovec (2013), "Hidden factors and hidden topics" (the original reviews)
- [Add 2 more you actually read, with access date]
