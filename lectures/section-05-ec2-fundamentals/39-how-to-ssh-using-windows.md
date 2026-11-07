# Bài 39: How to SSH using Windows

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `13528046` (`CCP_-_EC2_-_SSH_Windows_7_v2.mp4`)
- **Thời lượng:** `06:08`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### Kết nối SSH trên Windows bằng PuTTY & PuTTYgen
1. **Chuyển đổi khóa `.pem` sang `.ppk` bằng `PuTTYgen`** *(nếu lúc tạo Key Pair bạn tải file `.pem` thay vì `.ppk`)*:
   - Mở ứng dụng **PuTTYgen** -> Nhấn **Load** -> Chọn hiển thị `All Files (*.*)` -> Chọn file `EC2Tutorial.pem`.
   - Nhấn **Save private key** -> Lưu thành file `EC2Tutorial.ppk`.
2. **Cấu hình kết nối trong ứng dụng `PuTTY`:**
   - Tại mục **Session -> Host Name (or IP address)**: Nhập `ec2-user@<Public-IPv4-Address>`, Port `22`, Connection type `SSH`.
   - Tại menu bên trái, vào **Connection -> SSH -> Auth** (hoặc `Auth -> Credentials`): Nhấn **Browse** và chọn file `EC2Tutorial.ppk`.
   - Quay lại mục **Session**, đặt tên trong ô **Saved Sessions** (ví dụ: `EC2 Instance`) và nhấn **Save** để lưu cấu hình cho các lần sau.
   - Nhấn **Open** -> Chọn **Accept / Yes** để đăng nhập vào máy chủ Amazon Linux 2.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:54` | Let's learn how to SSH into our EC2 instance on Windows using **PuTTY** (works on Windows 7, 8, 10, 11). Download and install PuTTY, which includes **PuTTY** and **PuTTYgen**. If you downloaded a `.pem` file instead of `.ppk`, open **PuTTYgen**, click **Load** (show all files), select `EC2Tutorial.pem`, and click **Save private key** to save it as `EC2Tutorial.ppk`. | Hãy học cách SSH vào EC2 trên Windows bằng phần mềm miễn phí **PuTTY**. Sau khi cài đặt, bạn sẽ có **PuTTY** và **PuTTYgen**. Nếu bạn đang có file `.pem`, hãy mở **PuTTYgen**, nhấn **Load** để nạp file `EC2Tutorial.pem`, sau đó nhấn **Save private key** để chuyển đổi sang định dạng `EC2Tutorial.ppk`. |
| `02:54` - `06:08` | Open the **PuTTY** app. In **Host Name (or IP address)**, enter `ec2-user@<Public-IPv4>`. Then on the left menu, expand **SSH -> Auth**, click **Browse**, and select your `EC2Tutorial.ppk` private key file. Go back to **Session**, save the profile as `EC2 Instance`, and click **Open**. Accept the host key prompt, and you are logged into your Amazon Linux 2 instance as `ec2-user`. | Mở ứng dụng **PuTTY**. Tại ô **Host Name**, nhập `ec2-user@<Public-IPv4>`. Tiếp theo ở menu trái, vào **SSH -> Auth**, nhấn **Browse** và chọn file khóa `EC2Tutorial.ppk`. Quay lại mục **Session**, nhấn **Save** để lưu cấu hình rồi nhấn **Open** để đăng nhập thẳng vào máy ảo Amazon Linux 2. |
