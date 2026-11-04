# AWS Certified Solutions Architect Associate (SAA-C03) — Study Hub

Dự án cá nhân tổng hợp kiến thức ôn thi chứng chỉ **AWS Certified Solutions Architect Associate (SAA-C03)** theo giáo trình khóa học của **Stephane Maarek** trên Udemy.

Bao gồm:
1. **Sơ đồ kiến trúc & Cheat Sheet trực quan** cho từng dịch vụ AWS (thuần HTML/CSS, tự chứa, hỗ trợ Dark/Light mode, không phụ thuộc thư viện ngoài).
2. **Từ vựng tiếng Anh chuyên ngành** trích xuất trực tiếp từ phụ đề video bài giảng (`lecturesub-tu-vung.csv`).
3. **Trang Dashboard trung tâm** (`index.html`) quản lý lộ trình và tiến độ học tập.

---

## 🚀 Truy cập nhanh (Quick Start)

Mở trực tiếp trên trình duyệt máy tính:
```bash
# Mở Dashboard mục lục trung tâm
open index.html

# Mở các chủ đề đã hoàn thành
open aws_global_infra.html    # Section 3: Hạ tầng toàn cầu AWS
open aws_iam.html             # Section 4: Quản lý danh tính & phân quyền (IAM)
open aws_ec2.html             # Section 5: Máy chủ ảo IaaS (EC2)
```

---

## 📂 Danh mục tệp tin (File Inventory)

- [`index.html`](index.html): Trang chủ Dashboard, thống kê 4 Domain đề thi SAA-C03, bảng theo dõi tiến độ toàn khóa.
- [`aws_global_infra.html`](aws_global_infra.html): Sơ đồ Regions, AZs, Data Centers, Edge Locations, Local Zones, Wavelength, Outposts.
- [`aws_iam.html`](aws_iam.html): Cheat sheet IAM (Users, Groups, Roles, Policies JSON, Evaluation Logic, MFA, SCPs).
- [`aws_ec2.html`](aws_ec2.html): Cheat sheet EC2 (Instance Types, Spot/RI/Savings Plans, Security Groups, IMDSv2, SSM, Placement Groups).
- [`lecturesub-tu-vung.csv`](lecturesub-tu-vung.csv): Danh sách 86+ từ vựng tiếng Anh kèm nghĩa tiếng Việt, câu gốc phụ đề và URL video Udemy.
- [`AWS_SAA_C03_Vocabulary.apkg`](AWS_SAA_C03_Vocabulary.apkg): **Gói Deck Anki hoàn chỉnh** (Chuẩn format `4000Book1`: gợi ý điền từ, gõ phím kiểm tra chính tả `type:cloze`, IPA, nút bấm mở video Udemy đúng mốc thời gian).
- [`anki_4000_format.tsv`](anki_4000_format.tsv): File xuất 11 cột chuẩn Note Type `4000Book1` để import vào bất kỳ deck Anki nào.
- [`export_anki_4000.py`](export_anki_4000.py): Script Python tự chứa 100% tự động trích xuất từ CSV sang gói Anki `.apkg` và `.tsv` (không phụ thuộc file ngoài).
- [`.claude/skills/csv-to-apkg/`](.claude/skills/csv-to-apkg/SKILL.md): Skill `/csv-to-apkg` tự động hóa chuyển đổi CSV sang APKG.
- [`CLAUDE.md`](CLAUDE.md): Tài liệu hướng dẫn quy tắc lập trình, thiết kế UI và lộ trình chi tiết cho AI Agent / Pair Programmer.

---

## 🗂️ Hướng dẫn học Flashcard trên Anki (Chuẩn 4000 Essential English Words)

Dự án đã đóng gói sẵn toàn bộ từ vựng sang file [`AWS_SAA_C03_Vocabulary.apkg`](AWS_SAA_C03_Vocabulary.apkg) theo đúng cấu trúc của bộ **4000 Essential English Words 1**:

