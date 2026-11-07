# Phần 5: EC2 Fundamentals

- **Khóa học:** Ultimate AWS Certified Solutions Architect Associate 2026 (`SAA-C03`)
- **Chapter ID:** `6258026`
- **Tổng số bài giảng:** 16 bài giảng (Bài 31 -> Bài 46) + 1 bài kiểm tra trắc nghiệm (Quiz 2)

---

## Tóm tắt nhanh các dịch vụ trong Phần 5 (Service Cheat Sheet)

### 1. Amazon EC2 (Elastic Compute Cloud)
- **Là gì:** Dịch vụ cung cấp máy chủ ảo (Virtual Machines) dưới dạng Infrastructure as a Service (IaaS) có khả năng tùy chỉnh cấu hình CPU, RAM, ổ cứng và mạng trên AWS.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Cần toàn quyền kiểm soát hệ điều hành (OS-level access), cài đặt phần mềm tùy chỉnh hoặc chạy các ứng dụng truyền thống (monolithic/stateful).
  - Tự động chạy script khởi tạo (cài đặt web server, cập nhật OS) ngay lần đầu khởi động máy thông qua **EC2 User Data**.
- **Khác gì dịch vụ gần giống:**
  - **EC2 vs. AWS Lambda:** `EC2` là máy chủ ảo chạy liên tục, bạn tự quản lý OS và scaling (IaaS); `Lambda` là Serverless Function-as-a-Service (FaaS), không cần quản lý máy chủ, giới hạn chạy tối đa **15 phút/lần**.
  - **EC2 vs. AWS Fargate / ECS:** `EC2` quản lý cấp độ máy ảo (VM); `ECS/Fargate` chạy và điều phối ứng dụng đóng gói dưới dạng **Containers (Docker)**.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** **EC2 User Data** chỉ chạy **1 lần duy nhất khi khởi tạo instance lần đầu tiên** và chạy với quyền **`root` (`sudo`)**.
  - **Từ khóa gợi ý:** `"full control over the operating system"` $\rightarrow$ **EC2**; `"bootstrap script on first launch"` $\rightarrow$ **EC2 User Data**.

### 2. Security Groups (Nhóm bảo mật cho EC2)
- **Là gì:** Tường lửa ảo hoạt động ở cấp độ máy chủ EC2 / ENI dùng để kiểm soát lưu lượng mạng đi vào (**Inbound**) và đi ra (**Outbound**) dựa trên giao thức, cổng (port) và IP/Security Group nguồn.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Cô lập các tầng kiến trúc (ví dụ: Web Tier, App Tier, Database Tier) bằng cách **tham chiếu Security Group** (Security Group của App Tier chỉ cho phép Inbound từ Security Group của ALB).
- **Khác gì dịch vụ gần giống:**
  - **Security Group vs. Network ACL (NACL):**
    - `Security Group` hoạt động ở cấp **Instance/ENI**, chỉ có quy tắc **`Allow`** (không có `Deny`), và có tính chất **Stateful** (nếu lưu lượng đi vào được phép, phản hồi đi ra tự động được phép bất kể Outbound rules).
    - `NACL` hoạt động ở cấp **Subnet**, hỗ trợ cả **`Allow` và `Deny`**, và có tính chất **Stateless** (kiểm tra riêng biệt cả chiều vào lẫn chiều ra).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** Khi mới tạo một Security Group: **Inbound = Chặn tất cả (Deny All)**; **Outbound = Cho phép tất cả (Allow All `0.0.0.0/0`)**.
  - **Chẩn đoán lỗi trong đề thi:**
    - Lỗi **`Connection Timeout` (Hết thời gian chờ):** Luôn do **Security Group** (hoặc Firewall/NACL) chặn port/IP!
    - Lỗi **`Connection Refused` (Từ chối kết nối):** Đã đi qua được Security Group, nhưng ứng dụng/dịch vụ bên trong EC2 chưa chạy hoặc bị sập.

