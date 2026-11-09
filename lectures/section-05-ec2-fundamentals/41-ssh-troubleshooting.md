# Bài 41: SSH Troubleshooting (Bài đọc)

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `16666654` (`Article`)
- **Thời lượng:** `01:23`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## Hướng dẫn xử lý các lỗi kết nối SSH thường gặp (SSH Troubleshooting)

### 1. Lỗi `Connection timeout` (Quá thời gian kết nối)
- **Nguyên nhân:** Đây là lỗi do **Security Group** (hoặc tường lửa). Mọi lỗi `timeout` (không chỉ riêng SSH) đều liên quan đến Security Group hoặc Firewall.
- **Cách khắc phục:** Kiểm tra lại Security Group đang gắn vào EC2 Instance, đảm bảo đã có Inbound Rule mở **Port 22 (SSH)** cho phép từ `0.0.0.0/0` (`Anywhere-IPv4`) hoặc IP của bạn.

### 2. Đã cấu hình đúng Security Group nhưng vẫn bị `Connection timeout`
- **Nguyên nhân:** Mạng công ty (Corporate firewall) hoặc tường lửa cá nhân trên máy tính của bạn đang chặn cổng 22.
- **Cách khắc phục:** Hãy sử dụng **EC2 Instance Connect** ngay trên trình duyệt web (hướng dẫn ở bài tiếp theo).

### 3. Lệnh `ssh` không hoạt động trên Windows (`ssh command not found`)
- **Cách khắc phục:** Sử dụng phần mềm **PuTTY** hoặc dùng **EC2 Instance Connect** trên trình duyệt.

### 4. Lỗi `Connection refused` (Kết nối bị từ chối)
- **Nguyên nhân:** Máy ảo EC2 đã có thể tiếp cận được (đã đi qua Security Group), nhưng tiện ích SSH daemon trên instance không chạy.
- **Cách khắc phục:**
  - Thử khởi động lại (Restart/Reboot) instance.
  - Nếu vẫn không được, hãy Terminate instance đó và tạo lại một instance mới sử dụng **Amazon Linux 2**.

### 5. Lỗi `Permission denied (publickey,gssapi-keyex,gssapi-with-mic)`
- **Nguyên nhân (1 trong 2 lý do sau):**
  1. **Dùng sai khóa bảo mật (Security Key)** hoặc quên truyền khóa `-i <file.pem>`: Hãy kiểm tra lại tên Key Pair gắn với EC2 Instance.
  2. **Dùng sai tên User đăng nhập:** Với **Amazon Linux 2**, bắt buộc phải dùng user **`ec2-user`** (`ec2-user@<public-ip>`).

### 6. Không cách nào hoạt động ("Nothing is working")
- Đừng lo lắng! Hãy dùng **EC2 Instance Connect** trên trình duyệt web ở bài giảng tiếp theo với máy ảo **Amazon Linux 2**.

### 7. Hôm qua kết nối được nhưng hôm nay không kết nối được nữa
- **Nguyên nhân:** Bạn đã **Stop** EC2 instance vào hôm qua và **Start** lại vào hôm nay. Khi làm vậy, **địa chỉ Public IP của EC2 instance đã bị thay đổi**.
- **Cách khắc phục:** Sao chép địa chỉ Public IP mới trên AWS Console và cập nhật lại trong câu lệnh SSH hoặc cấu hình PuTTY của bạn.
