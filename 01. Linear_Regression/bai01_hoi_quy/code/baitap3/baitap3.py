#Bài 3: Đổi biến đầu vào sang tuổi nhà

import numpy as np
import pandas as pd
 
df = pd.read_csv("data/gia_nha.csv")
x = df["tuoi_nha"].to_numpy()
y = df["gia"].to_numpy()
 
x_tb = x.mean()
y_tb = y.mean()
 
tu_so = ((x - x_tb) * (y - y_tb)).sum()
mau_so = ((x - x_tb) ** 2).sum()
 
w = tu_so / mau_so
b = y_tb - w * x_tb
 
print(f"He so goc w = {w:.6f}")
print(f"He so chan b = {b:.6f}")
print()

print("Nhận xét: w mang dấu âm, nghĩa là nhà càng cũ, giá nhà càng giảm. Điều này phù hợp với thực tế. Vì nhà mới xây thường được định giá cao hơn nhà đã cũ.")