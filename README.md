# AWS Certified Solutions Architect Associate (SAA-C03) — Study Hub

Dự án cá nhân tổng hợp kiến thức ôn thi chứng chỉ **AWS Certified Solutions Architect - Associate (SAA-C03)** theo giáo trình khóa học Udemy *"Ultimate AWS Certified Solutions Architect Associate"* của **Stephane Maarek**.

Dự án gồm 3 phần:

1. **Dashboard trung tâm** (`index.html`): quản lý lộ trình 16 Section, tiến độ học, 4 Domain đề thi SAA-C03, tích hợp bộ chuyển đổi song ngữ (Tiếng Việt & English).
2. **Cheat sheet trực quan** cho từng dịch vụ AWS (`topics/`): thuần HTML/CSS, tự chứa, hỗ trợ Dark/Light mode, song ngữ VI/EN, responsive, chạy offline.
3. **Bộ từ vựng tiếng Anh chuyên ngành** trích từ phụ đề bài giảng (`data/`) và **script đóng gói thành deck Anki** (`scripts/` → `dist/`).

---

## 📂 Cấu trúc thư mục

```
learn_aws/
├── index.html                      # Dashboard trung tâm — mở file này trước
├── topics/                         # Cheat sheet từng Section (link về ../index.html)
│   ├── aws_global_infra.html       #   Section 3 — Global Infrastructure
│   ├── aws_iam.html                #   Section 4 — IAM (file mẫu chuẩn về thiết kế)
│   └── aws_ec2.html                #   Section 5 — EC2
├── assets/                         # Tài nguyên dùng chung tự chứa (chạy offline)
│   ├── css/style.css               #   CSS Design System, tokens màu, dark/light mode, components
│   ├── js/app.js                   #   Logic song ngữ VI/EN, lưu preference, auto-render Mermaid
│   └── vendor/mermaid.min.js       #   Thư viện Mermaid.js nội bộ (không kéo CDN)
├── scripts/
│   └── export_anki_4000.py         # CSV → .apkg + .tsv (Python 3 thuần, không cần thư viện ngoài)
├── data/                           # Dữ liệu đầu vào (gitignored, tự đặt vào)
│   └── lecturesub-tu-vung.csv      #   Từ vựng trích từ phụ đề bài giảng
├── dist/                           # Output sinh tự động (gitignored)
│   ├── AWS_SAA_C03_Vocabulary.apkg #   Gói Anki hoàn chỉnh (Note Type 4000Book1)
│   └── anki_4000_format.tsv        #   File TSV 11 cột để import thủ công
├── .claude/skills/                 # Skill cho Claude Code: /new-topic, /csv-to-apkg
├── CLAUDE.md                       # Quy ước thiết kế, quy trình & roadmap cho AI Agent
└── README.md
```

