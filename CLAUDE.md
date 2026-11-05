# CLAUDE.md

Tài liệu hướng dẫn dành cho AI Agent (Claude Code / Antigravity) và nhà phát triển khi làm việc với dự án này.

## Ngôn ngữ giao tiếp (Language)

- Luôn giao tiếp với người dùng bằng **tiếng Việt** (giải thích, trao đổi, tóm tắt, đặt câu hỏi).
- Giữ nguyên tên dịch vụ AWS và các thuật ngữ kỹ thuật chuyên ngành bằng **tiếng Anh** (ví dụ: *Explicit Deny*, *Trust Policy*, *Instance Store*, *Security Group Reference*, *Savings Plans*).

---

## Quy tắc an toàn & Giới hạn quyền hạn (Security & Permissions)

1. **Phạm vi chỉnh sửa (Project-Only Scope):** Chỉ được quyền chỉnh sửa, tạo mới hoặc ghi đè tệp tin nằm trong thư mục dự án này (learn_aws). Tuyệt đối không can thiệp tệp tin ngoài thư mục dự án.
2. **Thực thi ngoài dự án:** Bất kỳ thao tác hoặc lệnh terminal nào tác động ra ngoài phạm vi dự án **bắt buộc phải hỏi và được người dùng xác nhận trước khi chạy**.
3. **Bảo vệ tệp tin (Bắt buộc xác nhận khi xóa):** Tuyệt đối **không tự ý xóa bất kỳ tệp tin nào** (kể cả tệp tạm). Khi cần xóa, phải liệt kê danh sách tệp và chờ người dùng đồng ý mới được thực hiện.

---

## Mục tiêu dự án (Project Scope)

Kho tài liệu tự học và ôn thi chứng chỉ **AWS Certified Solutions Architect - Associate (SAA-C03)** dựa trên giáo trình khóa học Udemy *"Ultimate AWS Certified Solutions Architect Associate"* của Stephane Maarek. Gồm 3 phần:

1. **Dashboard** `index.html` — mục lục 16 Section, tiến độ, 4 Domain đề thi.
2. **Cheat sheet** `topics/aws_<topic>.html` — mỗi Section một trang HTML/CSS tự chứa.
3. **Từ vựng & Anki** — CSV từ vựng trích từ phụ đề (`data/`) → script (`scripts/`) → deck Anki (`dist/`).

Đặc trưng kỹ thuật:
- Hoàn toàn **tự chứa (self-contained)**: Không build system, không package manager, không linter/test suite. Script Python chỉ dùng thư viện chuẩn (Python 3).
- Trang HTML không dùng thư viện ngoài (CDN, Google Fonts, external JS/CSS); mở trực tiếp trên trình duyệt (`open index.html`).
- **Hỗ trợ Song ngữ (Bilingual VI/EN)**: Toàn bộ Dashboard và các trang Cheat sheet hỗ trợ chuyển đổi tức thì giữa Tiếng Việt và Tiếng Anh qua nút chuyển ngôn ngữ (`localStorage`).

---

## Cấu trúc thư mục & Danh mục tệp (File Inventory)

```
learn_aws/
├── index.html          # Dashboard trung tâm (entry point, nằm ở gốc)
├── topics/             # Cheat sheet từng Section: aws_<topic>.html
├── assets/             # Tài nguyên dùng chung tự chứa (không kéo CDN)
│   ├── css/style.css   #   Design system, tokens, dark/light, components
│   ├── js/app.js       #   Xử lý ngôn ngữ, theme listener, auto-render Mermaid
│   └── vendor/         #   Thư viện nội bộ (mermaid.min.js)
├── scripts/            # Script tiện ích: export_anki_4000.py
├── data/               # Dữ liệu đầu vào: lecturesub-tu-vung.csv (gitignored)
├── dist/               # Output sinh tự động: .apkg, .tsv (gitignored)
├── .claude/skills/     # Skill: new-topic, csv-to-apkg
├── CLAUDE.md           # Tài liệu này
└── README.md           # Giới thiệu dự án cho người đọc
```

### Quy tắc đặt file (bắt buộc)
- **Trang cheat sheet mới** → luôn đặt trong `topics/`, không đặt ở gốc. Chỉ `index.html` nằm ở gốc.
- **Link CSS/JS tương đối:**
  - Trang gốc: `<link rel="stylesheet" href="assets/css/style.css">` và `<script src="assets/js/app.js"></script>`.
  - Trang con trong `topics/`: `<link rel="stylesheet" href="../assets/css/style.css">`, `<script src="../assets/js/app.js"></script>` và nếu dùng diagram thì thêm `<script src="../assets/vendor/mermaid.min.js"></script>`.
