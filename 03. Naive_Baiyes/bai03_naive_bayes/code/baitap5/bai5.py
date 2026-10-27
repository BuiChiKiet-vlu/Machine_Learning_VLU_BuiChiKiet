# -*- coding: utf-8 -*-
"""Bài tập 5 (bài 3): Chọn sai biến thể Naive Bayes."""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB

df = pd.read_csv("data/sinh_vien.csv")
X = df[["gio_on", "diem_giua_ky"]]
y = df["qua_mon"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)

for ten, mh in [("MultinomialNB (sai the)", MultinomialNB()),
                ("GaussianNB (dung the)  ", GaussianNB())]:
    mh.fit(X_tr, y_tr)
    print(f"{ten}: accuracy = {accuracy_score(y_te, mh.predict(X_te)):.4f}")

print()
print("Ca hai deu chay khong bao loi (du lieu khong am nen MultinomialNB")
print("khong tu choi). Giai thich xem README, bai 3.5.")
