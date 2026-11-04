---
name: csv-to-apkg
description: Chuyển đổi danh sách từ vựng từ file CSV (phụ đề khóa học) sang file gói Anki .apkg hoàn chỉnh phân chia 20 từ/Unit, tự chứa 100% theo chuẩn Note Type 4000Book1 (Cloze deletion, ô gõ phím kiểm tra chính tả type:cloze, gợi ý điền từ t__ __n, phiên âm IPA và link mở video Udemy kèm timestamp).
argument-hint: [đường_dẫn_file.csv] [tên_file_xuat.apkg]
---

# /csv-to-apkg

Chuyển đổi dữ liệu từ vựng tiếng Anh từ file CSV sang gói thẻ Anki `.apkg` chuẩn **4000 Essential English Words 1 (Model: 4000Book1)**.

> **Đặc điểm nổi bật:** Hoàn toàn **tự chứa (Self-Contained)**. Không cần bất kỳ file mẫu `.apkg` nào bên ngoài (bạn có thể xóa an toàn file mẫu `4000_Essential_English_Words_1_-_Vietnamese.apkg` để tiết kiệm dung lượng).

- **Tham số:** `$ARGUMENTS`
  - Tham số 1 (tùy chọn): Đường dẫn file CSV đầu vào (mặc định: `data/lecturesub-tu-vung.csv`).
  - Tham số 2 (tùy chọn): Tên file `.apkg` xuất ra (mặc định: `dist/AWS_SAA_C03_Vocabulary.apkg`).

---

## Các bước thực hiện

1. **Xác định đường dẫn tệp**:
   - Tệp CSV nguồn: `$ARGUMENTS` (phần tử đầu tiên) hoặc mặc định `data/lecturesub-tu-vung.csv`.
   - Tệp APKG đích: `$ARGUMENTS` (phần tử thứ hai) hoặc mặc định `dist/AWS_SAA_C03_Vocabulary.apkg`.
   - Tệp TSV bổ trợ: `dist/anki_4000_format.tsv`.
   - Kiểm tra xem file CSV nguồn có tồn tại không. Nếu không, thông báo lỗi bằng tiếng Việt và dừng lại.

2. **Chạy script xuất dữ liệu tự chứa**:
   Thực thi lệnh Python:
   ```bash
   python3 scripts/export_anki_4000.py "<input_csv>" "<output_apkg>" "<output_tsv>"
   ```
   - Script tự động khởi tạo cơ sở dữ liệu SQLite theo đúng chuẩn Anki và nhúng sẵn định nghĩa Note Type `4000Book1`, cấu hình CSS, và phân chia phân cấp.
   - Tự động gom nhóm **cứ 20 từ thành 1 Unit** (Unit 01, Unit 02, Unit 03...).
   - Tạo cấu trúc Deck phân cấp trong Anki:
     - Deck cha: `AWS SAA-C03 Vocabulary (Stephane Maarek)`
     - Deck con: `AWS SAA-C03 Vocabulary (Stephane Maarek)::Unit 01` (từ 1 - 20)
     - Deck con: `AWS SAA-C03 Vocabulary (Stephane Maarek)::Unit 02` (từ 21 - 40)...
   - Gắn tag tương ứng cho mỗi thẻ: `AWS_SAA-C03 Stephane_Maarek Unit_01`, `Unit_02`...

3. **Đảm bảo chuẩn hóa 11 trường thông tin (Note Type `4000Book1`)**:
   Mỗi thẻ được tạo ra bắt buộc phải có đầy đủ 11 trường:
   - `0. №`: Số thứ tự thẻ (1, 2, 3...).
   - `1. Keyword`: Từ vựng tiếng Anh (ví dụ: `termination`, `latency`).
   - `2. Suggestion`: Gợi ý điền chữ cái đầu và cuối, ở giữa là khoảng trống `__ ` (ví dụ: `<div>t__ __ __ __ __ __ __ __ __n</div>`).
   - `3. Short Vietnamese`: Nghĩa tiếng Việt viết hoa chữ cái đầu (ví dụ: `Chấm dứt`).
   - `4. Keyword_Sound`: File phát âm (để trống).
   - `5. Image`: Hình ảnh minh họa (để trống).
   - `6. Transcription`: Phiên âm quốc tế IPA chuẩn UK/US (ví dụ: `/ˌtɜː.mɪˈneɪ.ʃən/`).
   - `7. Explanation`: Câu ngữ cảnh có đục lỗ Cloze: `to note in here is the delete on {{c1::termination}}.`
   - `8. Meaning_Sound` & `9. Example_Sound`: File âm thanh bổ trợ (để trống).
   - `10. Full Vietnamese`: Khối HTML chứa nghĩa chi tiết, câu ngữ cảnh, tên khóa học, và nút bấm `▶ Xem video trên Udemy: Lecture X (phút:giây)`.

4. **Đồng bộ hóa Dashboard & Thống kê**:
   - Đếm số lượng từ vựng thực tế trong file CSV.
   - Cập nhật số lượng từ vựng trong biến đếm `stats` của [`index.html`](file:///private/var/www/learn_aws/index.html) nếu số lượng thay đổi (ví dụ: `86+` thành số lượng mới).

5. **Kiểm tra tính toàn vẹn của file `.apkg`**:
   - Dùng script python kiểm tra database `collection.anki2` bên trong file `.apkg` vừa tạo (đảm bảo số thẻ `cards` khớp với số ghi chú `notes`, đủ 15 trường cho mỗi deck trong `col.decks`, và `usn = 0`).

6. **Báo cáo kết quả bằng tiếng Việt**:
   - Tên file `.apkg` đã tạo và dung lượng siêu nhẹ (chỉ khoảng ~20KB).
   - Tổng số thẻ flashcard và số lượng Units đã phân chia.
   - Hướng dẫn người dùng: Chỉ cần nhấp đúp file `.apkg` là Anki tự nạp đầy đủ cây thư mục Unit vào học ngay.
