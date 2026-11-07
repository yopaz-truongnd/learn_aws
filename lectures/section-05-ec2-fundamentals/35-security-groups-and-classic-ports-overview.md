# Bài 35: Security Groups & Classic Ports Overview

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098134` (`CCP_-_EC2_-_Security_Groups_Overview_v4.mp4`)
- **Thời lượng:** `07:18`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Bản chất và đặc điểm của Security Groups
- **Security Group** là lớp **tường lửa (firewall) hoạt động ở cấp độ EC2 Instance** (nằm bên ngoài EC2 Instance — nếu traffic bị chặn, bản thân EC2 Instance thậm chí không hề nhìn thấy gói tin đó).
- Kiểm soát lưu lượng đi vào (**Inbound traffic**: từ bên ngoài vào EC2) và đi ra (**Outbound traffic**: từ EC2 ra bên ngoài).
- **Các quy tắc cực kỳ quan trọng khi đi thi:**
  1. **Chỉ chứa các quy tắc CHO PHÉP (`Allow` rules only)** — không có quy tắc `Deny`.
  2. Có thể tham chiếu nguồn/đích theo **địa chỉ IP (CIDR block)** hoặc theo **một Security Group khác**.
  3. **Trạng thái mặc định (Default behavior):**
     - **Inbound traffic:** Mặc định bị **CHẶN TẤT CẢ (Blocked by default)**.
     - **Outbound traffic:** Mặc định được **CHO PHÉP TẤT CẢ (Authorized by default)**.
  4. **Quan hệ nhiều - nhiều (Many-to-Many):** Một Security Group có thể gắn vào nhiều EC2 Instances, và một EC2 Instance có thể gắn nhiều Security Groups cùng lúc.
  5. **Phạm vi khóa chặt theo `Region / VPC`:** Nếu chuyển sang Region khác hoặc tạo VPC mới, bạn phải tạo lại Security Group mới.
  6. *Best practice:* Nên duy trì một Security Group riêng biệt chỉ dùng để quản lý kết nối SSH (Port 22).

### 1.2. Chẩn đoán lỗi kết nối: `Time Out` vs. `Connection Refused` (Bẫy đề thi kinh điển)
- **Lỗi `Time Out` (Chờ xoay vòng rồi ngắt):** **100% là do Security Group** (hoặc Firewall) chặn cổng/IP nên gói tin không thể đi qua.
- **Lỗi `Connection Refused` (Từ chối kết nối ngay lập tức):** Traffic **ĐÃ ĐI QUA ĐƯỢC Security Group**, nhưng ứng dụng bên trong EC2 Instance bị lỗi hoặc chưa được bật lắng nghe ở cổng đó.

### 1.3. Tham chiếu chéo giữa các Security Groups (Referencing other Security Groups)
```mermaid
flowchart LR
    EC2_A["EC2 Instance A (SG 2)"] -->|Được phép kết nối| EC2_Main["EC2 Instance 1 (SG 1: Allow Inbound từ SG 1 & SG 2)"]
    EC2_B["EC2 Instance B (SG 1)"] -->|Được phép kết nối| EC2_Main
    EC2_C["EC2 Instance C (SG 3)"] -.->|Bị chặn (Denied)| EC2_Main
