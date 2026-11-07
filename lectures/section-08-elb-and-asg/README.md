# Phần 8: High Availability and Scalability: ELB & ASG (Tính sẵn sàng cao và Khả năng mở rộng: ELB & ASG)

---

## Tóm tắt nhanh các dịch vụ trong Phần 8 (Service Cheat Sheet)

### 1. Application Load Balancer (ALB - Layer 7)
- **Là gì:** Bộ cân bằng tải hoạt động ở **Tầng 7 (Application Layer - HTTP/HTTPS/gRPC/WebSocket)** có khả năng đọc hiểu nội dung HTTP header, URL path, hostname và query string để định tuyến thông minh.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Định tuyến **Microservices / Containers (ECS, EKS)** dựa trên đường dẫn URL (`/users`, `/posts`), Hostname (`api.example.com`), HTTP Headers hoặc Query Strings.
  - Cần chấm dứt kết nối SSL/TLS (**SSL Termination**) và gắn nhiều chứng chỉ SSL trên cùng một Listener nhờ **SNI (Server Name Indication)**.
- **Khác gì dịch vụ gần giống:**
  - **ALB vs. NLB:** `ALB` hoạt động ở **Layer 7** (chỉ HTTP/HTTPS), cung cấp một **DNS Name cố định** nhưng **không có IP tĩnh**; `NLB` hoạt động ở **Layer 4** (TCP/UDP/TLS), độ trễ cực thấp (~100 ms so với ~400 ms của ALB) và hỗ trợ **1 Static IP / Elastic IP trên mỗi AZ**.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** **Cross-Zone Load Balancing** luôn **BẬT mặc định (`Enabled by default`)** trên ALB và **không tính phí** truyền dữ liệu liên AZ.
  - **Lấy IP thật của Client:** ALB ẩn IP gốc của Client và ghi vào HTTP Header **`X-Forwarded-For`** (kèm `X-Forwarded-Proto` và `X-Forwarded-Port`).
  - **Từ khóa gợi ý:** `"HTTP/HTTPS, path-based / host-based routing, microservices, Docker/ECS dynamic port mapping, WebSockets"` $\rightarrow$ **Application Load Balancer (ALB)**.

### 2. Network Load Balancer (NLB - Layer 4)
- **Là gì:** Bộ cân bằng tải hoạt động ở **Tầng 4 (Transport Layer - TCP/UDP/TLS)** có khả năng xử lý hàng triệu request mỗi giây với độ trễ cực thấp.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Ứng dụng yêu cầu hiệu năng cực đại (hàng triệu requests/giây), độ trễ siêu thấp (gaming, tài chính), sử dụng giao thức **TCP hoặc UDP**.
  - Đối tác/khách hàng yêu cầu cung cấp một danh sách **địa chỉ IP tĩnh cố định (Static / Elastic IP)** để cấu hình tường lửa (**Firewall Whitelisting**).
- **Khác gì dịch vụ gần giống:**
  - Khác với `ALB` (không có IP tĩnh, chỉ hỗ trợ HTTP/HTTPS), `NLB` cung cấp **1 Static IP / Elastic IP cho mỗi Availability Zone** (nếu cần đưa Elastic IP ra phía trước một ALB, có thể đặt NLB làm tầng trước trỏ vào ALB hoặc dùng AWS Global Accelerator).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** **Cross-Zone Load Balancing** mặc định **TẮT (`Disabled by default`)** trên NLB; nếu bạn bật lên sẽ **bị tính phí** truyền dữ liệu giữa các AZ.
  - **Từ khóa gợi ý:** `"extreme performance, millions of requests per second, ultra-low latency, TCP/UDP, static IP / Elastic IP whitelisting"` $\rightarrow$ **Network Load Balancer (NLB)**.