- **Script/công cụ** → `scripts/`. Đường dẫn mặc định trong script phải tính theo gốc dự án (`os.path.dirname(__file__)`), không phụ thuộc thư mục hiện hành.
- **Dữ liệu đầu vào** (CSV…) → `data/`; **file sinh ra** (`.apkg`, `.tsv`, …) → `dist/`. Cả hai đều bị `.gitignore` — không commit, không xoá file trong `data/` khi chưa hỏi người dùng.
- File CSV có thể không tồn tại trên máy (repo vừa clone). Khi cần đọc mà không có, báo người dùng chép vào `data/lecturesub-tu-vung.csv` thay vì tự tạo dữ liệu giả.
- Khi đổi tên/di chuyển file: cập nhật đồng thời `index.html`, `README.md`, `CLAUDE.md` và các `.claude/skills/*/SKILL.md`.

| Tệp tin | Vai trò & Mô tả | Trạng thái |
| :--- | :--- | :--- |
| `index.html` | **Trang Dashboard trung tâm:** Thống kê tiến độ, 4 Domain đề thi SAA-C03, bảng mục lục 16 Section liên kết đến từng cheat sheet, trích đoạn từ vựng nổi bật và hướng dẫn Anki. | Hoàn thành |
| `topics/aws_global_infra.html` | **Section 3:** AWS Global Infrastructure (Regions, AZs, Data Centers, Edge PoP, Sơ đồ Mermaid định tuyến, Ma trận chi phí Data Transfer, AZ ID vs AZ Name, Local Zones, Wavelength, Outposts, Direct Connect, Whitepapers). | Hoàn thành |
| `topics/aws_iam.html` | **Section 4:** AWS IAM (Users, Groups, Roles, Policies JSON, Sơ đồ Mermaid đánh giá logic, Ma trận Cross-Account AssumeRole vs Resource Policy, Top Condition Keys, Bộ 3 công cụ Audit, SCPs, Golden Rules). **File mẫu chuẩn**. | Hoàn thành |
| `topics/aws_ec2.html` | **Section 5:** AWS EC2 (Instance Types, Sơ đồ Mermaid vòng đời Lifecycle &amp; Hibernate, Ma trận 7 mô hình Purchasing Options &amp; Spot Fleet, Ma trận SG vs NACL, ENA/EFA, Nitro System, SSM Session Manager). | Hoàn thành |
| `topics/aws_storage.html` | **Section 6:** AWS Storage — EBS, EFS &amp; Instance Store (Tam giác lưu trữ, Sơ đồ Mermaid Cây quyết định, Ma trận 6 loại đĩa EBS gp3/io2, Snapshots &amp; KMS, Multi-Attach, EFS POSIX Multi-AZ &amp; Tiers, Ephemeral Instance Store). | Hoàn thành |
| `topics/aws_elb_asg.html` | **Section 7:** AWS High Availability &amp; Scalability — ELB &amp; ASG (Sơ đồ Mermaid luồng VPC, Ma trận ALB vs NLB vs GWLB vs CLB, Cross-Zone, SNI, Sticky Sessions, ASG Launch Templates &amp; 4 cơ chế Co giãn). | Hoàn thành |
| `topics/aws_databases.html` | **Section 8 &amp; 20:** AWS Databases — RDS, Aurora, DynamoDB &amp; ElastiCache (Cây quyết định Mermaid, RDS Multi-AZ vs Read Replicas, Aurora 6 bản sao trên 3 AZ, DynamoDB NoSQL &amp; DAX, ElastiCache Redis/Memcached). | Hoàn thành |
| `topics/aws_route53.html` | **Section 9:** Amazon Route 53 (CNAME vs Alias Record, Cây quyết định Mermaid, 8 Chính sách định tuyến, Health Checks &amp; Failover tự động). | Hoàn thành |
| `topics/aws_s3.html` | **Section 11 &amp; 13:** Amazon S3 &amp; Advanced Storage (7 Tầng lưu trữ, Cây quyết định Mermaid, Vòng đời Lifecycle, SSE Encryption, Object Lock WORM, Nhân bản CRR/SRR &amp; Multipart Upload). | Hoàn thành |
| `topics/aws_cloudfront.html` | **Section 14:** CloudFront &amp; AWS Global Accelerator (Cây quyết định Mermaid, Ma trận CloudFront vs Global Accelerator, OAC, Signed URLs vs Cookies, CloudFront Functions vs Lambda@Edge). | Hoàn thành |
| `assets/css/style.css` | **Hệ thống Design System dùng chung:** Tokens màu, Dark/Light mode, typography, cards, grids, flows, matrix tables, mermaid containers. | Hoàn thành |
| `assets/js/app.js` | **Xử lý ứng dụng client-side:** Nhận diện và chuyển đổi song ngữ VI/EN, lưu `localStorage`, render tự động sơ đồ Mermaid theo theme/lang. | Hoàn thành |
| `assets/vendor/mermaid.min.js` | **Thư viện Mermaid.js nội bộ (100% offline):** Dùng để render Decision Trees, Sequence Diagrams, Logic Flowcharts mà không kéo CDN. | Hoàn thành |
| `scripts/export_anki_4000.py` | **Script CSV → Anki (tự chứa 100%):** Tự sinh SQLite và đóng gói `.apkg` + `.tsv`, không cần file `.apkg` mẫu. Cú pháp: `python3 scripts/export_anki_4000.py [input.csv] [output.apkg] [output.tsv]`. | Hoàn thành |
| `scripts/csv_to_sub_json.py` | **Script CSV → Subtitle JSON:** Chuyển đổi danh sách từ vựng CSV sang JSON chuẩn cấu trúc subtitle extension (`sub.json`), tự động bảo tồn `createdAt` và SRS state. Cú pháp: `python3 scripts/csv_to_sub_json.py [input.csv] [output.json]`. | Hoàn thành |
| `scripts/find_diff_vocab.py` | **Script so sánh từ vựng CSV:** So sánh đối chiếu 2 file CSV từ vựng, lọc ra các từ không chung hoặc từ mới. Cú pháp: `python3 scripts/find_diff_vocab.py [file1.csv] [file2.csv]`. | Hoàn thành |
| `scripts/clean.py` | **Script dọn dẹp Anki & Vocabulary:** Quét và xóa các tệp JSON (`sub.json`), CSV tạm/so sánh (`tu-vung-khong-chung.csv`, `tu-vung-moi.csv`, `lecturesub-tu-vung (*).csv`), bản build trong `dist/` và cache. Có bước xác nhận `y/N` hoặc cờ `-y`. Cú pháp: `python scripts/clean.py [-y]`. | Hoàn thành |
| `data/lecturesub-tu-vung.csv` | **Bộ từ vựng trích xuất từ phụ đề bài giảng:** UTF-8 with BOM, trường bọc ngoặc kép (`"Từ"`, `"Nghĩa"`, `"Nguồn"`, `"Đích"`, `"Câu gốc"`, `"Bài học"`, `"Giây"`, `"Liên kết"`). Đọc bằng CSV parser (có trường chứa dấu phẩy/xuống dòng). | Đang duy trì (86+ từ), gitignored |
| `dist/AWS_SAA_C03_Vocabulary.apkg` | **Gói Anki chuẩn Note Type 4000Book1:** Cloze, ô gõ kiểm tra (`type:cloze`), chia 20 từ/Unit, IPA và link Udemy. | Sinh bởi script |
| `dist/anki_4000_format.tsv` | **Flashcard dạng TSV 11 cột** của model `4000Book1` để import vào deck Anki bất kỳ. | Sinh bởi script |
| `.claude/skills/new-topic/` | Skill `/new-topic`: sinh trang cheat sheet mới trong `topics/` theo mẫu chuẩn. | Sẵn sàng |
| `.claude/skills/csv-to-apkg/` | Skill `/csv-to-apkg`: chạy script chuyển CSV từ vựng sang `.apkg` và kiểm tra kết quả. | Sẵn sàng |

