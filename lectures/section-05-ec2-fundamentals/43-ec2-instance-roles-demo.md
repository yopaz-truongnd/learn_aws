# Bài 43: EC2 Instance Roles Demo

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098166` (`CCP_-_EC2_-_IAM_Roles_Hands_On_v2.mp4`)
- **Thời lượng:** `04:19`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Quy tắc bảo mật vàng trên EC2 Instance
- Khi kết nối vào bên trong EC2 Instance (Amazon Linux 2 đã cài sẵn AWS CLI) và chạy lệnh `aws iam list-users`, hệ thống báo lỗi: `Unable to locate credentials. You can configure credentials by running "aws configure"`.
- **TUYỆT ĐỐI KHÔNG BAO GIỜ chạy `aws configure` và nhập Access Key ID / Secret Access Key cá nhân vào bên trong EC2 Instance!**
  - *Lý do:* Bất kỳ ai khác trong công ty có quyền SSH / EC2 Instance Connect vào máy ảo đó đều có thể đọc file thông tin xác thực và đánh cắp toàn bộ quyền hạn của bạn.
- **Giải pháp chuẩn duy nhất:** Gắn một **IAM Role** vào EC2 Instance (**Instance Profile**).

### 1.2. Cách gắn và thay đổi IAM Role cho EC2 đang chạy
1. Trên EC2 Console: Chọn Instance -> **Actions -> Security -> Modify IAM role**.
2. Chọn IAM Role đã tạo (ví dụ: `DemoRoleForEC2` có gắn policy `IAMReadOnlyAccess`) -> Nhấn **Update IAM role / Save**.
3. Ngay lập tức (không cần khởi động lại EC2 và không cần chạy `aws configure`), chạy lệnh `aws iam list-users` bên trong EC2 trả về đầy đủ danh sách người dùng IAM!
4. Nếu gỡ bỏ policy `IAMReadOnlyAccess` khỏi Role `DemoRoleForEC2`, lệnh `aws iam list-users` trên EC2 lập tức bị từ chối (`AccessDenied`).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:12` | Let's practice using IAM Roles with our EC2 instance. Connect to the instance using EC2 Instance Connect. Amazon Linux 2 comes with the AWS CLI pre-installed. If we run `aws iam list-users`, it says `Unable to locate credentials. You can configure credentials by running "aws configure"`. **NEVER run `aws configure` or enter your IAM Access Keys inside an EC2 instance!** Anyone else who connects to that EC2 instance could steal your credentials. Instead, always use **IAM Roles**. | Hãy thực hành sử dụng IAM Roles cho EC2 instance. Sau khi kết nối vào máy ảo bằng EC2 Instance Connect, thử chạy lệnh `aws iam list-users`, hệ thống báo chưa có thông tin xác thực và gợi ý chạy `aws configure`. **TUYỆT ĐỐI KHÔNG BAO GIỜ chạy `aws configure` hay nhập Access Keys vào trong EC2 instance**, vì bất kỳ ai truy cập vào máy ảo đều có thể lấy cắp khóa của bạn. Thay vào đó, hãy luôn dùng **IAM Roles**. |
| `02:12` - `04:19` | In the EC2 Console, select the instance -> **Actions -> Security -> Modify IAM role**, select `DemoRoleForEC2` (which has `IAMReadOnlyAccess` attached), and click **Save**. Now back in the EC2 terminal, running `aws iam list-users` succeeds immediately without running `aws configure`! If we detach `IAMReadOnlyAccess` from the role in IAM, the command immediately returns `AccessDenied`, and re-attaching the policy restores access within a few seconds. | Trên EC2 Console, chọn instance -> **Actions -> Security -> Modify IAM role**, chọn `DemoRoleForEC2` (đã có quyền `IAMReadOnlyAccess`) và nhấn **Save**. Quay lại cửa sổ dòng lệnh của EC2, chạy `aws iam list-users` lập tức trả về kết quả mà không hề cần `aws configure`! Nếu gỡ quyền khỏi Role trong IAM, lệnh sẽ bị `AccessDenied` ngay, và khi gắn lại quyền thì lệnh chạy thành công trở lại. |
