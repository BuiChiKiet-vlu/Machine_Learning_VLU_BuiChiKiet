# -*- coding: utf-8 -*-
"""Bài tập 3 (bài 3): Đổi tham số làm trơn alpha."""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("data/tin_nhan.csv")
vec = CountVectorizer(token_pattern=r"(?u)\S+")
X = vec.fit_transform(df["noi_dung"])
y = df["la_rac"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)

print("  alpha    accuracy  precision  recall")
for alpha in [0.001, 0.1, 1.0, 10.0, 100.0]:
    mh = MultinomialNB(alpha=alpha).fit(X_tr, y_tr)
    du_doan = mh.predict(X_te)
    a = accuracy_score(y_te, du_doan)
    p = precision_score(y_te, du_doan, zero_division=0)
    r = recall_score(y_te, du_doan)
    print(f"  {alpha:7.3f}  {a:8.4f}  {p:9.4f}  {r:6.4f}")

print()
print("Nhan xet: xem muc README, bai 3.3. Alpha qua lon lam moi xac suat tu")
print("xich lai gan nhau (gan 1/V), mo hinh mat kha nang phan biet hai lop.")
