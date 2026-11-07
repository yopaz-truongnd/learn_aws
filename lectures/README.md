# Khóa học: Ultimate AWS Certified Solutions Architect Associate 2026 (SAA-C03)

- **Giảng viên:** Stéphane Maarek
- **Course ID:** `2196488`

## Danh sách các phần (Phần 4 -> Phần 10)

| Phần | Tên phần (Section) | Số bài giảng | Trắc nghiệm | Trạng thái | Đường dẫn thư mục |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **04** | **IAM & AWS CLI** | 20 bài (11 - 30) | Quiz 1 (6 câu) | **Đã hoàn thành (100%)** | [section-04-iam-and-aws-cli](./section-04-iam-and-aws-cli/README.md) |
| **05** | **EC2 Fundamentals** | 16 bài (31 - 46) | Quiz 2 (13 câu) | **Đã hoàn thành (100%)** | [section-05-ec2-fundamentals](./section-05-ec2-fundamentals/README.md) |
| **06** | **EC2 - Solutions Architect Associate Level** | 9 bài (47 - 55) | Quiz 3 (8 câu) | **Đã hoàn thành (100%)** | [section-06-ec2-saa-level](./section-06-ec2-saa-level/README.md) |
| **07** | **EC2 Instance Storage** | 14 bài (56 - 69) | Quiz 4 (11 câu) | **Đã hoàn thành (100%)** | [section-07-ec2-instance-storage](./section-07-ec2-instance-storage/README.md) |
| **08** | **High Availability and Scalability: ELB & ASG** | 17 bài (70 - 86) | Quiz 5 (14 câu) | **Đã hoàn thành (100%)** | [section-08-elb-and-asg](./section-08-elb-and-asg/README.md) |
| **09** | **AWS Fundamentals: RDS + Aurora + ElastiCache** | 14 bài (87 - 100) | Quiz 6 (24 câu) | **Đã hoàn thành (100%)** | [section-09-rds-aurora-elasticache](./section-09-rds-aurora-elasticache/README.md) |
| **10** | **Route 53** | 20 bài (101 - 120) | Quiz 7 (7 câu) | **Đã hoàn thành (100%)** | [section-10-route-53](./section-10-route-53/README.md) |

---

## Tóm tắt nhanh toàn bộ các dịch vụ từ Phần 4 -> Phần 10 (SAA-C03 Service Cheat Sheet)

> Mỗi dịch vụ dưới đây được tóm gọn theo đúng 4 tiêu chí cốt lõi phục vụ ôn thi **SAA-C03**:
> 1. **Là gì** (một câu).
> 2. **Dùng khi nào** (use case điển hình trong đề).
> 3. **Khác gì dịch vụ gần giống**.
> 4. **Điểm hay bị hỏi** (giới hạn, mặc định, từ khóa gợi ý).

---

### I. Nhóm Danh tính, Bảo mật & Công cụ Quản trị (Phần 4)

#### 1. AWS IAM (Identity and Access Management)
- **Là gì:** Dịch vụ toàn cầu (Global service) quản lý danh tính người dùng và phân quyền truy cập an toàn vào các tài nguyên AWS.
- **Dùng khi nào:** Cấp quyền theo nguyên tắc đặc quyền tối thiểu (**Least Privilege**) cho Users/Groups; cấp quyền cho dịch vụ AWS (`EC2`, `Lambda`, `ECS`) gọi dịch vụ khác (`S3`, `DynamoDB`) mà không cần lưu khóa tĩnh bằng **`IAM Roles`**; kiểm toán bảo mật bằng **Credentials Report** & **Access Advisor**.
- **Khác gì dịch vụ gần giống:**
  - **IAM Policies vs. S3 Bucket Policies:** `IAM Policy` gắn vào Identity (User/Group/Role); `S3 Bucket Policy` gắn trực tiếp vào tài nguyên S3 (hỗ trợ cấp quyền Cross-Account trực tiếp hoặc mở Public).
  - **IAM Roles vs. Access Keys:** `IAM Role` cấp **Temporary Credentials** tự động xoay vòng qua STS; `Access Keys` là khóa dài hạn gắn với IAM User (tuyệt đối không lưu cứng trong code hay trên EC2).