| Đường dẫn | Mô tả |
| :--- | :--- |
| [`index.html`](index.html) | Dashboard: thống kê tiến độ, 4 Domain đề thi SAA-C03, mục lục 16 Section, trích đoạn từ vựng, hướng dẫn Anki. |
| [`topics/aws_global_infra.html`](topics/aws_global_infra.html) | Regions, AZs, Data Centers, Edge PoP, Sơ đồ Mermaid định tuyến, Ma trận chi phí Data Transfer, AZ ID vs AZ Name, Local Zones, Wavelength, Outposts, Direct Connect, Whitepapers. |
| [`topics/aws_iam.html`](topics/aws_iam.html) | Users, Groups, Roles, Policies JSON, Sơ đồ Mermaid đánh giá logic, Ma trận Cross-Account AssumeRole vs Resource Policy, Top Condition Keys, Bộ 3 công cụ Audit, SCPs, Golden Rules. |
| [`topics/aws_ec2.html`](topics/aws_ec2.html) | Instance Types, Sơ đồ Mermaid vòng đời Lifecycle &amp; Hibernate, Ma trận 7 mô hình Purchasing Options &amp; Spot Fleet, Ma trận SG vs NACL, ENA/EFA, Nitro System, SSM Session Manager. |
| [`topics/aws_storage.html`](topics/aws_storage.html) | Tam giác lưu trữ EC2, Cây quyết định Mermaid, Ma trận phân loại đĩa EBS gp3/io2, Snapshots &amp; KMS, Multi-Attach, EFS Multi-AZ POSIX &amp; Tiers, Ephemeral Instance Store. |
| [`topics/aws_elb_asg.html`](topics/aws_elb_asg.html) | Kiến trúc sẵn sàng cao Multi-AZ, Sơ đồ Mermaid luồng ELB, Ma trận 4 dòng Load Balancer ALB/NLB/GWLB, Target Groups, SNI, ASG Scaling Policies. |
| [`topics/aws_databases.html`](topics/aws_databases.html) | Hệ cơ sở dữ liệu AWS, Cây quyết định Mermaid, RDS Multi-AZ vs Read Replicas, Aurora Serverless &amp; Global DB, DynamoDB NoSQL &amp; DAX, ElastiCache. |
| [`topics/aws_route53.html`](topics/aws_route53.html) | Dịch vụ DNS Route 53, CNAME vs Alias Record, Cây quyết định Mermaid, 8 Chính sách định tuyến, Health Checks &amp; Khôi phục sự cố thảm họa. |
| [`topics/aws_s3.html`](topics/aws_s3.html) | Amazon S3 lưu trữ đối tượng, Cây quyết định 7 Storage Classes, Lifecycle Rules, SSE Encryption, Object Lock (WORM), Nhân bản CRR/SRR. |
| [`topics/aws_cloudfront.html`](topics/aws_cloudfront.html) | Mạng biên toàn cầu, Cây quyết định Mermaid, Ma trận CloudFront vs Global Accelerator, OAC, Signed URLs/Cookies, CloudFront Functions vs Lambda@Edge. |
| [`topics/lab_ec2.html`](topics/lab_ec2.html) | **Hands-on Lab 1:** EC2 User Data (`ec2-user-data.sh`) &amp; Instance Metadata CLI (`ec2-metadata.sh`, IMDSv1/v2). |
| [`topics/lab_storage.html`](topics/lab_storage.html) | **Hands-on Lab 2:** EBS Volume Benchmark (`commands.txt`, `fio`/`ioping`) &amp; EFS Multi-AZ Shared Mount (`efs.sh`). |
| [`topics/lab_route53.html`](topics/lab_route53.html) | **Hands-on Lab 3:** Route 53 Multi-AZ/Region Routing Demo với IMDSv1/IMDSv2 User Data (`route53/user-data.sh`). |
| [`topics/lab_s3.html`](topics/lab_s3.html) | **Hands-on Lab 4:** S3 Static Website, CORS (`CORS_CONFIG.json`), Pre-signed URL, MFA Delete &amp; Athena Access Logs SQL. |
| [`topics/lab_decoupling.html`](topics/lab_decoupling.html) | **Hands-on Lab 5:** Amazon SQS CLI (`sqs.sh`) &amp; Kinesis Data Streams Producer/Consumer (`kinesis-data-streams.sh`). |
| [`topics/lab_serverless.html`](topics/lab_serverless.html) | **Hands-on Lab 6:** AWS Lambda &amp; Amazon API Gateway Proxy Integration (`api-gateway/lambda-code.py`). |
| [`topics/lab_security_ssm_kms.html`](topics/lab_security_ssm_kms.html) | **Hands-on Lab 7:** AWS KMS CLI Encryption (`kms-demo-cli.sh`) &amp; SSM Parameter Store với Lambda (`ssm/cli.sh`, `handler.py`). |
| [`topics/lab_cloudformation.html`](topics/lab_cloudformation.html) | **Hands-on Lab 8:** AWS CloudFormation Infrastructure as Code (`0-just-ec2.yaml`, `1-ec2-with-sg-eip.yaml`). |
| [`assets/css/style.css`](assets/css/style.css) | Toàn bộ CSS Design System dùng chung, tokens màu, Dark/Light mode, typography, components, matrix tables. |
| [`assets/js/app.js`](assets/js/app.js) | Script xử lý chuyển đổi song ngữ VI/EN tức thì, lưu `localStorage`, render tự động Mermaid. |
| [`assets/vendor/mermaid.min.js`](assets/vendor/mermaid.min.js) | Thư viện Mermaid.js nội bộ 100% offline vẽ sơ đồ tư duy, decision tree, sequence diagrams, state diagrams. |
| [`scripts/export_anki_4000.py`](scripts/export_anki_4000.py) | Sinh SQLite Anki và đóng gói `.apkg` tự chứa 100% (không cần file `.apkg` mẫu). |
| [`scripts/csv_to_sub_json.py`](scripts/csv_to_sub_json.py) | Chuyển đổi CSV từ vựng sang JSON (`sub.json`) chuẩn cấu trúc extension phụ đề video. |
| [`scripts/find_diff_vocab.py`](scripts/find_diff_vocab.py) | So sánh đối chiếu 2 file CSV từ vựng, lọc ra các từ không chung hoặc từ mới. |
| [`scripts/clean.py`](scripts/clean.py) | Dọn dẹp các tệp sinh ra trong `dist/`, bộ nhớ đệm `__pycache__` và file tạm. |
| `data/lecturesub-tu-vung.csv` | UTF-8 with BOM, các cột: `Từ`, `Nghĩa`, `Nguồn`, `Đích`, `Câu gốc`, `Bài học`, `Giây`, `Liên kết`. |
| `dist/*` | Kết quả build — không commit, sinh lại bất cứ lúc nào bằng script. |

