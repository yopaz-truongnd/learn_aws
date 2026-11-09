# Bài 27: IAM Security Tools

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098070` (`CCP_-_IAM_-_Security_Tools.mp4`)
- **Thời lượng:** `00:54`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

Có **2 công cụ kiểm toán bảo mật (Security Tools) trong IAM** rất hay xuất hiện trong đề thi:

| Công cụ | Phạm vi (Level) | Chức năng chính |
| :--- | :---: | :--- |
| **1. IAM Credentials Report** *(Báo cáo thông tin xác thực)* | **Account-level** *(Cấp độ toàn tài khoản)* | Xuất ra một báo cáo (file `.csv`) liệt kê **tất cả các Users trong tài khoản** (bao gồm cả Root) cùng **trạng thái các thông tin xác thực của họ** (mật khẩu có bật không, đổi lần cuối khi nào, đã bật MFA chưa, Access Keys có tạo không và dùng lần cuối khi nào...). |
| **2. IAM Access Advisor** *(Cố vấn truy cập)* | **User-level** *(Cấp độ từng User)* | Hiển thị **các quyền dịch vụ (service permissions) đã được cấp cho một User cụ thể** và **thời điểm lần cuối cùng User đó truy cập vào từng dịch vụ**. Giúp rà soát các quyền không sử dụng để thu hồi theo **nguyên tắc đặc quyền tối thiểu (Least Privilege)**. |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:20` | Let's talk about the security tools we have in IAM. First, we can create an **IAM Credentials Report** at the **account-level**. This report contains all your account's users and the status of their various credentials. | Hãy tìm hiểu về các công cụ bảo mật trong IAM. Công cụ thứ nhất là **IAM Credentials Report** ở **cấp độ tài khoản (account-level)**. Báo cáo này liệt kê tất cả người dùng trong tài khoản cùng trạng thái thông tin xác thực của họ. |
| `00:20` - `00:54` | The second security tool is **IAM Access Advisor** at the **user-level**. Access Advisor shows the service permissions granted to a user and when those services were last accessed. Using this tool, you can see which permissions are not used and reduce permissions to align with the **principle of least privilege**. | Công cụ thứ hai là **IAM Access Advisor** ở **cấp độ người dùng (user-level)**. Access Advisor cho biết các quyền dịch vụ đã cấp cho một user và thời điểm lần cuối các dịch vụ đó được truy cập. Nhờ đó, bạn biết được quyền nào không được dùng tới để cắt giảm theo đúng **nguyên tắc đặc quyền tối thiểu (Least Privilege)**. |
