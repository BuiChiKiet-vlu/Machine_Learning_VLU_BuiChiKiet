# -*- coding: utf-8 -*-
"""Bài tập 3 (bài 4): Đổi đơn vị đo của cột chi tiêu."""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/sinh_vien_mo_rong.csv")
cot = ["gio_on", "diem_giua_ky", "chi_tieu"]
y = df["qua_mon"]

X_nghin = df[cot].copy()                 # chi tieu tinh bang nghin dong
X_trieu = df[cot].copy()
X_trieu["chi_tieu"] = X_trieu["chi_tieu"] / 1000   # doi sang trieu dong

print("Do lech chuan cua ba cot (don vi nghin dong -> trieu dong):")
print("  ", X_nghin.std().round(2).to_dict())
print("  ", X_trieu.std().round(2).to_dict())
print()


def cham(X, chuan_hoa):
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.25, random_state=17, stratify=y
    )
    knn = KNeighborsClassifier(n_neighbors=7)
    mh = make_pipeline(StandardScaler(), knn) if chuan_hoa else knn
    mh.fit(X_tr, y_tr)
    return accuracy_score(y_te, mh.predict(X_te))


print("Accuracy tren tap kiem tra (KNN, k = 7)")
print(f"  nghin dong, khong chuan hoa : {cham(X_nghin, False):.4f}")
print(f"  trieu dong, khong chuan hoa : {cham(X_trieu, False):.4f}")
print(f"  nghin dong, co chuan hoa    : {cham(X_nghin, True):.4f}")
print(f"  trieu dong, co chuan hoa    : {cham(X_trieu, True):.4f}")
