# Bài 19: AWS CLI Setup on Windows

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `13528246` (`CLI - Install on Windows v2.mp4`)
- **Thời lượng:** `01:45`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

- **Cài đặt AWS CLI v2 trên Windows:**
  1. Tải bộ cài đặt **MSI Installer** chính thức của AWS CLI version 2 cho Windows (`AWSCLIV2.msi`).
  2. Chạy file `.msi` và nhấn Next -> Install -> Finish.
  3. Mở **Command Prompt** (hoặc PowerShell) và kiểm tra bằng lệnh:
     ```powershell
     aws --version
     ```
  4. Kết quả trả về bắt đầu bằng `aws-cli/2.x.x Python/... Windows/...` nghĩa là đã cài đặt thành công.
- **Cách nâng cấp (Upgrade):** Tải lại bộ cài MSI mới nhất và chạy đè lên bản cũ.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:01` | We are going to install the AWS CLI version 2 on Windows. Search for "aws cli install windows" on Google, scroll down to the Windows section, download the **MSI installer**, and run it (Next -> Accept license -> Install -> Finish). | Để cài đặt AWS CLI v2 trên Windows: tìm trang hướng dẫn cài đặt AWS CLI v2 cho Windows, tải về bộ cài **MSI installer** và chạy trình cài đặt (Next -> Accept -> Install -> Finish). |
| `01:01` - `01:45` | Open Command Prompt on Windows and type `aws --version`. If you get an output starting with `aws-cli/2... Python/... Windows/...`, your AWS CLI is properly installed. To upgrade in the future, simply re-download the MSI installer and re-run it. | Mở Command Prompt và gõ `aws --version`. Nếu kết quả hiển thị `aws-cli/2... Python/... Windows/...` thì bạn đã cài đặt thành công. Khi muốn nâng cấp bản mới, chỉ cần tải lại file MSI và chạy cài đặt lại. |
