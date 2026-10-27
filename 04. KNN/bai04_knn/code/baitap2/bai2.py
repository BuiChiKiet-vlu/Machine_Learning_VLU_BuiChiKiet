# -*- coding: utf-8 -*-
"""Bài tập 2 (bài 4): Khoảng cách Manhattan so với Euclid."""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("data/hai_vang_trang.csv")
X = df[["x1", "x2"]]
y = df["nhan"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)

for metric in ["euclidean", "manhattan"]:
    diem = {}
    for k in range(1, 52, 2):
        mh = KNeighborsClassifier(n_neighbors=k, metric=metric)
        diem[k] = cross_val_score(mh, X_tr, y_tr, cv=5).mean()
    k_tot = max(diem, key=diem.get)
    mh = KNeighborsClassifier(n_neighbors=k_tot, metric=metric).fit(X_tr, y_tr)
    acc = accuracy_score(y_te, mh.predict(X_te))
    print(f"{metric:10s}: k tot nhat = {k_tot:2d}, "
          f"diem kiem dinh cheo = {diem[k_tot]:.4f}, "
          f"accuracy tap kiem tra = {acc:.4f}")