---

## Lộ trình các chủ đề tiếp theo (Roadmap for Next Sessions)

Đã hoàn thành: **Section 3** (Global Infrastructure), **Section 4** (IAM), **Section 5** (EC2), **Section 6** (EC2 Storage), **Section 7** (ELB & ASG), **Section 8 & 20** (Databases), **Section 9** (Route 53), **Section 11 & 13** (S3), **Section 14** (CloudFront & Global Accelerator). Khi tiếp tục phiên làm việc mới, hãy đối chiếu danh sách các Section cần làm tiếp dưới đây:

1. **Section 6: EC2 Instance Storage (`topics/aws_storage.html`)**
   - *Nguồn:* Udemy Section 6 (EC2 - Instance Storage: EBS & EFS)
   - EBS volume types (gp3, gp2, io2 Block Express, st1, sc1), EBS Snapshots, Multi-Attach.
   - EFS (Elastic File System): Multi-AZ, POSIX, EFS One Zone, Storage classes (Standard, IA).
   - EC2 Instance Store: Ephemeral storage, IOPS siêu cao, mất dữ liệu khi stop/terminate.
2. **Section 7: High Availability & Scalability (`topics/aws_elb_asg.html`)**
   - *Nguồn:* Udemy Section 7 (High Availability and Scalability: ELB & ASG)
   - Elastic Load Balancing: ALB (Layer 7), NLB (Layer 4 - Ultra performance), GWLB (Layer 3 - Firewalls).
   - Target Groups, Health Checks, Cross-Zone Load Balancing, SNI (Server Name Indication).
   - Auto Scaling Groups (ASG): Dynamic scaling, Predictive scaling, Lifecycle hooks, Target tracking.
