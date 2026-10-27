# -*- coding: utf-8 -*-
"""Bài tập 5 (bài 4): Chọn k cho KNN hồi quy bằng kiểm định chéo."""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv("data/gia_nha.csv")
X = df[["dien_tich"]]
y = df["gia"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2,
                                          random_state=42)

# Điểm trả về mang dấu âm, nên đổi dấu để ra MAE
print("  k   MAE kiem dinh cheo")
mae_cv = {}
for k in range(1, 21):
    diem = cross_val_score(KNeighborsRegressor(n_neighbors=k), X_tr, y_tr,
                           cv=5, scoring="neg_mean_absolute_error")
    mae_cv[k] = -diem.mean()
    print(f" {k:2d}   {mae_cv[k]:.4f}")

k_tot = min(mae_cv, key=mae_cv.get)
print()
print(f"k tot nhat = {k_tot}")

knn = KNeighborsRegressor(n_neighbors=k_tot).fit(X_tr, y_tr)
duong = LinearRegression().fit(X_tr, y_tr)
mae_knn = mean_absolute_error(y_te, knn.predict(X_te))
mae_duong = mean_absolute_error(y_te, duong.predict(X_te))
print("MAE tren tap kiem tra (ty dong)")
print(f"  KNN, k = {k_tot:<2d}: {mae_knn:.4f}")
print(f"  Duong thang : {mae_duong:.4f}")
print("KNN vuot duong thang?", "CO" if mae_knn < mae_duong else "KHONG")
