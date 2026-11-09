# Phần 4: IAM & AWS CLI

- **Khóa học:** Ultimate AWS Certified Solutions Architect Associate 2026 (`SAA-C03`)
- **Chapter ID:** `6258010`
- **Tổng số bài giảng:** 20 bài giảng (Bài 11 -> Bài 30) + 1 bài kiểm tra trắc nghiệm (Quiz 1)
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## Tóm tắt nhanh các dịch vụ trong Phần 4 (Service Cheat Sheet)

### 1. AWS IAM (Identity and Access Management)
- **Là gì:** Dịch vụ toàn cầu (Global service) quản lý danh tính người dùng và phân quyền truy cập an toàn vào các tài nguyên AWS.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Cấp quyền theo nguyên tắc đặc quyền tối thiểu (**Least Privilege**) cho người dùng (`IAM Users` / `IAM Groups`).
  - Cho phép một dịch vụ AWS (như `EC2`, `Lambda`, `ECS`) truy cập dịch vụ AWS khác (như `S3`, `DynamoDB`) mà **không cần lưu trữ Access Keys trong code** bằng cách dùng **`IAM Roles`**.
  - Kiểm toán bảo mật tài khoản định kỳ bằng **IAM Credentials Report** (cấp Account) và **IAM Access Advisor** (cấp User/Role).
- **Khác gì dịch vụ gần giống:**
  - **IAM Policies vs. S3 Bucket Policies:** `IAM Policy` gắn vào **Identity** (User, Group, Role), còn `S3 Bucket Policy` là **Resource-based Policy** gắn trực tiếp vào tài nguyên (S3 Bucket) — phù hợp khi muốn chia sẻ quyền cross-account mà không cần Assume Role hoặc mở public bucket.
  - **IAM Roles vs. Access Keys:** `IAM Role` cấp **thông tin xác thực tạm thời (Temporary Credentials)** tự động xoay vòng qua STS; `Access Keys` là khóa dài hạn gắn với IAM User (tuyệt đối không nhúng vào ứng dụng chạy trên EC2/Lambda).
  - **IAM Credentials Report vs. IAM Access Advisor:** `Credentials Report` liệt kê tất cả Users trong Account cùng trạng thái mật khẩu/MFA/Access Keys; `Access Advisor` hiển thị các dịch vụ được cấp quyền cho 1 User/Role và **thời điểm truy cập gần nhất** (dùng để thu hồi quyền dư thừa).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** Mọi hành động (ngoài Root account) đều bị **Implicit Deny** cho đến khi có `Allow` tường minh; một lệnh **`Explicit Deny`** luôn ghi đè mọi lệnh `Allow`.
  - **Giới hạn / Quy tắc:** `IAM Groups` **chỉ chứa IAM Users** (không thể chứa Group khác — không hỗ trợ lồng nhau/nested groups); 1 User có thể thuộc nhiều Groups hoặc không thuộc Group nào.
  - **Từ khóa gợi ý:** `"without hardcoding credentials"`, `"grant EC2 access to S3"`, `"temporary security credentials"` $\rightarrow$ **IAM Role (Instance Profile)**; `"remove unused permissions"`, `"last accessed"` $\rightarrow$ **IAM Access Advisor**.

### 2. AWS CLI & AWS SDK
- **Là gì:** Bộ công cụ dòng lệnh (`AWS CLI`) và thư viện lập trình (`AWS SDK`) cho phép tương tác trực tiếp với các API công khai của AWS bằng mã lệnh.
- **Dùng khi nào (Use case điển hình trong đề):** Tự động hóa thao tác hạ tầng bằng script (`CLI`) hoặc tích hợp các lệnh gọi dịch vụ AWS ngay bên trong mã nguồn ứng dụng (`SDK`).
- **Khác gì dịch vụ gần giống:**
  - **AWS CLI trên máy cá nhân vs. AWS CloudShell:** Máy cá nhân cần tự cài đặt CLI và cấu hình `aws configure` với Access Keys; **AWS CloudShell** chạy ngay trên trình duyệt, đã xác thực sẵn theo phiên đăng nhập Console và có **1 GB bộ nhớ lưu trữ bền vững (`$HOME`)** theo từng Region.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** Nếu không chỉ định Region trong AWS SDK, một số SDK mặc định dùng **`us-east-1`**.
  - **Từ khóa gợi ý:** `"EC2 instance cannot call S3 via AWS CLI"` $\rightarrow$ Không bao giờ chạy `aws configure` điền Access Key lên EC2, mà phải gắn **IAM Role** cho EC2 instance.

