#Bài 1: Lọc ra nhóm căn hộ lớn 
import pandas as pd

df = pd.read_csv("data/gia_nha.csv")
print(df.head())

nhom_lon = df[df['dien_tich'] > 100]

so_can_lon = len(nhom_lon)
gia_trung_binh = nhom_lon["gia"].mean()
 
print(f"So can co dien tich > 100 m2: {so_can_lon}")
print(f"Gia trung binh cua nhom nay: {gia_trung_binh:.4f} ty dong")