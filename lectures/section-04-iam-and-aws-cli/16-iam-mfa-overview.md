# Bài 16: IAM MFA Overview

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098020` (`CCP_-_IAM_-_MFA_Overview_v2.mp4`)
- **Thời lượng:** `04:10`

---

## 1. Kiến thức trọng tâm (Exam Notes)

Để bảo vệ Root Account và các IAM Users khỏi bị tấn công chiếm quyền, IAM cung cấp **2 cơ chế phòng vệ chính**:

### 1.1. Cơ chế 1: IAM Password Policy (Chính sách mật khẩu)
Giúp chống lại các cuộc tấn công dò mật khẩu (**Brute-force attacks**). Trong AWS, bạn có thể cấu hình:
- Độ dài mật khẩu tối thiểu (Minimum password length).
- Yêu cầu các loại ký tự cụ thể: chữ hoa (uppercase), chữ thường (lowercase), chữ số (numbers), ký tự đặc biệt (non-alphanumeric characters).
- Cho phép hoặc cấm IAM Users tự đổi mật khẩu của họ.
- Yêu cầu mật khẩu hết hạn sau một khoảng thời gian (ví dụ: bắt buộc đổi sau mỗi 90 ngày).
- Ngăn chặn việc sử dụng lại mật khẩu cũ (**Prevent password reuse**).

### 1.2. Cơ chế 2: Multi-Factor Authentication (MFA - Xác thực đa yếu tố)
- **Công thức cốt lõi:**
  $$\text{MFA} = \text{Password you know (Mật khẩu bạn biết)} + \text{Security device you own (Thiết bị bảo mật bạn sở hữu)}$$
- **Lợi ích chính:** Ngay cả khi mật khẩu của người dùng bị lộ, bị đánh cắp hoặc bị hack, kẻ tấn công vẫn **không thể đăng nhập** vì không có thiết bị vật lý/điện thoại tạo mã MFA của người dùng.
- **Khuyến nghị bắt buộc:** Luôn bật MFA cho **Root Account** và các **IAM Users**.

### 1.3. Các tùy chọn thiết bị MFA trong AWS (Cần nhớ khi đi thi)

| Loại thiết bị MFA | Ví dụ / Nhà cung cấp | Đặc điểm quan trọng cho kỳ thi |
| :--- | :--- | :--- |
| **1. Virtual MFA Device** *(Thiết bị MFA ảo)* | **Google Authenticator** *(chỉ 1 điện thoại)*, **Authy** *(hỗ trợ đa thiết bị)* | Ứng dụng trên điện thoại. **Hỗ trợ nhiều tokens (nhiều Root/IAM users) trên cùng một thiết bị duy nhất**. |
| **2. Universal 2nd Factor (U2F) Security Key** | **YubiKey** của Yubico *(bên thứ 3)* | Khóa bảo mật vật lý cắm qua cổng USB/NFC. **Hỗ trợ nhiều Root và IAM users trên cùng một khóa bảo mật duy nhất**. |
| **3. Hardware Key Fob MFA Device** | **Gemalto** *(bên thứ 3)* | Thiết bị phần cứng hiển thị mã số (key fob). |
| **4. Hardware Key Fob MFA Device for AWS GovCloud (US)** | **SurePassID** *(bên thứ 3)* | Thiết bị key fob chuyên dụng bắt buộc khi dùng đám mây chính phủ Mỹ (**AWS GovCloud US**). |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:05` | Now that we have created users and groups, it is time to protect them from being compromised. We have two defense mechanisms. The first one is a **password policy**. You can set a minimum password length, require specific character types (uppercase, lowercase, numbers, non-alphanumeric), allow IAM users to change their own passwords, require password expiration (e.g., every 90 days), and prevent password reuse. A password policy is helpful against brute-force attacks. | Sau khi tạo users và groups, ta cần bảo vệ chúng bằng 2 cơ chế phòng vệ. Cơ chế đầu tiên là **Password Policy** (Chính sách mật khẩu): đặt độ dài tối thiểu, yêu cầu chữ hoa/thường/số/ký tự đặc biệt, cho phép user tự đổi mật khẩu, đặt hạn mật khẩu (ví dụ 90 ngày) và cấm dùng lại mật khẩu cũ. Chính sách này giúp chống tấn công brute-force. |
| `01:05` - `02:31` | The second defense mechanism is **Multi-Factor Authentication (MFA)**. You want to protect at least your root account and all your IAM users. MFA is the combination of a **password you know** and a **security device you own**. Even if Alice's password is stolen or hacked, the account is not compromised because the hacker would also need Alice's physical device (e.g., her phone). | Cơ chế thứ hai là **Multi-Factor Authentication (MFA)**. Bạn cần bảo vệ tối thiểu là Root account và tất cả IAM users. MFA kết hợp **mật khẩu bạn biết** và **thiết bị bảo mật bạn sở hữu**. Dù mật khẩu bị lộ hay bị hack, tài khoản vẫn an toàn vì kẻ tấn công không có thiết bị vật lý của bạn. |
| `02:31` - `04:10` | What are the MFA device options in AWS? 1) **Virtual MFA device** (Google Authenticator on one phone, or Authy) — supports multiple tokens (multiple root/IAM users) on a single device. 2) **Universal 2nd Factor (U2F) Security Key** (e.g., YubiKey by Yubico, a 3rd party) — a physical device that also supports multiple root and IAM users using a single security key. 3) **Hardware Key Fob MFA Device** provided by Gemalto (3rd party). 4) **Hardware Key Fob for AWS GovCloud (US)** provided by SurePassID (3rd party). | Các loại thiết bị MFA trong AWS gồm: 1) **Virtual MFA device** (ứng dụng Google Authenticator hoặc Authy) — hỗ trợ nhiều tài khoản/users trên một thiết bị; 2) **U2F Security Key** (khóa vật lý như YubiKey của Yubico) — cũng hỗ trợ nhiều Root và IAM users trên một khóa duy nhất; 3) **Hardware Key Fob** của Gemalto; 4) **Hardware Key Fob cho AWS GovCloud (US)** của SurePassID. |
