# Bài 20: AWS CLI Setup on Mac OS X

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `13528248` (`CLI - Install on Mac v2.mp4`)
- **Thời lượng:** `01:28`

---

## 1. Kiến thức trọng tâm (Exam Notes)

- **Cài đặt AWS CLI v2 trên macOS:**
  1. Tải bộ cài đặt giao diện đồ họa `.pkg` (`AWSCLIV2.pkg`) từ trang chủ AWS.
  2. Mở file `.pkg`, chọn cài đặt cho tất cả người dùng trên máy (**Install for all users on this computer**) và hoàn tất.
  3. Mở ứng dụng **Terminal** (hoặc iTerm) và kiểm tra bằng lệnh:
     ```bash
     aws --version
     ```
  4. Kết quả trả về `aws-cli/2.x.x ...` xác nhận cài đặt thành công.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:48` | Let's install the AWS CLI version 2 on macOS. From the AWS documentation page, download the `.pkg` graphical installer file. Open it, click Continue, agree to the license, choose "Install for all users on this computer", and click Install. | Để cài đặt AWS CLI v2 trên macOS: tải file bộ cài đồ họa `.pkg` từ tài liệu AWS. Mở file, nhấn Continue, đồng ý điều khoản, chọn cài đặt cho mọi người dùng trên máy và nhấn Install. |
| `00:48` - `01:28` | Open a terminal on Mac (Terminal or iTerm) and type `aws --version`. It returns `aws-cli/2...`, meaning everything has been installed correctly. | Mở ứng dụng Terminal trên Mac và gõ lệnh `aws --version`. Kết quả trả về `aws-cli/2...` nghĩa là đã cài đặt thành công. |
