# Dataset cỡ lớn (không commit lên Git)

- `data/raw/` dành cho dữ liệu tải về và tài liệu tham khảo chỉ dùng cục bộ, ví dụ CIFAR-10 hoặc bản tài liệu Chương 4.
- Tài liệu Chương 4 và mã ví dụ đi kèm hiện nằm trong `data/raw/reference-material/`; `.gitignore` loại chúng khỏi Git.
- Git bỏ qua toàn bộ file trong `data/raw/` ngoại trừ `.gitkeep`.
- Chỉ commit **ảnh mẫu nhỏ thực sự cần để tái lập notebook** vào `images/`.
- Trong notebook của Tiến, hãy ghi nguồn, hướng dẫn tải CIFAR-10 và cách chọn ảnh mẫu để người khác tái lập.
