# 7-Slide Deck Outline (paste into Gamma or PowerPoint)
Audience: third-year CSE students new to NLP. About 1 minute per slide.

1. **Title and question** - "Can we honestly measure how well a simple sentiment classifier works?" Name, course, date.
2. **Data and licence** - amazon_polarity, 22k-review sample, Apache-2.0 on the card, upstream-terms caution, dated 2013.
3. **Pipeline** - raw text -> TF-IDF (1-2 grams) -> Logistic Regression; side branch: pre-trained DistilBERT. Diagram.
4. **Results** - `metrics_chart.png` + a small table (accuracy, macro F1). Say "on a 2,000-review sample".
5. **Error analysis** - negation and sarcasm slices (`error_slices_chart.png`), 3 real examples from `errors.csv`.
6. **Verifying AI** - 3 hallucinations/outdated items you caught (from `verification_report.md`), tools used.
7. **Ethics and limits** - open data, bias, domain shift, no production claim; what you would do next.

Speaker tip: use your own numbers from `results/metrics.csv`. Do not quote numbers you have not produced.
