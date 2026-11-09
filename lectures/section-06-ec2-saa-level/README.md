# Section 6: EC2 - Solutions Architect Associate Level
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## Tóm tắt nhanh các dịch vụ & tính năng trong Phần 6 (Service Cheat Sheet)

### 1. Elastic IP (EIP)
- **Là gì:** Một địa chỉ **Public IPv4 tĩnh (static)** thuộc quyền sở hữu của tài khoản AWS cho đến khi bạn chủ động xóa nó.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Cần giữ cố định địa chỉ Public IPv4 của EC2 instance sau khi `Stop` và `Start` lại máy.
  - Chuyển đổi dự phòng nhanh (failover) giữa 2 EC2 instances bằng cách tháo EIP khỏi máy bị lỗi và gắn sang máy dự phòng (**Remap Elastic IP**), hoặc khi đối tác yêu cầu **whitelist IP cố định**.
- **Khác gì dịch vụ gần giống:**
  - **Elastic IP vs. Public IP mặc định:** `Public IP` mặc định sẽ **bị mất và đổi sang IP mới** mỗi khi bạn `Stop` rồi `Start` lại EC2; `Elastic IP` giữ nguyên không đổi.
  - **Elastic IP vs. Route 53 / Load Balancer:** AWS khuyến nghị dùng DNS (Route 53) kết hợp Load Balancer thay vì dùng EIP vì EIP giới hạn số lượng và là mô hình thiết kế kém linh hoạt.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Giới hạn mặc định (Soft limit):** Tối đa **5 Elastic IPs trên mỗi Region** (có thể xin tăng).
  - **Chi phí:** Miễn phí khi đang gắn vào một EC2 instance **đang chạy (`Running`)**; sẽ **bị tính phí** nếu EIP không gắn vào đâu hoặc gắn vào một EC2 đang `Stopped`.

### 2. EC2 Placement Groups (Nhóm bố trí vị trí phần cứng EC2)
- **Là gì:** Tính năng cho phép bạn kiểm soát chiến lược bố trí vị trí vật lý của các EC2 instances trên hạ tầng phần cứng AWS để tối ưu hiệu năng mạng hoặc giảm thiểu rủi ro lỗi phần cứng đồng thời.
- **Dùng khi nào & Khác nhau ở đâu:**
  - **Cluster Placement Group:** Đặt toàn bộ EC2 vào **cùng 1 Rack / cùng 1 AZ** $\rightarrow$ mang lại mạng tốc độ cực cao (**10 Gbps+**, độ trễ cực thấp) cho **HPC (High Performance Computing)**, nhưng nếu Rack hỏng thì toàn bộ instances sập cùng lúc.
  - **Spread Placement Group:** Trải từng EC2 lên **các phần cứng vật lý (Racks) hoàn toàn tách biệt nhau** (hỗ trợ đa AZ) $\rightarrow$ dùng cho **một số lượng nhỏ các instances cực kỳ quan trọng (Critical instances)** cần cách ly lỗi tối đa.
  - **Partition Placement Group:** Chia các EC2 thành nhiều phân vùng (**Partitions**), mỗi Partition nằm trên một cụm Racks độc lập (có thể trải qua nhiều AZ trong 1 Region) $\rightarrow$ dùng cho các hệ thống dữ liệu lớn phân tán nhận biết được cấu trúc phân vùng (**HDFS, HBase, Cassandra, Kafka**) với hàng trăm EC2 instances.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Giới hạn cứng:** **Spread Placement Group** giới hạn tối đa **7 instances trên mỗi AZ** cho mỗi nhóm! **Partition Placement Group** hỗ trợ tối đa **7 partitions trên mỗi AZ**.
  - **Từ khóa gợi ý:** `"low latency, high throughput, HPC, 10 Gbps"` $\rightarrow$ **Cluster**; `"small number of critical instances, separate underlying hardware"` $\rightarrow$ **Spread**; `"HDFS / Cassandra / Kafka, hundreds of instances, rack-aware"` $\rightarrow$ **Partition**.

### 3. Elastic Network Interface (ENI)
- **Là gì:** Card mạng ảo (Virtual Network Card) trong VPC đại diện cho kết nối mạng của một EC2 instance (chứa Private IP, Public/Elastic IP, Security Groups và địa chỉ MAC).
- **Dùng khi nào (Use case điển hình trong đề):**
  - Tháo ENI phụ (Secondary ENI) từ một EC2 bị lỗi sang gắn vào một EC2 dự phòng để **chuyển tiếp ngay lập tức lưu lượng mạng thông qua cùng một địa chỉ Private IP cố định**.
  - Tạo mạng quản trị riêng (Management Network) hoặc thiết bị bảo mật mạng (Firewall/NAT appliance) cần kết nối vào nhiều Subnets khác nhau trong cùng một AZ.
