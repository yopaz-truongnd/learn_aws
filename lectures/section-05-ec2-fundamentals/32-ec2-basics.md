# Bài 32: EC2 Basics

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098112` (`CCP - EC2 - Overview v4.mp4`)
- **Thời lượng:** `03:32`

---

## 1. Kiến thức trọng tâm (Exam Notes)

> [!TIP]
> **Tóm tắt nhanh dịch vụ Amazon EC2 (SAA-C03 Cheat Sheet)**
> - **Là gì:** Dịch vụ cung cấp máy chủ ảo (Virtual Machines) theo mô hình Infrastructure as a Service (IaaS) có khả năng tùy chỉnh CPU, RAM, ổ cứng và mạng trên AWS.
> - **Dùng khi nào (Use case điển hình trong đề):** Cần toàn quyền kiểm soát hệ điều hành (OS-level access), cài đặt phần mềm đặc thù, chạy ứng dụng dài hạn/stateful, hoặc tự động chạy script khởi tạo lần đầu qua **EC2 User Data**.
> - **Khác gì dịch vụ gần giống:**
>   - **EC2 vs. AWS Lambda:** `EC2` là máy chủ ảo chạy liên tục, bạn tự quản lý OS (IaaS); `Lambda` là Serverless FaaS không cần quản lý máy chủ, giới hạn chạy tối đa **15 phút/lần** (`"least operational overhead for short event-driven tasks"`).
>   - **EC2 Purchasing Options:** `On-Demand` (ngắn hạn, không cam kết) vs. `Reserved Instances / Savings Plans` (cam kết **1 hoặc 3 năm** cho tải ổn định, giảm ~72%) vs. `Spot Instances` (giảm tới **90%**, có thể bị thu hồi với thông báo 2 phút — dùng cho Batch jobs chịu lỗi) vs. `Dedicated Hosts` (nhìn thấy Physical Sockets/Cores cho bản quyền **BYOL**).
> - **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
>   - **Mặc định:** **EC2 User Data** chỉ chạy **1 lần duy nhất ở lần khởi tạo đầu tiên** dưới quyền **`root`**.
>   - **Từ khóa gợi ý:** `"full control over OS"` $\rightarrow$ **EC2**; `"most cost-effective fault-tolerant batch workload"` $\rightarrow$ **Spot Instances**; `"server-bound software licenses (per-socket/per-core)"` $\rightarrow$ **Dedicated Hosts**.

### 1.1. Amazon EC2 là gì?
- **EC2 (Elastic Compute Cloud):** Dịch vụ nền tảng theo mô hình **Infrastructure as a Service (IaaS)** phổ biến nhất của AWS.
- EC2 không chỉ là một dịch vụ đơn lẻ mà là sự kết hợp của nhiều thành phần:
  1. Thuê các máy chủ ảo (**EC2 Instances**).
  2. Lưu trữ dữ liệu trên các ổ đĩa ảo (**EBS Volumes**).
  3. Phân phối tải qua nhiều máy chủ (**Elastic Load Balancer - ELB**).
  4. Mở rộng quy mô dịch vụ tự động (**Auto Scaling Group - ASG**).

### 1.2. Các thông số cấu hình khi khởi tạo một EC2 Instance
1. **Operating System (OS) & Compute:**
   - Hệ điều hành: **Linux** (phổ biến nhất), **Windows**, hoặc **macOS**.
   - Lượng tài nguyên tính toán (**CPU** & cores) và bộ nhớ (**RAM**).
2. **Storage Space (Dung lượng lưu trữ):**
   - Gắn qua mạng (**Network-attached**): **EBS** và **EFS**.
   - Gắn trực tiếp vào phần cứng vật lý (**Hardware-attached**): **EC2 Instance Store**.
3. **Network & Firewall:**
   - Tốc độ card mạng, địa chỉ Public IP.
   - Tường lửa bảo vệ máy ảo: **Security Group**.
4. **Bootstrap Script (Kịch bản khởi tạo): `EC2 User Data`**

### 1.3. EC2 User Data & Bootstrapping (Rất hay hỏi trong đề thi)
- **Bootstrapping** nghĩa là tự động chạy các câu lệnh ngay khi máy chủ khởi động lần đầu tiên.
- **Đặc điểm cốt lõi của EC2 User Data:**
  - Chỉ chạy **DUY NHẤT MỘT LẦN (only run once)** vào lần đầu tiên Instance khởi chạy (**first launch**).
  - Dùng để tự động hóa các tác vụ lúc khởi động: cài đặt bản cập nhật OS, cài đặt phần mềm (như web server Apache/HTTPD), tải các tệp tin từ Internet...
  - Script trong EC2 User Data luôn được chạy dưới quyền **`root` user** (do đó mọi lệnh đều mặc định có quyền `sudo`).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:01` | What is Amazon EC2? It stands for **Elastic Compute Cloud**, and it is how you do **Infrastructure as a Service (IaaS)** on AWS. EC2 consists of: renting virtual machines (**EC2 instances**), storing data on virtual drives (**EBS volumes**), distributing load across machines (**Elastic Load Balancer**), and scaling services using an **Auto Scaling Group (ASG)**. | Amazon EC2 là viết tắt của **Elastic Compute Cloud**, cung cấp mô hình **Infrastructure as a Service (IaaS)** trên AWS. EC2 bao gồm: thuê máy ảo (**EC2 instances**), lưu dữ liệu trên ổ đĩa ảo (**EBS volumes**), cân bằng tải (**ELB**) và tự động co giãn số lượng máy (**Auto Scaling Group - ASG**). |
| `01:01` - `02:33` | For our EC2 instances, we can choose: 1) Operating System (**Linux**, **Windows**, or **macOS**); 2) Compute power & cores (**CPU**); 3) Random Access Memory (**RAM**); 4) Storage space: network-attached (**EBS** & **EFS**) or hardware-attached (**EC2 Instance Store**); 5) Network card speed & Public IP; 6) Firewall rules (**Security Group**); and 7) Bootstrap script (**EC2 User Data**). | Khi tạo EC2 instance, ta có thể chọn: 1) Hệ điều hành (**Linux**, **Windows** hoặc **macOS**); 2) Sức mạnh xử lý (**CPU**); 3) Bộ nhớ **RAM**; 4) Lưu trữ: gắn qua mạng (**EBS** & **EFS**) hoặc gắn phần cứng (**EC2 Instance Store**); 5) Mạng & Public IP; 6) Tường lửa (**Security Group**); và 7) Kịch bản khởi tạo (**EC2 User Data**). |
| `02:33` - `03:32` | **Bootstrapping** means launching commands when the machine starts. The **EC2 User Data** script is **only run once** at the instance's very first start. It automates boot tasks like installing updates, installing software, or downloading files from the internet. Importantly, the EC2 User Data script runs with the **`root` user** (sudo rights). | **Bootstrapping** nghĩa là chạy các câu lệnh khi máy bắt đầu khởi động. Script **EC2 User Data** **chỉ chạy duy nhất một lần** khi instance khởi chạy lần đầu tiên, dùng để tự động cài đặt bản vá, cài phần mềm hoặc tải file từ Internet. Đặc biệt, EC2 User Data chạy với quyền **`root` user** (quyền `sudo`). |
