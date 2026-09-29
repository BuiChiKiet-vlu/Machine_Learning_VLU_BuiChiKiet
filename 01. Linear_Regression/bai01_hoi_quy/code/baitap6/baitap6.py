#Bài 6: Viết hàm dự đoán có cảnh báo

W = 0.078367
B = 0.401752
dien_tich_nho_nhat = 35.5
dien_tich_lon_nhat = 117.5


def du_doan_gia(dien_tich):
    if dien_tich < dien_tich_nho_nhat or dien_tich > dien_tich_lon_nhat :
        print(f"Canh bao: dien tich {dien_tich} m2 nam ngoai khoang du"
              f" lieu da hoc ({dien_tich_nho_nhat} den"
              f" {dien_tich_lon_nhat} m2). Ket qua chi la ngoai suy,"
              f" khong dang tin cay hoan toan.")
    return W * dien_tich + B


for dt in [60, 80, 200]:
    gia_du_doan = du_doan_gia(dt)
    print(f"Can {dt} m2 -> du doan {gia_du_doan:.3f} ty dong")
    print()