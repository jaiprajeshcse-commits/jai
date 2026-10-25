# NLP Project Checklist
Tick each item only after you have done it and can show evidence.

## 1. Problem and data
- [ ] Task defined: binary sentiment (negative / positive) on English product reviews
- [ ] Dataset chosen, licence read on the dataset card, recorded in `dataset_note.md`
- [ ] Class balance checked and reported
- [ ] Sampling seed fixed and recorded (seed 42)
- [ ] Data age and source limits noted (reviews up to 2013, Amazon only)

## 2. Preprocessing
- [ ] Train/test split made BEFORE fitting the vectorizer (no leakage)
- [ ] Stop words NOT blindly removed (negations carry sentiment)
- [ ] Text length / truncation handled for the transformer (max 256 tokens)

## 3. Models
- [ ] Simple baseline trained first (TF-IDF + Logistic Regression)
- [ ] Pre-trained model run on the same test set
- [ ] Library versions saved (`results/environment.txt`)

## 4. Evaluation
- [ ] Accuracy AND precision/recall/F1 reported (not accuracy alone)
- [ ] Confusion matrix for each model
- [ ] Same test set used for both models
- [ ] Test set never used to tune anything

## 5. Error analysis
- [ ] Negation slice error rates
- [ ] Sarcasm cue slice (state its small size and crude detection)
- [ ] 20 wrong predictions read manually and categorised
- [ ] Domain shift discussed (model fine-tuned on movie reviews)

## 6. AI tool use
- [ ] At least 2 AI research tools used and compared
- [ ] At least 4 free AI tools used overall
- [ ] Every important prompt saved in `prompt_library.md`
- [ ] AI claims checked against official docs (`verification_report.md`)
- [ ] AI-written code run and tested by you

## 7. Ethics
- [ ] Open data only, no scraping
- [ ] Bias and limits reported
- [ ] No production-accuracy claims

## 8. Submission
- [ ] Research report, dataset note, models, error analysis
- [ ] Quiz + answer key, 7-slide deck
- [ ] GitHub repo, prompt library, verification report, before/after analysis
- [ ] Final demo rehearsed
