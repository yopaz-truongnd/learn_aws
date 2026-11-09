# Bài 37: SSH Overview

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098142` (`CCP_-_EC2_-_SSH_Theory.mp4`)
- **Thời lượng:** `02:47`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### So sánh 3 phương thức kết nối SSH vào máy chủ Linux EC2

| Phương thức | Hệ điều hành máy trạm hỗ trợ | Đặc điểm chính |
| :--- | :--- | :--- |
| **1. Lệnh `ssh` trên Terminal / CLI** | **Mac**, **Linux**, và **Windows 10/11** trở lên | Sử dụng công cụ dòng lệnh tích hợp sẵn cùng file khóa bảo mật định dạng **`.pem`**. |
| **2. Phần mềm PuTTY** | **Mọi phiên bản Windows** *(đặc biệt là Windows < 10 như Windows 7 / 8)* | Ứng dụng giao diện đồ họa miễn phí trên Windows, sử dụng file khóa định dạng **`.ppk`** (hoặc dùng `PuTTYgen` đổi `.pem` sang `.ppk`). |
| **3. EC2 Instance Connect** | **Mac, Linux, Windows (Mọi phiên bản)** | Kết nối SSH trực tiếp **ngay trên trình duyệt web (Web Browser)** mà không cần cài đặt phần mềm hay quản lý file khóa SSH thủ công (mặc định hỗ trợ sẵn trên **Amazon Linux 2 / Amazon Linux 2023** và Ubuntu). |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:24` | How do we connect inside our Linux servers to perform maintenance or actions? We use **SSH (Secure Shell)** via three possible methods depending on your computer's OS: 1) **SSH command-line utility** (works on Mac, Linux, and Windows 10+); 2) **PuTTY** (works on any version of Windows, especially Windows < 10); and 3) **EC2 Instance Connect**, which uses your web browser directly on Mac, Linux, or Windows without needing to manage keys manually (works out of the box with Amazon Linux 2). | Làm thế nào để kết nối vào bên trong máy chủ Linux? Chúng ta sử dụng giao thức **SSH** qua 3 cách tùy thuộc hệ điều hành máy tính của bạn: 1) **Tiện ích dòng lệnh `ssh`** (dùng trên Mac, Linux và Windows 10+); 2) **PuTTY** (dùng cho mọi bản Windows, nhất là Windows 7/8); và 3) **EC2 Instance Connect** — kết nối trực tiếp ngay trên trình duyệt web ở mọi hệ điều hành mà không cần dùng khóa `.pem`/`.ppk` (tương thích sẵn với Amazon Linux 2). |
| `01:24` - `02:47` | Watch the lecture corresponding to your OS (Mac/Linux, Windows PuTTY, or Windows 10), and definitely watch the **EC2 Instance Connect** lecture because I will use it throughout the rest of the course. If you run into any issues, check the SSH Troubleshooting guide right after these lectures. | Hãy xem bài hướng dẫn tương ứng với hệ điều hành của bạn và xem bài **EC2 Instance Connect** vì giảng viên sẽ sử dụng công cụ này xuyên suốt khóa học. Nếu gặp lỗi kết nối, hãy xem bài hướng dẫn xử lý sự cố (SSH Troubleshooting) ngay sau đó. |
