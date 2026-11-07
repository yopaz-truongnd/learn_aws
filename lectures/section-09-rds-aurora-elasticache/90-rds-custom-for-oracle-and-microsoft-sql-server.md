# Bài 90: RDS Custom for Oracle and Microsoft SQL Server (RDS Custom cho Oracle và MS SQL Server)

- **Phần (Section):** Section 9: AWS Fundamentals: RDS + Aurora + ElastiCache
- **Bài học (Lecture):** #90 (`id: 33878670`)
- **Video gốc:** `SAA_-_RDS_-_RDS_Custom_v1.mp4`
- **Thời lượng:** `01:49` (109 giây)

---

## 1. Kiến thức trọng tâm (Exam Notes)

> [!TIP]
> **Tóm tắt nhanh dịch vụ — Amazon RDS Custom (SAA-C03 Cheat Sheet)**
> - **Là gì (1 câu):** Phiên bản RDS đặc biệt dành cho **Oracle** và **Microsoft SQL Server** cho phép quản trị viên truy cập trực tiếp vào hệ điều hành bên dưới (OS root/admin access) và tùy biến sâu cơ sở dữ liệu trong khi vẫn giữ các tính năng tự động hóa của RDS.
> - **Dùng khi nào:** Cần di chuyển các ứng dụng đóng gói cũ (Legacy / COTS applications như SharePoint, Oracle E-Business Suite) lên AWS mà ứng dụng đó bắt buộc phải có quyền **SSH/RDP (Admin/Root) vào OS**, cài đặt custom patches hoặc truy cập file hệ thống trên máy chủ DB.
> - **Khác gì dịch vụ gần giống:**
>   - **RDS Custom vs RDS tiêu chuẩn vs Database trên EC2:** **RDS tiêu chuẩn** khóa hoàn toàn quyền truy cập OS/SSH; **Database tự cài trên EC2** cho toàn quyền OS nhưng bạn phải tự lo 100% backup/patching/HA; **RDS Custom** đứng ở giữa — vừa tự động hóa quản trị như RDS, vừa mở quyền truy cập OS/DB sâu khi cần (bằng cách tạm tắt Automation Mode).
> - **Điểm hay bị hỏi:**
>   - **Giới hạn & Mặc định:** **CHỈ hỗ trợ 2 engines duy nhất: Oracle và Microsoft SQL Server** (không có RDS Custom cho MySQL, PostgreSQL, MariaDB hay Aurora). Trước khi can thiệp OS, nên bật **Pause Automation Mode** (tối đa 24 giờ) để tác vụ tự động của RDS không ghi đè thay đổi của bạn.
>   - **Từ khóa gợi ý:** `"underlying OS access / SSH / RDP / root privilege"`, `"Oracle or SQL Server legacy/custom application"`, `"managed database with OS customization"`.

### 1.1. Amazon RDS Custom là gì?
- Thông thường với Amazon RDS chuẩn, bạn **không có quyền truy cập** vào hệ điều hành (OS) bên dưới hoặc tùy chỉnh sâu bên trong cơ sở dữ liệu.
- **Amazon RDS Custom** là dịch vụ cơ sở dữ liệu được quản lý (Managed DB) nhưng **cho phép truy cập đầy đủ (Full Admin Access) vào hệ điều hành (OS) và môi trường cơ sở dữ liệu bên dưới**.
- **Chỉ hỗ trợ 2 loại Database Engine duy nhất (Cực kỳ quan trọng cho kỳ thi):**
  1. **Oracle** (`RDS Custom for Oracle`)
  2. **Microsoft SQL Server** (`RDS Custom for SQL Server`)

### 1.2. Khả năng và Lưu ý vận hành của RDS Custom
- Bạn vẫn nhận được các lợi ích tự động hóa của RDS (Automated setup, operations, scaling), đồng thời có thể:
  - Cấu hình các thiết lập nội bộ (Configure internal settings).
  - Cài đặt các bản vá (Install patches) và bật các tính năng gốc (Enable native features) đòi hỏi quyền quản trị viên.
  - Truy cập trực tiếp vào **EC2 instance bên dưới** thông qua **SSH** hoặc **AWS Systems Manager (SSM) Session Manager**.
- **Lưu ý thực hành tốt nhất (Best Practices) khi tùy chỉnh trên RDS Custom:**
  1. **Tắt chế độ tự động hóa (Deactivate Automation Mode)** trước khi thực hiện tùy chỉnh để ngăn RDS chạy các tác vụ tự động bảo trì hay mở rộng (scaling) làm xung đột với quá trình tùy chỉnh của bạn.
  2. **Chụp một bản Database Snapshot trước khi tùy chỉnh**, vì bạn có quyền can thiệp sâu vào EC2 instance bên dưới nên có nguy cơ làm hỏng hệ thống.

### 1.3. Bảng so sánh RDS chuẩn vs RDS Custom

