# Bài 21: AWS CLI Setup on Linux

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `13528250` (`CLI - Install on Linux v2.mp4`)
- **Thời lượng:** `01:30`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

- **Cài đặt AWS CLI v2 trên Linux bằng 3 câu lệnh Terminal:**
  ```bash
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  unzip awscliv2.zip
  sudo ./aws/install
  ```
- Kiểm tra sau khi cài đặt:
  ```bash
  aws --version
  ```
  Kết quả hiển thị `aws-cli/2.x.x Python/... Linux/... botocore/...`.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:52` | Let's install the AWS CLI Version 2 on Linux. We just run three commands in the terminal: 1) download the zip file using `curl`, 2) `unzip` the installer, and 3) run the installer as root using `sudo ./aws/install`. | Để cài đặt AWS CLI v2 trên Linux, ta chạy 3 lệnh trong terminal: 1) tải file nén `.zip` bằng `curl`, 2) giải nén bằng `unzip`, và 3) chạy cài đặt với quyền root bằng lệnh `sudo ./aws/install`. |
| `00:52` - `01:30` | Now run `aws --version` in the terminal. It outputs `aws-cli/2... Python/... Linux/... botocore/...`, confirming the AWS CLI is installed and ready. | Sau đó chạy lệnh `aws --version`. Kết quả hiển thị `aws-cli/2... Python/... Linux/... botocore/...` xác nhận AWS CLI đã sẵn sàng sử dụng. |
