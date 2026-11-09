# Section 09: AWS Fundamentals: RDS + Aurora + ElastiCache

Thư mục này lưu trữ toàn bộ nội dung bài giảng, ghi chú trọng tâm kỳ thi SAA-C03 (Exam Notes), phụ đề song ngữ Anh - Việt chi tiết theo mốc thời gian (Full Transcript & Timestamps) và bộ câu hỏi trắc nghiệm của **Phần 9: AWS Fundamentals: RDS + Aurora + ElastiCache**.
- **Cheat sheet:** [topics/aws_databases.html](../../topics/aws_databases.html)

---

## Tóm tắt nhanh các dịch vụ trong Phần 9 (Service Cheat Sheet)

### 1. Amazon RDS (Relational Database Service)
- **Là gì:** Dịch vụ cơ sở dữ liệu quan hệ (SQL) được quản lý hoàn toàn (Managed DB service) hỗ trợ 6 engines: **PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server, IBM Db2**.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Chạy cơ sở dữ liệu quan hệ truyền thống với chi phí quản trị vận hành tối thiểu (**least operational overhead**): AWS tự động hóa vá lỗi OS, sao lưu liên tục (**Point-in-Time Recovery**), giám sát và chuyển đổi dự phòng (**Multi-AZ**).
  - Tăng tải đọc (**Scale Read Workload / Reporting / Analytics**) bằng **RDS Read Replicas**; hoặc đảm bảo tính sẵn sàng cao (**High Availability / Disaster Recovery**) bằng **RDS Multi-AZ**.
- **Khác gì dịch vụ gần giống:**
  - **RDS vs. Database trên EC2:** Tự cài DB trên `EC2` cho phép bạn truy cập SSH vào OS nhưng phải tự lo backup/patching/HA; `RDS` là dịch vụ quản lý hoàn toàn (**bạn KHÔNG thể SSH vào RDS**), trừ khi dùng **`RDS Custom`** (chỉ hỗ trợ **Oracle** và **MS SQL Server**) khi bắt buộc cần quyền admin OS/DB sâu.
  - **RDS Read Replicas vs. RDS Multi-AZ:**
    - `Read Replicas` dùng để **Mở rộng tải đọc (Scalability)**, sao chép **Bất đồng bộ (Asynchronous)**, ứng dụng phải cập nhật chuỗi kết nối tới các Read Replicas.
    - `Multi-AZ` dùng cho **Chống lỗi / Dự phòng thảm họa (HA / DR)**, sao chép **Đồng bộ (Synchronous)** sang 1 Standby DB, **Stanby KHÔNG phục vụ đọc**, và tự động Failover qua cùng 1 DNS Endpoint duy nhất mà không cần sửa code ứng dụng.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Giới hạn & Mặc định:** Hỗ trợ tối đa **15 Read Replicas**; lưu trữ **Automated Backups** tối đa **35 ngày** (nếu muốn giữ lâu hơn phải dùng **Manual DB Snapshots**).
  - **Chi phí mạng:** Nhân bản dữ liệu sang Read Replica nằm ở **cùng Region (dù khác AZ) là MIỄN PHÍ**; nhân bản **Cross-Region sẽ bị tính phí** truyền dữ liệu.
  - **Mã hóa:** Một RDS instance chưa mã hóa (Unencrypted) **không thể** bật mã hóa trực tiếp $\rightarrow$ phải tạo Snapshot $\rightarrow$ **Copy Snapshot và bật Encryption** $\rightarrow$ Restore từ Snapshot đã mã hóa.

### 2. Amazon Aurora
- **Là gì:** Công nghệ cơ sở dữ liệu đám mây độc quyền của AWS tương thích hoàn toàn với **PostgreSQL** và **MySQL**, nhanh gấp 5 lần MySQL và 3 lần PostgreSQL trên RDS với kiến trúc lưu trữ phân tán tự phục hồi.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Hệ thống cơ sở dữ liệu quan hệ cấp doanh nghiệp cần hiệu năng cực cao, tự động mở rộng dung lượng, **Failover tức thì (< 30 giây)**, hoặc cần kiến trúc đa vùng toàn cầu (**Aurora Global Database**) với RTO/RPO < 1 giây.
  - Tải truy cập thất thường, không dự đoán được hoặc chạy ngắt quãng $\rightarrow$ dùng **Aurora Serverless**.