3. **Section 8 & 20: AWS Databases (`topics/aws_databases.html`)**
   - *Nguồn:* Udemy Section 8 (RDS + Aurora + ElastiCache) & Section 20 (Databases in AWS)
   - RDS: Multi-AZ (DR/Failover) vs Read Replicas (Scale Reads, async).
   - Amazon Aurora: 6 bản sao trên 3 AZs, Aurora Serverless v2, Global Database.
   - In-memory Caching: ElastiCache (Redis vs Memcached), MemoryDB.
   - NoSQL & Special: DynamoDB (DAX, Global Tables), Redshift, OpenSearch, DocumentDB, Neptune.
4. **Section 9: Amazon Route 53 (`topics/aws_route53.html`)**
   - *Nguồn:* Udemy Section 9 (Route 53)
   - Routing Policies: Simple, Weighted, Latency, Failover (Health checks), Geolocation, Geoproximity, Multi-Value Answer.
5. **Section 11 & 13: Amazon S3 & Advanced S3 (`topics/aws_s3.html`)**
   - *Nguồn:* Udemy Section 11 (S3 Intro) & Section 13 (Advanced S3)
   - S3 Storage Classes: Standard, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive, Intelligent-Tiering.
   - S3 Security: Bucket Policies, KMS encryption, Object Lock, Versioning, S3 Replication (CRR/SRR).
6. **Section 14: CloudFront & Global Accelerator (`topics/aws_cloudfront.html`)**
   - *Nguồn:* Udemy Section 14 (CloudFront & AWS Global Accelerator)
   - CloudFront: Caching, TTL, Origin Shield, Signed URL/Cookies, OAC (Origin Access Control) cho S3.
   - AWS Global Accelerator: Anycast IP, định tuyến qua mạng AWS Backbone (so sánh với CloudFront).
7. **Section 16: Decoupling Applications (`topics/aws_decoupling.html`)**
   - *Nguồn:* Udemy Section 16 (Decoupling Applications: SQS, SNS, Kinesis, Active MQ)
   - Amazon SQS: Standard (at-least-once) vs FIFO (exactly-once, order), DLQ (Dead Letter Queue), Visibility Timeout.
   - Amazon SNS: Pub/Sub Fan-out pattern, Topic Subscriptions.
   - Amazon Kinesis: Data Streams (shards, real-time), Firehose (near real-time S3/Redshift loader), Data Analytics.
8. **Section 17: Containers on AWS (`topics/aws_containers.html`)**
   - *Nguồn:* Udemy Section 17 (Containers on AWS: ECS, Fargate, ECR, EKS)
   - ECS (Elastic Container Service): EC2 Launch Type vs Fargate (Serverless container).
   - ECR (Elastic Container Registry), EKS (Elastic Kubernetes Service).
9. **Section 18 & 19: Serverless Architecture (`topics/aws_serverless.html`)**
   - *Nguồn:* Udemy Section 18 (Serverless Overviews) & Section 19 (Serverless Solutions)
   - AWS Lambda: Concurrency, Cold start, Destinations, Execution limits (15 phút, 10GB RAM).
   - Amazon API Gateway: REST API, HTTP API, WebSocket, Throttling, API Keys, Caching.
   - AWS Step Functions: State machines for workflow orchestration.
10. **Section 23: Monitoring, Audit & Governance (`topics/aws_monitoring.html`)**
    - *Nguồn:* Udemy Section 23 (AWS Monitoring & Audit)
    - CloudWatch: Metrics, Alarms, Logs, Synthetics, Container Insights.
    - CloudTrail: Ghi nhận mọi API calls, Trail bảo mật, phân tích sự cố.
    - EventBridge: Phản ứng sự kiện thời gian thực (Rule & Target, cron scheduler).
