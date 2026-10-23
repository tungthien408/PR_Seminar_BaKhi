# Dataset cỡ lớn (không commit lên Git)

- `data/raw/` dành cho dữ liệu tải về để chạy cục bộ, ví dụ CIFAR-10 nếu cần.
- Git bỏ qua toàn bộ file trong `data/raw/` ngoại trừ `.gitkeep`.
- Chỉ commit **ảnh mẫu nhỏ thực sự cần để tái lập notebook** vào `images/`.
- Trong notebook của Tiến, hãy ghi nguồn, hướng dẫn tải CIFAR-10 và cách chọn ảnh mẫu để người khác tái lập.
