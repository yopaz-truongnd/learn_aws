# Bài 26: IAM Roles Hands On

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098068` (`CCP_-_IAM_-_Roles_Hands_On_v3.mp4`)
- **Thời lượng:** `02:05`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### Quy trình tạo một IAM Role cho dịch vụ AWS (ví dụ EC2)
1. Vào **IAM Console -> Roles -> Create role**.
2. **Bước 1 — Chọn Trusted Entity Type (Loại thực thể tin cậy):**
   - Chọn **AWS service** (phổ biến nhất cho kỳ thi SAA-C03).
   - Chọn dịch vụ sẽ đảm nhận (assume) role này: ví dụ chọn **EC2** (Use case: `EC2`).
3. **Bước 2 — Add Permissions (Gắn Policy):**
   - Chọn Policy cần cấp cho EC2 Instance, ví dụ: **`IAMReadOnlyAccess`** (cho phép EC2 đọc thông tin IAM).
4. **Bước 3 — Name, review, and create:**
   - Đặt tên Role: `DemoRoleForEC2`.
   - Kiểm tra phần **Trusted entities** (`ec2.amazonaws.com` được phép assume role này) và nhấn **Create role**.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:02` | Let's practice creating an IAM Role. On the left menu, click **Roles -> Create role**. A role gives AWS entities permissions to do things on AWS. For the exam and this hands-on, choose **AWS service** as the trusted entity type, and under Use case select **EC2** (you can create roles for EC2, Lambda, or almost any AWS service). | Hãy thực hành tạo IAM Role. Vào menu **Roles -> Create role**. Trong phần Trusted entity type, chọn **AWS service**, và ở mục Use case chọn **EC2** (bạn có thể tạo role cho EC2, Lambda hoặc hầu hết mọi dịch vụ trên AWS). |
| `01:02` - `02:05` | Click Next and attach a permissions policy — here we attach **`IAMReadOnlyAccess`** to allow our future EC2 instance to read IAM data. Click Next, name the role `DemoRoleForEC2`, verify that the trusted entity is the EC2 service (`ec2.amazonaws.com`) and the policy is `IAMReadOnlyAccess`, then click **Create role**. We will use this role when we get to the EC2 section. | Nhấn Next và chọn gắn policy **`IAMReadOnlyAccess`** để cho phép EC2 Instance đọc dữ liệu IAM. Nhấn Next, đặt tên role là `DemoRoleForEC2`, kiểm tra Trusted entity là dịch vụ EC2 rồi nhấn **Create role**. Chúng ta sẽ gắn role này vào EC2 trong chương tiếp theo. |
