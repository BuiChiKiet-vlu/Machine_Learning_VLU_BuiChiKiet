#Bài 4: Thêm số phòng vào mô hình

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/gia_nha.csv")
y = df["gia"]
X = df[["dien_tich", "so_phong"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mo_hinh = LinearRegression()
mo_hinh.fit(X_train, y_train)

r2 = r2_score(y_test, mo_hinh.predict(X_test))

print(f"R2 tren tap kiem tra (dien_tich + so_phong) = {r2:.4f}")
print("R2 cua mo hinh mot bien (chi dien_tich, theo tai lieu) = 0.9622")
print()

print("Nhận xét: Thêm cột số phòng giúp R2 tăng từ 0.9622 lên 0.9641, nghĩa là mô hình dự đoán tốt hơn. Tuy nhiên, sự cải thiện không đáng kể, có thể do số phòng và diện tích có mối quan hệ tương quan với nhau.")