# Bài 18: AWS Access Keys, CLI and SDK

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098034` (`CCP - IAM - Access Keys CLI SDK v2.mp4`)
- **Thời lượng:** `04:03`
- **Cheat sheet:** [topics/aws_iam.html](../../topics/aws_iam.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Ba phương thức để truy cập vào AWS

| Phương thức | Mục đích sử dụng | Thông tin xác thực bảo vệ |
| :--- | :--- | :--- |
| **1. AWS Management Console** | Giao diện web trực quan trên trình duyệt. | **Username + Password** (+ **MFA**). |
| **2. AWS CLI** *(Command Line Interface)* | Truy cập và quản lý dịch vụ AWS thông qua dòng lệnh trên terminal/shell; viết script tự động hóa. | **Access Keys** (`Access Key ID` + `Secret Access Key`). |
| **3. AWS SDK** *(Software Development Kit)* | Gọi AWS APIs trực tiếp từ bên trong mã nguồn ứng dụng (Application code). | **Access Keys** (`Access Key ID` + `Secret Access Key`) hoặc IAM Roles. |

### 1.2. Quản lý Access Keys an toàn
- **Access Keys** được tạo từ Management Console và do từng IAM User tự quản lý.
- **Nguyên tắc bảo mật sống còn:**
  - `Access Key ID` tương đương với **Username**.
  - `Secret Access Key` tương đương với **Password** (bí mật tuyệt đối).
  - **TUYỆT ĐỐI KHÔNG chia sẻ Access Keys** cho đồng nghiệp hay bất kỳ ai. Mỗi người phải có IAM User và Access Keys riêng.

### 1.3. AWS CLI vs. AWS SDK
- **AWS CLI:**
  - Công cụ dòng lệnh mã nguồn mở (open-source trên GitHub) bắt đầu bằng từ khóa `aws ...` (ví dụ: `aws s3 cp ...`).
  - Cho phép truy cập trực tiếp vào các **Public APIs** của các dịch vụ AWS.
- **AWS SDK:**
  - Bộ thư viện theo từng ngôn ngữ lập trình (JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++), Mobile SDK (Android, iOS) và IoT Device SDK.
  - Được nhúng (embed) trực tiếp vào bên trong ứng dụng của bạn.
  - *Fact thú vị:* Bản thân **AWS CLI** được xây dựng dựa trên **AWS SDK for Python** có tên là **`boto` (`botocore`)**.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:52` | There are three different options to access AWS: 1) **Management Console** (protected by username + password + MFA); 2) **AWS CLI (Command Line Interface)** on our computer terminal (protected by **Access Keys**); and 3) **AWS SDK (Software Development Kit)** whenever you want to call AWS APIs from within your application code (also protected by Access Keys). | Có 3 cách để truy cập AWS: 1) **Management Console** (giao diện web, bảo vệ bằng username + password + MFA); 2) **AWS CLI** trên terminal máy tính (bảo vệ bằng **Access Keys**); và 3) **AWS SDK** khi gọi AWS API từ bên trong code ứng dụng (cũng được bảo vệ bằng Access Keys). |
| `00:52` - `01:55` | Users generate their own Access Keys through the Management Console. Access keys are secret, just like a password — do not share them with colleagues! Treat your **Access Key ID** like your username and your **Secret Access Key** like your password. | Người dùng tự tạo Access Keys trên Management Console. Access Keys là thông tin mật giống hệt mật khẩu — tuyệt đối không chia sẻ cho đồng nghiệp! Hãy coi **Access Key ID** như username và **Secret Access Key** như password của bạn. |
| `01:55` - `02:50` | **AWS CLI** is a tool that allows you to interact with AWS services using commands from your command-line shell (every command starts with `aws`). It gives direct access to the public APIs of AWS services, lets you develop scripts to automate tasks, and is open-source on GitHub. | **AWS CLI** là công cụ cho phép tương tác với các dịch vụ AWS bằng câu lệnh trên shell/terminal (bắt đầu bằng từ khóa `aws`). Nó cung cấp quyền truy cập trực tiếp vào các Public APIs của AWS, giúp viết script tự động hóa và là mã nguồn mở trên GitHub. |
| `02:50` - `04:03` | **AWS SDK (Software Development Kit)** is a set of language-specific libraries embedded within your application code to access and manage AWS services programmatically. It supports JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++, Mobile SDKs (Android, iOS), and IoT Device SDKs. In fact, the AWS CLI itself is built on the AWS SDK for Python named **Boto**. | **AWS SDK** là bộ thư viện dành riêng cho từng ngôn ngữ lập trình, được nhúng vào trong ứng dụng để gọi AWS APIs bằng code. Hỗ trợ JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++, Mobile SDK (Android, iOS) và IoT Device SDK. Thực tế, chính công cụ AWS CLI được viết dựa trên AWS SDK cho Python tên là **Boto**. |
