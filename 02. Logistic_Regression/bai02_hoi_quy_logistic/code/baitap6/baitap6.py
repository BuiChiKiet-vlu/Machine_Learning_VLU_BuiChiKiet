#Bài 6:

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/sinh_vien.csv")
X = df[["gio_on"]]
y = df["qua_mon"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)
mo_hinh = LogisticRegression().fit(X_train, y_train)
y_pred = mo_hinh.predict(X_test)

# Lop duong la lop 1 (qua mon), giong tai lieu
precision_lop_1 = precision_score(y_test, y_pred, pos_label=1)
recall_lop_1 = recall_score(y_test, y_pred, pos_label=1)

# Lop duong la lop 0 (rot mon)
precision_lop_0 = precision_score(y_test, y_pred, pos_label=0)
recall_lop_0 = recall_score(y_test, y_pred, pos_label=0)

print("Cham diem lay lop 1 (qua mon) lam lop duong (giong tai liệu):")
print(f"  Precision = {precision_lop_1:.4f}")
print(f"  Recall    = {recall_lop_1:.4f}")
print()

print("Cham diem lay lop 0 (rot mon) lam lop duong:")
print(f"  Precision = {precision_lop_0:.4f}")
print(f"  Recall    = {recall_lop_0:.4f}")
print()

print("""Giải thích:
  - Mô hình và dữ liệu kiểm tra không đổi, chỉ đổi lớp nào được gọi là
    "dương". Khi đó, vai trò của TP, FP, FN bị hoán đổi cho nhau: TP của
    lớp 0 (rớt môn) chính là TN của lớp 1 (qua môn) trước đó, FP của
    lớp 0 chính là FN của lớp 1, và ngược lại.
  - Vì hai lớp không cân bằng số lượng (71 bạn qua, 49 bạn rớt), việc
    hoán đổi vai trò này khiến mẫu số của precision và recall thay đổi
    khác nhau, dẫn tới hai bộ con số có độ lớn khác hẳn nhau.
  - Bài học: mỗi khi báo cáo precision/recall, phải luôn nói rõ đang
    tính cho lớp nào, vì cùng một mô hình có thể "trông rất tốt" ở
    lớp này nhưng "trông rất tệ" ở lớp kia.""")