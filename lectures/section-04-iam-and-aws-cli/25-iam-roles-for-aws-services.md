# Bài 25: IAM Roles for AWS Services

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098066` (`CCP_-_IAM_-_Roles.mp4`)
- **Thời lượng:** `01:39`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. IAM Role là gì và khác gì với IAM User?
- Nhiều dịch vụ AWS (như máy chủ ảo **EC2 Instance**, hàm **AWS Lambda**, hay **CloudFormation**) cần thực hiện các hành động (gọi API) trên tài khoản AWS thay mặt cho bạn.
- Để làm được điều đó, dịch vụ AWS cũng cần được cấp quyền (Permissions).
- **Quy tắc cốt lõi:**
  - **IAM User** dành cho **con người vật lý (physical people)**.
  - **IAM Role** dành cho **các dịch vụ AWS (AWS services)** (không có mật khẩu cố định hay Access Keys lâu dài gắn cứng).
  - **KHÔNG BAO GIỜ** lưu Access Keys cá nhân vào bên trong EC2 Instance; thay vào đó, hãy tạo một **IAM Role** và gắn vào EC2 Instance.

```mermaid
flowchart LR
    subgraph Entity ["Một thực thể hợp nhất (One Entity)"]
        EC2["EC2 Instance (Virtual Server)"] --- Role["IAM Role (Permissions Policy)"]
    end
    Role -->|Gọi API (ví dụ đọc IAM / S3)| AWS["AWS Services (IAM, S3, DynamoDB...)"]
```

### 1.2. Các loại IAM Roles phổ biến
- **EC2 Instance Roles**
- **Lambda Function Roles**
- **Roles for CloudFormation**

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:38` | The last component of IAM is **IAM Roles**. Some AWS services will need to perform actions on your behalf. To do so, we assign permissions to AWS services using an **IAM Role**. IAM Roles are just like users, except they are intended to be used **not by physical people, but by AWS services**. | Thành phần cuối cùng của IAM là **IAM Roles**. Một số dịch vụ AWS cần thực hiện các hành động thay mặt chúng ta. Để cấp quyền cho các dịch vụ AWS, ta tạo **IAM Role**. IAM Role giống như một user nhưng **không dành cho con người thật sử dụng, mà dành cho các dịch vụ AWS**. |
| `00:38` - `01:39` | For example, an **EC2 Instance** (a virtual server) may want to perform actions on AWS. We create an IAM Role and attach it to the EC2 Instance so they form one entity. When the EC2 Instance tries to access AWS information, it uses the IAM Role, and if the role has the right permissions, the call succeeds. Common roles include EC2 Instance Roles, Lambda Function Roles, and CloudFormation Roles. | Ví dụ: một máy chủ ảo **EC2 Instance** muốn gọi API truy cập thông tin trên AWS. Ta tạo một IAM Role và gắn vào EC2 Instance đó. Khi EC2 Instance truy cập AWS, nó sẽ sử dụng quyền được cấp trong IAM Role. Các role phổ biến nhất gồm: EC2 Instance Roles, Lambda Function Roles và CloudFormation Roles. |