---

## Danh sách bài học trong Phần 4

| STT | Lecture ID | Tên bài giảng | Loại | Thời lượng | Trạng thái |
| :---: | :---: | :--- | :---: | :---: | :--- |
| 11 | `26097996` | [IAM Introduction: Users, Groups, Policies](./11-iam-introduction-users-groups-policies.md) | Video | 03:22 | **Đã lưu** |
| 12 | `26098012` | [IAM Users & Groups Hands On](./12-iam-users-and-groups-hands-on.md) | Video | 06:23 | **Đã lưu** |
| 13 | `51960287` | [AWS Console Simultaneous Sign-in](./13-aws-console-simultaneous-sign-in.md) | Video | 01:48 | **Đã lưu** |
| 14 | `26623458` | [IAM Policies](./14-iam-policies.md) | Video | 02:50 | **Đã lưu** |
| 15 | `26098018` | [IAM Policies Hands On](./15-iam-policies-hands-on.md) | Video | 08:01 | **Đã lưu** |
| 16 | `26098020` | [IAM MFA Overview](./16-iam-mfa-overview.md) | Video | 04:10 | **Đã lưu** |
| 17 | `26098028` | [IAM MFA Hands On](./17-iam-mfa-hands-on.md) | Video | 04:01 | **Đã lưu** |
| 18 | `26098034` | [AWS Access Keys, CLI and SDK](./18-aws-access-keys-cli-and-sdk.md) | Video | 04:03 | **Đã lưu** |
| 19 | `13528246` | [AWS CLI Setup on Windows](./19-aws-cli-setup-on-windows.md) | Video | 01:45 | **Đã lưu** |
| 20 | `13528248` | [AWS CLI Setup on Mac OS X](./20-aws-cli-setup-on-mac-os-x.md) | Video | 01:28 | **Đã lưu** |
| 21 | `13528250` | [AWS CLI Setup on Linux](./21-aws-cli-setup-on-linux.md) | Video | 01:30 | **Đã lưu** |
| 22 | `26098056` | [AWS CLI Hands On](./22-aws-cli-hands-on.md) | Video | 03:50 | **Đã lưu** |
| 23 | `26207478` | [AWS CloudShell: Region Availability](./23-aws-cloudshell-region-availability.md) | Article | 00:12 | **Đã lưu** |
| 24 | `26098060` | [AWS CloudShell](./24-aws-cloudshell.md) | Video | 03:53 | **Đã lưu** |
| 25 | `26098066` | [IAM Roles for AWS Services](./25-iam-roles-for-aws-services.md) | Video | 01:39 | **Đã lưu** |
| 26 | `26098068` | [IAM Roles Hands On](./26-iam-roles-hands-on.md) | Video | 02:05 | **Đã lưu** |
| 27 | `26098070` | [IAM Security Tools](./27-iam-security-tools.md) | Video | 00:54 | **Đã lưu** |
| 28 | `26098074` | [IAM Security Tools Hands On](./28-iam-security-tools-hands-on.md) | Video | 02:23 | **Đã lưu** |
| 29 | `26098082` | [IAM Best Practices](./29-iam-best-practices.md) | Video | 01:29 | **Đã lưu** |
| 30 | `26098086` | [IAM Summary](./30-iam-summary.md) | Video | 01:05 | **Đã lưu** |
| Quiz 1 | `5334490` | [IAM & AWS CLI Quiz](./quiz-01-iam-and-aws-cli-quiz.md) | Quiz | 9 câu | **Đã lưu** |
