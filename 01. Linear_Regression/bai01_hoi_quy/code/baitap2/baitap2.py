#Bài 2: Vẽ biểu đồ phân tán theo số phòng

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/gia_nha.csv")

plt.figure(figsize=(7, 5))
plt.scatter(df["so_phong"], df["gia"], color="tab:blue")
plt.xlabel("So phong ngu")
plt.ylabel("Gia (ty dong)")
plt.title("Gia nha theo so phong ngu")


plt.savefig("bai2.png", dpi=150)
plt.show()
 
print("Nhận xét: Biểu đồ phân tán cho thấy mối quan hệ giữa số phòng ngủ và giá nhà. Có thể thấy rằng, khi số phòng ngủ tăng lên, giá nhà cũng có xu hướng tăng. Tuy nhiên, vẫn có một số căn hộ có giá cao nhưng số phòng ngủ thấp, điều này có thể do các yếu tố khác như vị trí, diện tích hoặc tiện ích đi kèm.")