- **Điểm hay bị hỏi:**
  - **Mặc định:** Mọi thao tác đều bị **Implicit Deny** trừ khi có `Allow`; **`Explicit Deny`** luôn thắng mọi lệnh `Allow`.
  - **Giới hạn:** `IAM Groups` chỉ chứa Users, **không thể lồng Group trong Group**.
  - **Từ khóa gợi ý:** `"without hardcoding credentials"`, `"grant EC2 access to S3"` $\rightarrow$ **IAM Role**; `"identify unused permissions / last accessed service"` $\rightarrow$ **IAM Access Advisor**; `"account-wide audit of MFA and access key rotation"` $\rightarrow$ **IAM Credentials Report**.

#### 2. AWS CLI, SDK & AWS CloudShell
- **Là gì:** Bộ công cụ dòng lệnh (`CLI`), thư viện lập trình (`SDK`) và môi trường terminal trên trình duyệt (`CloudShell`) giúp tương tác trực tiếp với các API của AWS.
- **Dùng khi nào:** Tự động hóa quản trị bằng script (`CLI`), gọi dịch vụ AWS từ code ứng dụng (`SDK`), hoặc chạy lệnh nhanh ngay trên trình duyệt mà không cần cài đặt công cụ cục bộ (`CloudShell`).
- **Khác gì dịch vụ gần giống:** `AWS CLI` trên máy cá nhân cần tự cài và cấu hình Access Keys; `AWS CloudShell` miễn phí, kế thừa sẵn quyền của User đang đăng nhập Console và có **1 GB bộ nhớ lưu trữ bền vững (`$HOME`)** theo từng Region.
- **Điểm hay bị hỏi:**
  - **Mặc định:** Một số AWS SDK nếu không khai báo Region sẽ mặc định trỏ về **`us-east-1`**.
  - **Từ khóa gợi ý:** `"browser-based shell with 1 GB persistent storage"` $\rightarrow$ **AWS CloudShell**.

---

### II. Nhóm Máy chủ ảo & Mạng EC2 (Phần 5 & Phần 6)

#### 3. Amazon EC2 (Elastic Compute Cloud)
- **Là gì:** Dịch vụ cung cấp máy chủ ảo (IaaS) cho phép toàn quyền kiểm soát hệ điều hành và tùy chỉnh cấu hình phần cứng (CPU, RAM, Storage, Networking).
- **Dùng khi nào:** Chạy các ứng dụng yêu cầu quyền quản trị cấp OS, phần mềm đóng gói riêng hoặc tự động cài đặt phần mềm khi khởi tạo lần đầu qua **EC2 User Data**.
- **Khác gì dịch vụ gần giống:**
  - **EC2 vs. AWS Lambda:** `EC2` là máy ảo chạy liên tục, bạn tự quản lý OS; `Lambda` là Serverless FaaS chạy theo sự kiện, giới hạn tối đa **15 phút/lần thực thi** (`"least operational overhead for short event-driven tasks"`).
  - **EC2 Purchasing Options:**
    - `On-Demand`: Ngắn hạn, không cam kết.
    - `Reserved Instances (RI)` / `Savings Plans`: Cam kết **1 hoặc 3 năm** cho tải ổn định (`steady-state`), giảm giá tới ~72% (`Convertible RI` đổi được Instance Family; `Savings Plans` cam kết theo \$/giờ).
    - `Spot Instances`: Giảm tới **90%**, có thể bị AWS thu hồi bất kỳ lúc nào với thông báo trước 2 phút (dùng cho tải chịu lỗi: `batch jobs, big data, stateless workloads`).
    - `Dedicated Hosts`: Máy chủ vật lý riêng cho phép nhìn thấy **Physical Sockets / Cores**, dùng cho **BYOL (Bring Your Own License)** tính theo socket/core và tuân thủ nghiêm ngặt.
- **Điểm hay bị hỏi:**
  - **Mặc định:** **EC2 User Data** chỉ chạy **1 lần ở lần khởi tạo đầu tiên** dưới quyền **`root`**.
  - **Từ khóa gợi ý:** `"server-bound software licenses (per-socket/per-core)"` $\rightarrow$ **Dedicated Hosts**; `"most cost-effective, fault-tolerant batch job"` $\rightarrow$ **Spot Instances**.