11. **Section 24: Security, Encryption & Compliance (`topics/aws_security.html`)**
    - *Nguồn:* Udemy Section 24 (AWS Security & Encryption)
    - AWS KMS: Customer Master Keys (CMK), Symmetric vs Asymmetric, Automatic Key Rotation.
    - Secrets Manager (tự động rotate password RDS) vs SSM Parameter Store.
    - AWS WAF, AWS Shield Standard/Advanced, AWS Network Firewall, AWS GuardDuty, AWS Inspector, AWS Macie.
12. **Section 25: Networking — Virtual Private Cloud (`topics/aws_vpc.html`)**
    - *Nguồn:* Udemy Section 25 (Networking - VPC)
    - CIDR, Public Subnets, Private Subnets, Internet Gateway (IGW), Route Tables.
    - NAT Gateway (quản lý bởi AWS, Multi-AZ) vs NAT Instance.
    - Network ACL (NACL - Stateless, Subnet-level, có Deny rules) vs Security Group (SG - Stateful, Instance-level).
    - VPC Peering, VPC Endpoints (Gateway vs Interface Endpoints / PrivateLink), Transit Gateway.
13. **Section 26: Disaster Recovery & Data Migration (`topics/aws_disaster_recovery.html`)**
    - *Nguồn:* Udemy Section 26 (Disaster Recovery & Migrations)
    - 4 chiến lược DR: Backup & Restore, Pilot Light, Warm Standby, Multi-Region Active-Active.
    - AWS DRS (Elastic Disaster Recovery), AWS DMS (Database Migration Service), AWS Snow Family, DataSync.

---

## Quy ước thiết kế & Thành phần HTML (Design System)

Khi tạo mới hoặc cập nhật một trang `topics/aws_<topic>.html`:

### 1. Token CSS & Chế độ màu (Dark/Light mode)
- Nhúng toàn bộ tài nguyên dùng chung trong thẻ `<head>`:
  ```html
  <link rel="stylesheet" href="../assets/css/style.css">
  <script src="../assets/vendor/mermaid.min.js"></script>
  <script src="../assets/js/app.js"></script>
  ```
- Tuyệt đối không sao chép lại khối `<style>` hay mã JavaScript trùng lặp vào các trang cheat sheet con.
- Sử dụng triệt để các biến CSS `:root`:
  - Nền & Thẻ: `--bg`, `--card`, `--bd`, `--sub`, `--tx`, `--mu`, `--gy`.
  - Cặp màu trạng thái (Chữ / Nền): Xanh lam (`--bl` / `--blb`), Xanh lá (`--gr` / `--grb`), Cam (`--or` / `--orb`), Đỏ (`--rd` / `--rdb`).
  - Tuyệt đối không dùng mã hex màu trực tiếp ngoài token (ngoại trừ thẻ code `.json`).

### 2. Cấu trúc khung trang chuẩn
1. **Thanh điều hướng trên cùng (`.top-nav`) & Nút chuyển ngôn ngữ**:
   ```html
   <div class="top-nav">
     <a href="../index.html" class="nav-back">
       <span class="lang-vi">← Mục lục khóa học</span>
       <span class="lang-en">← Course Hub</span>
     </a>
     <div style="display:flex;align-items:center;gap:12px">
       <span style="font-size:12px;color:var(--mu)">Section X · Udemy SAA-C03</span>
       <div class="lang-switch" role="group" aria-label="Language selector">
         <button type="button" class="lang-btn active" data-lang-val="vi" onclick="setLanguage('vi')">🇻🇳 VI</button>
         <button type="button" class="lang-btn" data-lang-val="en" onclick="setLanguage('en')">🇬🇧 EN</button>
       </div>
     </div>
   </div>
   ```
2. **Tiêu đề (`.header`)**:
   - `.badge`: Phạm vi dịch vụ (`Global Service` / `Regional Service` / `AZ-Scoped`).
   - `h1`: Tên chính thức của dịch vụ AWS.
   - `p`: Một câu tóm tắt giá trị kiến trúc (có cặp `<p class="lang-vi">` và `<p class="lang-en">`).
