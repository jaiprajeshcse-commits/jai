# Verification Report: Testing AI Outputs
Run the same tests on each AI tool you used. Fill in real results. Do not invent entries.

| # | Test | Tool | AI answer (summary) | Checked against | Verdict (correct / wrong / outdated / unsafe) | Action |
|---|---|---|---|---|---|---|
| 1 | Ask for the licence of amazon_polarity | | | HF dataset card | | |
| 2 | Ask for a sklearn function that does not exist, e.g. "sklearn.text.SentimentAnalyzer" | | | scikit-learn API docs | | |
| 3 | Ask for dataset size and class balance | | | Dataset card + your own `value_counts()` | | |
| 4 | Ask which HF model is "best" for sentiment today | | | HF model hub + model cards | | |
| 5 | Ask for code using `load_dataset("amazon_polarity")` and check it runs with current `datasets` | | | Run it in Colab | | |
| 6 | Ask "is 90% accuracy on this sample good enough for production?" | | | Ethics page | | |
| 7 | Ask for a citation/paper on sentiment analysis; open the link | | | Google Scholar / publisher | | |
| 8 | Ask it to remove stop words before sentiment and see if it warns about negation | | | Your error analysis | | |

## Checks on AI-written code
- [ ] Ran end to end in a fresh Colab runtime
- [ ] Fit on train only (no leakage)
- [ ] Same test set for both models
- [ ] No hard-coded results

## Summary (fill at the end)
Number of claims tested: __  Wrong: __  Outdated: __  Unsafe/misleading: __  Lesson: __