#### 4. Security Groups (Nhóm bảo mật)
- **Là gì:** Tường lửa ảo hoạt động ở cấp độ EC2 Instance / ENI dùng để lọc lưu lượng mạng Inbound và Outbound theo port, giao thức và IP/Security Group.
- **Dùng khi nào:** Bảo vệ từng tầng máy chủ (Web, App, DB) bằng cách chỉ mở cổng cần thiết và **tham chiếu chéo Security Group** giữa các tầng.
- **Khác gì dịch vụ gần giống:**
  - **Security Group vs. Network ACL (NACL):** `Security Group` ở cấp Instance, **Stateful** (vào được là ra được), chỉ có lệnh **`Allow`**; `NACL` ở cấp Subnet, **Stateless**, có cả **`Allow` và `Deny`**.
- **Điểm hay bị hỏi:**
  - **Mặc định:** Mới tạo thì **Inbound chặn hết**, **Outbound mở hết (`0.0.0.0/0`)**.
  - **Từ khóa gợi ý:** `"Connection Timeout"` $\rightarrow$ lỗi **Security Group** chặn kết nối; `"Connection Refused"` $\rightarrow$ ứng dụng trong EC2 chưa chạy.

#### 5. Elastic IP (EIP) & Elastic Network Interface (ENI)
- **Là gì:** `Elastic IP` là địa chỉ **Public IPv4 tĩnh** thuộc sở hữu của tài khoản; `ENI` là **card mạng ảo** trong VPC chứa Private IP, Public/Elastic IP, Security Groups và MAC address.
- **Dùng khi nào:** Dùng `EIP` khi cần cố định Public IPv4 qua các lần Stop/Start hoặc di chuyển nhanh IP giữa 2 máy; dùng `ENI` khi cần di chuyển **Private IP cố định** hoặc gắn máy chủ vào nhiều Subnets trong cùng 1 AZ.
- **Khác gì dịch vụ gần giống:** `Public IP` mặc định bị đổi mỗi khi Stop/Start EC2, còn `Elastic IP` giữ nguyên; `ENI` gắn chặt với **1 AZ duy nhất**, còn `EIP` gắn ở cấp Region.
- **Điểm hay bị hỏi:**
  - **Giới hạn & Mặc định:** Giới hạn mặc định **5 Elastic IPs / Region**; EIP bị tính phí nếu gắn vào máy đang `Stopped` hoặc để không; `Primary ENI (eth0)` không thể tháo rời.

#### 6. EC2 Placement Groups & EC2 Hibernate
- **Là gì:** `Placement Groups` kiểm soát vị trí đặt EC2 trên phần cứng vật lý; `EC2 Hibernate` bảo toàn trạng thái bộ nhớ **RAM** xuống ổ đĩa Root EBS khi dừng máy.
- **Dùng khi nào & Khác nhau ở đâu:**
  - **`Cluster` Placement Group:** Cùng 1 Rack / 1 AZ $\rightarrow$ mạng **10 Gbps+**, độ trễ thấp nhất cho **HPC** (rủi ro sập cả cụm nếu hỏng Rack).
  - **`Spread` Placement Group:** Mỗi máy nằm trên 1 phần cứng riêng biệt across AZs $\rightarrow$ cách ly lỗi tối đa cho các **Critical instances** (giới hạn cứng **tối đa 7 instances / AZ**).
  - **`Partition` Placement Group:** Chia thành các phân vùng Racks độc lập (tối đa **7 partitions / AZ**) cho hàng trăm instances chạy **HDFS, HBase, Cassandra, Kafka**.
  - **`EC2 Hibernate`:** Giữ nguyên cache/state trong RAM để khởi động lại cực nhanh (yêu cầu **Root EBS Volume phải được mã hóa**, RAM < 150 GB, tối đa 60 ngày).

---

### III. Nhóm Lưu trữ cho EC2 (Phần 7)

#### 7. Amazon EBS (Elastic Block Store), EC2 Instance Store & Amazon EFS
- **Là gì:**
  - **`EBS`:** Ổ đĩa mạng dạng khối (**Network Block Storage**) gắn vào 1 EC2 trong **1 AZ**.
  - **`EC2 Instance Store`:** Ổ cứng vật lý gắn trực tiếp trên host vật lý (**Hardware Block Storage**), tốc độ I/O cực đại nhưng mất dữ liệu khi Stop máy (**Ephemeral**).
  - **`Amazon EFS`:** Hệ thống tệp mạng quản lý hoàn toàn (**Managed NFS File System**) chia sẻ đồng thời cho hàng trăm máy **Linux EC2** trên **nhiều AZs**.
