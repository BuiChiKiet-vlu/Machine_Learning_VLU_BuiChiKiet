#Bài 5: 

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/sinh_vien.csv")
X = df[["gio_on"]]
y = df["qua_mon"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)
mo_hinh = LogisticRegression().fit(X_train, y_train)

p = mo_hinh.predict_proba(X_test)[:, 1]

f1_tot_nhat = -1.0
nguong_tot_nhat = None

print("Nguong   F1")
for nguong in np.arange(0.05, 1.0, 0.05):
    y_pred = (p >= nguong).astype(int)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    print(f"  {nguong:.2f}   {f1:.4f}")
    if f1 > f1_tot_nhat:
        f1_tot_nhat = f1
        nguong_tot_nhat = nguong
print()

print(f"Nguong cho F1 cao nhat: {nguong_tot_nhat:.2f} voi F1 = {f1_tot_nhat:.4f}")
print()

print("""Giải thích:
  - Nguong cho F1 cao nhat: Đây là giá trị ngưỡng được chọn để đạt được F1 score cao nhất.
  - F1 score: Là trung bình điều hòa của precision và recall, phản ánh sự cân bằng giữa hai chỉ số này.""")
