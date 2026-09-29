# Chương 2: Hồi quy logistic

**Sinh viên:** Bùi Chí Kiệt <br>
**Mã số sinh viên:** 2374802010255 <br>
**Giảng viên lý thuyết + thực hành:** ThS. Nguyễn Thái Anh <br>
**Học kỳ:** Năm học 2026 – 2027 <br>

---

## Nội dung học

Bài này chuyển từ bài toán dự đoán một con số (hồi quy) sang bài toán phân loại nhị phân: dự đoán một sinh viên qua môn hay rớt môn dựa trên số giờ ôn tập (và điểm giữa kỳ), sử dụng bộ dữ liệu mô phỏng gồm 120 sinh viên. Các nội dung chính bao gồm:

- Vì sao không thể dùng đường thẳng của hồi quy tuyến tính cho nhãn nhị phân (0/1), do đường thẳng cho ra giá trị vượt ngoài khoảng 0–1.
- Hàm sigmoid: công thức, ba tính chất cơ bản, và cách nó ép mọi giá trị thực về khoảng (0, 1) để biểu diễn xác suất.
- Khớp mô hình hồi quy logistic bằng `scikit-learn` (`LogisticRegression`), theo đúng quy trình ba bước `fit` – `predict` / `predict_proba` giống bài 1.
- Ma trận nhầm lẫn (confusion matrix): bốn thành phần TP, TN, FP, FN.
- Bốn thước đo chấm điểm mô hình phân loại: Accuracy, Precision, Recall, F1, và ý nghĩa thực tế của từng con số.
- Ngưỡng quyết định (threshold): mô hình thực chất trả về xác suất, ngưỡng 0.5 chỉ là mặc định; hiểu được sự đánh đổi giữa Precision và Recall khi thay đổi ngưỡng.
- Cách chọn ngưỡng phù hợp theo bài toán thực tế (loại sai lầm nào đắt giá hơn).
- Mở rộng mô hình sang nhiều biến đầu vào, và khái niệm biên quyết định (decision boundary) luôn là một đường thẳng/mặt phẳng trong hồi quy logistic.

## Sau khi học xong, nắm được

- Giải thích được vì sao cần hàm sigmoid thay vì dùng trực tiếp đường thẳng cho bài toán phân loại.
- Tự cài đặt và kiểm chứng được hàm sigmoid.
- Dùng được `LogisticRegression` của `scikit-learn` để huấn luyện mô hình phân loại.
- Đọc được xác suất mô hình trả về và chuyển nó thành nhãn dự đoán.
- Lập được ma trận nhầm lẫn và tính được Accuracy, Precision, Recall, F1 (cả bằng thư viện lẫn bằng công thức tay).
- Tự điều chỉnh ngưỡng quyết định và giải thích được sự đánh đổi giữa Precision và Recall.
- Mở rộng mô hình phân loại sang nhiều biến đầu vào.

## Ghi chú

- Toàn bộ mã nguồn được chạy từ thư mục gốc của bài thực hành (`bai02_hoi_quy_logistic`), theo đúng quy ước đường dẫn tương đối `data/sinh_vien.csv` mà giảng viên yêu cầu.
- Môi trường sử dụng: Python 3.11+, môi trường ảo `venv`, cùng bốn thư viện `numpy`, `pandas`, `matplotlib`, `scikit-learn`.
