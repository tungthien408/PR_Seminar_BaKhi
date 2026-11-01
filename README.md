# Seminar Nhận diện mẫu — Chapter 4: Exploring Image Data

Repo chung của nhóm **Bá Khí**, phục vụ bài seminar môn Nhận diện mẫu.

**Nguyên tắc:** mỗi bạn làm notebook riêng; dùng chung dữ liệu ảnh cần thiết; lưu ảnh kết quả và slide theo từng người; một bản PPTX cuối cùng do Tú tổng hợp.

## Ai phụ trách gì?

| Người | Notebook | Công việc chính | Slide |
|---|---|---|---|
| Thiện | `01_EDA.ipynb` | RGB, grayscale, channels, histogram, EDA; kiểm tra kỹ thuật toàn bài | 3–4 slide, ~7 phút |
| Tiến | `02_Segmentation_HOG.ipynb` | Segmentation, HOG, so sánh threshold 60/100/140 | 3–4 slide, ~8 phút |
| Tú | `03_Preprocessing.ipynb` | Aspect ratio, resize, normalization, augmentation; ghép bài | 4–5 slide, ~10 phút |

**Trạng thái hiện tại:** Notebook Thiện đã có code và kết quả chạy; phần Tiến đã có notebook thực thi, ba hình thí nghiệm và 4 slide; notebook Tú vẫn là khung TODO. Trước khi bàn giao, mỗi người cần chạy lại notebook trên máy mình.

## Cấu trúc repo

```text
PR_Seminar_Chapter04/
├── README.md                    # Bắt đầu tại đây
├── requirements.txt            # Phần chung, gồm thư viện cho notebook Tiến
├── requirements-tu.txt         # Phần mở rộng cho Tú
├── .gitignore
├── notebooks/
│   ├── 01_EDA.ipynb              # Thiện — hoàn chỉnh
│   ├── 02_Segmentation_HOG.ipynb # Tiến — segmentation và HOG
│   └── 03_Preprocessing.ipynb    # Tú — khung TODO
├── images/
│   ├── roseflower.jpeg          # Ảnh mẫu chung từ ZIP ban đầu
│   └── samples/                 # Thêm ảnh nhỏ cần cho demo
├── data/raw/                   # Dataset/tài liệu tham khảo cục bộ (không commit vào Git)
├── outputs/
│   ├── thien/                   # 3 PNG từ notebook 01
│   ├── tien/                    # PNG của Tiến
│   └── tu/                      # PNG của Tú
├── slides/
│   ├── parts/{thien,tien,tu}/   # Slide cá nhân
│   └── final/                   # Seminar.pptx chung
├── docs/                       # Phân công, nguồn, checklist
└── scripts/
    └── package_submission.py   # Chỉ dùng khi hoàn thiện bài
```

Các thư mục đang trống chứa `.gitkeep` để Git lưu cấu trúc. Các hình đã xuất trong `outputs/thien/` được giữ lại để dùng cho slide.

## Khởi động (VS Code/Jupyter)

Mở **toàn bộ thư mục repo** bằng VS Code, không chỉ mở một notebook rời.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Mở notebook trong `notebooks/`, chọn kernel của `.venv` và chọn **Run All**. Notebook Tú dùng ảnh mẫu trong `images/` và xuất PNG vào `outputs/tu/`. Tài liệu tham khảo và dataset chỉ dùng cục bộ có thể đặt trong `data/raw/`; thư mục này không được đưa lên Git.

- Tiến: `requirements.txt` đã gồm TensorFlow và scikit-image cho CIFAR-10/HOG; chạy notebook 02, lần đầu Keras sẽ tải CIFAR-10 vào cache máy cục bộ.
- Tú: `python -m pip install -r requirements-tu.txt` rồi hoàn thiện notebook 03; bổ sung phụ thuộc khác nếu chọn kỹ thuật khác.
- CIFAR-10 tải lúc chạy hoặc sử dụng cache ở máy từng người; **không đẩy nguyên dataset lên Git**.

## Quy tắc làm việc nhóm

1. Mỗi người chỉ chỉnh notebook, ảnh đầu ra và slide thuộc phần mình; chia sẻ sample vào `images/samples/` khi thật sự cần.
2. Trước khi bàn giao, chạy **Run All**, tự kiểm tra kết quả và lưu 2–3 hình kết quả tiêu biểu. Tránh commit dữ liệu lớn, `.venv` hoặc cache.
3. Nếu dùng GitHub, mỗi người làm branch riêng: `feature/thien-eda`, `feature/tien-hog`, `feature/tu-preprocessing`; tạo Pull Request vào `main` để người còn lại review. Không cần tạo ba repo riêng.
4. Tiến chịu trách nhiệm đối chiếu thí nghiệm; Thiện review nội dung kỹ thuật; Tú tổng hợp PPTX. Người sở hữu tự sửa phần mình.
5. Tú xuất file cuối: `slides/final/Seminar.pptx` và phối hợp Thiện kiểm tra trước khi nộp.

Chi tiết trách nhiệm trong [`docs/phan-cong.md`](docs/phan-cong.md); nguồn trong [`docs/references.md`](docs/references.md); checklist tại [`docs/checklist-nop-bai.md`](docs/checklist-nop-bai.md).

## Đóng gói nộp bài

Khi 3 notebook và slide cuối đã hoàn chỉnh:

```bash
python scripts/package_submission.py --output submission/Seminar_submission_DRAFT.zip
```

Script chỉ lấy **PPTX cuối**, 3 notebook, ảnh demo/kết quả và README, nguồn tham khảo. Nó **không** lấy môi trường ảo/dataset gốc; sẽ báo lỗi nếu notebook còn `TODO:` hoặc thiếu PPTX. Đổi tên ZIP theo **quy định chính thức của giảng viên** sau khi nhóm xác nhận mẫu MSSV (bản phân công hiện chỉ nêu hai MSSV dù nhóm có ba người). Dung lượng tối đa: **30 MB**.

**Lưu ý:** ZIP repo này dùng để làm việc; **không phải** ZIP bài nộp cuối cùng.
