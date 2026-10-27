# -*- coding: utf-8 -*-
"""Bài tập 1 (bài 4): Tự viết KNN không dùng thư viện."""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def knn_du_doan(X_hoc, y_hoc, x_moi, k):
    """Du doan nhan cho MOT mau moi bang k lang gieng gan nhat."""
    khoang = np.sqrt(((X_hoc - x_moi) ** 2).sum(axis=1))   # buoc 1
    gan = np.argsort(khoang)[:k]                            # buoc 2
    phieu = np.bincount(y_hoc[gan])                         # buoc 3
    return int(np.argmax(phieu))


df = pd.read_csv("data/hai_vang_trang.csv")
X = df[["x1", "x2"]].to_numpy(dtype=float)
y = df["nhan"].to_numpy()
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)

K = 13
du_doan_tay = np.array([knn_du_doan(X_tr, y_tr, x, K) for x in X_te])
acc_tay = (du_doan_tay == y_te).mean()

mh = KNeighborsClassifier(n_neighbors=K).fit(X_tr, y_tr)
du_doan_sk = mh.predict(X_te)
acc_sk = (du_doan_sk == y_te).mean()

print(f"Accuracy KNN tu viet        (k = {K}): {acc_tay:.4f}")
print(f"Accuracy KNeighborsClassifier (k = {K}): {acc_sk:.4f}")
print(f"So mau hai ben doan khac nhau: {(du_doan_tay != du_doan_sk).sum()}")
