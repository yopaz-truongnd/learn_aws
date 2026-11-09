# Bài 28: IAM Security Tools Hands On

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098074` (`CCP_-_IAM_-_Security_Tools_Hands_On_v2.mp4`)
- **Thời lượng:** `02:23`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Thực hành IAM Credentials Report (Account-level)
- Vào **IAM Console -> Credential report -> Download credential report**.
- Hệ thống tải về một file `.csv` chứa các dòng tương ứng với `<root_account>` và từng IAM User (`stephane`), bao gồm các cột thông tin:
  - `user_creation_time`: Thời điểm tạo user.
  - `password_enabled`, `password_last_used`, `password_last_changed`, `password_next_rotation`.
  - `mfa_active`: Đã bật MFA chưa (ví dụ: `TRUE` cho Root, `FALSE` cho `stephane`).
  - `access_key_1_active`, `access_key_1_last_rotated`, `access_key_1_last_used_date` (và tương tự cho `access_key_2`, `cert_1`, `cert_2`).
- **Ứng dụng:** Phát hiện nhanh các tài khoản chưa bật MFA, lâu ngày không đổi mật khẩu hoặc có Access Keys cũ không dùng đến cần vô hiệu hóa.

### 1.2. Thực hành IAM Access Advisor (User-level)
- Vào **IAM Console -> Users -> Chọn User (`stephane`) -> Tab Access Advisor**.
- Hiển thị danh sách toàn bộ các dịch vụ AWS mà User được phép truy cập, kèm theo:
  - **Last accessed:** Thời gian truy cập gần nhất (ví dụ: IAM, EC2, Organizations, Health đã được truy cập gần đây; trong khi Alexa for Business, App2Container hiển thị `Not accessed in the tracking period`).
  - **Policy granting access:** Cho biết chính xác Policy nào (ví dụ `AdministratorAccess`) đã cấp quyền truy cập dịch vụ đó.
- **Ứng dụng:** Thu hẹp quyền hạn (Granular user access permissions) theo đúng nguyên tắc Least Privilege.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:05` | Let's generate a credentials report: click **Credential report -> Download credential report** to get a CSV file. In the CSV, we have rows for `<root_account>` and `stephane`. We can see when each user was created, whether the password is enabled, when it was last used/changed, next rotation, whether **MFA is active** (`true` for root, `false` for `stephane`), and whether **Access Keys** are created and last rotated/used. This report is great for finding users that need security attention. | Hãy tạo báo cáo thông tin xác thực bằng cách vào **Credential report -> Download credential report** để tải về file CSV. File này có dòng cho `<root_account>` và `stephane`, cho biết ngày tạo user, trạng thái mật khẩu, lần cuối dùng/đổi mật khẩu, trạng thái **MFA** (`true` ở root, `false` ở `stephane`), và trạng thái các **Access Keys**. Báo cáo này rất hữu ích để phát hiện các user cần chú ý về bảo mật. |
| `01:05` - `02:23` | Next, let's check **IAM Access Advisor**: go to **Users -> `stephane` -> Access Advisor** tab. It shows which services were accessed by the user and when (e.g., Organizations, Health, IAM, EC2 were accessed recently, while Alexa for Business and App2Container were never accessed). It also shows which policy (e.g., `AdministratorAccess`) granted access to each service, helping you enforce granular permissions and least privilege. | Tiếp theo, kiểm tra **IAM Access Advisor** bằng cách vào **Users -> `stephane` -> tab Access Advisor**. Công cụ này hiển thị những dịch vụ nào đã được user truy cập và vào lúc nào (ví dụ: IAM, EC2 vừa được truy cập, còn Alexa for Business chưa từng được dùng), đồng thời chỉ rõ policy nào đã cấp quyền đó để bạn tinh chỉnh quyền hạn tối thiểu. |
