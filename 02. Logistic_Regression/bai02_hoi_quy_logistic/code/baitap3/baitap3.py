#Bài 3:

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('data/sinh_vien.csv')
X = df[['gio_on']]
Y = df['qua_mon']

mo_hinh = LogisticRegression()
mo_hinh.fit(X, Y)

w = float(mo_hinh.coef_[0][0])
b = float(mo_hinh.intercept_[0])

print(f"Hệ số góc w: {w:.6f}")
print(f"Hệ số chặn b: {b:.6f}")
print()

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def du_doan(gio):
    z = w * gio + b
    xac_xuat = sigmoid(z)
    nhan = 1 if xac_xuat >= 0.5 else 0
    print(f"Giờ ôn tập: {gio:5.2f}, Xác suất qua môn: {xac_xuat:.4f}, Dự đoán: {'Qua môn' if nhan == 1 else 'Trượt'}")

print("Dự đoán cho các giờ ôn tập khác nhau:")
for gio in [3, 8, 12.89, 18, 26]:
    du_doan(gio)
print()

print("Giải thích: Vì 12.89 giờ ôn là nghiệm của phương trình w * gio + b = 0")
