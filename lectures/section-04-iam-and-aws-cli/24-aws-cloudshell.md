# Bài 24: AWS CloudShell

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098060` (`CCP - CloudShell v2.mp4`)
- **Thời lượng:** `03:53`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. AWS CloudShell là gì?
- Là một **terminal trên đám mây (browser-based shell)** tích hợp sẵn ngay trên giao diện AWS Management Console và **hoàn toàn miễn phí (free to use)**.
- Đã được cài đặt sẵn **AWS CLI v2** cùng nhiều công cụ phát triển.

### 1.2. Các đặc điểm nổi bật của AWS CloudShell
1. **Tự động nhận thông tin xác thực (Pre-authenticated):**
   - Không cần tạo Access Keys hay chạy `aws configure`.
   - Mọi lệnh AWS CLI chạy trong CloudShell tự động sử dụng chính quyền hạn (credentials) của tài khoản/IAM User đang đăng nhập trên AWS Console.
2. **Region-specific:**
   - Mặc định thực thi lệnh ở chính **Region mà bạn đang mở trên Console** (vẫn có thể truyền cờ `--region` nếu muốn gọi sang Region khác).
3. **Lưu trữ bền vững (Persistent Storage):**
   - Bạn có một thư mục cá nhân (`$HOME` repository, dung lượng lưu trữ miễn phí 1 GB trên mỗi Region).
   - Các tệp tin tạo trong thư mục này (ví dụ: `echo "test" > demo.txt`) **vẫn được giữ nguyên** ngay cả khi bạn đóng hoặc khởi động lại CloudShell.
4. **Tính năng tiện ích trên giao diện:**
   - Hỗ trợ **Upload file** từ máy tính lên CloudShell và **Download file** từ CloudShell về máy tính.
   - Hỗ trợ mở nhiều **Tabs** hoặc chia đôi màn hình (**Split into columns/rows**) để làm việc với nhiều cửa sổ terminal cùng lúc.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:08` | An alternative to using your local terminal to issue commands against AWS is **AWS CloudShell** (the terminal icon on the top navigation bar). Note that CloudShell is only available in supported regions. CloudShell is basically a free terminal in the AWS cloud with AWS CLI v2 pre-installed. | Một giải pháp thay thế cho việc dùng terminal trên máy cá nhân là **AWS CloudShell** (biểu tượng terminal trên thanh công cụ phía trên cùng của Console). Lưu ý rằng CloudShell chỉ khả dụng tại các Region được hỗ trợ. Về cơ bản, đây là một terminal miễn phí trên đám mây đã cài sẵn AWS CLI v2. |
| `01:08` - `01:43` | Whenever you run CLI commands in CloudShell (like `aws iam list-users`), it automatically uses the credentials of the account you are currently logged in with in the Console, and defaults to the region you are currently in. | Khi bạn chạy lệnh CLI trong CloudShell (như `aws iam list-users`), nó tự động sử dụng thông tin xác thực của chính tài khoản bạn đang đăng nhập trên Console, và mặc định trỏ vào Region bạn đang chọn. |
| `01:43` - `03:53` | CloudShell also gives you persistent file storage: if you create a file (e.g., `echo test > demo.txt`) and restart CloudShell, the file stays there. You can customize font size/theme, **download and upload files** via the Actions menu, and open multiple tabs or split terminals into columns. | CloudShell còn cung cấp bộ nhớ lưu trữ tệp bền vững: nếu bạn tạo file (ví dụ `echo test > demo.txt`) rồi khởi động lại CloudShell, file đó vẫn còn nguyên. Ngoài ra bạn có thể tùy chỉnh giao diện, **tải file lên (upload) và tải file xuống (download)** qua menu Actions, cũng như mở nhiều tab hoặc chia cột màn hình terminal. |
