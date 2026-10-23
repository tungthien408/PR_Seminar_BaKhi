# Phân công seminar — Chapter 4

Dựa trên bản phân công nhóm đã duyệt ngày 20/10/2026. [Google Doc gốc](https://docs.google.com/document/d/1wFhBEXDEkIFGgQUre67VVSwvHj6JRZdzt-BljhjsMoU/edit).

| Người | Phần trình bày | Sản phẩm bàn giao | Phần việc chung |
|---|---|---|---|
| **Thiện** | EDA, histogram, RGB/grayscale, channels, kết luận (~7 phút) | `notebooks/01_EDA.ipynb`, 2–3 hình trong `outputs/thien/`, 3–4 slide trong `slides/parts/thien/`, ghi chú thuyết trình | Chọn ý quan trọng; review nội dung kỹ thuật; rà soát quy định nộp |
| **Tiến** | Segmentation theo threshold, HOG (~8 phút) | `notebooks/02_Segmentation_HOG.ipynb`, hình so sánh trong `outputs/tien/`, 3–4 slide trong `slides/parts/tien/` | Đối chiếu kết quả thực nghiệm; so sánh ngưỡng 60/100/140 |
| **Tú** | Aspect ratio, resizing, normalization, augmentation (~10 phút) | `notebooks/03_Preprocessing.ipynb`, hình minh họa trong `outputs/tu/`, 4–5 slide trong `slides/parts/tu/` | Ghép slide cuối `slides/final/Seminar.pptx`, đóng gói bài |

- Tiến cần nhấn mạnh: tỷ lệ pixel qua ngưỡng **không** phải độ chính xác segmentation khi thiếu nhãn đúng.
- Tú cần lưu ý: resize về kích thước cố định có thể **làm méo ảnh** nếu thay đổi aspect ratio.
- Thiện review sản phẩm chung nhưng **không phải** người viết notebook của hai bạn khác.
- **Slide 20–30 phút**: phần chính dự kiến 25 phút, cộng chuyển phần khoảng 1–2 phút.

## Timeline nội bộ

| Mốc | Đầu việc |
|---|---|
| 20–22/10/2026 | Đọc phần được giao, tải code và ảnh |
| 23–26/10/2026 | Notebook chạy được, hình kết quả đầu tiên |
| 27–28/10/2026 | Hoàn thiện notebook, giải thích, slide cá nhân |
| 29–30/10/2026 | Tú tổng hợp PPTX, tài liệu tham khảo |
| 31/10/2026 | Cả nhóm tập thuyết trình, sửa lỗi |
| **01/11/2026** | Hạn **nội bộ**: Tú và Thiện rà soát, đóng gói |
| 02–08/11/2026 | Sẵn sàng nếu xung phong tuần 9 |
| Tuần 10 | Sẵn sàng khi được gọi ngẫu nhiên |

Gói nộp cuối dự kiến chứa PPTX + `Resources/` (notebook, hình minh họa, nguồn và README), **≤30 MB**. Người nộp và mẫu tên ZIP có MSSV vẫn cần xác nhận.
