# IMPROVEMENT_PLAN.md — Kế hoạch cải tiến `topics/` & `lectures/`

> **Đối tượng đọc:** AI Agent (Claude Code / Antigravity / Gemini…) hoặc người phát triển sẽ thực hiện cải tiến.
> **Mục tiêu:** Biến kho tài liệu thành công cụ **học nhanh nhất & dễ hiểu nhất** cho SAA-C03.
> **Ngày khảo sát:** 2026-11-09 · Commit gốc: `917efa1` · Trạng thái git lúc khảo sát: clean.

---

## 0. Quy tắc bắt buộc trước khi làm (đọc kỹ)

1. Đọc `CLAUDE.md` trước. Mọi quy tắc trong đó **ưu tiên cao hơn** tài liệu này.
2. **Không tự ý xóa file** (kể cả `.backup.html`, CSV, file tạm). Khi cần xóa/di chuyển → liệt kê và **chờ người dùng xác nhận**. Các task cần xác nhận được đánh dấu 🔒.
3. Chỉ chỉnh sửa trong thư mục dự án. Không dùng CDN / thư viện ngoài. Script Python chỉ dùng thư viện chuẩn.
4. Giữ song ngữ: mỗi `lang-vi` phải có `lang-en` tương ứng. Chỉ dùng token màu CSS (`--bl`, `--gr`, …), không hex trực tiếp.
5. Sau mỗi task chỉnh HTML: chạy `python3 tools/verify_all.py` (phải `ALL PASSED`) và kiểm tra link nội bộ (script mục 5.2).
6. Mỗi task làm xong → đánh dấu `[x]` tại mục 4 của file này, ghi ngắn gọn kết quả.
7. Giao tiếp với người dùng bằng tiếng Việt, giữ nguyên thuật ngữ AWS bằng tiếng Anh.

---

## 1. Thống kê hiện trạng

### 1.1. `topics/` — Cheat sheet & Lab (18 file)

| File | Size | Cards | Mermaid | Matrix | Study-mode class¹ | Link `lectures/` | Link Udemy | Nút Study Mode |
|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| `aws_global_infra.html` | 35KB | 9 | 1 | 1 | 0 | 0 | 4 | ❌ |
| `aws_iam.html` (file mẫu) | 53KB | 11 | 2 | 1 | **16** | 4 | 14 | ✅ |
| `aws_ec2.html` | 60KB | 11 | 1 | 2 | 0 | 4 | 18 | ❌ |
| `aws_storage.html` | 62KB | 12 | 1 | 2 | 0 | 4 | 18 | ❌ |
| `aws_elb_asg.html` | 66KB | 10 | 1 | 1 | 0 | 4 | 20 | ❌ |
| `aws_databases.html` | 60KB | 11 | 1 | 1 | 0 | 14 | 4 | ❌ |
| `aws_route53.html` | 47KB | 10 | 1 | 2 | 0 | 4 | 20 | ❌ |
| `aws_s3.html` | 44KB | 10 | 1 | 1 | 0 | 0 | 10 | ❌ |
| `aws_cloudfront.html` | 33KB | 8 | 1 | 2 | 0 | 0 | 8 | ❌ |
| `aws_iam.backup.html` ⚠️ | 28KB | 9 | 0 | 0 | 0 | 0 | 5 | ❌ |
| `lab_*.html` (8 file) | 12–21KB | 3–4 | 1 | 0 | 0 | 0 | 0 | ❌ |

¹ Số lần dùng class `pi-exam` / `kw-target` / `ans-blur` (CSS ở `assets/css/style.css:658-671`, JS `toggleExamFocus` / `toggleHideAnswers` ở `assets/js/app.js:120-140`).

- `tools/verify_all.py`: **ALL PASSED** (thẻ `div` cân bằng, số `lang-vi` = `lang-en` ở mọi file).
- Link nội bộ (`href`/`src`) trong `index.html` + `topics/*.html`: **0 link hỏng**.
- Mỗi trang cheat sheet 33–66KB, 8–12 card **full-width** → đọc hết mất ~30–45 phút/trang.

### 1.2. `lectures/` — Ghi chú bài giảng (7 Section, Udemy numbering)