- **Khác gì dịch vụ gần giống:**
  - **Aurora vs. RDS thông thường:** `Aurora` luôn lưu trữ **6 bản sao dữ liệu trên 3 Availability Zones** (cần 4/6 bản sao để ghi và 3/6 bản sao để đọc), dung lượng tự động tăng từ **10 GB lên tới 128 TB**; đặc biệt mọi **Aurora Replicas (tối đa 15 cái) đều dùng chung tầng Shared Storage** nên vừa phục vụ tải đọc thông qua **Reader Endpoint** vừa đóng vai trò mục tiêu Failover Multi-AZ!
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Tính năng độc quyền của Aurora:**
    - **Aurora Cloning:** Tạo bản sao DB cực nhanh và tiết kiệm cho môi trường staging/testing nhờ cơ chế **`Copy-on-Write`** (không sao chép vật lý dữ liệu ngay lập tức).
    - **Aurora Global Database:** 1 Primary Region + tối đa **5 Secondary Regions** (mỗi Secondary Region tối đa 16 Read Replicas), độ trễ sao chép **< 1 giây**, thời gian khôi phục thảm họa liên vùng (RTO) **< 1 phút**.
    - **Aurora Custom Endpoints:** Nhóm một tập con các Aurora Replicas có cấu hình mạnh hơn để chạy riêng các truy vấn phân tích (**Analytical queries**).
  - **Từ khóa gợi ý:** `"MySQL/PostgreSQL compatible, 6 copies across 3 AZs, Reader Endpoint, fast cloning (copy-on-write), Global Database < 1s replication"` $\rightarrow$ **Amazon Aurora**.

### 3. Amazon RDS Proxy
- **Là gì:** Dịch vụ quản lý tập trung và chia sẻ các kết nối cơ sở dữ liệu (**Fully Managed Database Connection Pooling**) nằm giữa ứng dụng và RDS/Aurora.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Các ứng dụng Serverless (**AWS Lambda**) mở rộng đột biến tạo ra hàng nghìn kết nối mới làm quá tải CPU/RAM của RDS/Aurora (`Too many connections` / `Connection timeout`).
  - Cần giảm thời gian chuyển đổi dự phòng (**giảm tới 66% thời gian Failover**) và bắt buộc xác thực qua **IAM Authentication** kèm lưu trữ thông tin đăng nhập trong **AWS Secrets Manager**.
- **Khác gì dịch vụ gần giống:**
  - Khác với `ElastiCache` (lưu bộ nhớ đệm cho **kết quả truy vấn** để giảm tải đọc), `RDS Proxy` quản lý và tái sử dụng **kết nối TCP/DB (Connection Pool)** tới cơ sở dữ liệu.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định / Bảo mật:** RDS Proxy **chỉ truy cập được từ bên trong VPC** (không bao giờ truy cập công khai từ Internet).
  - **Từ khóa gợi ý:** `"Lambda functions exhausting database connections"`, `"connection pooling"`, `"reduce RDS/Aurora failover time by 66%"`, `"enforce IAM authentication with Secrets Manager"` $\rightarrow$ **Amazon RDS Proxy**.

### 4. Amazon ElastiCache (Redis & Memcached)
- **Là gì:** Dịch vụ cơ sở dữ liệu lưu trữ trên bộ nhớ RAM được quản lý hoàn toàn (**Managed In-Memory Data Store & Cache**) hỗ trợ hai engine là **Redis** và **Memcached** với độ trễ dưới một phần nghìn giây (sub-millisecond).
- **Dùng khi nào (Use case điển hình trong đề):**
  - Giảm tải các truy vấn đọc lặp đi lặp lại trên RDS/Aurora (**Cache-aside / Lazy Loading**).
  - Lưu trữ trạng thái phiên đăng nhập của người dùng (**User Session Store**) để làm cho tầng EC2/Application trở nên **Stateless**.
  - Xây dựng bảng xếp hạng thời gian thực (**Gaming Leaderboards**) bằng cấu trúc dữ liệu **`Redis Sorted Sets`**.
