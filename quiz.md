# Quiz: Sentiment Analysis on Product Reviews (12 questions)

1. What does TF-IDF measure?
   A) How many letters a word has  B) How important a word is to a document relative to the whole collection  C) Whether a word is positive  D) The order of words in a sentence

2. Why does this project NOT remove stop words like "not"?
   A) They slow training  B) They are always rare  C) Negations can flip sentiment  D) Logistic Regression cannot read them

3. Why is accuracy alone a weak metric?
   A) It cannot be computed on text  B) It can look high when classes are imbalanced  C) It ignores true positives  D) It only works for regression

4. F1 score is:
   A) The average of accuracy and recall  B) The harmonic mean of precision and recall  C) The number of correct predictions  D) The error rate

5. Why fit the TF-IDF vectorizer on training data only?
   A) To save memory  B) To avoid data leakage from the test set  C) Because test data has no words  D) To increase vocabulary

6. A bag-of-words/n-gram baseline mostly ignores:
   A) Word frequency  B) Individual words  C) Long-range word order and context  D) Lowercase text

7. The Hugging Face model used here was fine-tuned on movie reviews, then tested on product reviews. This is an example of:
   A) Overfitting  B) Domain shift  C) Data leakage  D) Tokenisation

8. Which sentence is hardest for both models?
   A) "Absolutely love it."  B) "Terrible, it broke."  C) "Great, just great. It broke on day one."  D) "Works perfectly."

9. A model has 95% precision and 50% recall for the negative class. This means:
   A) It finds most negative reviews  B) When it says negative it is usually right, but it misses about half of the negative reviews  C) It is wrong 95% of the time  D) It is perfectly balanced

10. Why must you avoid claiming "production accuracy"?
   A) Production is always lower than 50%  B) The test set is a small sample from one old, English-only source  C) Hugging Face forbids it  D) Accuracy cannot be reported

11. The dataset card lists Apache-2.0. Why still check where the data came from?
   A) The licence is always wrong  B) The review text originally came from Amazon customers, and the upstream terms are not fully documented  C) Apache-2.0 does not exist  D) You do not need to

12. An AI tool tells you to use a scikit-learn function you have never seen. What do you do first?
   A) Trust it  B) Search the official scikit-learn docs and run a small test  C) Ask the same AI to confirm  D) Rename the function

---
## Answer key
1. B  2. C  3. B  4. B  5. B  6. C  7. B  8. C  9. B  10. B  11. B  12. B

## Short explanations
1. TF-IDF raises the weight of words frequent in one document but rare overall.
2. "not good" and "good" are opposite; removing "not" destroys the signal.
3. A model predicting only the majority class can score high accuracy.
4. F1 = 2PR/(P+R); it punishes imbalance between precision and recall.
5. Fitting on test data lets test information shape the features.
6. Bigrams capture only short phrases like "not good".
7. The training and deployment text styles differ.
8. Positive words ("great") with negative meaning; this is sarcasm.
9. Precision = correct among predicted; recall = found among actual.
10. Sample, source age, language and label noise all limit generalisation.
11. A card's licence label does not prove the upstream terms.
12. Verify against primary sources; asking the same AI again is not verification.
