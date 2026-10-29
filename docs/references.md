# Tài liệu tham khảo

## Nguồn chính

- Vijaya Kumar Suda (2024), *Data Labeling in Machine Learning with Python*, Chapter 4 — *Exploring Image Data*. [Google Books](https://books.google.com.vn/books?id=2u_xEAAAQBAJ) (bản xem trước giới hạn; không thay thế toàn văn).
- [Notebook ví dụ Ch04 — PacktPublishing](https://github.com/PacktPublishing/Data-Labeling-in-Machine-Learning-with-Python/tree/main/code/Ch04).
- [Ảnh `roseflower.jpeg` trong kho của tác giả](https://github.com/PacktPublishing/Data-Labeling-in-Machine-Learning-with-Python/blob/main/images/Ch4/roseflower.jpeg) (cần đối chiếu bản quyền/nguồn trước khi phân phối công khai).

## Nguồn bổ trợ

- [HOG — scikit-image](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_hog.html).
- [OpenCV — Geometric Transformations](https://docs.opencv.org/4.10.0/dd/d52/tutorial_js_geometric_transformations.html).

## Chú thích nội dung

- Phần Thiện: code tải/hiển thị ảnh, chuyển grayscale, split RGB, histogram dựa trên ý tưởng và ví dụ của sách; bổ sung histogram 3 kênh, thống kê pixel, xuất hình.
- Phần Tiến: ví dụ CIFAR-10, phân ngưỡng và HOG ở Chapter 4 (trang in 98–101 theo kết quả tìm kiếm trong bản xem trước Google Books). Notebook dùng `x_train[0]`, ảnh xám trung bình ba kênh, threshold 100, cùng cấu hình HOG `pixels_per_cell=(8, 8)`, `cells_per_block=(2, 2)`, `visualize=True`. So sánh 60/100/140 là mở rộng của nhóm; phần giải thích được viết.
- Phần Tú: bổ sung tài liệu đã **thực sự sử dụng** ngay tại notebook và slide tương ứng khi triển khai.
- File `images/roseflower.jpeg` trong repo được giữ từ **ZIP Thiện cung cấp**; chưa đối chiếu byte-for-byte với ảnh trên GitHub.