- **Dùng khi nào & Khác nhau ở đâu:**

| Dịch vụ | Phạm vi & Chia sẻ | Độ bền dữ liệu | Use Case & Từ khóa trong đề thi |
|---|---|---|---|
| **EBS (`gp2/gp3`, `io1/io2`, `st1/sc1`)** | **1 AZ**, gắn 1 EC2 (trừ `io1/io2` **Multi-Attach** tối đa **16 EC2 trong cùng 1 AZ**) | Bền vững qua Stop/Start | Ổ đĩa OS/Database; cần **> 16.000 IOPS** hoặc **Multi-Attach** $\rightarrow$ `io1/io2`; Big Data tuần tự giá rẻ (không boot được) $\rightarrow$ `st1/sc1`. |
| **EC2 Instance Store** | Gắn cứng trên máy vật lý | **Mất dữ liệu khi Stop / Hibernate / Terminate** (giữ khi Reboot) | `"Temporary / ephemeral storage, cache, buffer, scratch data, extreme IOPS (>100k IOPS)"`. |
| **Amazon EFS** | **Multi-AZ**, mount cho **hàng trăm Linux EC2** qua NFS | Bền vững, tự động co giãn | `"Shared POSIX file system across multiple AZs for Linux instances"`; tiết kiệm chi phí bằng **EFS-IA (Lifecycle)** hoặc **EFS One Zone**. |

- **Điểm hay bị hỏi:**
  - **Mặc định EBS:** Khi Terminate EC2, **Root EBS Volume mặc định bị xóa**, các EBS Volume phụ mặc định được giữ lại.
  - **Giới hạn EFS:** Chỉ hỗ trợ **Linux (POSIX)**, không hỗ trợ Windows (Windows dùng **FSx for Windows File Server**).

---

### IV. Nhóm Cân bằng tải & Tự động co giãn (Phần 8)

#### 8. Elastic Load Balancing (ALB, NLB, GWLB) & Auto Scaling Group (ASG)
- **Là gì:** Dịch vụ phân phối lưu lượng tự động (`ELB`) kết hợp với dịch vụ tự động co giãn số lượng EC2 theo tải (`ASG`) across Multiple AZs.
- **Dùng khi nào & Khác nhau ở đâu:**
  - **`ALB` (Layer 7 - HTTP/HTTPS/gRPC/WebSocket):** Định tuyến theo URL Path, Hostname, Header, Query String cho Microservices/Containers; **Cross-Zone LB bật mặc định (miễn phí)**.
  - **`NLB` (Layer 4 - TCP/UDP/TLS):** Xử lý hàng triệu requests/giây, độ trễ ~100 ms, cung cấp **1 Static / Elastic IP mỗi AZ** (dùng khi cần Whitelist IP); **Cross-Zone LB tắt mặc định (tính phí nếu bật)**.
  - **`GWLB` (Layer 3 - IP Packets / GENEVE port `6081`):** Điều hướng toàn bộ lưu lượng mạng qua đội thiết bị bảo mật ảo của bên thứ 3 (**3rd-party Firewalls, IDS/IPS, Deep Packet Inspection**).
  - **`ASG`:** Tự động Scale Out / Scale In theo **Target Tracking** (đơn giản nhất, giữ CPU ở mức đích), **Step Scaling**, **Scheduled Scaling**, hoặc **Predictive Scaling** (dự báo bằng Machine Learning).
- **Điểm hay bị hỏi:**
  - **Mặc định:** ASG Default Cooldown = **300 giây**; Connection Draining (Deregistration Delay) mặc định = **300 giây**; IP thật của Client đi qua ALB nằm trong header **`X-Forwarded-For`**.

---

### V. Nhóm Cơ sở dữ liệu Quan hệ & Bộ nhớ đệm (Phần 9)