| Thư mục | Số bài | Số từ (bài giảng) | Có transcript | Mermaid | Quiz (thực tế) | Quiz (theo `lectures/README.md`) |
|---|---:|---:|---:|---:|---:|---:|
| `section-04-iam-and-aws-cli` | 20 | 12.704 | 19 | 2 | 9 | 6 ❌ |
| `section-05-ec2-fundamentals` | 16 | 13.280 | 15 | 2 | 12 | 13 ❌ |
| `section-06-ec2-saa-level` | 9 | 20.221 | 8 | 4 | 5 | 8 ❌ |
| `section-07-ec2-instance-storage` | 14 | 27.168 | 14 | 7 | 9 | 11 ❌ |
| `section-08-elb-and-asg` | 17 | 45.208 | 17 | 12 | 21 | 14 ❌ |
| `section-09-rds-aurora-elasticache` | 14 | 34.603 | 13 | 9 | 24 | 24 ✅ |
| `section-10-route-53` | 20 | 40.822 | 20 | 19 | 7 | 7 ✅ |
| **Tổng** | **110** | **~194.000** | 106 | 55 | 87 | — |

- 4 bài không có transcript là bài dạng **Article** (hợp lệ, không cần sửa): `23-aws-cloudshell-region-availability.md`, `41-ssh-troubleshooting.md`, `53-eni-extra-reading.md`, `100-list-of-ports-to-be-familiar-with.md`.
- Cấu trúc mỗi bài: Metadata → `## 1. Kiến thức trọng tâm (Exam Notes)` → `## 2. Phụ đề chi tiết theo mốc thời gian` (bảng EN/VI).
- Định dạng quiz **không đồng nhất**: Quiz 6 dùng `### Câu N (\`id: …\`)`, các quiz khác dùng `## Câu hỏi N (ID: …)`.
- Đáp án quiz hiển thị sẵn `- [x]` + `> **Giải thích:**` ngay dưới câu hỏi → không tự kiểm tra được.
- Liên kết chéo: `topics/` → `lectures/*/README.md` (raw Markdown, mở bằng trình duyệt không render bảng/Mermaid). `lectures/` → `topics/`: **0 link**.

### 1.3. Độ phủ đề thi (so với các Section Udemy)

| Section Udemy | Cheat sheet `topics/` | Ghi chú `lectures/` | Lab |
|---|:---:|:---:|:---:|
| 3 Global Infra | ✅ | ❌ | — |
| 4 IAM & CLI | ✅ | ✅ | `lab_security_ssm_kms` (một phần) |
| 5–6 EC2 | ✅ | ✅ | `lab_ec2` |
| 7 Storage (EBS/EFS) | ✅ | ✅ | `lab_storage` |
| 8 ELB & ASG | ✅ | ✅ | — |
| 9 & 20 Databases | ✅ | ✅ (chỉ Sec 9) | — |
| 10 Route 53 | ✅ | ✅ | `lab_route53` |
| 11 & 13 S3 | ✅ | ❌ | `lab_s3` |
| 14 CloudFront & GA | ✅ | ❌ | — |
| 16 Decoupling (SQS/SNS/Kinesis) | ❌ | ❌ | `lab_decoupling` |
| 17 Containers | ❌ | ❌ | — |
| 18–19 Serverless | ❌ | ❌ | `lab_serverless` |
| 23 Monitoring | ❌ | ❌ | — |
| 24 Security & Encryption | ❌ | ❌ | `lab_security_ssm_kms` |
| 25 **VPC** (trọng số cao) | ❌ | ❌ | — |
| 26 DR & Migration | ❌ | ❌ | — |

---

## 2. Danh sách vấn đề phát hiện (Issues)

### ISSUE-01 · 🔴 Lẫn ký tự ngoại ngữ / lỗi chính tả trong nội dung (Critical)
| File | Dòng | Lỗi | Sửa thành |
|---|---:|---|---|
| `lectures/section-10-route-53/107-route-53-cname-vs-alias.md` | 16 | `Trỏ یک hostname` (Ba Tư, xuất hiện **2 lần** trên dòng) | `Trỏ một hostname` |
| `lectures/section-10-route-53/107-route-53-cname-vs-alias.md` | 37 | `Cẫy bẫy đề thi` | `Cái bẫy đề thi` |
| `lectures/section-06-ec2-saa-level/47-private-vs-public-vs-elastic-ip.md` | 18 | `переmap Elastic IP` (Nga) | `remap Elastic IP` |
| `lectures/section-06-ec2-saa-level/49-ec2-placement-groups.md` | 20 | `сотни instances` (Nga = "hàng trăm") | `hundreds of instances` |
| `lectures/section-07-ec2-instance-storage/README.md` | 13 | `Ứng dụng критическое` (Nga) | `Ứng dụng quan trọng (mission-critical)` |