> **Lưu ý:** `data/*.csv` và `dist/` nằm trong `.gitignore`, nên khi clone repo về bạn cần tự chép file CSV vào `data/` rồi chạy script để tạo deck Anki.

---

## 🚀 Bắt đầu nhanh & Tổng hợp lệnh chạy (Command Reference)

Dự án thuần HTML/CSS/JS và Python 3, không cần cài đặt web server hay thư viện ngoài.

### 1. Mở trang học tập trên trình duyệt

```bash
# Windows (PowerShell / Command Prompt)
start index.html                      # Mở Dashboard trung tâm
start topics/aws_global_infra.html    # Mở Section 3: Global Infrastructure
start topics/aws_iam.html             # Mở Section 4: IAM
start topics/aws_ec2.html             # Mở Section 5: EC2

# macOS
open index.html

# Linux
xdg-open index.html
```

---

### 2. Bộ công cụ xử lý từ vựng & Flashcard (Scripts)

#### 🗂️ A. Đóng gói Flashcard Anki (chuẩn 4000 Essential English Words)
```bash
# Mặc định: data/lecturesub-tu-vung.csv → dist/AWS_SAA_C03_Vocabulary.apkg + dist/anki_4000_format.tsv
python scripts/export_anki_4000.py

# Hoặc chỉ định đường dẫn file tùy ý:
python scripts/export_anki_4000.py <input.csv> <output.apkg> <output.tsv>
```
- Tự động chia **20 từ / Unit** (Unit 01, Unit 02,...).
- **Cách nạp vào Anki:** Nhấp đúp file `dist/AWS_SAA_C03_Vocabulary.apkg` (yêu cầu cài [Anki Desktop](https://apps.ankiweb.net/)), hoặc chọn **File → Import...** file `dist/anki_4000_format.tsv`.

#### 🔄 B. Chuyển đổi CSV sang Subtitle JSON (`sub.json`)
```bash
# Mặc định: lecturesub-tu-vung.csv → sub.json
python scripts/csv_to_sub_json.py

# Hoặc chỉ định file nguồn và file đích:
python scripts/csv_to_sub_json.py <input.csv> <output.json>
```
- Chuẩn hóa trường `id` dạng `["en","vi","word"]`, bảo toàn mốc `createdAt` và tiến độ SRS.

#### 🔍 C. So sánh đối chiếu & lọc từ vựng giữa 2 file CSV
```bash
# So sánh file gốc và file tải về mới:
python scripts/find_diff_vocab.py lecturesub-tu-vung.csv "lecturesub-tu-vung (1).csv"
```
- Tự động sinh `tu-vung-khong-chung.csv` (các từ không trùng lặp) và `tu-vung-moi.csv` (các từ mới thêm).

---

### 3. Lệnh dọn dẹp dự án (Cleanup)

Lệnh dọn dẹp chuyên dụng để quét và xóa an toàn các tệp JSON, CSV tạm và bản build sinh ra liên quan tới script từ vựng Anki:
- **Tệp JSON phụ đề:** `sub.json`
- **Các tệp CSV so sánh / tạm:** `tu-vung-khong-chung.csv`, `tu-vung-moi.csv`, `lecturesub-tu-vung (*).csv`, `diff_*.csv` *(bảo toàn tệp gốc `data/lecturesub-tu-vung.csv`)*
- **Bản build Anki:** Toàn bộ file trong thư mục `dist/` (`.apkg`, `.tsv`)
- **Bộ nhớ đệm:** `__pycache__`

```bash
# Chạy ở chế độ an toàn (quét, liệt kê danh sách tệp và yêu cầu nhập y/N xác nhận):
python scripts/clean.py

# Tự động xác nhận xóa mà không cần hỏi (thích hợp cho script tự động):
python scripts/clean.py -y
```

> [!NOTE]
> Tuân thủ chính sách bảo vệ tệp tin: Script luôn liệt kê danh sách tệp rõ ràng trước khi yêu cầu xác nhận xóa.

---

## 🗺️ Lộ trình & Nguồn bài giảng Udemy

- [x] **Section 3:** AWS Global Infrastructure ([`topics/aws_global_infra.html`](topics/aws_global_infra.html))
  - *Lectures:* `26097978` (Overview), `26097980` (Regions & AZs)
- [x] **Section 4:** AWS IAM & AWS CLI ([`topics/aws_iam.html`](topics/aws_iam.html) · [`lectures/section-04-iam-and-aws-cli`](lectures/section-04-iam-and-aws-cli/README.md))
  - *Lectures 11–30:* `26097996` (IAM Intro), `51960287` (Simultaneous Sign-in), `26623458` (Policies), `26098020` (MFA), `26098034` (CLI & SDK), `26098060` (CloudShell), `26098066` (IAM Roles), `26098070` (Security Tools)
- [x] **Section 5 & 6:** AWS EC2 — Fundamentals & SAA Level ([`topics/aws_ec2.html`](topics/aws_ec2.html) · [`lectures/section-05-ec2-fundamentals`](lectures/section-05-ec2-fundamentals/README.md) · [`lectures/section-06-ec2-saa-level`](lectures/section-06-ec2-saa-level/README.md))
  - *Lectures 31–55:* `26098112` (EC2 Basics), `26098122` (User Data), `26098128` (Instance Types), `26098134` (Security Groups), `26098164` (Instance Connect), `26098170` (Purchasing Options), `18756818` (Spot Fleet), `13528052` (Elastic IP), `13528080` (Placement Groups), `18077955` (ENI), `18104377` (EC2 Hibernate)
- [x] **Section 7:** EC2 Instance Storage — EBS, EFS, AMI & Instance Store ([`topics/aws_storage.html`](topics/aws_storage.html) · [`lectures/section-07-ec2-instance-storage`](lectures/section-07-ec2-instance-storage/README.md))
  - *Lectures 56–69:* `26098272` (EBS Overview), `26098276` (EBS Snapshots), `26098280` (AMI Overview), `26098288` (Instance Store), `26098296` (EBS Volume Types), `26098298` (EBS Multi-Attach), `13528122` (EBS Encryption), `13528128` (Amazon EFS), `13528138` (EFS vs EBS)
- [x] **Section 8:** High Availability & Scalability — ELB & ASG ([`topics/aws_elb_asg.html`](topics/aws_elb_asg.html) · [`lectures/section-08-elb-and-asg`](lectures/section-08-elb-and-asg/README.md))
  - *Lectures 70–86:* `13531374` (HA & Scalability), `13528090` (ELB Overview), `18078003` (ALB), `18078013` (NLB), `28874688` (GWLB), `13528094` (Sticky Sessions), `18078093` (Cross-Zone), `18078099` (SSL & SNI), `18611524` (Connection Draining), `13528102` (ASG), `26148326` (Scaling Policies)
- [x] **Section 9 & 20:** AWS Databases — RDS, Aurora, RDS Proxy, ElastiCache & DynamoDB ([`topics/aws_databases.html`](topics/aws_databases.html) · [`lectures/section-09-rds-aurora-elasticache`](lectures/section-09-rds-aurora-elasticache/README.md))
  - *Lectures 87–100:* RDS Overview, Multi-AZ vs Read Replicas, RDS Custom, Amazon Aurora, Aurora Cloning/Custom Endpoints, RDS Proxy, ElastiCache (Redis vs Memcached), Important Ports
- [x] **Section 10:** Amazon Route 53 ([`topics/aws_route53.html`](topics/aws_route53.html) · [`lectures/section-10-route-53`](lectures/section-10-route-53/README.md))
  - *Lectures 101–120:* `28384280` (DNS), `13528180` (Route 53 Overview), `13528188` (TTL), `13528190` (CNAME vs Alias), `13528200` (Health Checks), `13528204` (Failover), `26099214` (Geoproximity), `37045728` (IP-based), `13528212` (3rd Party Domains), `51771513` (Route 53 Resolver & Hybrid DNS)
- [x] **Section 11 & 13:** Amazon S3 & Advanced S3 ([`topics/aws_s3.html`](topics/aws_s3.html))
  - *Lectures:* `26098336` (S3 Overview), `26098348` (Bucket Policies), `26098360` (Storage Classes), `26098372` (Lifecycle), `26098384` (Performance)
- [x] **Section 14:** CloudFront & Global Accelerator ([`topics/aws_cloudfront.html`](topics/aws_cloudfront.html))
  - *Lectures:* `26098394` (Overview), `26098404` (S3 & OAC), `26098414` (Signed URLs & Edge), `26098424` (Global Accelerator)
- [ ] **Section 16:** Decoupling Applications — SQS, SNS, Kinesis, MQ (`topics/aws_decoupling.html`)
- [ ] **Section 17:** Containers on AWS — ECS, Fargate, ECR, EKS (`topics/aws_containers.html`)
- [ ] **Section 18 & 19:** Serverless — Lambda, API Gateway, Step Functions (`topics/aws_serverless.html`)
- [ ] **Section 23:** Monitoring & Audit — CloudWatch, CloudTrail, EventBridge (`topics/aws_monitoring.html`)
- [ ] **Section 24:** Security & Encryption — KMS, Secrets Manager, WAF, Shield (`topics/aws_security.html`)
- [ ] **Section 25:** Networking — VPC, Subnets, NAT, SG/NACL, Transit Gateway (`topics/aws_vpc.html`)
- [ ] **Section 26:** Disaster Recovery & Migrations — DRS, DMS (`topics/aws_disaster_recovery.html`)

Chi tiết nội dung cần có của từng Section xem trong [`CLAUDE.md`](CLAUDE.md#lộ-trình-các-chủ-đề-tiếp-theo-roadmap-for-next-sessions).

---

## ✍️ Thêm chủ đề mới

1. Tạo `topics/aws_<topic>.html` (hoặc chạy skill `/new-topic <chủ đề>` trong Claude Code).
2. Nhúng tài nguyên dùng chung tự chứa trong `<head>`:
   ```html
   <link rel="stylesheet" href="../assets/css/style.css">
   <script src="../assets/vendor/mermaid.min.js"></script>
   <script src="../assets/js/app.js"></script>
   ```
3. Link quay về Dashboard dùng đường dẫn tương đối `../index.html`.
4. Bổ sung đầy đủ các khối cốt lõi: Khái niệm &rarr; Sơ đồ kiến trúc Mermaid &rarr; Bảng ma trận so sánh &rarr; Bổ sung hay gặp trong đề thi SAA-C03 &rarr; Nguyên tắc vàng &rarr; **Nguồn bài giảng &amp; Tài liệu tìm hiểu thêm (Further Study Resources)** ở cuối trang.
5. Cập nhật `index.html`: link `topics/aws_<topic>.html`, đổi trạng thái sang **Đã có**, tăng bộ đếm "Chủ đề hoàn thành".
6. Đánh dấu `[x]` trong mục Lộ trình ở README này và cập nhật `CLAUDE.md`.

Quy ước thiết kế chi tiết: xem [`CLAUDE.md`](CLAUDE.md).

---

## 🎨 Chuẩn thiết kế Cheat Sheet

- **100% Tự chứa &amp; Chạy Offline:** Không kéo thư viện ngoài (CDN, Google Fonts, external JS/CSS); toàn bộ thư viện Mermaid và Design System đều nằm cục bộ trong `assets/`.
- **Hỗ trợ Song ngữ toàn diện (Bilingual VI / EN):** Toàn bộ tiêu đề, nội dung và sơ đồ đều hỗ trợ chuyển đổi tức thì giữa Tiếng Việt và Tiếng Anh qua nút chuyển ngôn ngữ (`localStorage`).
- **Thích ứng Sáng / Tối (Dark / Light mode):** Tự động thích ứng theo hệ thống qua CSS Custom Properties (`:root`), không hard-code mã màu trực tiếp.
- **Sơ đồ tư duy &amp; Ma trận chuyên sâu:** Sử dụng Mermaid.js để vẽ flowchart, sequence diagram, state machine và bảng ma trận đa chiều giúp ghi nhớ sâu kiến trúc.
- **Responsive:** Hiển thị tối ưu trên máy tính bảng và điện thoại (không cuộn ngang ở màn hình hẹp).
- **Liên kết tài liệu chuẩn xác:** Luôn đính kèm nguồn bài giảng Udemy (kèm lecture ID) và tài liệu chính thức AWS Whitepapers/Docs tương ứng.
