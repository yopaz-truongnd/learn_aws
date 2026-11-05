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
| [`assets/css/style.css`](assets/css/style.css) | Toàn bộ CSS Design System dùng chung, tokens màu, Dark/Light mode, typography, components, matrix tables. |
| [`assets/js/app.js`](assets/js/app.js) | Script xử lý chuyển đổi song ngữ VI/EN tức thì, lưu `localStorage`, render tự động Mermaid. |
| [`assets/vendor/mermaid.min.js`](assets/vendor/mermaid.min.js) | Thư viện Mermaid.js nội bộ 100% offline vẽ sơ đồ tư duy, decision tree, sequence diagrams, state diagrams. |
| [`scripts/export_anki_4000.py`](scripts/export_anki_4000.py) | Sinh SQLite Anki và đóng gói `.apkg` tự chứa 100% (không cần file `.apkg` mẫu). |
| `data/lecturesub-tu-vung.csv` | UTF-8 with BOM, các cột: `Từ`, `Nghĩa`, `Nguồn`, `Đích`, `Câu gốc`, `Bài học`, `Giây`, `Liên kết`. |
| `dist/*` | Kết quả build — không commit, sinh lại bất cứ lúc nào bằng script. |

> **Lưu ý:** `data/*.csv` và `dist/` nằm trong `.gitignore`, nên khi clone repo về bạn cần tự chép file CSV vào `data/` rồi chạy script để tạo deck Anki.

---

## 🚀 Bắt đầu nhanh (Quick Start)

Không cần cài đặt gì — mở trực tiếp bằng trình duyệt:

```bash
open index.html                      # Dashboard mục lục trung tâm

open topics/aws_global_infra.html    # Section 3: Hạ tầng toàn cầu AWS
open topics/aws_iam.html             # Section 4: Quản lý danh tính & phân quyền (IAM)
open topics/aws_ec2.html             # Section 5: Máy chủ ảo IaaS (EC2)
```

---

## 🗂️ Học từ vựng bằng Anki (chuẩn 4000 Essential English Words)

### 1. Tạo deck

```bash
# Mặc định: data/lecturesub-tu-vung.csv → dist/AWS_SAA_C03_Vocabulary.apkg + dist/anki_4000_format.tsv
python3 scripts/export_anki_4000.py

# Hoặc chỉ định đường dẫn tùy ý
python3 scripts/export_anki_4000.py <input.csv> <output.apkg> <output.tsv>
```

Script chạy được từ bất kỳ thư mục nào và tự tạo thư mục `dist/` nếu chưa có. Mỗi khi bổ sung từ mới vào CSV, chỉ cần chạy lại lệnh trên (hoặc dùng skill `/csv-to-apkg` trong Claude Code).

### 2. Nạp vào Anki

- **Cách 1 — Mở trực tiếp (khuyên dùng):** cài [Anki Desktop](https://apps.ankiweb.net/), nhấp đúp `dist/AWS_SAA_C03_Vocabulary.apkg`.
- **Cách 2 — Import vào deck có sẵn:** trong Anki chọn **File → Import...** → `dist/anki_4000_format.tsv` (ánh xạ 11 trường của Note Type `4000Book1`).

### 3. Cấu trúc deck

- **Deck cha:** `AWS SAA-C03 Vocabulary (Stephane Maarek)`, chia subdeck **20 từ / Unit** (`Unit 01`, `Unit 02`, …). Với bộ ~86 từ hiện tại → 5 Units.
- **Mặt trước:** gợi ý chữ cái đầu/cuối (`t__ __ __ __n`), câu ngữ cảnh đục lỗ Cloze, nghĩa tiếng Việt, ô gõ từ (`type:cloze`).
- **Mặt sau:** so sánh từ đã gõ (xanh đúng / đỏ sai), phiên âm IPA, câu ngữ cảnh đầy đủ, nút mở video Udemy đúng mốc thời gian.

---

## 🗺️ Lộ trình & Nguồn bài giảng Udemy

- [x] **Section 3:** AWS Global Infrastructure ([`topics/aws_global_infra.html`](topics/aws_global_infra.html))
  - *Lectures:* `26097978` (Overview), `26097980` (Regions & AZs)
- [x] **Section 4:** AWS IAM ([`topics/aws_iam.html`](topics/aws_iam.html))
  - *Lectures:* `26097996` (Overview), `26098020` (Root User), `26098028` (Users & Credentials), `26098070` (Tools), `26623458` (Policies in Depth)
- [x] **Section 5:** AWS EC2 ([`topics/aws_ec2.html`](topics/aws_ec2.html))
  - *Lectures:* `26098112` (User Data), `26098122` (Lifecycle & Termination), `26098128` (Instance Types), `26098134` (Security Groups)
- [ ] **Section 6:** EC2 Storage — EBS, EFS & Instance Store (`topics/aws_storage.html`)
- [ ] **Section 7:** High Availability & Scalability — ELB & ASG (`topics/aws_elb_asg.html`)
- [ ] **Section 8 & 20:** AWS Databases — RDS, Aurora, ElastiCache, DynamoDB (`topics/aws_databases.html`)
- [ ] **Section 9:** Amazon Route 53 (`topics/aws_route53.html`)
- [ ] **Section 11 & 13:** Amazon S3 & Advanced S3 (`topics/aws_s3.html`)
- [ ] **Section 14:** CloudFront & Global Accelerator (`topics/aws_cloudfront.html`)
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
