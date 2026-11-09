# Bài 17: IAM MFA Hands On

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098028` (`CCP_-_IAM_-_MFA_Hands_On_v5.mp4`)
- **Thời lượng:** `04:01`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Thiết lập Password Policy trên IAM Console
- Vào **IAM -> Account settings -> Password policy -> Edit**.
- Có thể chọn mặc định (**IAM default password policy**) hoặc tùy chỉnh (**Custom**) các quy tắc: độ dài tối thiểu, chữ hoa, chữ thường, số, ký tự đặc biệt, thời hạn hết hạn mật khẩu (ví dụ 90 ngày), yêu cầu Admin reset khi hết hạn, cho phép user tự đổi mật khẩu, và chống trùng lặp mật khẩu cũ.

### 1.2. Kích hoạt MFA cho Root User
- Vào menu tài khoản góc trên bên phải -> **Security credentials** -> Phần **Multi-factor authentication (MFA)** -> **Assign MFA device**.
- AWS cho phép đăng ký **tối đa 8 thiết bị MFA** cho một tài khoản.
- **3 loại thiết bị khi đăng ký trên Console:**
  1. **Authenticator app** (Ứng dụng xác thực ảo như Authy, Google Authenticator).
  2. **Security key** (Khóa bảo mật vật lý FIDO/U2F).
  3. **Hardware TOTP token** (Thiết bị phần cứng tạo mã).
- **Quy trình kích hoạt Virtual MFA:**
  1. Mở ứng dụng Authenticator trên điện thoại và quét mã **QR Code**.
  2. Nhập **2 mã MFA liên tiếp** (MFA code 1 & chờ 30 giây nhập tiếp MFA code 2) để AWS xác nhận thiết bị đồng bộ thời gian chính xác.
  3. Nhấn **Add MFA**. Từ lần đăng nhập sau, ngoài email/password sẽ phải nhập thêm mã 6 số từ ứng dụng MFA.

> [!WARNING]
> Nếu bạn bật MFA trên Root Account mà làm mất điện thoại/thiết bị MFA, bạn sẽ bị khóa khỏi tài khoản và phải liên hệ AWS Support để khôi phục rất phức tạp.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:44` | First, let's define a password policy. Click on **Account settings** on the left-hand side, find **Password policy**, and click Edit. We can use the IAM default password policy or customize it: minimum length, uppercase, lowercase, number, non-alphanumeric character, password expiration (e.g., 90 days), allow users to change their own password, and prevent password reuse. | Đầu tiên, hãy thiết lập Password Policy bằng cách vào **Account settings -> Password policy -> Edit**. Bạn có thể dùng chính sách mặc định của IAM hoặc tùy chỉnh độ dài tối thiểu, chữ hoa, chữ thường, số, ký tự đặc biệt, thời gian hết hạn (ví dụ 90 ngày) và ngăn dùng lại mật khẩu cũ. |
| `00:44` - `02:05` | Second, let's set up MFA for your root account. Click on the account name -> **Security credentials**. Be careful: if you lose access to your MFA device (phone), you will lock yourself out of your root account! Click **Assign MFA device**, name it `MyiPhone`, and select **Authenticator app** (other options are Security key or Hardware TOTP token). | Thứ hai, thiết lập MFA cho Root account tại mục **Security credentials**. Lưu ý: nếu làm mất thiết bị MFA bạn sẽ bị khóa khỏi tài khoản. Nhấn **Assign MFA device**, đặt tên thiết bị là `MyiPhone` và chọn **Authenticator app** (các tùy chọn khác là Security key hoặc Hardware TOTP token). |
| `02:05` - `04:01` | Launch your authenticator app (e.g., Twilio Authy) on your phone, click **Show QR code**, and scan it. Then AWS asks for **two consecutive MFA codes** (`MFA code 1` and `MFA code 2`) to ensure the device is set up and synced accurately. Click **Add MFA** (you can register up to 8 MFA devices). Now when logging out and logging back in with the root account, after entering the password, AWS prompts for the MFA code from the phone app. | Mở ứng dụng Authenticator trên điện thoại, nhấn **Show QR code** và quét mã. AWS sẽ yêu cầu nhập **2 mã MFA liên tiếp** để đảm bảo thiết bị đồng bộ thời gian chính xác, sau đó nhấn **Add MFA** (có thể đăng ký tối đa 8 thiết bị MFA). Khi đăng xuất và đăng nhập lại, sau bước nhập mật khẩu, AWS sẽ yêu cầu nhập mã MFA từ điện thoại. |