| Tiêu chí | Amazon RDS (Chuẩn) | Amazon RDS Custom |
| :--- | :--- | :--- |
| **Quản lý OS & DB** | AWS quản lý toàn bộ 100% | AWS quản lý tự động hóa + **User có quyền Full Admin vào OS & DB** |
| **Truy cập SSH / SSM** | **Không** | **Có** (SSH hoặc SSM Session Manager vào EC2 bên dưới) |
| **Engine hỗ trợ** | PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Db2, Aurora | **Chỉ hỗ trợ Oracle và Microsoft SQL Server** |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00.450 --> 00:00:03.600` | So now let's do a short lecture on RDS Custom. | Bây giờ hãy cùng đến với một bài giảng ngắn về RDS Custom. |
| `00:00:03.600 --> 00:00:12.930` | So, we know that with RDS we don't have access to any underlying operating system, or customization, but with RDS Custom we actually do. | Chúng ta biết rằng với RDS thông thường, chúng ta không có quyền truy cập vào hệ điều hành bên dưới hay tùy chỉnh hệ thống, nhưng với RDS Custom thì chúng ta hoàn toàn có thể. |
| `00:00:12.930 --> 00:00:25.080` | And RDS Custom is for two database types, it's for Oracle and Microsoft SQL Server. In which, thanks to RDS Custom, we have access to the OS, and database customization. | RDS Custom chỉ dành cho hai loại cơ sở dữ liệu là **Oracle** và **Microsoft SQL Server**. Nhờ RDS Custom, chúng ta có quyền truy cập vào hệ điều hành (OS) và tùy chỉnh cơ sở dữ liệu. |
| `00:00:25.080 --> 00:00:32.010` | So with RDS, we still get all the benefits of automated setup, operations, and scaling of the database in AWS. | Với RDS Custom, chúng ta vẫn nhận được mọi lợi ích từ việc thiết lập tự động, vận hành và mở rộng cơ sở dữ liệu trên AWS. |
| `00:00:32.010 --> 00:00:39.810` | But with the RDS Custom option, the custom part of RDS Custom, we actually have access to the underlying database and operating system. | Nhưng với phần "Custom" của RDS Custom, chúng ta thực sự có quyền truy cập vào cơ sở dữ liệu và hệ điều hành bên dưới. |
| `00:00:39.810 --> 00:00:53.790` | So we can actually configure internal settings, install patches, enable native features, and we can actually access the underlying EC2 instance behind RDS, using SSH or SSM Session Manager. | Vì vậy, chúng ta có thể cấu hình các cài đặt nội bộ, cài đặt các bản vá, bật các tính năng gốc (native features), và truy cập trực tiếp vào EC2 instance bên dưới RDS bằng SSH hoặc SSM Session Manager. |
| `00:00:53.790 --> 00:01:02.400` | So here is my EC2 instance, and as a user, we can now, if it's using Amazon RDS Custom, apply customizations and SSH into it. | Đây là EC2 instance của tôi, và với tư cách người dùng, nếu đang sử dụng Amazon RDS Custom, giờ đây chúng ta có thể áp dụng các tùy chỉnh và SSH vào đó. |
| `00:01:02.400 --> 00:01:14.280` | To perform any customization it is recommended to deactivate the automation mode, so that RDS does not perform any automation, or maintenance, or scaling, or whatever you want, while you perform your customization. | Để thực hiện bất kỳ tùy chỉnh nào, khuyến nghị bạn nên tắt chế độ tự động hóa (deactivate automation mode), để RDS không thực hiện bất kỳ tác vụ tự động, bảo trì hay mở rộng nào trong lúc bạn đang tùy chỉnh. |
| `00:01:14.280 --> 00:01:25.830` | And also because you may actually break things, because now you have access to the underlying EC2 instance, it is much better to take a database snapshot, otherwise you will not be able to recover from your actions. | Và cũng bởi vì bạn có thể vô tình làm hỏng hệ thống do đã có quyền truy cập vào EC2 instance bên dưới, tốt nhất bạn nên chụp một bản database snapshot trước, nếu không bạn sẽ không thể khôi phục lại từ các thao tác của mình. |
| `00:01:25.830 --> 00:01:35.070` | So to summarize, RDS versus RDS Custom. RDS will manage your entire database, and your operating system. Everything is managed by AWS, you don't have to do anything, | Tóm lại, khi so sánh RDS và RDS Custom: RDS quản lý toàn bộ cơ sở dữ liệu và hệ điều hành của bạn, mọi thứ đều do AWS quản lý và bạn không phải làm gì cả; |
| `00:01:35.070 --> 00:01:45.000` | and RDS Custom, it's for Oracle and Microsoft SQL Server only, and you have actually full admin access to the underlying operating system and the database. | còn RDS Custom chỉ dành cho Oracle và Microsoft SQL Server, và bạn có toàn quyền quản trị (full admin access) vào hệ điều hành cũng như cơ sở dữ liệu bên dưới. |
| `00:01:45.000 --> 00:01:49.113` | So that's it for this lecture, I hope you liked it, and I will see you in the next lecture. | Đó là tất cả cho bài giảng này, hy vọng bạn thích nó, và hẹn gặp lại bạn ở bài giảng tiếp theo. |
