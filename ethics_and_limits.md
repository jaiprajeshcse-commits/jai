# Ethics and Limits
1. **Open data only.** The dataset is a public, documented benchmark. No scraping, no private reviews.
2. **Privacy.** Reviews can contain names or personal details. Do not publish `predictions.csv` rows you have not skimmed; remove any that identify a person.
3. **Bias.** Data is English, Amazon-only, pre-2013, and polarity labels come from star ratings. Reviewers are not a representative population. The pre-trained model was fine-tuned on movie reviews and may favour that style.
4. **Limits.** Scores come from a 2,000-review test sample of one dataset. Treat them as a classroom comparison, not production accuracy.
5. **Sarcasm and negation.** The keyword slices are crude heuristics with small samples. Report counts next to every rate.
6. **AI tool use.** Every AI-generated claim or code block was checked (see `verification_report.md`). Say which parts AI helped with.
7. **Do not say:** "our model is 9X% accurate in real life", "the transformer understands sentiment", or "the model is unbiased".
