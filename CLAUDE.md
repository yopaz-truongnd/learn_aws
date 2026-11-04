# CLAUDE.md

Tài liệu hướng dẫn dành cho AI Agent (Claude Code / Antigravity) và nhà phát triển khi làm việc với dự án này.

## Ngôn ngữ giao tiếp (Language)

- Luôn giao tiếp với người dùng bằng **tiếng Việt** (giải thích, trao đổi, tóm tắt, đặt câu hỏi).
- Giữ nguyên tên dịch vụ AWS và các thuật ngữ kỹ thuật chuyên ngành bằng **tiếng Anh** (ví dụ: *Explicit Deny*, *Trust Policy*, *Instance Store*, *Security Group Reference*, *Savings Plans*).

---

## Mục tiêu dự án (Project Scope)

Kho tài liệu tự học và ôn thi chứng chỉ **AWS Certified Solutions Architect - Associate (SAA-C03)** dựa trên giáo trình khóa học Udemy *"Ultimate AWS Certified Solutions Architect Associate"* của Stephane Maarek.

Đặc trưng kỹ thuật:
- Hoàn toàn **tự chứa (self-contained)**: Không dùng build system, không package manager, không linter/test suite phức tạp.
- Không dùng JavaScript bên ngoài, không kéo font/CSS từ CDN; mở trực tiếp file HTML trên trình duyệt (`open <file>.html`) hoặc mở file CSV bằng Excel/Numbers.

---

## Cấu trúc thư mục & Danh mục tệp (File Inventory)

| Tệp tin | Vai trò & Mô tả | Trạng thái |
| :--- | :--- | :--- |
| `index.html` | **Trang Dashboard trung tâm:** Thống kê tiến độ, 4 Domain đề thi SAA-C03, bảng mục lục 16 Section liên kết đến từng cheat sheet, trích đoạn từ vựng nổi bật và nguồn bài giảng Udemy. | Hoàn thành |
| `aws_global_infra.html` | **Section 3:** AWS Global Infrastructure (Regions, AZs, Data Centers, Edge Locations / PoP, Local Zones, Wavelength, Outposts, nguồn bài giảng Udemy). | Hoàn thành |
| `aws_iam.html` | **Section 4:** AWS IAM (Users, Groups, Roles, Policies JSON, Evaluation Logic, MFA, Tools, Golden Rules, nguồn bài giảng Udemy). | Hoàn thành |
| `aws_ec2.html` | **Section 5:** AWS EC2 (Instance Types, Purchasing Options, Security Groups, User Data, IMDSv2, SSM Session Manager, Placement Groups, nguồn bài giảng Udemy). | Hoàn thành |
| `lecturesub-tu-vung.csv` | **Bộ từ vựng trích xuất từ phụ đề bài giảng:** UTF-8 with BOM, trường bọc ngoặc kép (`"Từ"`, `"Nghĩa"`, `"Nguồn"`, `"Đích"`, `"Câu gốc"`, `"Bài học"`, `"Giây"`, `"Liên kết"`). | Đang duy trì (86+ từ) |
| `AWS_SAA_C03_Vocabulary.apkg` | **Gói Anki hoàn chỉnh chuẩn format 4000Book1:** Tự chứa 100%, đóng gói sẵn Note Type Cloze, kiểm tra gõ phím (`type:cloze`), chia 20 từ/Unit, IPA và link Udemy. | Sẵn sàng mở |
| `anki_4000_format.tsv` | **Bộ Flashcard dạng TSV 11 cột:** Chuẩn 11 trường của model `4000Book1` để import vào bất kỳ deck Anki nào. | Sẵn sàng import |
| `export_anki_4000.py` | **Script chuyển đổi tự động (Tự chứa 100%):** Tự sinh SQLite và đóng gói `AWS_SAA_C03_Vocabulary.apkg`, không phụ thuộc bất kỳ file mẫu ngoài nào. | Hoàn thành |
| `.claude/skills/new-topic/` | Skill tự động sinh khung cheat sheet chủ đề mới theo mẫu chuẩn. | Sẵn sàng |
| `.claude/skills/csv-to-apkg/` | Skill chuyển đổi file CSV từ vựng sang gói Anki `.apkg` chuẩn model 4000Book1 (tự chứa 100%). | Sẵn sàng |

---

## Lộ trình các chủ đề tiếp theo (Roadmap for Next Sessions)

Khi tiếp tục phiên làm việc mới, hãy đối chiếu danh sách các Section cần làm tiếp dưới đây:

1. **Section 6: EC2 Instance Storage (`aws_storage.html`)**
   - *Nguồn:* Udemy Section 6 (EC2 - Instance Storage: EBS & EFS)
   - EBS volume types (gp3, gp2, io2 Block Express, st1, sc1), EBS Snapshots, Multi-Attach.
   - EFS (Elastic File System): Multi-AZ, POSIX, EFS One Zone, Storage classes (Standard, IA).
   - EC2 Instance Store: Ephemeral storage, IOPS siêu cao, mất dữ liệu khi stop/terminate.