- **Khác gì dịch vụ gần giống:**
  - **ElastiCache for Redis vs. ElastiCache for Memcached:**
    - **`Redis`:** Hỗ trợ **Multi-AZ với Auto-Failover**, **Read Replicas**, sao lưu bền vững (**AOF Persistence, Backup & Restore**), **IAM Auth / Redis AUTH / SSL**, và cấu trúc **`Sorted Sets`** (dùng cho Leaderboards).
    - **`Memcached`:** Kiến trúc phân mảnh đa luồng đơn giản (**Multi-threaded, Sharding**), **KHÔNG có High Availability (Multi-AZ)**, **KHÔNG có Backup/Restore**, mất dữ liệu khi node khởi động lại.
  - **ElastiCache vs. DynamoDB Accelerator (DAX):** Nếu cơ sở dữ liệu phía sau là `DynamoDB` và cần cache tích hợp sẵn không phải viết lại logic ứng dụng thì dùng `DAX`; nếu là `RDS/Aurora` hoặc cần Session Store / Leaderboard thì dùng `ElastiCache`.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Từ khóa gợi ý:** `"sub-millisecond latency cache for RDS"`, `"stateless session store"` $\rightarrow$ **ElastiCache**; `"gaming leaderboards / real-time ranking"` $\rightarrow$ **ElastiCache for Redis (Sorted Sets)**; `"multi-threaded pure cache without persistence/HA"` $\rightarrow$ **ElastiCache for Memcached**.

---

## Danh sách bài học (Lectures)

| STT | Tên bài học (Lecture Title) | Loại | Thời lượng | Tài liệu chi tiết | Trạng thái |
| :-: | :--- | :-: | :-: | :--- | :-: |
| 87 | Amazon RDS Overview | Video | `03:38` | [87-amazon-rds-overview.md](./87-amazon-rds-overview.md) | **Đã lưu** |
| 88 | RDS Read Replicas vs Multi AZ | Video | `07:22` | [88-rds-read-replicas-vs-multi-az.md](./88-rds-read-replicas-vs-multi-az.md) | **Đã lưu** |
| 89 | Amazon RDS Hands On | Video | `08:44` | [89-amazon-rds-hands-on.md](./89-amazon-rds-hands-on.md) | **Đã lưu** |
| 90 | RDS Custom for Oracle and Microsoft SQL Server | Video | `01:49` | [90-rds-custom-for-oracle-and-microsoft-sql-server.md](./90-rds-custom-for-oracle-and-microsoft-sql-server.md) | **Đã lưu** |
| 91 | Amazon Aurora | Video | `06:27` | [91-amazon-aurora.md](./91-amazon-aurora.md) | **Đã lưu** |
| 92 | Amazon Aurora - Hands On | Video | `08:22` | [92-amazon-aurora-hands-on.md](./92-amazon-aurora-hands-on.md) | **Đã lưu** |
| 93 | Amazon Aurora - Advanced Concepts | Video | `07:31` | [93-amazon-aurora-advanced-concepts.md](./93-amazon-aurora-advanced-concepts.md) | **Đã lưu** |
| 94 | RDS & Aurora - Backup and Monitoring | Video | `05:36` | [94-rds-and-aurora-backup-and-monitoring.md](./94-rds-and-aurora-backup-and-monitoring.md) | **Đã lưu** |
| 95 | RDS & Aurora Security | Video | `02:32` | [95-rds-and-aurora-security.md](./95-rds-and-aurora-security.md) | **Đã lưu** |
| 96 | Amazon RDS Proxy | Video | `04:32` | [96-amazon-rds-proxy.md](./96-amazon-rds-proxy.md) | **Đã lưu** |
| 97 | ElastiCache Overview | Video | `04:42` | [97-elasticache-overview.md](./97-elasticache-overview.md) | **Đã lưu** |
| 98 | ElastiCache Hands On | Video | `05:00` | [98-elasticache-hands-on.md](./98-elasticache-hands-on.md) | **Đã lưu** |
| 99 | ElastiCache for Solution Architects | Video | `03:00` | [99-elasticache-for-solution-architects.md](./99-elasticache-for-solution-architects.md) | **Đã lưu** |
| 100 | List of Ports to be familiar with | Article | `00:29` | [100-list-of-ports-to-be-familiar-with.md](./100-list-of-ports-to-be-familiar-with.md) | **Đã lưu** |
| Quiz 6 | RDS, Aurora, and ElastiCache Quiz (24 câu hỏi) | Quiz | `24 câu` | [quiz-06-rds-aurora-and-elasticache-quiz.md](./quiz-06-rds-aurora-and-elasticache-quiz.md) | **Đã lưu** |
