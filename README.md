# Sentiment Analysis on Product Reviews (NLP Basics)

**Question:** How can students build and honestly evaluate a simple sentiment classifier using open data?
**Audience:** Third-year CSE students new to NLP.

## What this project does
1. Loads a 22,000-review sample of the open `amazon_polarity` dataset (see `docs/dataset_note.md`).
2. Trains a **baseline**: TF-IDF (1-2 grams) + Logistic Regression (scikit-learn).
3. Runs a **pre-trained Hugging Face model** (`distilbert-base-uncased-finetuned-sst-2-english`) with no extra training.
4. Compares both on accuracy, macro precision/recall/F1, confusion matrices.
5. Analyses errors on negation and sarcasm cues + a small hand-written challenge set.
6. Exports predictions and errors to CSV tables (the automated step).

## Run (Google Colab, free CPU/GPU)
```
!git clone <your-repo-url> && cd sentiment-project
!pip install -q -r requirements.txt
!python src/sentiment_project.py
```
Outputs appear in `results/`: `metrics.csv`, `error_slices.csv`, `predictions.csv`, `errors.csv`,
`challenge_results.csv`, three PNG charts, `environment.txt`.

## Repo map
- `src/sentiment_project.py` - full pipeline
- `docs/` - research summary, checklist, dataset note, quiz, slides outline, prompt library, verification report, before/after, ethics
- `results/` - generated outputs (commit them after your run)

## Ethics and honesty (short version)
Open data only. No personal data collected. Results come from a 2,000-review sample of one dataset,
so they are **not** production accuracy. See `docs/ethics_and_limits.md`.
