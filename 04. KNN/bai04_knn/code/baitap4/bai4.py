# -*- coding: utf-8 -*-
"""Bài tập 4 (bài 4): Láng giềng có trọng số theo khoảng cách."""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("data/hai_vang_trang.csv")
X = df[["x1", "x2"]]
y = df["nhan"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)

print("   k   |   weights='uniform'    |   weights='distance'")
print("       |  tap hoc  tap kiem tra |  tap hoc  tap kiem tra")
for k in [1, 13, 101]:
    dong = f" {k:4d}  |"
    for w in ["uniform", "distance"]:
        mh = KNeighborsClassifier(n_neighbors=k, weights=w).fit(X_tr, y_tr)
        a = accuracy_score(y_tr, mh.predict(X_tr))
        b = accuracy_score(y_te, mh.predict(X_te))
        dong += f"  {a:.4f}   {b:.4f}      |"
    print(dong.rstrip("|"))
