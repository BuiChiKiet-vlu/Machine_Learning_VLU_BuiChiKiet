# -*- coding: utf-8 -*-
"""Bài tập 6 (bài 4): Đo thời gian .fit và .predict của KNN."""

import time

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

rng = np.random.default_rng(0)
X_moi = rng.random((1000, 2))   # 1000 mau moi de du doan

print(f" {'so mau':>8s}  {'fit (s)':>10s}  {'predict 1000 mau (s)':>22s}")
for n in [1000, 10000, 100000]:
    X = rng.random((n, 2))
    y = rng.integers(0, 2, n)
    # algorithm="brute" so moi mau moi voi TOAN BO du lieu,
    # dung la y tuong KNN trong bai (mac dinh scikit-learn tu chon
    # cau truc cay KD nen fit co ton chut thoi gian)
    mh = KNeighborsClassifier(n_neighbors=5, algorithm="brute")

    mh.fit(X[:50], y[:50]); mh.predict(X_moi[:5])   # khoi dong, khong tinh gio

    t0 = time.perf_counter()
    mh.fit(X, y)
    t_fit = time.perf_counter() - t0

    t0 = time.perf_counter()
    mh.predict(X_moi)
    t_pred = time.perf_counter() - t0
    print(f" {n:8d}  {t_fit:10.5f}  {t_pred:22.5f}")
