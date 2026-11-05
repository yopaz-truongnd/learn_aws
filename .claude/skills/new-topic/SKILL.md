---
name: new-topic
description: Tạo trang cheat sheet topics/aws_<topic>.html mới cho một chủ đề/dịch vụ AWS (SAA-C03), theo đúng mẫu và quy ước của topics/aws_iam.html.
argument-hint: <chủ đề AWS, ví dụ "EC2" hoặc "S3 Storage Classes"> [ghi chú/nội dung nguồn tùy chọn]
---

# /new-topic

Tạo một trang cheat sheet ôn thi SAA-C03 cho chủ đề: **$ARGUMENTS**

Nếu `$ARGUMENTS` trống, hỏi người dùng chủ đề AWS muốn tạo rồi mới làm tiếp.

## Các bước

1. **Đặt tên file**: `topics/aws_<slug>.html` (trong thư mục `topics/`; trang con dùng link `../index.html` để quay về Dashboard). `slug` viết thường, các từ nối bằng `_` (ví dụ `topics/aws_ec2.html`, `topics/aws_s3_storage_classes.html`). Nếu file đã tồn tại, hỏi người dùng muốn ghi đè, cập nhật hay đổi tên. Không tự ghi đè.

2. **Liên kết tài nguyên dùng chung**:
   - Trong thẻ `<head>`:
     ```html
     <link rel="stylesheet" href="../assets/css/style.css">
     <script src="../assets/vendor/mermaid.min.js"></script> <!-- nếu có dùng diagram -->
     <script src="../assets/js/app.js"></script>
     ```
   - Tuyệt đối không nhúng lại khối `<style>` hay code script trùng lặp vào file HTML con; toàn bộ design system, Dark/Light tokens, component matrix và logic song ngữ đã nằm trong `assets/`.

3. **Thu thập nội dung & Nguồn bài giảng**:
   - Nếu người dùng đưa ghi chú hoặc nội dung nguồn trong lệnh, dùng nó làm chính.
   - Tham khảo `data/lecturesub-tu-vung.csv` (đọc bằng CSV parser vì có trường chứa dấu phẩy và xuống dòng): trích xuất từ vựng, câu gốc và link bài giảng Udemy tương ứng.
   - Bổ sung kiến thức AWS chính xác, tập trung vào những gì đề SAA-C03 hay hỏi. Không bịa số liệu (giới hạn, giá, SLA); không chắc thì bỏ qua hoặc ghi "kiểm tra lại tài liệu AWS".

4. **Viết trang** theo cấu trúc của `topics/aws_iam.html`:
   - `<html lang="vi">`, `<title>AWS <Chủ đề> — SAA-C03</title>`.
   - `.top-nav`: `.nav-back` và `.lang-switch` (nút chuyển đổi `🇻🇳 VI` / `🇬🇧 EN`).
   - `.header`: `.badge` (phạm vi dịch vụ, ví dụ `Global Service` / `Regional Service` / `AZ-scoped`), `h1` tên đầy đủ, `p` mô tả ngắn song ngữ (`.lang-vi` và `.lang-en`).
   - `.grid` gồm các `.card` (dùng `.full` cho card cần rộng). Mỗi card có `.ch` với icon emoji trong `.ci` (nền bằng token `--*b`), `.ct` tiêu đề đánh số, `.cs` phụ đề.
   - Dùng lại component có sẵn cho hợp nội dung: `.g2/.it` (khái niệm), `.flow/.st/.ar` (luồng xử lý, thứ tự), `.cols/.pi` (so sánh), `.tag` (từ khóa), `.sl` (danh sách có icon), `.tools` (công cụ), `.json` (cấu hình/policy, tô màu bằng `.jk/.jv/.jc/.jp`).
   - Hỗ trợ song ngữ (Bilingual) xuyên suốt nội dung bằng các thẻ `.lang-vi` và `.lang-en`.
   - Nên có các phần: khái niệm cốt lõi → cách hoạt động/kiến trúc → so sánh các lựa chọn → bảo mật/giám sát nếu liên quan → card **"Bổ sung hay gặp trong đề thi"** → card **"Nguyên tắc vàng — SAA-C03"** dạng `.bp/.bi` (mục cảnh báo quan trọng nhất dùng `.bn` nền `--rd`) → card **"Nguồn bài giảng & Tài liệu tìm hiểu thêm (Further Study Resources)"** (3 cột: Video bài giảng Udemy, AWS Docs/Whitepapers, và Cheat Sheet bổ trợ).
   - Tên dịch vụ và thuật ngữ AWS giữ tiếng Anh. Escape `&` thành `&amp;`.
   - Cơ chế tự chứa (self-contained), không kéo tài nguyên ngoài (CDN, Google Fonts, external CSS/JS). Script chuyển ngôn ngữ inline siêu gọn và lưu qua `localStorage`.

5. **Kiểm tra & Cập nhật Dashboard**:
   - HTML đóng thẻ đầy đủ; mọi màu đều đi qua `var(--...)` (trừ khối `.json`); trên màn hình hẹp không bị cuộn ngang.
   - Cập nhật `index.html`: Thêm link, đổi trạng thái từ "Sắp ra mắt" sang "Đã có", tăng biến đếm số bài hoàn thành.
   - Mở trang bằng `open topics/aws_<slug>.html` để người dùng xem.

6. **Báo lại** bằng tiếng Việt: tên file, các phần đã tạo, nguồn bài giảng đã gắn kèm, và những chỗ người dùng nên tự kiểm tra lại.
