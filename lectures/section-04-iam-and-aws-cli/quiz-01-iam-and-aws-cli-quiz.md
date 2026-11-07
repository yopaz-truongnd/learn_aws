# Quiz 1: IAM & AWS CLI Quiz

- **Phần:** Phần 4: IAM & AWS CLI
- **Quiz ID:** `5334490`
- **Số lượng câu hỏi:** 9 câu hỏi trắc nghiệm

---

## Câu hỏi 1
**What is a proper definition of an IAM Role?**
*(Định nghĩa nào sau đây là đúng về một IAM Role?)*

- [ ] A. IAM Users in multiple User Groups
- [ ] B. An IAM entity that defines a password policy for IAM Users
- [x] **C. An IAM entity that defines a set of permissions for making requests to AWS services, and will be used by an AWS service**
- [ ] D. Permissions assigned to IAM Users to perform actions

> **Giải thích:** Một số dịch vụ AWS cần thực hiện hành động thay mặt bạn. Để làm vậy, bạn gán quyền cho các dịch vụ AWS thông qua **IAM Roles**.

---

## Câu hỏi 2
**Which of the following is an IAM Security Tool?**
*(Công cụ nào sau đây là một Công cụ Bảo mật của IAM?)*

- [x] **A. IAM Credentials Report**
- [ ] B. IAM Root Account Manager
- [ ] C. IAM Services Report
- [ ] D. IAM Security Advisor

> **Giải thích:** **IAM Credentials Report** liệt kê tất cả IAM Users trong tài khoản AWS của bạn cùng trạng thái các thông tin xác thực của họ (ngoài ra công cụ thứ hai là **IAM Access Advisor**). Các tên ở đáp án B, C, D không tồn tại.

---

## Câu hỏi 3
**Which answer is INCORRECT regarding IAM Users?**
*(Phát biểu nào sau đây là **SAI** về IAM Users?)*

- [ ] A. IAM Users can belong to multiple User Groups
- [ ] B. IAM Users don't have to belong to a User Group
- [ ] C. IAM Policies can be attached directly to IAM Users
- [x] **D. IAM Users access AWS services using root account credentials**

> **Giải thích:** IAM Users truy cập dịch vụ AWS bằng **thông tin xác thực riêng của chính họ** (Username & Password hoặc Access Keys), tuyệt đối không dùng thông tin đăng nhập của Root account.

---

## Câu hỏi 4
**Which of the following is an IAM best practice?**
*(Điều nào sau đây là thực hành tốt nhất trong IAM?)*

- [ ] A. Create several IAM Users for one physical person
- [x] **B. Don't use the root user account**
- [ ] C. Share your AWS account credentials with your colleague, so (s)he can perform a task for you
- [ ] D. Do not enable MFA for easier access

> **Giải thích:** Chỉ sử dụng tài khoản Root để tạo IAM User đầu tiên và một vài tác vụ quản trị cấp tài khoản đặc biệt. Với mọi công việc hàng ngày, hãy sử dụng IAM User.

---

## Câu hỏi 5
**What are IAM Policies?**
*(IAM Policies là gì?)*

- [ ] A. A set of policies that defines how AWS accounts interact with each other
- [x] **B. JSON documents that define a set of permissions for making requests to AWS services, and can be used by IAM Users, User Groups, and IAM Roles**
- [ ] C. A set of policies that define a password for IAM Users
- [ ] D. A set of policies defined by AWS that show how customers interact with AWS

> **Giải thích:** IAM Policies là các tài liệu định dạng **JSON** định nghĩa tập hợp các quyền để gửi yêu cầu tới các dịch vụ AWS, được gắn cho IAM Users, User Groups và IAM Roles.

---

## Câu hỏi 6
**Which principle should you apply regarding IAM Permissions?**
*(Bạn nên áp dụng nguyên tắc nào đối với quyền hạn trong IAM?)*

- [ ] A. Grant most privilege
- [ ] B. Grant more permissions if your employee asks you to
- [x] **C. Grant least privilege**
- [ ] D. Restrict root account permissions

> **Giải thích:** Áp dụng nguyên tắc đặc quyền tối thiểu (**Grant least privilege**): không cấp cho người dùng nhiều quyền hơn mức họ cần để hoàn thành công việc. (Lưu ý: bạn không thể giới hạn quyền của Root account).

---

## Câu hỏi 7
**What should you do to increase your root account security?**
*(Bạn nên làm gì để tăng cường bảo mật cho tài khoản Root?)*

- [ ] A. Remove permissions from the root account
- [ ] B. Only access AWS services through AWS Command Line Interface (CLI)
- [ ] C. Don't create IAM Users, only access your AWS account using the root account
- [x] **D. Enable Multi-Factor Authentication (MFA)**

> **Giải thích:** Bật **MFA** giúp bổ sung thêm một lớp bảo mật. Ngay cả khi mật khẩu bị đánh cắp hoặc bị lộ, tài khoản của bạn vẫn không bị xâm nhập.

---

## Câu hỏi 8
**IAM User Groups can contain IAM Users and other User Groups.**
*(IAM User Groups có thể chứa cả IAM Users và các User Groups khác. Đúng hay Sai?)*

- [ ] A. True
- [x] **B. False**

> **Giải thích:** **Sai (False)**. IAM User Groups **chỉ có thể chứa IAM Users**, không thể chứa các User Groups khác.

---

## Câu hỏi 9
**An IAM policy consists of one or more statements. A statement in an IAM Policy consists of the following, EXCEPT:**
*(Một IAM Policy bao gồm một hoặc nhiều câu lệnh Statement. Một Statement trong IAM Policy bao gồm các thành phần sau, **NGOẠI TRỪ**:)*

- [ ] A. Effect
- [ ] B. Principal
- [x] **C. Version**
- [ ] D. Action
- [ ] E. Resource

> **Giải thích:** Một `Statement` trong IAM Policy bao gồm `Sid`, `Effect`, `Principal`, `Action`, `Resource` và `Condition`. Thuộc tính **`Version`** nằm ở cấp độ ngoài cùng của chính IAM Policy chứ không nằm bên trong `Statement`.