3. **Quy tắc song ngữ (Bilingual)**:
   - Các đoạn văn bản/tiêu đề dùng cặp `<span class="lang-vi">` / `<span class="lang-en">` hoặc `<div class="lang-vi">` / `<div class="lang-en">`.
   - CSS tự động ẩn/hiện theo thuộc tính `data-lang` trên thẻ `<html>`:
     `[data-lang="en"] .lang-vi{display:none !important}`
     `:root:not([data-lang="en"]) .lang-en{display:none !important}`
   - Trạng thái ngôn ngữ được lưu tự động trong `localStorage` key `'aws_study_lang'`.
3. **Lưới thẻ (`.grid`)**: Chứa các thẻ `.card` (dùng thêm class `.full` cho thẻ trải rộng cả 2 cột).
4. **Các component tái sử dụng**:
   - `.mermaid-diagram`: Khối sơ đồ tư duy Mermaid tự động render song ngữ theo theme.
   - `.matrix-wrap` + `.matrix-table`: Bảng ma trận so sánh đa chiều các lựa chọn kỹ thuật.
   - `.g2` + `.it`: Lưới 2 cột cho định nghĩa thực thể/khái niệm.
   - `.flow` + `.st` + `.ar`: Sơ đồ luồng xử lý hoặc thứ tự đánh giá.
   - `.cols` + `.col` + `.pi`: So sánh giữa 2 hoặc 3 phương án kiến trúc.
   - `.tag`: Nhãn từ khóa ngắn gọn (`tb`, `tg`, `to`, `tr`, `ty`).
   - `.sl`: Danh sách tính năng kèm icon nền màu.
   - `.tools`: Lưới các dịch vụ/công cụ vệ tinh liên quan.
   - `.json`: Khối code JSON cấu hình/policy có tô màu `.jk`, `.jv`, `.jc`, `.jp`.
   - Card **"Bổ sung hay gặp trong đề thi SAA-C03"**: Điểm danh các bẫy đề thi, số liệu quan trọng, sự cố thực tế.
   - Card **"Nguyên tắc vàng — SAA-C03"**: Dạng `.bp` / `.bi`, mục cảnh báo cốt lõi dùng số `.bn` màu đỏ `--rd`.
   - Card **"Nguồn bài giảng & Tài liệu tìm hiểu thêm (Further Study Resources)"** (BẮT BUỘC): Bố trí 3 cột dạng `.cols` / `.col` / `.pi`:
     - Cột 1: Video bài giảng Udemy cốt lõi kèm link chính xác từ `data/lecturesub-tu-vung.csv` (`https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/<id>`).
     - Cột 2: Tài liệu chính thức từ AWS Documentation / Architecture Whitepaper liên quan.
     - Cột 3: Khảo sát sản phẩm & Cheat Sheet bổ trợ (Interactive Maps, Tutorials Dojo Cheat Sheet).

### 3. Quy trình thực hiện khi tạo bài mới (Workflow)
1. Tạo file `topics/aws_<topic>.html` (trong thư mục `topics/`).
2. Nhúng `../assets/css/style.css`, `../assets/vendor/mermaid.min.js`, `../assets/js/app.js` trong `<head>`.
3. Tra cứu `data/lecturesub-tu-vung.csv` để lấy danh sách từ vựng, câu ngữ cảnh và link video bài giảng tương ứng đưa vào nội dung và khối Nguồn tham chiếu.
4. Bổ sung card "Nguồn bài giảng & Tài liệu tìm hiểu thêm (Further Study Resources)" với đầy đủ liên kết video bài giảng, AWS Documentation, Whitepapers và Cheat Sheet.
5. Đảm bảo toàn bộ HTML đóng thẻ hợp lệ và cân bằng song ngữ (kiểm tra bằng script python validator).
6. **Cập nhật `index.html`**:
   - Thêm/sửa link tới `topics/aws_<topic>.html` (đường dẫn có tiền tố `topics/`).
   - Thêm dòng chú thích nguồn bài giảng `📚 Nguồn: Udemy Section X · Lectures...`.
   - Sửa trạng thái mục bài học từ `btn-pending` / `Kế tiếp` sang `btn-open` / `Đã có`.
   - Tăng biến đếm "Chủ đề hoàn thành" trong khối `.stats`.
7. **Cập nhật `README.md`**: đánh dấu `[x]` Section trong mục Lộ trình, thêm dòng vào bảng file và cây thư mục; cập nhật bảng File Inventory + dòng "Đã hoàn thành" trong `CLAUDE.md`.
8. Báo cáo lại cho người dùng và mở kiểm tra bằng lệnh `open topics/aws_<topic>.html`.
