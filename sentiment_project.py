"""Sentiment analysis on product reviews.
Baseline (TF-IDF + Logistic Regression) vs pre-trained Hugging Face model.
Run in Google Colab:  !pip install -q -r requirements.txt  then  !python src/sentiment_project.py
Outputs go to results/ (metrics, predictions, errors, charts).
"""
import os, re, platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import torch
import sklearn, transformers, datasets as hf_datasets
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from transformers import pipeline

SEED, N_TRAIN, N_TEST, OUT = 42, 20000, 2000, "results"
HF_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"  # fine-tuned on SST-2 (movie reviews)

NEG_RE = re.compile(r"\b(not|no|never|none|nothing|neither|nor|hardly|barely|without|cannot)\b|n't", re.I)
SARC_RE = re.compile(r"(yeah,? right|oh,? great|great,? just great|thanks a lot|what a joke|"
                     r"so[- ]called|big surprise|just what i needed|wow,? thanks|as if)", re.I)

# Small hand-written challenge set (1 = positive, 0 = negative). Extend it yourself.
CHALLENGE = [
    ("The battery is not bad at all, lasts two days.", 1),
    ("I wouldn't say this is a waste of money.", 1),
    ("Not good. Stopped working after a week.", 0),
    ("This is never going to work as advertised.", 0),
    ("No complaints, works perfectly.", 1),
    ("Great, just great. It broke on day one.", 0),
    ("Oh great, another charger that overheats.", 0),
    ("Thanks a lot for the broken screen, amazing quality.", 0),
    ("Yeah right, 'waterproof'. It died in the rain.", 0),
    ("I love how it never connects to wifi.", 0),
    ("Absolutely love it, would buy again.", 1),
    ("Terrible packaging and the item was scratched.", 0),
]

def load_data():
    ds = load_dataset("fancyzhx/amazon_polarity")
    def to_df(split, n):
        d = ds[split].shuffle(seed=SEED).select(range(n))
        return pd.DataFrame({"text": [t + ". " + c for t, c in zip(d["title"], d["content"])],
                             "label": d["label"]})
    return to_df("train", N_TRAIN), to_df("test", N_TEST)

def hf_predict(texts):
    clf = pipeline("sentiment-analysis", model=HF_MODEL, truncation=True, max_length=256,
                   batch_size=32, device=0 if torch.cuda.is_available() else -1)
    out = clf(list(texts))
    return (np.array([1 if o["label"] == "POSITIVE" else 0 for o in out]),
            np.array([o["score"] for o in out]))

def metrics(y, p, name):
    pr, rc, f1, _ = precision_recall_fscore_support(y, p, average="macro", zero_division=0)
    return {"model": name, "accuracy": accuracy_score(y, p), "precision_macro": pr,
            "recall_macro": rc, "f1_macro": f1}

def main():
    os.makedirs(OUT, exist_ok=True)
    train, test = load_data()
    print("class balance (train):", train.label.value_counts().to_dict())

    # --- Baseline: no stop-word removal on purpose (words like "not" carry sentiment) ---
    vec = TfidfVectorizer(lowercase=True, ngram_range=(1, 2), min_df=2, max_features=50000)
    Xtr = vec.fit_transform(train.text)          # fit on TRAIN only (avoids leakage)
    base = LogisticRegression(max_iter=1000, random_state=SEED).fit(Xtr, train.label)
    test["base_pred"] = base.predict(vec.transform(test.text))

    # --- Pre-trained Hugging Face model (no training; zero adaptation to product reviews) ---
    test["hf_pred"], test["hf_conf"] = hf_predict(test.text)

    # --- Metrics ---
    m = pd.DataFrame([metrics(test.label, test.base_pred, "TF-IDF + LogReg"),
                      metrics(test.label, test.hf_pred, "DistilBERT SST-2")])
    m.round(4).to_csv(f"{OUT}/metrics.csv", index=False)
    print(m.round(4).to_string(index=False))

    # --- Error analysis slices (keyword heuristics: crude, report them as such) ---
    test["has_negation"] = test.text.str.contains(NEG_RE)
    test["sarcasm_cue"] = test.text.str.contains(SARC_RE)
    test["base_wrong"] = test.base_pred != test.label
    test["hf_wrong"] = test.hf_pred != test.label
    slices = {"all": pd.Series(True, index=test.index), "has negation": test.has_negation,
              "no negation": ~test.has_negation, "sarcasm cue": test.sarcasm_cue}
    rows = [{"slice": k, "n": int(v.sum()),
             "baseline_error_rate": test[v].base_wrong.mean(), "hf_error_rate": test[v].hf_wrong.mean()}
            for k, v in slices.items()]
    sl = pd.DataFrame(rows); sl.round(4).to_csv(f"{OUT}/error_slices.csv", index=False)
    print(sl.round(4).to_string(index=False))

    # --- Automation step: export predictions + errors as tables ---
    test.to_csv(f"{OUT}/predictions.csv", index=False)
    test[test.base_wrong | test.hf_wrong].to_csv(f"{OUT}/errors.csv", index=False)

    # --- Challenge set (negation / sarcasm) ---
    ch = pd.DataFrame(CHALLENGE, columns=["text", "label"])
    ch["base_pred"] = base.predict(vec.transform(ch.text))
    ch["hf_pred"], ch["hf_conf"] = hf_predict(ch.text)
    ch.to_csv(f"{OUT}/challenge_results.csv", index=False)
    print("challenge accuracy  baseline:", round((ch.base_pred == ch.label).mean(), 3),
          " HF:", round((ch.hf_pred == ch.label).mean(), 3))

    # --- Charts ---
    ax = m.set_index("model")[["accuracy", "precision_macro", "recall_macro", "f1_macro"]].T.plot.bar(rot=0, figsize=(7, 4))
    ax.set_ylim(0, 1); ax.set_title("Test metrics (2,000 reviews)"); plt.tight_layout()
    plt.savefig(f"{OUT}/metrics_chart.png", dpi=150); plt.close()

    fig, axs = plt.subplots(1, 2, figsize=(8, 3.6))
    for a, (col, title) in zip(axs, [("base_pred", "TF-IDF + LogReg"), ("hf_pred", "DistilBERT SST-2")]):
        cm = confusion_matrix(test.label, test[col], labels=[0, 1])
        a.imshow(cm, cmap="Blues"); a.set_title(title); a.set_xlabel("predicted"); a.set_ylabel("true")
        a.set_xticks([0, 1]); a.set_xticklabels(["neg", "pos"]); a.set_yticks([0, 1]); a.set_yticklabels(["neg", "pos"])
        for i in range(2):
            for j in range(2):
                a.text(j, i, cm[i, j], ha="center", va="center")
    plt.tight_layout(); plt.savefig(f"{OUT}/confusion_matrices.png", dpi=150); plt.close()

    labels = sl["slice"] + " (n=" + sl.n.astype(str) + ")"
    ax = sl.set_index(labels)[["baseline_error_rate", "hf_error_rate"]].plot.bar(rot=15, figsize=(8, 4))
    ax.set_title("Error rate by slice"); plt.tight_layout()
    plt.savefig(f"{OUT}/error_slices_chart.png", dpi=150); plt.close()

    with open(f"{OUT}/environment.txt", "w") as f:
        f.write(f"python {platform.python_version()}\nsklearn {sklearn.__version__}\n"
                f"transformers {transformers.__version__}\ndatasets {hf_datasets.__version__}\n"
                f"torch {torch.__version__}\nseed {SEED}\nmodel {HF_MODEL}\n")
    print("Done. See results/")

if __name__ == "__main__":
    main()
