# Dataset cỡ lớn (không commit lên Git)

- `data/raw/` dành cho dữ liệu tải về và tài liệu tham khảo chỉ dùng cục bộ, ví dụ CIFAR-10 hoặc bản tài liệu Chương 4.
- Tài liệu Chương 4 và mã ví dụ đi kèm hiện nằm trong `data/raw/reference-material/`; `.gitignore` loại chúng khỏi Git.
- Git bỏ qua toàn bộ file trong `data/raw/` ngoại trừ `.gitkeep`.
- Chỉ commit **ảnh mẫu nhỏ thực sự cần để tái lập notebook** vào `images/`.
- Notebook của Tiến dùng `keras.datasets.cifar10.load_data()` và mẫu cố định `x_train[0]`; lần đầu chạy, Keras tải dataset vào cache cục bộ (thường là `~/.keras/datasets/`), không phải `data/raw/`.
