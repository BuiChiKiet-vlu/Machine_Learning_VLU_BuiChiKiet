#Bài 4: 

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/sinh_vien.csv")
X = df[["gio_on"]]
y = df["qua_mon"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=17, stratify=y
)

print("So sinh vien de hoc :", len(X_train))
print("So sinh vien de kiem tra:", len(X_test))
print()

mo_hinh = LogisticRegression()
mo_hinh.fit(X_train, y_train)

y_pred = mo_hinh.predict(X_test)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("Ma tran nham lan (lay tu confusion_matrix, khong dung cac ham")
print("accuracy_score/precision_score/recall_score/f1_score cua thu vien)")
print(f"  TN = {tn}, FP = {fp}, FN = {fn}, TP = {tp}")
print()

n = tp + tn + fp + fn
accuracy = (tp + tn) / n
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)

print("Bon thuoc do tu tinh bang cong thuc:")
print(f"  Accuracy  = ({tp} + {tn}) / {n} = {accuracy:.4f}")
print(f"  Precision = {tp} / ({tp} + {fp}) = {precision:.4f}")
print(f"  Recall    = {tp} / ({tp} + {fn}) = {recall:.4f}")
print(f"  F1        = 2 * (P * R) / (P + R) = {f1:.4f}")
print()

print("""Giải thích:
  - Accuracy: tỷ lệ dự đoán đúng trên tổng số mẫu.
  - Precision: tỷ lệ dự đoán dương đúng trên tổng số dự đoán dương.
  - Recall: tỷ lệ dự đoán đúng trên tổng số mẫu dương thực tế.
  - F1 Score: trung bình điều hòa của Precision và Recall.

  Bốn con số tự tính bằng tay phải khớp chính xác với bốn con số mà
  các hàm accuracy_score, precision_score, recall_score, f1_score của
  scikit-learn trả về, vì cả hai cách đều xuất phát từ đúng bốn số
  TP, TN, FP, FN lấy từ ma trận nhầm lẫn, rồi áp dụng đúng một công
  thức toán học giống nhau. Thư viện không hề tính theo cách khác hay
  dùng thuật toán bí mật nào, nó chỉ code hoá sẵn đúng công thức này.
  Vì vậy việc hai kết quả trùng khớp là bằng chứng cho thấy đã hiểu
  và cài đặt đúng bản chất của bốn thước đo, chứ không phải sự trùng
  hợp ngẫu nhiên.""")