# Dataset Note

| Field | Value |
|---|---|
| Name | Amazon Review Polarity (`fancyzhx/amazon_polarity` on Hugging Face) |
| Task | Binary sentiment: stars 1-2 = negative (0), 4-5 = positive (1); 3-star reviews excluded |
| Language | English |
| Source | Amazon product reviews (McAuley and Leskovec, 2013), polarity version prepared by Xiang Zhang |
| Size | ~3.6M train / 400k test; this project uses a random 20,000 train and 2,000 test sample (seed 42) |
| Licence on dataset card | Apache License 2.0 |
| Retrieved | (write the date you downloaded it) |
| Link | https://huggingface.co/datasets/fancyzhx/amazon_polarity |

## Licence caution (write this honestly in your report)
The Hugging Face dataset card lists Apache-2.0, which is what I verified. The review text itself originally
comes from Amazon customers, and the card gives little detail about the original terms. So: use it for
learning and research only, do not redistribute large copies of it in your repo (your repo should
download it by name, not store it), and say clearly that the upstream terms are not fully documented.

## Known limits
- Reviews end in 2013: product vocabulary and slang are dated.
- One platform, English only; no regional or Tamil/Hinglish text.
- Star ratings are a noisy proxy for sentiment (a 4-star review can contain complaints).
- Dataset card sections on bias and sensitive information are marked "Needs More Information".
- Neutral (3-star) reviews are excluded, so the task is easier than real-world sentiment.
