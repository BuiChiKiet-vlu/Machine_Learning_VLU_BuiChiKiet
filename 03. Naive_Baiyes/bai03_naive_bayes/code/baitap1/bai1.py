# -*- coding: utf-8 -*-
"""Bài tập 1 (bài 3): Bayes với ba nguyên nhân."""


def bayes_nhieu_nhanh(tien_nghiem, kha_nang):
    """Hậu nghiệm cho nhiều nhánh.

    tien_nghiem : danh sách P(nhóm i)
    kha_nang    : danh sách P(bằng chứng | nhóm i)
    Mẫu số là xác suất toàn phần: tổng của mọi nhánh.
    """
    tu_so = [p * l for p, l in zip(tien_nghiem, kha_nang)]
    mau_so = sum(tu_so)
    return [t / mau_so for t in tu_so]


nhom = ["hoc deu", "hoc don", "it hoc"]
tien_nghiem = [0.50, 0.30, 0.20]
ty_le_qua = [0.95, 0.70, 0.30]

hau_nghiem = bayes_nhieu_nhanh(tien_nghiem, ty_le_qua)
print("Gap mot ban da qua mon. Xac suat ban do thuoc tung nhom:")
for ten, p in zip(nhom, hau_nghiem):
    print(f"  {ten:8s}: {p:.4f}")
print(f"Tong ba xac suat = {sum(hau_nghiem):.4f}  (phai bang 1)")
print()

# Kiểm lại bằng cách đếm trên 1000 sinh viên
print("Kiem lai bang cach dem tren 1000 sinh vien:")
so_qua = [1000 * p * q for p, q in zip(tien_nghiem, ty_le_qua)]
tong_qua = sum(so_qua)
for ten, n in zip(nhom, so_qua):
    print(f"  {ten:8s}: {n:6.1f} ban qua mon -> {n / tong_qua:.4f}")
print(f"  Tong so ban qua mon = {tong_qua:.1f}")
