# Bài 38: How to SSH using Linux or Mac

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `13528044` (`CCP_-_EC2_-_SSH_Linux_Mac_v2.mp4`)
- **Thời lượng:** `07:05`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### Quy trình chuẩn để SSH vào Amazon Linux 2 từ Linux / macOS
1. **Kiểm tra điều kiện cần:**
   - File khóa `EC2Tutorial.pem` đã được tải về máy (nên xóa khoảng trắng trong tên file nếu có) và terminal đang đứng đúng tại thư mục chứa file `.pem` đó.
   - Security Group của EC2 Instance đã mở **Port 22 (SSH)** ở chiều Inbound.
2. **Phân quyền bảo mật cho file `.pem` (Bắt buộc trên Linux/Mac):**
   - Nếu chạy SSH ngay sẽ gặp lỗi **`WARNING: UNPROTECTED PRIVATE KEY FILE!`** vì quyền truy cập file quá rộng.
   - Chạy lệnh thu hẹp quyền chỉ cho phép chủ sở hữu đọc (Read-only):
     ```bash
     chmod 0400 EC2Tutorial.pem
     ```
3. **Thực thi lệnh kết nối SSH:**
   - User mặc định trên **Amazon Linux 2** luôn là **`ec2-user`**.
   ```bash
   ssh -i EC2Tutorial.pem ec2-user@<Public-IPv4-Address>
   ```
   - Gõ `yes` khi được hỏi xác nhận fingerprint ở lần kết nối đầu tiên.
4. **Thoát phiên SSH:** Gõ lệnh `exit` hoặc nhấn tổ hợp phím `Ctrl + D`.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:17` | Let's SSH into our EC2 instance from a Linux or Mac computer over Port 22. First, make sure your downloaded key file has no spaces in its name (`EC2Tutorial.pem`) and place it in a folder like `aws-course`. Verify your EC2 instance has a Public IPv4 address and its Security Group allows inbound **Port 22 (SSH)**. | Hãy kết nối SSH vào EC2 instance từ máy Linux hoặc Mac qua cổng 22. Trước tiên, đảm bảo file khóa không có dấu cách (`EC2Tutorial.pem`) và đặt vào thư mục làm việc. Kiểm tra EC2 đã có Public IPv4 và Security Group đã mở cổng **Port 22 (SSH)**. |
| `02:17` - `05:19` | On Amazon Linux 2 AMI, the default user is **`ec2-user`**. If we just run `ssh ec2-user@<public-ip>` without specifying the key, authentication fails. Using `cd` and `ls`, navigate your terminal to the directory containing `EC2Tutorial.pem`, then run `ssh -i EC2Tutorial.pem ec2-user@<public-ip>`. | Trên Amazon Linux 2 AMI, user mặc định là **`ec2-user`**. Di chuyển terminal tới đúng thư mục chứa file `EC2Tutorial.pem` rồi chạy lệnh `ssh -i EC2Tutorial.pem ec2-user@<public-ip>`. |
| `05:19` - `07:05` | At first, SSH complains about an **unprotected key file**. Fix the file permissions by running **`chmod 0400 EC2Tutorial.pem`**, then re-run `ssh -i EC2Tutorial.pem ec2-user@<public-ip>` and type `yes`. Now you are logged into the Amazon Linux 2 EC2 instance (`whoami` returns `ec2-user`, and you can `ping google.com`). Type `exit` or press `Ctrl + D` to close the connection. Remember that if you stop and start the instance, its Public IP will change! | Lần đầu chạy sẽ gặp lỗi **unprotected key file** (file khóa chưa được bảo vệ quyền truy cập). Hãy chạy lệnh **`chmod 0400 EC2Tutorial.pem`** để khóa quyền file, sau đó chạy lại lệnh `ssh -i EC2Tutorial.pem ec2-user@<public-ip>` và gõ `yes`. Khi đã vào trong máy ảo EC2, bạn có thể gõ `whoami` (`ec2-user`) hoặc `ping google.com`. Gõ `exit` hoặc nhấn `Ctrl + D` để thoát. |