→ Dấu hiệu nội dung do AI sinh **chưa được soát lại**. Cần quét toàn bộ, không chỉ 5 vị trí này.

### ISSUE-02 · 🟠 Thiếu lớp "ôn nhanh" — quá nhiều chữ
- Không có bản tóm tắt ≤ 1 màn hình cho mỗi Section. Người học buộc phải đọc 8–12 card hoặc transcript dài.

### ISSUE-03 · 🟠 Học thụ động — không tự kiểm tra
- Study Mode chỉ có ở `aws_iam.html`; 8 cheat sheet còn lại không có class `pi-exam` / `kw-target` / `ans-blur` và không có nút toggle.
- Quiz hiển thị đáp án ngay.

### ISSUE-04 · 🟡 Liên kết rời rạc & trùng lặp nội dung
- `topics/` link sang `.md` thô; `lectures/` không link về `topics/`.
- Bảng "4-Point Cheat Sheet" tồn tại song song ở `lectures/README.md` và trong card topics → nguy cơ lệch nội dung.

### ISSUE-05 · 🟡 Số liệu & đánh số Section không nhất quán
- `lectures/README.md`: cột "Trắc nghiệm" ghi sai số câu (xem bảng 1.2).
- `CLAUDE.md` mục *Roadmap*: đánh số lệch 1 so với Udemy (ghi Storage = Section 6, ELB = 7, DB = 8, Route 53 = 9; đúng phải là 7, 8, 9, 10) và vẫn liệt kê các mục đã hoàn thành như việc cần làm. Dòng "Đã hoàn thành" cũng lệch số.
- `index.html` và `lectures/` đã dùng đúng numbering Udemy → lấy làm chuẩn.
- Quiz 6 khác định dạng heading với các quiz khác.

### ISSUE-06 · 🟡 Thiếu chủ đề trọng số cao
- VPC, Decoupling, Security, Serverless, Monitoring, Containers, DR chưa có cheat sheet. S3, CloudFront, Global Infra chưa có lecture notes.

### ISSUE-07 · ⚪ Dọn dẹp cấu trúc (🔒 cần xác nhận)
- `topics/aws_iam.backup.html` nằm trong `topics/` (đã gitignored qua `*.backup.html`, nhưng vẫn bị `verify_all.py` quét).
- CSV ở thư mục gốc thay vì `data/`: `lecturesub-tu-vung.csv`, `lecturesub-tu-vung (2).csv`, `tu-vung-khong-chung.csv`, `tu-vung-moi.csv`. `data/` hiện **trống**.
- `tools/` (`verify_all.py`, `update_style.py`, `update_iam_cheat_sheet.py`) chưa có trong File Inventory của `CLAUDE.md`/`README.md`. `verify_all.py` dùng `os.getcwd()` thay vì `os.path.dirname(__file__)` (vi phạm quy tắc đường dẫn script).
- Lecture ID trích dẫn cho S3 / Global Infra trong `index.html` (`26097978`, `26098336`…) có format khác các ID trong `lectures/` (`13528190`…) → **cần xác minh** với CSV / Udemy, không tự bịa ID.

---

## 3. Lộ trình học đề xuất (kiến trúc nội dung đích)

```
Tầng 1 — ⚡ 5-minute Review (đầu mỗi cheat sheet)  → ôn trước thi, 5 phút/Section
Tầng 2 — Cheat sheet topics/aws_<topic>.html        → hiểu bản chất, 30 phút/Section
Tầng 3 — Quiz tự kiểm tra (ẩn đáp án)               → đo mức nắm bài
Tầng 4 — lectures/*.md (Exam Notes + transcript)     → tra cứu khi sai quiz
```

---