- **Khác gì dịch vụ gần giống:**
  - **ENI vs. Elastic IP:** `Elastic IP` chỉ là một địa chỉ Public IPv4 tĩnh; `ENI` là nguyên một card mạng ảo gắn chặt với một **Availability Zone (AZ)** cụ thể và giữ cả **Private IPv4** lẫn **MAC Address**.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Giới hạn:** ENI **bị ràng buộc vào 1 Availability Zone (AZ-bound)** — bạn **không thể** gắn một ENI ở `us-east-1a` vào một EC2 nằm ở `us-east-1b`!
  - **Mặc định:** Card mạng chính (`Primary ENI - eth0`) không thể tháo rời khỏi EC2; chỉ các `Secondary ENIs (eth1..ethN)` mới có thể tháo lắp nóng giữa các EC2.

### 4. EC2 Hibernate (Ngủ đông máy chủ EC2)
- **Là gì:** Chế độ dừng EC2 (`Stop - Hibernate`) giúp bảo toàn toàn bộ trạng thái dữ liệu đang chạy trong bộ nhớ **RAM** bằng cách ghi kết xuất RAM xuống ổ cứng **Root EBS Volume** trước khi tắt máy.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Các ứng dụng mất rất nhiều thời gian để khởi động (`long-running processing`), hoặc các dịch vụ cần nạp bộ nhớ đệm (cache) lớn vào RAM mà cần khôi phục hoạt động tức thì khi bật lại máy.
- **Khác gì dịch vụ gần giống:**
  - **EC2 Stop vs. EC2 Hibernate:** Khi `Stop` thông thường, dữ liệu trên EBS được giữ lại nhưng **dữ liệu trong RAM bị xóa sạch** và hệ điều hành phải boot lại từ đầu khi `Start`; khi `Hibernate`, trạng thái trong RAM được khôi phục nguyên vẹn nên khởi động cực nhanh.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Điều kiện bắt buộc:** Ổ cứng **Root EBS Volume BẮT BUỘC phải được mã hóa (Encrypted)** và phải đủ dung lượng trống để chứa toàn bộ dung lượng RAM!
  - **Giới hạn:** Dung lượng RAM của instance phải **nhỏ hơn 150 GB**; thời gian Hibernate tối đa không quá **60 ngày**.
  - **Từ khóa gợi ý:** `"preserve in-memory (RAM) state"`, `"fast boot time after stopping"` $\rightarrow$ **EC2 Hibernate (with Encrypted Root EBS Volume)**.

---

## Danh sách các bài giảng trong Section 6

| STT | Lecture ID | Tên bài học | Thời lượng | Trạng thái |
| :-: | :---: | :--- | :---: | :---: |
| 47 | `13528052` | [Private vs Public vs Elastic IP](./47-private-vs-public-vs-elastic-ip.md) | 04:42 | **Đã lưu** |
| 48 | `13528054` | [Private vs Public vs Elastic IP Hands On](./48-private-vs-public-vs-elastic-ip-hands-on.md) | 06:06 | **Đã lưu** |
| 49 | `13528080` | [EC2 Placement Groups](./49-ec2-placement-groups.md) | 06:55 | **Đã lưu** |
| 50 | `26118770` | [EC2 Placement Groups - Hands On](./50-ec2-placement-groups-hands-on.md) | 01:42 | **Đã lưu** |
| 51 | `18077955` | [Elastic Network Interfaces (ENI) - Overview](./51-elastic-network-interfaces-eni-overview.md) | 02:16 | **Đã lưu** |
| 52 | `26118774` | [Elastic Network Interfaces (ENI) - Hands On](./52-elastic-network-interfaces-eni-hands-on.md) | 05:23 | **Đã lưu** |
| 53 | `20680996` | [ENI - Extra Reading (Article)](./53-eni-extra-reading.md) | 00:21 | **Đã lưu** |
| 54 | `18104377` | [EC2 Hibernate](./54-ec2-hibernate.md) | 03:13 | **Đã lưu** |
| 55 | `18105183` | [EC2 Hibernate - Hands On](./55-ec2-hibernate-hands-on.md) | 04:07 | **Đã lưu** |
| Quiz 3 | `5334512` | [EC2 - Solutions Architect Associate Level Quiz (5 Questions)](./quiz-03-ec2-saa-level-quiz.md) | 5 câu hỏi | **Đã lưu** |
