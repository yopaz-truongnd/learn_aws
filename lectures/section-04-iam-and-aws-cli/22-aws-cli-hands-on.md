# Bài 22: AWS CLI Hands On

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098056` (`CCP_-_IAM_-_CLI_Hands_On_v2.mp4`)
- **Thời lượng:** `03:50`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Tạo Access Keys trên IAM Console
- Vào **IAM -> Users -> Chọn User (`Stephane`) -> Tab Security credentials -> Create access key**.
- Chọn mục đích sử dụng: **Command Line Interface (CLI)**.
- Lưu ý: `Secret Access Key` chỉ hiển thị **duy nhất một lần** tại thời điểm khởi tạo (có thể tải về file `.csv`).

### 1.2. Cấu hình AWS CLI với lệnh `aws configure`
Chạy lệnh sau trên terminal:
```bash
aws configure
```
Hệ thống sẽ yêu cầu nhập 4 thông số:
1. **`AWS Access Key ID`**: Nhập mã Access Key ID vừa tạo.
2. **`AWS Secret Access Key`**: Nhập mã Secret Access Key.
3. **`Default region name`**: Nhập mã Region gần bạn hoặc đang học (ví dụ: `eu-west-1`, `us-east-1`, `ap-southeast-1`).
4. **`Default output format`**: Định dạng kết quả trả về (để trống nhấn Enter hoặc `json`).

### 1.3. Thử nghiệm lệnh CLI & Quyền hạn IAM
- Chạy lệnh liệt kê danh sách IAM Users:
  ```bash
  aws iam list-users
  ```
- Kết quả trả về định dạng JSON chứa `UserName`, `UserId`, `Arn`, `CreateDate`, `PasswordLastUsed` — tương đương thông tin trên Management Console.
- **Tính đồng nhất về quyền hạn:** Khi xóa User `Stephane` khỏi group `admin`, lệnh `aws iam list-users` trên CLI cũng lập tức bị từ chối (`AccessDenied`) giống hệt như trên giao diện web. Quyền của Access Key chính là quyền IAM của User sở hữu nó.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:15` | Let me show you how to create access keys. Click on username `Stephane` -> **Security credentials** -> scroll down and click **Create access key**. Select **Command Line Interface (CLI)**, acknowledge the recommendation, and click Create. Note that this is the only time you can view or download the Secret Access Key. | Để tạo Access Keys: vào user `Stephane` -> tab **Security credentials** -> nhấn **Create access key**. Chọn mục đích sử dụng **Command Line Interface (CLI)**, tích xác nhận và nhấn tạo. Lưu ý: đây là lần duy nhất bạn có thể xem hoặc tải về Secret Access Key. |
| `01:15` - `02:34` | Next, configure the AWS CLI in the terminal by typing `aws configure`. Enter your `AWS Access Key ID`, `AWS Secret Access Key`, `Default region name` (e.g., `eu-west-1`), and `Default output format` (press Enter). Now test it by running `aws iam list-users`. It returns a JSON list of users (`UserName`, `UserId`, `Arn`, `CreateDate`, `PasswordLastUsed`), matching what we see in the Management Console UI. | Mở terminal và chạy lệnh `aws configure`. Nhập lần lượt `AWS Access Key ID`, `AWS Secret Access Key`, `Default region name` (ví dụ `eu-west-1`) và `Default output format`. Sau đó chạy thử lệnh `aws iam list-users` — CLI sẽ trả về danh sách người dùng dưới dạng JSON giống hệt thông tin trên giao diện Console. |
| `02:34` - `03:50` | If we remove `Stephane` from the `admin` group using the root account, refreshing the Console UI gives an error, and running `aws iam list-users` in the CLI is also denied. CLI permissions are the exact same as the IAM user's permissions. Finally, don't forget to add `Stephane` back into the `admin` group! | Nếu dùng tài khoản Root xóa `Stephane` khỏi group `admin`, cả giao diện Console lẫn lệnh `aws iam list-users` trên CLI đều bị từ chối truy cập. Quyền hạn trên CLI hoàn toàn giống với quyền của IAM User đó. Cuối cùng, đừng quên thêm `Stephane` trở lại group `admin`. |