## 4. Danh sách task (thực hiện theo thứ tự)

### Phase 1 — Sửa lỗi & đồng bộ (ít rủi ro, làm trước)

- [x] **T1.1 — Sửa ISSUE-01.** Đã sửa 5 vị trí lỗi ký tự Ba Tư/Nga/chính tả trong `lectures/section-10-route-53/107-route-53-cname-vs-alias.md`, `lectures/section-06-ec2-saa-level/47-private-vs-public-vs-elastic-ip.md`, `lectures/section-06-ec2-saa-level/49-ec2-placement-groups.md`, `lectures/section-07-ec2-instance-storage/README.md`. Quét toàn bộ repo không còn ký tự lạ.
- [x] **T1.2 — Mở rộng `tools/verify_all.py`.** Đường dẫn gốc dùng `os.path.dirname`, bỏ qua `*.backup.html`, thêm quét regex ký tự ngoại ngữ bất thường, kiểm tra link nội bộ `href`/`src`. Chạy từ mọi thư mục đều `ALL PASSED`.
- [x] **T1.3 — Sửa số câu quiz trong `lectures/README.md`** theo số lượng câu hỏi thực tế (Quiz 1: 9 câu, Quiz 2: 12 câu, Quiz 3: 5 câu, Quiz 4: 9 câu, Quiz 5: 21 câu).
- [x] **T1.4 — Chuẩn hóa heading Quiz 6** (`section-09-.../quiz-06-*.md`): đổi 24 câu thành `## Câu hỏi N (ID: \`X\`)`, tách đoạn EN/VI riêng, chuyển giải thích sang `> [!NOTE]\n> **Giải thích:**`.
- [x] **T1.5 — Đồng bộ đánh số Section theo Udemy** trong `CLAUDE.md` (mục Roadmap + danh sách đã hoàn thành 9 cheat sheet) và `README.md`.
- [x] **T1.6 — Ghi `tools/` vào File Inventory** của `CLAUDE.md` và cây thư mục/bảng `README.md`.

### Phase 2 — Tăng tốc độ học (giá trị cao nhất)

- [x] **T2.1 — Card "⚡ 5-minute Review / Ôn nhanh 5 phút"** đặt ngay sau `.header` ở toàn bộ 9 cheat sheet `aws_*.html` (Global Infra, IAM, EC2, Storage, ELB & ASG, Databases, Route 53, S3, CloudFront). Mỗi card bao gồm 5 con số vàng/bẫy đề cốt lõi, bảng ánh xạ từ khóa &rarr; đáp án (`.kw-target`) song ngữ đầy đủ.
- [x] **T2.2 — Nhân rộng Study Mode** sang toàn bộ 9 cheat sheet: tích hợp Toolbar 2 nút (`toggleExamFocus`, `toggleHideAnswers`), gắn `pi-exam` cho các điểm bẫy thi và `kw-target` cho đáp án từ khóa (mỗi trang đạt từ 10 đến 21 study-mode classes).
- [x] **T2.3 — Ẩn đáp án quiz** trong 7 file `lectures/*/quiz-*.md`: giữ danh sách lựa chọn dạng `- [ ]` (đã bỏ `[x]` và bỏ in đậm đáp án), chuyển toàn bộ 87 câu hỏi sang dạng `<details><summary>👉 Xem đáp án</summary>` kèm đáp án và blockquote giải thích `> [!NOTE]`. `grep -c '\[x\]'` = 0.

### Phase 3 — Kết nối các tầng nội dung

- [x] **T3.1 — Link ngược lectures → topics.** Đã thêm dòng `- **Cheat sheet:** [topics/aws_<topic>.html](../../topics/aws_<topic>.html)` vào đầu 124 bài giảng và README trong 7 thư mục `lectures/section-*/` tương ứng.
- [ ] **T3.2 — Sửa link topics → lectures.** Link `../lectures/.../README.md` hiện mở ra Markdown thô. Chọn 1 trong 2 (hỏi người dùng nếu chưa rõ):
  - (a) Đổi sang link Udemy chính xác của bài (lấy từ metadata `Lecture ID` trong file `.md`), giữ link `.md` làm phụ; hoặc
  - (b) Viết `scripts/md_to_html.py` (stdlib only) sinh bản HTML của lectures vào `lectures_html/` dùng chung `assets/css/style.css` + Mermaid nội bộ.
