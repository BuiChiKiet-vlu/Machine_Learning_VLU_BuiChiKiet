# Chương 1: Hồi quy tuyến tính

**Sinh viên:** Bùi Chí Kiệt
**Mã số sinh viên:** 2374802010255
**Giảng viên lý thuyết + thực hành:** ThS. Nguyễn Thái Anh
**Học kỳ:** Năm học 2026 – 2027

---

## Nội dung học

Bài này xây dựng một mô hình dự đoán giá căn hộ dựa trên diện tích (và mở rộng thêm số phòng, tuổi nhà), sử dụng bộ dữ liệu mô phỏng gồm 60 căn hộ. Các nội dung chính bao gồm:

- Đọc và khảo sát dữ liệu dạng bảng bằng thư viện `pandas`, kiểm tra kích thước, giá trị thiếu, và thống kê mô tả.
- Khái niệm hồi quy tuyến tính: mô hình một đường thẳng `ŷ = w·x + b` dự đoán một giá trị liên tục.
- Cách đo sai số của mô hình bằng MSE (sai số toàn phương trung bình), và vì sao không thể cộng thẳng các sai số lại với nhau.
- Hai cách tìm hệ số `w` và `b` tối ưu: công thức bình phương tối thiểu (closed-form) và thư viện `scikit-learn` (`LinearRegression`), đối chiếu để xác nhận hai cách cho cùng kết quả.
- Đánh giá mô hình đúng cách: chia tập học/tập kiểm tra (`train_test_split`), và bốn thước đo MAE, MSE, RMSE, R².
- Cơ chế gradient descent: cách máy tự dò lời giải từng bước nhỏ khi không có công thức đóng, vai trò của tốc độ học (learning rate) và bước chuẩn hoá dữ liệu.
- Mở rộng mô hình sang nhiều biến đầu vào (hồi quy tuyến tính bội), cách đọc hệ số của từng biến, và giới hạn của việc ngoại suy ra ngoài khoảng dữ liệu đã học.

## Sau khi học xong, nắm được

- Giải thích được hồi quy tuyến tính là gì và ý nghĩa của hệ số góc, hệ số chặn.
- Đọc và xử lý dữ liệu CSV bằng `pandas`.
- Tính và diễn giải được MSE, MAE, RMSE, R².
- Dùng được cả công thức tay và `scikit-learn` để huấn luyện mô hình hồi quy tuyến tính.
- Hiểu và cài đặt được gradient descent cơ bản, biết cách chọn tốc độ học phù hợp.
- Xây dựng được mô hình hồi quy tuyến tính với nhiều biến đầu vào.

## Cấu trúc thư mục nộp bài

```
bai01_hoi_quy/
├── data/gia_nha.csv
├── code/               (các tệp mẫu b1 → b7)
└── baitap01/           (bài làm: bai1.py → bai6.py, bai2.png)
```

## Ghi chú

- Toàn bộ mã nguồn được chạy từ thư mục gốc của bài thực hành (`bai01_hoi_quy`), theo đúng quy ước đường dẫn tương đối `data/gia_nha.csv` mà giảng viên yêu cầu.
- Môi trường sử dụng: Python 3.11+, môi trường ảo `venv`, cùng bốn thư viện `numpy`, `pandas`, `matplotlib`, `scikit-learn`.