```
- Cho phép các EC2 Instances giao tiếp trực tiếp với nhau thông qua định danh Security Group mà **không cần quan tâm địa chỉ IP của chúng thay đổi thế nào** (rất phổ biến khi kết hợp với Load Balancer và Auto Scaling).

---

### 1.4. Các cổng mạng kinh điển (Classic Ports) bắt buộc phải thuộc lòng

| Cổng (Port) | Giao thức | Mục đích sử dụng |
| :---: | :---: | :--- |
| **`22`** | **SSH** *(Secure Shell)* | Đăng nhập dòng lệnh vào **Linux** EC2 instance. |
| **`21`** | **FTP** *(File Transfer Protocol)* | Tải tệp tin lên hệ thống chia sẻ file (Upload files into a file share). |
| **`22`** | **SFTP** *(Secure File Transfer Protocol)* | Tải tệp tin an toàn thông qua giao thức SSH. |
| **`80`** | **HTTP** | Truy cập các trang web không mã hóa (Unsecured websites). |
| **`443`** | **HTTPS** | Truy cập các trang web có bảo mật/mã hóa (Secured websites). |
| **`3389`** | **RDP** *(Remote Desktop Protocol)* | Đăng nhập giao diện màn hình từ xa vào **Windows** EC2 instance. |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:52` | Security groups are fundamental to network security in AWS. They act as a firewall controlling traffic allowed into (**inbound**) and out of (**outbound**) your EC2 instances. Security groups **only contain `Allow` rules** and can reference IP address ranges (`0.0.0.0/0` means anywhere, `/32` means a single IP) or other security groups. By default, **all inbound traffic is blocked** and **all outbound traffic is allowed**. | Security Groups là nền tảng bảo mật mạng trong AWS, đóng vai trò tường lửa kiểm soát lưu lượng đi vào (**inbound**) và đi ra (**outbound**) khỏi EC2 instances. Security Groups **chỉ chứa các quy tắc cho phép (`Allow` rules)** và có thể tham chiếu theo dải IP hoặc tham chiếu tới các Security Groups khác. Mặc định, **mọi lưu lượng đi vào (inbound) đều bị chặn** và **mọi lưu lượng đi ra (outbound) đều được cho phép**. |
| `02:52` - `04:23` | Good to know about Security Groups: 1) They can be attached to multiple instances, and an instance can have multiple security groups. 2) They are locked down to a **Region / VPC** combination. 3) They live **outside** the EC2 instance — if traffic is blocked, the EC2 instance won't even see it. 4) It's good practice to maintain one separate security group just for SSH access. 5) If your application gives a **Timeout**, it is a **Security Group issue**. If you receive a **Connection Refused** error, the Security Group allowed the traffic through, but the application inside EC2 wasn't launched or errored. | Những điều cần nhớ về Security Groups: 1) Quan hệ nhiều - nhiều giữa Security Groups và Instances. 2) Bị giới hạn trong phạm vi một cặp **Region / VPC**. 3) Nằm **bên ngoài** EC2 instance. 4) Nên tách riêng một Security Group chuyên cho SSH. 5) Nếu kết nối bị **Timeout**, đó là lỗi của **Security Group**. Nhưng nếu báo **Connection Refused**, nghĩa là lưu lượng đã đi qua được Security Group nhưng ứng dụng bên trong EC2 chưa chạy hoặc bị lỗi. |
| `04:23` - `05:53` | Security groups can reference other security groups in their rules. For example, if EC2 Instance 1 has `Security Group 1` which authorizes inbound traffic from `Security Group 1` and `Security Group 2`, then any other EC2 instance with `SG 1` or `SG 2` attached can connect directly to Instance 1 regardless of its IP address, while an instance with `SG 3` is denied. | Một Security Group có thể tham chiếu tới các Security Groups khác trong quy tắc Inbound. Ví dụ: nếu `SG 1` cho phép Inbound từ chính `SG 1` và `SG 2`, thì bất kỳ máy EC2 nào mang `SG 1` hoặc `SG 2` đều kết nối thẳng tới được mà không cần quan tâm địa chỉ IP là gì, còn máy mang `SG 3` sẽ bị từ chối. |
| `05:53` - `07:18` | Classic ports you must know for the exam: **Port 22 = SSH** (log into Linux instances) and **SFTP** (secure file transfer over SSH); **Port 21 = FTP** (upload files to a file share); **Port 80 = HTTP** (unsecured websites); **Port 443 = HTTPS** (secured websites); and **Port 3389 = RDP** (Remote Desktop Protocol to log into Windows instances). | Các cổng mạng bắt buộc phải nhớ khi đi thi: **Port 22 = SSH** (đăng nhập máy Linux) và **SFTP** (truyền file bảo mật qua SSH); **Port 21 = FTP** (truyền file); **Port 80 = HTTP** (web không mã hóa); **Port 443 = HTTPS** (web bảo mật); và **Port 3389 = RDP** (Remote Desktop đăng nhập máy Windows). |
