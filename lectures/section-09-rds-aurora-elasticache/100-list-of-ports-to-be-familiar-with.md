# Bài 100: List of Ports to be familiar with (Danh sách các cổng mạng cần làm quen)

- **Phần (Section):** Section 9: AWS Fundamentals: RDS + Aurora + ElastiCache
- **Bài học (Lecture):** #100 (`id: 18630414`)
- **Loại bài học:** Bài viết (Article)
- **Thời lượng ước tính:** `00:29` (29 giây)

---

## 1. Nội dung bài viết & Kiến thức trọng tâm (Exam Notes)

Dưới đây là danh sách các cổng (ports) tiêu chuẩn mà bạn nên xem qua ít nhất một lần. Bạn không cần học thuộc lòng máy móc từng số cổng (đề thi sẽ không đánh đố bạn theo kiểu nhớ vẹt số cổng), nhưng **bạn cần phân biệt được đâu là cổng giao thức mạng quan trọng (như HTTPS - cổng `443`) và đâu là cổng của cơ sở dữ liệu RDS (như PostgreSQL - cổng `5432`)** khi đọc cấu hình Security Group hoặc Network ACL trong đề thi.

### 1.1. Các cổng giao thức mạng quan trọng (Important Ports)

| Giao thức (Protocol) | Cổng (Port) | Ghi chú |
| :--- | :---: | :--- |
| **FTP** (File Transfer Protocol) | `21` | Truyền tệp tin tiêu chuẩn |
| **SSH** (Secure Shell) | `22` | Đăng nhập dòng lệnh từ xa vào Linux EC2 |
| **SFTP** (Secure File Transfer Protocol) | `22` | Truyền tệp tin bảo mật qua SSH (dùng chung cổng `22` với SSH) |
| **HTTP** | `80` | Lưu lượng web không mã hóa |
| **HTTPS** | `443` | Lưu lượng web được mã hóa SSL/TLS |
| **RDP** (Remote Desktop Protocol) | `3389` | *(Bổ sung từ phần EC2)* Đăng nhập giao diện từ xa vào Windows EC2 |

### 1.2. Các cổng cơ sở dữ liệu RDS & ElastiCache (RDS Databases Ports)

| Hệ quản trị Cơ sở dữ liệu (Database Engine) | Cổng mặc định (Port) | Ghi chú |
| :--- | :---: | :--- |
| **PostgreSQL** | `5432` | RDS PostgreSQL |
| **MySQL** | `3306` | RDS MySQL |
| **MariaDB** | `3306` | Dùng chung cổng `3306` với MySQL |
| **Oracle RDS** | `1521` | RDS for Oracle |
| **Microsoft SQL Server (MSSQL)** | `1433` | RDS for SQL Server |
| **Amazon Aurora (PostgreSQL-compatible)** | `5432` | Dùng cổng của PostgreSQL |
| **Amazon Aurora (MySQL-compatible)** | `3306` | Dùng cổng của MySQL |
| **ElastiCache (Redis / Memcached)** | `6379` / `11211` | *(Bổ sung tham khảo)* Redis (`6379`), Memcached (`11211`) |

> [!TIP]
> **Lời khuyên từ giảng viên Stéphane Maarek:**
> *"Đừng căng thẳng việc phải học thuộc lòng các con số này, chỉ cần đọc qua danh sách này một lần hôm nay và một lần trước khi bước vào phòng thi là bạn đã hoàn toàn sẵn sàng. Hãy nhớ rằng bạn chỉ cần phân biệt được đâu là 'Important Port' (như `22`, `80`, `443`) và đâu là 'RDS Database Port' (như `3306`, `5432`, `1433`, `1521`)."*
