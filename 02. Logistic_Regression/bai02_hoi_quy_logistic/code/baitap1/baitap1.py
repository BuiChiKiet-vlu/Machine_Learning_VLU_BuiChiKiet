#Bài 1:

import pandas as pd

df = pd.read_csv('data/sinh_vien.csv')

diem_cao = df[df['diem_giua_ky'] >= 7]
diem_thap = df[df['diem_giua_ky'] < 7]

ty_le_qua_mon_diem_cao = diem_cao["qua_mon"].mean()
ty_le_qua_mon_diem_thap = diem_thap["qua_mon"].mean()

print(f"Danh sách sinh viên có điểm cao (>= 7): {len(diem_cao)} sinh viên")
print(f"Tỷ lệ qua môn (điểm cao): {ty_le_qua_mon_diem_cao:.2f}")
print(f"Tỷ lệ qua môn (điểm thấp): {ty_le_qua_mon_diem_thap:.2f}")
print()

print("Nhận xét: Điểm giữa kỳ có phân biệt rõ ràng về tỷ lệ qua môn. Sinh viên có điểm giữa kỳ cao (>= 7) có tỷ lệ qua môn cao hơn so với sinh viên có điểm giữa kỳ thấp (< 7).")