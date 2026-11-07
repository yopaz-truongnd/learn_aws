# Bài 30: IAM Summary

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098086` (`CCP_-_IAM_-_Summary_v2.mp4`)
- **Thời lượng:** `01:05`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### Tổng kết toàn bộ kiến thức Chương 4 (IAM & AWS CLI)
- **IAM Users:** Ánh xạ tới từng nhân sự thực tế trong công ty; có mật khẩu để đăng nhập vào AWS Management Console.
- **IAM Groups:** Chứa các Users (chỉ chứa Users, không chứa Groups khác) để quản lý quyền tập trung.
- **IAM Policies:** Tài liệu JSON định nghĩa quyền hạn (Permissions) cho Users, Groups hoặc Roles.
- **IAM Roles:** Danh tính có gắn quyền hạn dành cho các dịch vụ AWS (như EC2 Instances, Lambda) thực hiện hành động thay mặt bạn.
- **Bảo mật (Security):** Bật **MFA (Multi-Factor Authentication)** và thiết lập **Password Policy**.
- **AWS CLI & AWS SDK:** Quản lý dịch vụ AWS qua dòng lệnh (CLI) hoặc qua ngôn ngữ lập trình (SDK) bằng cách sử dụng **Access Keys**.
- **Kiểm toán (Auditing):** Sử dụng **IAM Credentials Report** (cấp Account) và **IAM Access Advisor** (cấp User).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:37` | Here is a summary for IAM: **Users** map to actual physical users and have a password for the AWS Console. **Groups** group users together (users only). **Policies** are JSON documents outlining permissions for users or groups. **Roles** are identities for EC2 instances or other AWS services. For security, enable **MFA** and set a **Password Policy**. | Tóm tắt về IAM: **Users** tương ứng với người dùng thật và có mật khẩu vào Console. **Groups** gom nhóm các users (chỉ chứa users). **Policies** là tài liệu JSON quy định quyền cho users/groups. **Roles** là danh tính dành cho EC2 hoặc các dịch vụ AWS khác. Về bảo mật, hãy bật **MFA** và thiết lập **Password Policy**. |
| `00:37` - `01:05` | Use the **CLI** to manage AWS services via command line, or the **SDK** using a programming language, authenticated with **Access Keys**. Finally, audit IAM usage with the **IAM Credentials Report** and **IAM Access Advisor**. | Sử dụng **CLI** để quản lý dịch vụ AWS qua dòng lệnh hoặc **SDK** qua ngôn ngữ lập trình, xác thực bằng **Access Keys**. Cuối cùng, kiểm toán việc sử dụng IAM bằng **IAM Credentials Report** và **IAM Access Advisor**. |