2. **Section 7: High Availability & Scalability (`aws_elb_asg.html`)**
   - *Nguồn:* Udemy Section 7 (High Availability and Scalability: ELB & ASG)
   - Elastic Load Balancing: ALB (Layer 7), NLB (Layer 4 - Ultra performance), GWLB (Layer 3 - Firewalls).
   - Target Groups, Health Checks, Cross-Zone Load Balancing, SNI (Server Name Indication).
   - Auto Scaling Groups (ASG): Dynamic scaling, Predictive scaling, Lifecycle hooks, Target tracking.
3. **Section 8 & 20: AWS Databases (`aws_databases.html`)**
   - *Nguồn:* Udemy Section 8 (RDS + Aurora + ElastiCache) & Section 20 (Databases in AWS)
   - RDS: Multi-AZ (DR/Failover) vs Read Replicas (Scale Reads, async).
   - Amazon Aurora: 6 bản sao trên 3 AZs, Aurora Serverless v2, Global Database.
   - In-memory Caching: ElastiCache (Redis vs Memcached), MemoryDB.
   - NoSQL & Special: DynamoDB (DAX, Global Tables), Redshift, OpenSearch, DocumentDB, Neptune.
4. **Section 9: Amazon Route 53 (`aws_route53.html`)**
   - *Nguồn:* Udemy Section 9 (Route 53)
   - Routing Policies: Simple, Weighted, Latency, Failover (Health checks), Geolocation, Geoproximity, Multi-Value Answer.
5. **Section 11 & 13: Amazon S3 & Advanced S3 (`aws_s3.html`)**
   - *Nguồn:* Udemy Section 11 (S3 Intro) & Section 13 (Advanced S3)
   - S3 Storage Classes: Standard, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive, Intelligent-Tiering.
   - S3 Security: Bucket Policies, KMS encryption, Object Lock, Versioning, S3 Replication (CRR/SRR).
6. **Section 14: CloudFront & Global Accelerator (`aws_cloudfront.html`)**
   - *Nguồn:* Udemy Section 14 (CloudFront & AWS Global Accelerator)
   - CloudFront: Caching, TTL, Origin Shield, Signed URL/Cookies, OAC (Origin Access Control) cho S3.
   - AWS Global Accelerator: Anycast IP, định tuyến qua mạng AWS Backbone (so sánh với CloudFront).
7. **Section 16: Decoupling Applications (`aws_decoupling.html`)**
   - *Nguồn:* Udemy Section 16 (Decoupling Applications: SQS, SNS, Kinesis, Active MQ)
   - Amazon SQS: Standard (at-least-once) vs FIFO (exactly-once, order), DLQ (Dead Letter Queue), Visibility Timeout.
   - Amazon SNS: Pub/Sub Fan-out pattern, Topic Subscriptions.
   - Amazon Kinesis: Data Streams (shards, real-time), Firehose (near real-time S3/Redshift loader), Data Analytics.
8. **Section 17: Containers on AWS (`aws_containers.html`)**
   - *Nguồn:* Udemy Section 17 (Containers on AWS: ECS, Fargate, ECR, EKS)
   - ECS (Elastic Container Service): EC2 Launch Type vs Fargate (Serverless container).
   - ECR (Elastic Container Registry), EKS (Elastic Kubernetes Service).
9. **Section 18 & 19: Serverless Architecture (`aws_serverless.html`)**
   - *Nguồn:* Udemy Section 18 (Serverless Overviews) & Section 19 (Serverless Solutions)
   - AWS Lambda: Concurrency, Cold start, Destinations, Execution limits (15 phút, 10GB RAM).
   - Amazon API Gateway: REST API, HTTP API, WebSocket, Throttling, API Keys, Caching.
   - AWS Step Functions: State machines for workflow orchestration.
10. **Section 23: Monitoring, Audit & Governance (`aws_monitoring.html`)**
    - *Nguồn:* Udemy Section 23 (AWS Monitoring & Audit)
    - CloudWatch: Metrics, Alarms, Logs, Synthetics, Container Insights.
    - CloudTrail: Ghi nhận mọi API calls, Trail bảo mật, phân tích sự cố.
    - EventBridge: Phản ứng sự kiện thời gian thực (Rule & Target, cron scheduler).
11. **Section 24: Security, Encryption & Compliance (`aws_security.html`)**
    - *Nguồn:* Udemy Section 24 (AWS Security & Encryption)
    - AWS KMS: Customer Master Keys (CMK), Symmetric vs Asymmetric, Automatic Key Rotation.
    - Secrets Manager (tự động rotate password RDS) vs SSM Parameter Store.
    - AWS WAF, AWS Shield Standard/Advanced, AWS Network Firewall, AWS GuardDuty, AWS Inspector, AWS Macie.
12. **Section 25: Networking — Virtual Private Cloud (`aws_vpc.html`)**
    - *Nguồn:* Udemy Section 25 (Networking - VPC)
    - CIDR, Public Subnets, Private Subnets, Internet Gateway (IGW), Route Tables.
    - NAT Gateway (quản lý bởi AWS, Multi-AZ) vs NAT Instance.
    - Network ACL (NACL - Stateless, Subnet-level, có Deny rules) vs Security Group (SG - Stateful, Instance-level).
    - VPC Peering, VPC Endpoints (Gateway vs Interface Endpoints / PrivateLink), Transit Gateway.
