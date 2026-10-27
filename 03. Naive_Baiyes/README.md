# Chương 3: Naive Bayes

**Sinh viên:** Bùi Chí Kiệt <br>
**Mã số sinh viên:** 2374802010255 <br>
**Giảng viên lý thuyết + thực hành:** ThS. Nguyễn Thái Anh <br>
**Học kỳ:** Năm học 2026 – 2027 <br>

---

## Nội dung học

Bài này chuyển sang một cách học khác hẳn hai bài trước: thay vì vẽ ranh giới, mô hình mô tả mỗi lớp trông như thế nào rồi hỏi lớp nào dễ sinh ra mẫu đang xét hơn. Ứng dụng chính là bộ lọc tin nhắn rác trên bộ dữ liệu mô phỏng gồm 300 tin nhắn, đồng thời dùng lại bộ sinh viên của bài 2 để so sánh công bằng. Các nội dung chính bao gồm:

- Định lý Bayes: tiên nghiệm, khả năng, bằng chứng, hậu nghiệm; giải thích vì sao xét nghiệm chính xác 99 phần trăm vẫn có thể báo nhầm quá nửa số ca, bằng cả cách đếm người lẫn công thức.
- Biến văn bản thành bảng số bằng túi từ (bag of words) và `CountVectorizer`, cùng giới hạn của cách làm này (mất thứ tự từ).
- Công thức Naive Bayes và giả định ngây thơ: huấn luyện chỉ là đếm; dùng `MultinomialNB` để lọc tin nhắn rác.
- Chấm điểm bộ lọc bằng ma trận nhầm lẫn, Precision, Recall; vì sao với thư rác sai kiểu FP đắt hơn FN, và vì sao xác suất của Naive Bayes thường quá tự tin.
- Vấn đề số không và làm trơn Laplace (tham số `alpha`), tự cài đặt lại để thấy tận mắt; hiện tượng tràn dưới (underflow) và cách chữa bằng cộng loga.
- Naive Bayes cho số liệu liên tục (`GaussianNB`), so sánh với hồi quy logistic của bài 2, và vì sao Naive Bayes trụ tốt khi dữ liệu ít.
- Phân biệt ba biến thể `MultinomialNB`, `GaussianNB`, `BernoulliNB` và hậu quả của việc chọn sai.

## Sau khi học xong, nắm được

- Tính được xác suất hậu nghiệm bằng định lý Bayes, cả bằng công thức lẫn bằng cách đếm.
- Giải thích được hậu quả của việc đảo hai vế của xác suất có điều kiện.
- Biến một tập văn bản thành bảng số bằng `CountVectorizer`.
- Huấn luyện và chấm điểm được bộ lọc tin rác bằng `MultinomialNB`.
- Chỉ ra được chỗ mô hình gãy khi bỏ làm trơn Laplace, và tự viết được bộ lọc không dùng thư viện học máy.
- Dùng được `GaussianNB` cho số liệu liên tục và so sánh với hồi quy logistic.
- Nhận ra được lỗi im lặng khi chọn sai biến thể Naive Bayes hoặc khi dữ liệu mất cân bằng lớp.

## Cấu trúc thư mục nộp bài

```
bai03_naive_bayes/
├── data/
│   ├── tin_nhan.csv
│   └── sinh_vien.csv
├── code/               (các tệp mẫu d1 → d5)
└── baitap03/           (bài làm: bai1.py → bai6.py, NHAN_XET.md)
```

## Ghi chú

- Toàn bộ mã nguồn được chạy từ thư mục gốc của bài thực hành (`bai03_naive_bayes`), theo đúng quy ước đường dẫn tương đối `data/tin_nhan.csv` mà giảng viên yêu cầu.
- Môi trường sử dụng: Python 3.11+, môi trường ảo `venv`, cùng bốn thư viện `numpy`, `pandas`, `matplotlib`, `scikit-learn`.
- Phần nhận xét và giải thích bằng lời cho từng bài tập nằm trong tệp `NHAN_XET.md` của thư mục `baitap03`.
