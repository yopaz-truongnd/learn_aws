# Bài 42: EC2 Instance Connect

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098164` (`CCP - EC2 - Instance Connect v2.mp4`)
- **Thời lượng:** `03:15`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### Cách hoạt động của EC2 Instance Connect
- **EC2 Instance Connect** cho phép mở phiên kết nối SSH vào EC2 Instance **trực tiếp ngay trên trình duyệt web** (`Select Instance -> Connect -> EC2 Instance Connect -> Connect`).
- **Ưu điểm lớn:**
  - Không cần tải hoặc chỉ định file khóa `.pem` / `.ppk` thủ công: Đằng sau hậu trường, AWS tự động tải lên một **khóa SSH tạm thời (temporary SSH key)** có hiệu lực ngắn hạn để thiết lập kết nối.
  - Tự động điền sẵn username mặc định (`ec2-user` đối với Amazon Linux 2).
- **Điều kiện bắt buộc để EC2 Instance Connect hoạt động (Cần nhớ khi đi thi):**
  - Vẫn dựa trên giao thức SSH ở tầng dưới, nên **Security Group của EC2 Instance BẮT BUỘC phải mở cổng Inbound `Port 22 (SSH)`** (cho IPv4 `0.0.0.0/0` hoặc dải IP của dịch vụ EC2 Instance Connect / IPv6 `::/0`). Nếu xóa rule Port 22 trong Security Group, EC2 Instance Connect cũng sẽ báo lỗi không thể kết nối.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:45` | An easier alternative to terminal SSH is **EC2 Instance Connect**. Select your instance -> click **Connect** -> choose **EC2 Instance Connect**. It verifies the Public IP and pre-fills the default username `ec2-user` (for Amazon Linux 2). Notice there is no SSH key option because AWS automatically uploads a **temporary SSH key** behind the scenes to establish the browser-based SSH session. Click **Connect** and a new browser tab opens directly inside your EC2 terminal. | Một giải pháp thay thế dễ dàng hơn nhiều cho SSH truyền thống là **EC2 Instance Connect**. Chọn instance -> nhấn **Connect** -> tab **EC2 Instance Connect**. AWS tự động điền sẵn username `ec2-user` và bạn không cần truyền file khóa SSH vì hệ thống sẽ tự động đẩy một **khóa SSH tạm thời (temporary SSH key)** lên máy ảo để mở phiên kết nối ngay trên tab trình duyệt. |
| `01:45` - `03:15` | Behind the scenes, EC2 Instance Connect still relies on SSH over **Port 22**. If we remove the Port 22 SSH inbound rule from the instance's Security Group and try to connect again, EC2 Instance Connect fails! Re-adding the SSH Port 22 inbound rule (for IPv4 and/or IPv6) immediately allows EC2 Instance Connect to work again. | Đằng sau hậu trường, EC2 Instance Connect vẫn sử dụng giao thức SSH qua **Port 22**. Nếu ta xóa quy tắc Inbound Port 22 khỏi Security Group, EC2 Instance Connect sẽ lập tức báo lỗi không kết nối được. Khi mở lại Port 22 trên Security Group, kết nối hoạt động bình thường trở lại. |