### 3. Gateway Load Balancer (GWLB - Layer 3)
- **Là gì:** Bộ cân bằng tải hoạt động ở **Tầng 3 (Network Layer - IP Packets)** dùng để triển khai, mở rộng và quản lý một đội ngũ các thiết bị mạng ảo của bên thứ 3 (**3rd-party Virtual Network Appliances**) trên AWS.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Cần cho **toàn bộ lưu lượng mạng** đi qua một cụm thiết bị bảo mật của bên thứ 3 (như **Firewall, IDS/IPS, Deep Packet Inspection**) để kiểm tra gói tin trước khi cho vào ứng dụng, đảm bảo khả năng mở rộng và dự phòng cao cho cụm thiết bị đó.
- **Khác gì dịch vụ gần giống:**
  - Khác với `ALB` (Layer 7) và `NLB` (Layer 4) phân phối lưu lượng trực tiếp tới máy chủ ứng dụng, `GWLB` đóng vai trò **Transparent Network Gateway** (chặn thu toàn bộ lưu lượng IP ở tầng 3) kết hợp với **Load Balancer** sử dụng giao thức đóng gói **`GENEVE` trên cổng `6081`**.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** Cross-Zone Load Balancing mặc định **TẮT (`Disabled by default`)** và sẽ tính phí nếu bật.
  - **Từ khóa gợi ý:** `"third-party virtual appliances, Firewalls, IDS/IPS, Deep Packet Inspection, inspect all network traffic at Layer 3, GENEVE port 6081"` $\rightarrow$ **Gateway Load Balancer (GWLB)**.

### 4. Amazon EC2 Auto Scaling Group (ASG)
- **Là gì:** Dịch vụ tự động tăng (`Scale Out`) hoặc giảm (`Scale In`) số lượng máy chủ EC2 theo tải thực tế, đồng thời tự động thay thế các máy chủ bị lỗi và đăng ký chúng vào Load Balancer.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Đảm bảo luôn duy trì đúng số lượng EC2 tối thiểu/mong muốn (`Min / Desired / Max capacity`) trên nhiều AZ và tự động co giãn theo các chính sách **Scaling Policies** (`Target Tracking`, `Step Scaling`, `Scheduled Scaling`, `Predictive Scaling`).
- **Khác gì dịch vụ gần giống:**
  - **Launch Template vs. Launch Configuration:** `Launch Configuration` là chuẩn cũ (legacy) phải tạo mới mỗi lần sửa; **`Launch Template`** là chuẩn khuyến nghị mới hỗ trợ đánh phiên bản (Versioning), kết hợp cả On-Demand & Spot Instances và dùng tính năng `T2/T3 Unlimited`.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:**
    - **Default Cooldown Period** = **`300 giây` (5 phút)** (khoảng thời gian chờ sau một hoạt động scaling trước khi kích hoạt scaling tiếp theo).
    - **Default Termination Policy:** Khi Scale In, ASG ưu tiên chọn **AZ đang có nhiều EC2 instances nhất**, sau đó xóa instance có **Launch Template / Launch Configuration cũ nhất**.
  - **Từ khóa gợi ý:** `"maintain a single metric at a specific value (e.g. Average CPU at 40%)"` $\rightarrow$ **Target Tracking Scaling**; `"known usage patterns on Friday 5 PM"` $\rightarrow$ **Scheduled Scaling**; `"machine learning forecast of future traffic"` $\rightarrow$ **Predictive Scaling**.

---

## Danh sách toàn bộ bài giảng và bài kiểm tra trong Phần 8

