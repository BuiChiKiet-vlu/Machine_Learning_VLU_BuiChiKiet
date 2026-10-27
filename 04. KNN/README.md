# Chương 4: K láng giềng gần nhất (KNN)

**Sinh viên:** Bùi Chí Kiệt <br>
**Mã số sinh viên:** 2374802010255 <br>
**Giảng viên lý thuyết + thực hành:** ThS. Nguyễn Thái Anh <br>
**Học kỳ:** Năm học 2026 – 2027 <br>

---

## Nội dung học

Bài này giới thiệu một mô hình làm ngược lại các bài trước: thay vì rút dữ liệu huấn luyện thành vài con số rồi bỏ đi, KNN giữ nguyên toàn bộ dữ liệu và, khi gặp mẫu mới, đi hỏi những mẫu cũ giống nó nhất. Bài dùng bộ sinh viên mở rộng (có thêm cột chi tiêu), bộ dữ liệu hai vầng trăng gồm 300 điểm có ranh giới cong, và dùng lại bộ giá nhà của bài 1. Các nội dung chính bao gồm:

- Khoảng cách Euclid và ý tưởng láng giềng gần nhất; tự cài đặt việc tìm k láng giềng bằng `numpy`; KNN là mô hình học lười (lazy learning).
- Chuẩn hoá dữ liệu (`StandardScaler`): vì sao một cột thang đo lớn nuốt trọn khoảng cách và làm KNN tệ hơn cả đoán bừa.
- Gộp chuẩn hoá và mô hình bằng `make_pipeline` để tránh rò rỉ dữ liệu.
- Chọn số láng giềng k bằng kiểm định chéo, không nhìn tập kiểm tra; k nhỏ thì học vẹt, k lớn thì cẩu thả, nên chọn k lẻ.
- So sánh KNN với hồi quy logistic và Naive Bayes trên dữ liệu có biên cong; mô hình không tham số và lời nguyền số chiều.
- KNN cho bài toán hồi quy (`KNeighborsRegressor`) và vì sao KNN không ngoại suy được ra ngoài vùng dữ liệu đã thấy.

## Sau khi học xong, nắm được

- Tự tính được khoảng cách Euclid và tìm được k láng giềng gần nhất bằng `numpy`.
- Chỉ ra được vì sao thang đo ảnh hưởng tới KNN và chữa bằng chuẩn hoá.
- Dùng được `make_pipeline` để gộp chuẩn hoá với mô hình đúng cách.
- Chọn được k bằng kiểm định chéo mà vẫn giữ tập kiểm tra nguyên vẹn.
- So sánh được KNN với các mô hình đã học và giải thích khi nào KNN thắng, khi nào thua.
- Dùng được KNN cho hồi quy và giải thích được giới hạn ngoại suy của nó.

## Cấu trúc thư mục nộp bài

```
bai04_knn/
├── data/
│   ├── sinh_vien_mo_rong.csv
│   ├── hai_vang_trang.csv
│   └── gia_nha.csv
├── code/               (các tệp mẫu e1 → e5)
└── baitap04/           (bài làm: bai1.py → bai6.py, NHAN_XET.md)
```

## Ghi chú

- Toàn bộ mã nguồn được chạy từ thư mục gốc của bài thực hành (`bai04_knn`), theo đúng quy ước đường dẫn tương đối `data/hai_vang_trang.csv` mà giảng viên yêu cầu.
- Môi trường sử dụng: Python 3.11+, môi trường ảo `venv`, cùng bốn thư viện `numpy`, `pandas`, `matplotlib`, `scikit-learn`.
- Phần nhận xét và giải thích bằng lời cho từng bài tập nằm trong tệp `NHAN_XET.md` của thư mục `baitap04`.
