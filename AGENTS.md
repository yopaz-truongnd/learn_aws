# Workspace Security & Operating Rules

## 1. Giới hạn phạm vi chỉnh sửa (Project-Only Edit Scope)
- Chỉ được quyền tạo mới, chỉnh sửa hoặc ghi đè các tệp tin và thư mục nằm trong phạm vi thư mục dự án `learn_aws`.
- Tuyệt đối không tự ý sửa đổi hoặc tạo mới tệp tin ngoài thư mục dự án.

## 2. Thực thi lệnh ngoài dự án (Execution Outside Project Scope)
- Mọi lệnh terminal (PowerShell, CMD, Bash) hoặc thao tác có phạm vi ảnh hưởng ngoài thư mục `learn_aws` bắt buộc phải giải thích lý do và hỏi ý kiến xác nhận của người dùng trước khi chạy.

## 3. Chính sách bảo vệ tệp tin: Bắt buộc xác nhận khi xóa (File Deletion Protection)
- Tuyệt đối không tự ý xóa file hoặc thư mục (kể cả tệp tạm, file build hay file dữ liệu).
- Khi cần xóa, phải liệt kê danh sách tệp dự kiến xóa và chờ người dùng xác nhận đồng ý mới được thực hiện.
