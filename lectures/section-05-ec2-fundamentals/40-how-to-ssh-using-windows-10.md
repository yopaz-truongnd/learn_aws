# Bài 40: How to SSH using Windows 10

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `16560336` (`CCP_-_EC2_-_SSH_Windows_10_v2.mp4`)
- **Thời lượng:** `05:01`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Sử dụng lệnh `ssh` tích hợp sẵn trên Windows 10 / 11
- Mở **PowerShell** hoặc **Command Prompt**, di chuyển tới thư mục chứa file khóa `.pem` (ví dụ `cd .\Desktop`) và chạy lệnh giống hệt như trên Mac/Linux:
  ```powershell
  ssh -i .\EC2Tutorial.pem ec2-user@<Public-IPv4-Address>
  ```

### 1.2. Cách xử lý lỗi quyền truy cập file `.pem` (Permission Issues) trên Windows
Nếu Windows báo lỗi `WARNING: UNPROTECTED PRIVATE KEY FILE!` (tương tự lỗi cần `chmod 0400` trên Linux/Mac), thực hiện như sau:
1. Nhấp chuột phải vào file `EC2Tutorial.pem` -> Chọn **Properties** -> Tab **Security** -> Nhấn **Advanced**.
2. Đảm bảo mục **Owner** là tài khoản người dùng Windows hiện tại của bạn.
3. Nhấn nút **Disable inheritance** -> Chọn **Remove all inherited permissions from this object**.
4. Nhấn **Add** -> **Select a principal** -> Nhập tên user Windows của bạn -> **Check Names** -> OK -> Cấp quyền **Full control** -> Nhấn **OK** để lưu lại (chỉ giữ lại duy nhất tài khoản của bạn trong danh sách quyền, loại bỏ `SYSTEM` và `Administrators`).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:27` | On Windows 10+, you can use the built-in `ssh` command in **PowerShell** or **Command Prompt**. Navigate to the directory where your `.pem` file is stored (e.g., `cd .\Desktop`) and run `ssh -i .\EC2Tutorial.pem ec2-user@<Public-IPv4>`. Type `yes` when prompted, and you are connected to the EC2 instance. | Trên Windows 10 trở lên, bạn có thể dùng lệnh `ssh` có sẵn trong **PowerShell** hoặc **Command Prompt**. Di chuyển tới thư mục chứa file `.pem` (ví dụ `cd .\Desktop`) và chạy lệnh `ssh -i .\EC2Tutorial.pem ec2-user@<Public-IPv4>`, gõ `yes` để kết nối vào máy ảo EC2. |
| `02:27` - `05:01` | If you get a key file permission error on Windows: right-click `EC2Tutorial.pem` -> **Properties** -> **Security** tab -> **Advanced**. Verify you are the **Owner**, click **Disable inheritance** -> **Remove all inherited permissions from this object**, then click **Add** -> **Select a principal**, enter your Windows username, grant **Full control**, and click OK so only your user has access to the `.pem` file. | Nếu gặp lỗi quyền truy cập file `.pem` trên Windows: chuột phải vào file `EC2Tutorial.pem` -> **Properties -> Security -> Advanced**. Đảm bảo bạn là **Owner**, nhấn **Disable inheritance -> Remove all inherited permissions**, sau đó nhấn **Add -> Select a principal**, nhập tên user Windows của bạn và cấp quyền **Full control** (chỉ một mình user của bạn có quyền trên file đó). |