### 3. EC2 Purchasing Options (Các mô hình mua EC2)
- **Là gì:** Tập hợp các phương thức thanh toán và đặt chỗ tài nguyên EC2 nhằm tối ưu chi phí hoặc đáp ứng yêu cầu tuân thủ bản quyền phần mềm.
- **Dùng khi nào & Khác nhau ở đâu:**
  - **On-Demand:** Chạy ngắn hạn, tải không đoán trước được, không cam kết.
  - **Reserved Instances (RI) vs. Savings Plans:** Cùng cam kết **1 hoặc 3 năm** (giảm tới ~72%): `RI` gắn với Instance Type/OS/Tenancy cụ thể (có `Convertible RI` cho phép đổi Instance Family); `Savings Plans` cam kết theo **mức chi tiêu \$/giờ** và linh hoạt đổi giữa EC2, Fargate, Lambda.
  - **Spot Instances:** Tận dụng tài nguyên nhàn rỗi của AWS, giảm tới **90%**, nhưng **có thể bị thu hồi bất cứ lúc nào** với thông báo trước 2 phút (dùng cho Batch jobs, xử lý dữ liệu phân tán có khả năng chịu lỗi).
  - **Dedicated Hosts vs. Dedicated Instances:** Cùng chạy trên phần cứng vật lý dành riêng cho bạn; nhưng chỉ **`Dedicated Hosts`** mới cho phép nhìn thấy **Physical Sockets / Cores** và hỗ trợ **BYOL (Bring Your Own License)** tính theo core/socket (như Windows Server, SQL Server, Oracle).
  - **Capacity Reservations:** Giữ chỗ dung lượng EC2 tại một AZ cụ thể trong thời gian bất kỳ (không giảm giá nếu không kết hợp RI/Savings Plans).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Từ khóa gợi ý:** `"steady state / predictable usage"` $\rightarrow$ **Reserved Instances / Savings Plans**; `"most cost-effective, fault-tolerant, batch processing, can be interrupted"` $\rightarrow$ **Spot Instances**; `"server-bound software licenses (per-socket / per-core BYOL), strong compliance"` $\rightarrow$ **Dedicated Hosts**.

---

## Danh sách bài học trong Phần 5

| STT | Lecture ID | Tên bài giảng | Loại | Thời lượng | Trạng thái |
| :---: | :---: | :--- | :---: | :---: | :--- |
| 31 | `26098410` | [AWS Budget Setup](./31-aws-budget-setup.md) | Video | 05:05 | **Đã lưu** |
| 32 | `26098112` | [EC2 Basics](./32-ec2-basics.md) | Video | 03:32 | **Đã lưu** |
| 33 | `26098122` | [Create an EC2 Instance with EC2 User Data to have a Website Hands On](./33-create-ec2-instance-with-user-data-hands-on.md) | Video | 13:48 | **Đã lưu** |
| 34 | `26098128` | [EC2 Instance Types Basics](./34-ec2-instance-types-basics.md) | Video | 04:51 | **Đã lưu** |
| 35 | `26098134` | [Security Groups & Classic Ports Overview](./35-security-groups-and-classic-ports-overview.md) | Video | 07:18 | **Đã lưu** |
| 36 | `26098138` | [Security Groups Hands On](./36-security-groups-hands-on.md) | Video | 04:45 | **Đã lưu** |
| 37 | `26098142` | [SSH Overview](./37-ssh-overview.md) | Video | 02:47 | **Đã lưu** |
| 38 | `13528044` | [How to SSH using Linux or Mac](./38-how-to-ssh-using-linux-or-mac.md) | Video | 07:05 | **Đã lưu** |
| 39 | `13528046` | [How to SSH using Windows](./39-how-to-ssh-using-windows.md) | Video | 06:08 | **Đã lưu** |
| 40 | `16560336` | [How to SSH using Windows 10](./40-how-to-ssh-using-windows-10.md) | Video | 05:01 | **Đã lưu** |
| 41 | `16666654` | [SSH Troubleshooting](./41-ssh-troubleshooting.md) | Article | 01:23 | **Đã lưu** |
| 42 | `26098164` | [EC2 Instance Connect](./42-ec2-instance-connect.md) | Video | 03:15 | **Đã lưu** |
| 43 | `26098166` | [EC2 Instance Roles Demo](./43-ec2-instance-roles-demo.md) | Video | 04:19 | **Đã lưu** |
| 44 | `26098170` | [EC2 Instance Purchasing Options](./44-ec2-instance-purchasing-options.md) | Video | 09:48 | **Đã lưu** |
| 45 | `18756818` | [Spot Instances & Spot Fleet](./45-spot-instances-and-spot-fleet.md) | Video | 08:52 | **Đã lưu** |
| 46 | `27694918` | [EC2 Instances Launch Types Hands On](./46-ec2-instances-launch-types-hands-on.md) | Video | 08:52 | **Đã lưu** |
| Quiz 2 | `5334510` | [EC2 Fundamentals Quiz](./quiz-02-ec2-fundamentals-quiz.md) | Quiz | 12 câu | **Đã lưu** |