#### 9. Amazon RDS, Amazon Aurora, RDS Proxy & Amazon ElastiCache
- **Là gì:**
  - **`Amazon RDS`:** Dịch vụ CSDL quan hệ (SQL) quản lý hoàn toàn cho Postgres, MySQL, MariaDB, Oracle, SQL Server, Db2.
  - **`Amazon Aurora`:** CSDL quan hệ độc quyền của AWS tương thích MySQL/Postgres, lưu **6 bản sao trên 3 AZs**, tự động tăng dung lượng tới **128 TB**.
  - **`RDS Proxy`:** Dịch vụ quản lý tập trung kết nối (**Connection Pooling**) cho RDS/Aurora.
  - **`Amazon ElastiCache`:** Dịch vụ bộ nhớ đệm trong RAM (**In-memory Cache**) hỗ trợ **Redis** và **Memcached**.
- **Dùng khi nào & Khác nhau ở đâu:**
  - **RDS Read Replicas vs. Multi-AZ:** `Read Replicas` (tối đa 15, sao chép **Bất đồng bộ**) dùng để **tăng tải đọc (Scale Reads)**; `Multi-AZ` (sao chép **Đồng bộ**) dùng cho **High Availability / Disaster Recovery** (Standby không phục vụ đọc).
  - **RDS vs. RDS Custom:** `RDS` không cho phép truy cập OS/SSH; `RDS Custom` (chỉ có cho **Oracle** và **MS SQL Server**) cho phép quyền **OS Admin / SSH** để cài gói phần mềm đặc thù.
  - **ElastiCache Redis vs. Memcached:** `Redis` có **Multi-AZ Auto-Failover**, **Read Replicas**, **Backup/Restore**, và **`Sorted Sets`** (cho **Gaming Leaderboards**); `Memcached` là bộ đệm đa luồng phân mảnh thuần túy, **không có HA, không có Backup**.
- **Điểm hay bị hỏi:**
  - **Từ khóa gợi ý:** `"Lambda exhausting DB connections / reduce failover time by 66%"` $\rightarrow$ **RDS Proxy**; `"fast DB cloning for staging without copying data (copy-on-write)"` $\rightarrow$ **Aurora Cloning**; `"global database with < 1s replication lag"` $\rightarrow$ **Aurora Global Database**; `"offload read queries / user session store / leaderboards"` $\rightarrow$ **ElastiCache (Redis)**.

---

### VI. Nhóm Định tuyến Tên miền Toàn cầu & Hybrid DNS (Phần 10)

#### 10. Amazon Route 53 & Route 53 Resolver
- **Là gì:** Dịch vụ Managed Authoritative DNS, Domain Registrar và Health Checks toàn cầu có **100% Availability SLA**.
- **Dùng khi nào & Khác nhau ở đâu:**
  - **Alias vs. CNAME:** `Alias` trỏ tới tài nguyên AWS (ALB, CloudFront, S3 Website, API Gateway... **TRỪ EC2 DNS Name**), **miễn phí** và **dùng được ở Zone Apex (`example.com`)**; `CNAME` tính phí và **chỉ dùng được cho Subdomain (`www.example.com`)**.
  - **Geolocation vs. Latency vs. Geoproximity:**
    - `Latency`: Chọn AWS Region có **độ trễ mạng thấp nhất**.
    - `Geolocation`: Chọn theo **Quốc gia / Châu lục / Bang Mỹ** của người dùng (bản địa hóa ngôn ngữ, giới hạn pháp lý theo nước).
    - `Geoproximity`: Dịch chuyển vùng phủ lưu lượng giữa các Region bằng hệ số **`Bias`**.
  - **Simple (Multiple Values) vs. Multi-Value Answer:** `Simple` không gắn được Health Check; `Multi-Value Answer` gắn được **Health Checks** và trả về tối đa **8 IP khỏe mạnh**.
  - **Route 53 Resolver Inbound vs. Outbound Endpoint:**
    - `Inbound Endpoint`: Phân giải chiều **On-Premises $\rightarrow$ AWS Private Hosted Zone**.
    - `Outbound Endpoint`: Phân giải chiều **AWS VPC $\rightarrow$ On-Premises DNS Server**.
- **Điểm hay bị hỏi:**
  - **Health Check cho Private Resource:** Tạo **CloudWatch Alarm** theo dõi tài nguyên nội bộ, sau đó cấu hình Route 53 Health Check giám sát **CloudWatch Alarm** đó.
  - **Tên miền bên thứ 3 (GoDaddy):** Tạo **Public Hosted Zone** trên Route 53, sau đó cập nhật **NS records trên GoDaddy** trỏ về 4 Name Servers của Route 53.