13. **Section 26: Disaster Recovery & Data Migration (`aws_disaster_recovery.html`)**
    - *Nguồn:* Udemy Section 26 (Disaster Recovery & Migrations)
    - 4 chiến lược DR: Backup & Restore, Pilot Light, Warm Standby, Multi-Region Active-Active.
    - AWS DRS (Elastic Disaster Recovery), AWS DMS (Database Migration Service), AWS Snow Family, DataSync.

---

## Quy ước thiết kế & Thành phần HTML (Design System)

Khi tạo mới hoặc cập nhật một trang `aws_<topic>.html`:

### 1. Token CSS & Chế độ màu (Dark/Light mode)
- Copy nguyên vẹn khối `<style>` từ [`aws_iam.html`](file:///private/var/www/learn_aws/aws_iam.html).
- Sử dụng triệt để các biến CSS `:root`:
  - Nền & Thẻ: `--bg`, `--card`, `--bd`, `--sub`, `--tx`, `--mu`, `--gy`.
  - Cặp màu trạng thái (Chữ / Nền): Xanh lam (`--bl` / `--blb`), Xanh lá (`--gr` / `--grb`), Cam (`--or` / `--orb`), Đỏ (`--rd` / `--rdb`).
  - Tuyệt đối không dùng mã hex màu trực tiếp ngoài token (ngoại trừ thẻ code `.json`).

### 2. Cấu trúc khung trang chuẩn
1. **Thanh điều hướng trên cùng (`.top-nav`)**:
   ```html
   <div class="top-nav">
     <a href="index.html" class="nav-back">← Mục lục khóa học</a>
     <span style="font-size:12px;color:var(--mu)">Section X · Udemy SAA-C03</span>
   </div>
   ```
2. **Tiêu đề (`.header`)**:
   - `.badge`: Phạm vi dịch vụ (`Global Service` / `Regional Service` / `AZ-Scoped`).
   - `h1`: Tên chính thức của dịch vụ AWS.
   - `p`: Một câu tóm tắt giá trị kiến trúc bằng tiếng Việt.
3. **Lưới thẻ (`.grid`)**: Chứa các thẻ `.card` (dùng thêm class `.full` cho thẻ trải rộng cả 2 cột).
4. **Các component tái sử dụng**:
   - `.g2` + `.it`: Lưới 2 cột cho định nghĩa thực thể/khái niệm.
   - `.flow` + `.st` + `.ar`: Sơ đồ luồng xử lý hoặc thứ tự đánh giá.
   - `.cols` + `.col` + `.pi`: So sánh giữa 2 hoặc 3 phương án kiến trúc.
   - `.tag`: Nhãn từ khóa ngắn gọn (`tb`, `tg`, `to`, `tr`, `ty`).
   - `.sl`: Danh sách tính năng kèm icon nền màu.
   - `.tools`: Lưới các dịch vụ/công cụ vệ tinh liên quan.
   - `.json`: Khối code JSON cấu hình/policy có tô màu `.jk`, `.jv`, `.jc`, `.jp`.
   - Card **"Bổ sung hay gặp trong đề thi SAA-C03"**: Điểm danh các bẫy đề thi, số liệu quan trọng, sự cố thực tế.
   - Card **"Nguyên tắc vàng — SAA-C03"**: Dạng `.bp` / `.bi`, mục cảnh báo cốt lõi dùng số `.bn` màu đỏ `--rd`.
   - Card **"Nguồn bài giảng tham chiếu (Udemy Lectures)"** (BẮT BUỘC): Liệt kê 2 cột dạng `.g2/.it`:
     - Cột 1: Video bài giảng Udemy cốt lõi kèm link chính xác từ `lecturesub-tu-vung.csv` (`https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/<id>`).
     - Cột 2: Tài liệu chính thức từ AWS Documentation / Architecture Whitepaper liên quan.

### 3. Quy trình thực hiện khi tạo bài mới (Workflow)
1. Tạo file `aws_<topic>.html` ở thư mục gốc.
2. Tra cứu `lecturesub-tu-vung.csv` để lấy danh sách từ vựng, câu ngữ cảnh và link video bài giảng tương ứng đưa vào nội dung và khối Nguồn tham chiếu.
3. Bổ sung card "Nguồn bài giảng tham chiếu (Udemy Lectures)" với đầy đủ liên kết video bài giảng và AWS Documentation.
4. Đảm bảo toàn bộ HTML đóng thẻ hợp lệ (kiểm tra bằng script python validator).
5. **Cập nhật `index.html`**:
   - Thêm dòng chú thích nguồn bài giảng `📚 Nguồn: Udemy Section X · Lectures...`.
   - Sửa trạng thái mục bài học từ `btn-pending` / `Kế tiếp` sang `btn-open` / `Đã có`.
   - Tăng biến đếm "Chủ đề hoàn thành" trong khối `.stats`.
6. Báo cáo lại cho người dùng và mở kiểm tra bằng lệnh `open aws_<topic>.html`.