- [ ] **T3.3 — Chọn một nguồn sự thật cho "4-Point Cheat Sheet"**: giữ ở `topics/` (HTML), trong `lectures/README.md` thay bằng bảng tóm tắt ngắn + link sang topics để tránh lệch nội dung. 🔒 (xóa nội dung → hỏi người dùng trước)

### Phase 4 — Mở rộng độ phủ (dùng skill `/new-topic`)

Thứ tự ưu tiên theo trọng số đề thi:
- [ ] **T4.1** `topics/aws_vpc.html` — Section 25
- [ ] **T4.2** `topics/aws_decoupling.html` — Section 16 (liên kết `lab_decoupling.html`)
- [ ] **T4.3** `topics/aws_security.html` — Section 24 (liên kết `lab_security_ssm_kms.html`)
- [ ] **T4.4** `topics/aws_serverless.html` — Section 18–19 (liên kết `lab_serverless.html`)
- [ ] **T4.5** `topics/aws_monitoring.html` — Section 23
- [ ] **T4.6** `topics/aws_containers.html` — Section 17
- [ ] **T4.7** `topics/aws_disaster_recovery.html` — Section 26

Mỗi trang mới phải có sẵn card ⚡ 5-minute Review (T2.1) và Study Mode (T2.2). Làm theo Workflow mục 3 trong `CLAUDE.md` (cập nhật `index.html`, `README.md`, `CLAUDE.md`). Link Udemy chỉ lấy từ `data/lecturesub-tu-vung.csv` — nếu CSV không có trong `data/` thì **báo người dùng**, không tự bịa ID.

### Phase 5 — Dọn dẹp 🔒 (chỉ làm khi người dùng đồng ý)

- [ ] **T5.1** Di chuyển 4 file CSV ở gốc vào `data/` (hoặc theo chỉ định của người dùng). Kiểm tra script trong `scripts/` vẫn trỏ đúng `data/lecturesub-tu-vung.csv`.
- [ ] **T5.2** Xử lý `topics/aws_iam.backup.html` (giữ / chuyển ra ngoài `topics/` / xóa).
- [ ] **T5.3** Xác minh các Lecture ID dạng `2609xxxx` trong `index.html` (Section 3, 11, 13, 14) với CSV; sửa nếu sai.

---

## 5. Lệnh kiểm tra dùng lại

### 5.1. Quét ký tự ngoại ngữ lạ
```bash
grep -rnP '[\x{0600}-\x{06FF}\x{0400}-\x{04FF}\x{4E00}-\x{9FFF}\x{3040}-\x{30FF}\x{AC00}-\x{D7AF}\x{0E00}-\x{0E7F}]' lectures topics index.html README.md
```

### 5.2. Kiểm tra link nội bộ
```bash
python3 - <<'EOF'
import re, os, glob
for f in ['index.html'] + glob.glob('topics/*.html'):
    s = open(f, encoding='utf-8').read(); d = os.path.dirname(f)
    for h in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', s):
        if not os.path.exists(os.path.normpath(os.path.join(d, h))):
            print(f, '->', h)
EOF
```

### 5.3. Đếm câu quiz thực tế
```bash
for q in lectures/*/quiz-*.md; do echo "$q: $(grep -cE '^#{2,3} Câu' "$q")"; done
```

### 5.4. Đếm Study Mode class mỗi trang
```bash
grep -c "pi-exam\|kw-target\|ans-blur" topics/aws_*.html
```

### 5.5. Validator tổng
```bash
python3 tools/verify_all.py
```

---

## 6. Định nghĩa hoàn thành (Definition of Done)

- Lệnh 5.1 trả về rỗng; 5.2 không in gì; 5.5 in `ALL PASSED`.
- 100% cheat sheet `aws_*.html` có card ⚡ 5-minute Review và Study Mode hoạt động.
- 0 đáp án lộ sẵn trong quiz.
- Số liệu trong `lectures/README.md`, `index.html`, `README.md`, `CLAUDE.md` khớp với thực tế.
- Không file nào bị xóa/di chuyển khi chưa có xác nhận của người dùng.