### 🎯 Cách 1: Mở trực tiếp (1 Click - Khuyên dùng)
1. Cài đặt phần mềm [Anki Desktop](https://apps.ankiweb.net/) (nếu chưa có).
2. Nhấp đúp trực tiếp vào file **[`AWS_SAA_C03_Vocabulary.apkg`](AWS_SAA_C03_Vocabulary.apkg)**.
3. Anki sẽ tự động nhập toàn bộ 86 thẻ vào cây thư mục phân cấp **20 từ / Unit**:
   - **Deck cha:** `AWS SAA-C03 Vocabulary (Stephane Maarek)`
   - **Các Subdeck con:**
     - `Unit 01`: 20 từ (từ 1 đến 20)
     - `Unit 02`: 20 từ (từ 21 đến 40)
     - `Unit 03`: 20 từ (từ 41 đến 60)
     - `Unit 04`: 20 từ (từ 61 đến 80)
     - `Unit 05`: 6 từ (từ 81 đến 86)
   - **Mặt trước:** Gợi ý điền chữ cái đầu/cuối `t__ __ __ __ __ __ __ __ __n`, câu ngữ cảnh đục lỗ `to note in here is the delete on [...]`, nghĩa tiếng Việt, và **hộp gõ phím (Type-in)** để bạn tự gõ từ kiểm tra trí nhớ.
   - **Mặt sau:** Tự động so sánh từ bạn gõ (xanh nếu gõ đúng, đỏ nếu gõ sai), phiên âm quốc tế IPA, câu ngữ cảnh đầy đủ, và **nút bấm xem lại video bài giảng Udemy đúng mốc thời gian**.

### 🛠️ Cách 2: Tự động cập nhật khi thêm từ vựng mới
Khi bạn cập nhật thêm từ vựng vào `lecturesub-tu-vung.csv`, chạy lệnh sau để làm mới file `.apkg`:
```bash
python3 export_anki_4000.py
```

---

## 🗺️ Lộ trình & Nguồn bài giảng Udemy (Course Lectures Roadmap)

- [x] **Section 3:** AWS Global Infrastructure ([`aws_global_infra.html`](aws_global_infra.html))
  - *Nguồn bài học:* Lectures `26097978` (Overview), `26097980` (Regions & AZs)
- [x] **Section 4:** AWS IAM ([`aws_iam.html`](aws_iam.html))
  - *Nguồn bài học:* Lectures `26097996` (Overview), `26098020` (Root User), `26098028` (Users & Credentials), `26098070` (Tools), `26623458` (Policies in Depth)
- [x] **Section 5:** AWS EC2 ([`aws_ec2.html`](aws_ec2.html))
  - *Nguồn bài học:* Lectures `26098112` (User Data), `26098122` (Lifecycle & Termination), `26098128` (Instance Types), `26098134` (Security Groups)
- [ ] **Section 6:** EC2 Storage — EBS, EFS & Instance Store (`aws_storage.html`)
  - *Nguồn bài học:* Section 6: EC2 - Instance Storage (EBS & EFS)
- [ ] **Section 7:** High Availability & Scalability — ELB & ASG (`aws_elb_asg.html`)
  - *Nguồn bài học:* Section 7: High Availability and Scalability: ELB & ASG
- [ ] **Section 8 & 20:** AWS Databases — RDS, Aurora, ElastiCache, DynamoDB (`aws_databases.html`)
  - *Nguồn bài học:* Section 8 (RDS, Aurora, ElastiCache) & Section 20 (Databases in AWS)
- [ ] **Section 9:** Amazon Route 53 (`aws_route53.html`)
  - *Nguồn bài học:* Section 9: Route 53
- [ ] **Section 11 & 13:** Amazon S3 & Advanced S3 (`aws_s3.html`)
  - *Nguồn bài học:* Section 11 (S3 Intro) & Section 13 (Advanced S3)
- [ ] **Section 14:** CloudFront & Global Accelerator (`aws_cloudfront.html`)
  - *Nguồn bài học:* Section 14: CloudFront & AWS Global Accelerator
- [ ] **Section 16:** Decoupling Applications — SQS, SNS, Kinesis, MQ (`aws_decoupling.html`)
  - *Nguồn bài học:* Section 16: Decoupling Applications: SQS, SNS, Kinesis, Active MQ
- [ ] **Section 17:** Containers on AWS — ECS, Fargate, ECR, EKS (`aws_containers.html`)
  - *Nguồn bài học:* Section 17: Containers on AWS: ECS, Fargate, ECR, EKS
- [ ] **Section 18 & 19:** Serverless Architecture — Lambda, API Gateway, Step Functions (`aws_serverless.html`)
  - *Nguồn bài học:* Section 18 (Serverless Overviews) & Section 19 (Serverless Solutions)
- [ ] **Section 23:** Monitoring & Audit — CloudWatch, CloudTrail, EventBridge (`aws_monitoring.html`)
  - *Nguồn bài học:* Section 23: AWS Monitoring & Audit
- [ ] **Section 24:** Security & Encryption — KMS, Secrets Manager, WAF, Shield (`aws_security.html`)
  - *Nguồn bài học:* Section 24: AWS Security & Encryption
- [ ] **Section 25:** Networking — VPC, Subnets, NAT, SG/NACL, Transit Gateway (`aws_vpc.html`)
  - *Nguồn bài học:* Section 25: Networking - VPC
- [ ] **Section 26:** Disaster Recovery & Migrations — DRS, DMS (`aws_disaster_recovery.html`)
  - *Nguồn bài học:* Section 26: Disaster Recovery & Migrations

---

## 🎨 Chuẩn thiết kế Cheat Sheet (Design Conventions)
- Mọi trang cheat sheet đều có cấu trúc tự chứa: không dùng JavaScript, không thư viện ngoài, tối ưu tải trang cực nhanh và chạy offline.
- Tự động chuyển đổi giao diện Sáng / Tối (Light / Dark mode) dựa trên cấu hình hệ thống thông qua CSS Custom Properties (`:root`).
- Hỗ trợ xem mượt mà trên cả máy tính bảng và điện thoại di động (Responsive mobile layout).
