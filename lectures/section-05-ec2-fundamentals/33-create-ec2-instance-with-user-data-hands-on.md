# Bài 33: Create an EC2 Instance with EC2 User Data to have a Website Hands On

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098122` (`CCP_-_EC2_-_Hands_On_v2.mp4`)
- **Thời lượng:** `13:48`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các bước khởi tạo một EC2 Instance trên Console
1. **Name and tags:** Đặt tên (ví dụ: `My First Instance`, thực chất là một Tag có `Key = Name`).
2. **Application and OS Images (AMI):** Chọn hệ điều hành gốc, ví dụ **Amazon Linux 2 AMI** (64-bit x86, thuộc diện Free Tier eligible).
3. **Instance type:** Chọn **`t2.micro`** (hoặc `t3.micro` tùy Region) — miễn phí 750 giờ/tháng trong năm đầu tiên (Free Tier).
4. **Key pair (login):** Tạo khóa dùng để đăng nhập SSH (ví dụ: `EC2 Tutorial`, loại mã hóa `RSA`):
   - Định dạng **`.pem`**: Dùng cho Mac, Linux và Windows 10 trở lên (OpenSSH).
   - Định dạng **`.ppk`**: Dùng cho phần mềm **PuTTY** (trên Windows 7 / Windows 8 hoặc Windows bất kỳ dùng PuTTY).
5. **Network settings & Security Group:**
   - Tự động cấp Public IP.
   - Tạo Security Group (`launch-wizard-1`) mở 2 cổng Inbound:
     - **SSH (Port 22)** từ mọi nơi (`0.0.0.0/0`) để quản trị từ xa.
     - **HTTP (Port 80)** từ mọi nơi (`0.0.0.0/0`) để truy cập web server.
6. **Configure storage:**
   - Mặc định tạo 1 ổ đĩa Root volume **8 GiB `gp2`** (Free Tier cho phép tối đa **30 GB** EBS General Purpose SSD).
   - Thuộc tính **Delete on termination** mặc định là **`Yes`** cho ổ Root volume (khi Terminate EC2 thì ổ đĩa này cũng bị xóa theo).
7. **Advanced details -> User data:**
   - Truyền bash script cài đặt Apache (`httpd`) và tạo trang `index.html` hiển thị `"Hello World from <hostname>"`.

```bash
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
```

### 1.2. Các lưu ý cực kỳ quan trọng khi vận hành EC2
- **Truy cập Web Server:** Phải dùng giao thức `http://<Public-IPv4>` (nếu trình duyệt tự nhảy sang `https://` sẽ bị treo xoay vòng vô tận / timeout vì ta chỉ mở Port 80 chứ chưa mở Port 443).
- **Sự khác biệt giữa Stop, Start và Terminate:**
  - Khi **Stop** instance: AWS **không tính phí** chạy EC2 (nhưng vẫn giữ ổ đĩa EBS nên trạng thái dữ liệu được bảo toàn).
  - Khi **Stop rồi Start lại** một EC2 instance:
    - **Private IPv4** luôn **GIỮ NGUYÊN** không bao giờ đổi.
    - **Public IPv4** sẽ **BỊ THAY ĐỔI** sang một địa chỉ IP mới.
  - Khi **Terminate** instance: Xóa vĩnh viễn máy ảo (và xóa luôn ổ EBS gốc nếu `Delete on termination = Yes`).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:56` | In this lecture we launch our first EC2 instance running Amazon Linux 2. In the EC2 Console -> Instances -> **Launch instances**, name it `My First Instance`, select **Amazon Linux 2 AMI** (Free tier eligible, 64-bit x86), and choose instance type **`t2.micro`** (Free tier eligible: 750 hours per month). | Trong bài này, ta khởi chạy EC2 instance đầu tiên. Vào EC2 Console -> **Launch instances**, đặt tên `My First Instance`, chọn hệ điều hành **Amazon Linux 2 AMI** (thuộc Free tier) và loại máy **`t2.micro`** (miễn phí 750 giờ mỗi tháng). |
| `02:56` - `05:51` | Next, create a new **Key pair** named `EC2 Tutorial` (RSA). Choose `.pem` format for Mac, Linux, or Windows 10+; choose `.ppk` for PuTTY on Windows 7/8. Under Network settings, allow **SSH traffic** (port 22) and **HTTP traffic** (port 80) from the internet in the new security group `launch-wizard-1`. Under Storage, keep the default 8 GiB `gp2` root volume (Free tier includes up to 30 GB of EBS SSD). Note under Advanced storage that **Delete on termination** is enabled (`Yes`) by default. | Tiếp theo, tạo một **Key pair** tên là `EC2 Tutorial`: chọn `.pem` cho Mac/Linux/Windows 10+, hoặc `.ppk` cho PuTTY. Ở phần Network settings, tạo Security Group `launch-wizard-1` cho phép cả **SSH (port 22)** và **HTTP (port 80)** từ Internet. Phần Storage giữ nguyên ổ đĩa gốc 8 GiB `gp2` (Free tier miễn phí tới 30 GB EBS). Lưu ý tùy chọn **Delete on termination** mặc định bật là `Yes`. |
| `05:51` - `08:25` | Scroll down to **Advanced details -> User data** and paste the bash script from `ec2-user-data.sh` (which runs once on first boot to install `httpd`, start it, and write an HTML file). Click **Launch instance**. Within 15 seconds, the instance goes from `Pending` to `Running`. | Cuộn xuống mục **Advanced details -> User data** và dán đoạn bash script cài đặt web server `httpd` cùng trang HTML mẫu. Nhấn **Launch instance**. Chỉ sau khoảng 15 giây, trạng thái máy chuyển từ `Pending` sang `Running`. |
| `08:25` - `11:10` | Inspecting the running instance, we see its Instance ID, **Public IPv4 address** (for external access), **Private IPv4 address** (for internal AWS network), Security Group rules (ports 22 and 80 inbound), and 8 GB volume. Copy the Public IPv4 address and open `http://<Public-IP>` in the browser (make sure to use `http://`, not `https://`). It displays `"Hello World from ip-172-31-33-135..."` (showing its internal private hostname). | Kiểm tra instance đang chạy, ta thấy Instance ID, **Public IPv4** (truy cập từ ngoài), **Private IPv4** (mạng nội bộ AWS), và Security Group. Sao chép địa chỉ Public IPv4 và mở bằng `http://<Public-IP>` trên trình duyệt (chú ý phải dùng `http://` chứ không phải `https://`). Trang web sẽ hiển thị dòng chữ `"Hello World from ip-172-31-..."`. |
| `11:10` - `13:48` | You can **Stop** the instance (`Instance state -> Stop instance`) so AWS won't bill you for compute while keeping its attached EBS volume. When you **Start** the instance again later, notice that the old URL times out because **stopping and starting an instance changes its Public IPv4 address**, whereas its **Private IPv4 address always stays the same**! Accessing the new Public IPv4 over `http://` works immediately. | Bạn có thể **Stop** instance khi không dùng để không bị tính phí compute mà vẫn giữ lại dữ liệu trên ổ đĩa. Khi **Start** lại instance đó, lưu ý rằng địa chỉ cũ sẽ không vào được nữa vì **khi Stop rồi Start lại, địa chỉ Public IPv4 sẽ bị thay đổi sang IP mới**, trong khi **địa chỉ Private IPv4 luôn giữ nguyên**. |