| STT | Mã bài (ID) | Tên bài học | Thời lượng | Tài liệu chi tiết | Trạng thái |
| :-: | :---: | :--- | :---: | :--- | :---: |
| 70 | `13531374` | High Availability and Scalability | `05:05` | [70-high-availability-and-scalability.md](./70-high-availability-and-scalability.md) | **Đã lưu** |
| 71 | `13528090` | Elastic Load Balancing (ELB) Overview | `06:15` | [71-elastic-load-balancing-elb-overview.md](./71-elastic-load-balancing-elb-overview.md) | **Đã lưu** |
| 72 | `18078003` | Application Load Balancer (ALB) | `05:49` | [72-application-load-balancer-alb.md](./72-application-load-balancer-alb.md) | **Đã lưu** |
| 73 | `35136194` | Application Load Balancer (ALB) - Hands On - Part 1 | `08:34` | [73-application-load-balancer-alb-hands-on-part-1.md](./73-application-load-balancer-alb-hands-on-part-1.md) | **Đã lưu** |
| 74 | `26099120` | Application Load Balancer (ALB) - Hands On - Part 2 | `05:37` | [74-application-load-balancer-alb-hands-on-part-2.md](./74-application-load-balancer-alb-hands-on-part-2.md) | **Đã lưu** |
| 75 | `18078013` | Network Load Balancer (NLB) | `03:24` | [75-network-load-balancer-nlb.md](./75-network-load-balancer-nlb.md) | **Đã lưu** |
| 76 | `26148292` | Network Load Balancer (NLB) - Hands On | `06:03` | [76-network-load-balancer-nlb-hands-on.md](./76-network-load-balancer-nlb-hands-on.md) | **Đã lưu** |
| 77 | `28874688` | Gateway Load Balancer (GWLB) | `03:47` | [77-gateway-load-balancer-gwlb.md](./77-gateway-load-balancer-gwlb.md) | **Đã lưu** |
| 78 | `13528094` | Elastic Load Balancer - Sticky Sessions | `05:51` | [78-elastic-load-balancer-sticky-sessions.md](./78-elastic-load-balancer-sticky-sessions.md) | **Đã lưu** |
| 79 | `18078093` | Elastic Load Balancer - Cross Zone Load Balancing | `05:53` | [79-elastic-load-balancer-cross-zone-load-balancing.md](./79-elastic-load-balancer-cross-zone-load-balancing.md) | **Đã lưu** |
| 80 | `18078099` | Elastic Load Balancer - SSL Certificates | `06:03` | [80-elastic-load-balancer-ssl-certificates.md](./80-elastic-load-balancer-ssl-certificates.md) | **Đã lưu** |
| 81 | `35136224` | Elastic Load Balancer - SSL Certificates - Hands On | `01:59` | [81-elastic-load-balancer-ssl-certificates-hands-on.md](./81-elastic-load-balancer-ssl-certificates-hands-on.md) | **Đã lưu** |
| 82 | `18611524` | Elastic Load Balancer - Connection Draining | `02:22` | [82-elastic-load-balancer-connection-draining.md](./82-elastic-load-balancer-connection-draining.md) | **Đã lưu** |
| 83 | `13528102` | Auto Scaling Groups (ASG) Overview | `04:42` | [83-auto-scaling-groups-asg-overview.md](./83-auto-scaling-groups-asg-overview.md) | **Đã lưu** |
| 84 | `13528104` | Auto Scaling Groups Hands On | `08:56` | [84-auto-scaling-groups-hands-on.md](./84-auto-scaling-groups-hands-on.md) | **Đã lưu** |
| 85 | `26148326` | Auto Scaling Groups - Scaling Policies | `04:23` | [85-auto-scaling-groups-scaling-policies.md](./85-auto-scaling-groups-scaling-policies.md) | **Đã lưu** |
| 86 | `18078107` | Auto Scaling Groups - Scaling Policies Hands On | `09:15` | [86-auto-scaling-groups-scaling-policies-hands-on.md](./86-auto-scaling-groups-scaling-policies-hands-on.md) | **Đã lưu** |
| Quiz 5 | `5334526` | High Availability and Scalability - ELB & ASG Quiz | `21 câu hỏi` | [quiz-05-elb-and-asg-quiz.md](./quiz-05-elb-and-asg-quiz.md) | **Đã lưu** |
