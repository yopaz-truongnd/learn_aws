# Section 7: EC2 Instance Storage
- **Cheat sheet:** [topics/aws_storage.html](../../topics/aws_storage.html)

---

## Tóm tắt nhanh các dịch vụ lưu trữ trong Phần 7 (Service Cheat Sheet)

### 1. Amazon EBS (Elastic Block Store) & EBS Snapshots
- **Là gì:** Dịch vụ ổ cứng mạng dạng khối (**Network Block Storage**) gắn vào EC2 instance tại **1 Availability Zone (AZ)** cụ thể, cho phép dữ liệu tồn tại độc lập ngay cả khi EC2 bị xóa.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Làm ổ đĩa hệ điều hành (Root volume) hoặc ổ đĩa dữ liệu có độ bền cao cho cơ sở dữ liệu tự cài trên EC2.
  - Chọn loại ổ đĩa theo yêu cầu hiệu năng:
    - **`gp2` / `gp3` (General Purpose SSD):** Cân bằng chi phí & hiệu năng (`gp3` cho phép chỉnh IOPS và Throughput độc lập với dung lượng).
    - **`io1` / `io2` / `io2 Block Express` (Provisioned IOPS SSD):** Ứng dụng quan trọng (mission-critical) cần **trên 16.000 IOPS** (lên tới 64.000 – 256.000 IOPS) hoặc cần tính năng **EBS Multi-Attach** (gắn 1 ổ đĩa vào tối đa 16 EC2 instances trong cùng 1 AZ).
    - **`st1` (Throughput Optimized HDD) & `sc1` (Cold HDD):** Lưu trữ dữ liệu tuần tự lớn (Big Data, Data Warehouse) hoặc ít truy cập với chi phí thấp (**KHÔNG THỂ làm Boot/Root Volume**).
- **Khác gì dịch vụ gần giống:**
  - **EBS vs. EC2 Instance Store:** `EBS` là ổ đĩa mạng (network drive) bền vững qua các lần Stop/Start; `Instance Store` là ổ cứng vật lý gắn trực tiếp vào máy chủ host, mang lại **IOPS cực đại** nhưng là bộ nhớ tạm (**Ephemeral** — mất sạch dữ liệu nếu EC2 bị `Stop` hoặc phần cứng lỗi).
  - **EBS vs. EFS:** `EBS` gắn với **1 AZ** và mặc định chỉ gắn cho **1 EC2 instance** (trừ `io1/io2` Multi-Attach trong 1 AZ); `EFS` là hệ thống tệp mạng (NFS) chia sẻ đồng thời cho **hàng trăm EC2 instances trải rộng trên nhiều AZs**.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Mặc định:** Khi Terminate EC2: **Root EBS Volume mặc định bị xóa** (`Delete on Termination = Yes`), còn các **Additional EBS Volumes mặc định được giữ lại** (`Delete on Termination = No`).
  - **Ràng buộc AZ:** Một EBS Volume tạo ở `us-east-1a` **không thể** gắn trực tiếp cho EC2 ở `us-east-1b` — phải tạo **EBS Snapshot** rồi khôi phục (Restore) thành Volume mới tại `us-east-1b`.
  - **Tính năng bảo vệ Snapshot:** Dùng **Recycle Bin** để khôi phục Snapshot bị xóa nhầm (từ 1 ngày đến 1 năm) và **Fast Snapshot Restore (FSR)** để loại bỏ độ trễ khởi tạo lần đầu cho Volume lớn.

### 2. EC2 Instance Store
- **Là gì:** Ổ đĩa cứng vật lý gắn trực tiếp trên máy chủ vật lý chứa EC2 instance, cung cấp hiệu năng đọc/ghi I/O cực cao nhưng dữ liệu mang tính tạm thời (Ephemeral).
- **Dùng khi nào (Use case điển hình trong đề):**
  - Lưu trữ bộ đệm (**buffer, cache**), dữ liệu nháp (**scratch data**), tệp tạm thời hoặc dữ liệu đã được nhân bản tự động sang các node khác trong cụm mà yêu cầu **IOPS cực cao / độ trễ đĩa thấp nhất**.
- **Khác gì dịch vụ gần giống:**
  - Khác với `EBS` (ổ đĩa mạng bền vững), `Instance Store` **mất toàn bộ dữ liệu khi EC2 bị `Stop`, `Hibernate` hoặc `Terminate`** (nhưng vẫn giữ được dữ liệu khi `Reboot`).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Từ khóa gợi ý:** `"very high IOPS / hardware disk performance"`, `"temporary / ephemeral / scratch data / cache"`, `"data can be recreated if lost"` $\rightarrow$ **EC2 Instance Store**.

### 3. Amazon Machine Image (AMI)
- **Là gì:** Bản đóng gói mẫu (template) chứa hệ điều hành, cấu hình, phần mềm cài sẵn và dữ liệu ổ đĩa dùng để khởi tạo nhanh các EC2 instances giống hệt nhau.
- **Dùng khi nào (Use case điển hình trong đề):**
  - **Tăng tốc thời gian khởi động (Faster boot time)** cho Auto Scaling Group bằng cách cài đặt sẵn toàn bộ phần mềm vào **Golden AMI** thay vì chạy script `EC2 User Data` lâu mỗi khi scale out.
  - Sao chép cấu hình máy chủ sang Region khác (**Copy AMI Cross-Region**).
- **Khác gì dịch vụ gần giống:**
  - **AMI vs. EC2 User Data:** `User Data` tải và cài đặt phần mềm lúc máy mới bật (chậm hơn); `AMI` đóng gói sẵn phần mềm đã cài đặt vào image (khởi động nhanh nhất).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Giới hạn:** AMI **bị ràng buộc theo từng Region (Region-scoped)** — muốn khởi chạy EC2 từ một AMI ở Region khác, bạn phải **Copy AMI** sang Region đích trước.

### 4. Amazon EFS (Elastic File System)
- **Là gì:** Hệ thống lưu trữ tệp mạng được quản lý hoàn toàn (**Managed NFS - Network File System**) có thể gắn kết (mount) đồng thời lên hàng trăm máy chủ **Linux EC2** across **Multiple AZs**.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Chia sẻ tệp tin chung (Content Management System như WordPress, chia sẻ code/media) giữa nhiều EC2 instances chạy **Linux** trải rộng trên nhiều Availability Zones với yêu cầu POSIX-compliant.
- **Khác gì dịch vụ gần giống:**
  - **EFS vs. EBS:** `EFS` là File Storage (NFSv4) chia sẻ **Multi-AZ** cho nhiều Linux instances; `EBS` là Block Storage chỉ nằm trong **1 AZ**.
  - **EFS vs. Amazon S3:** `EFS` được mount như một thư mục hệ thống tệp POSIX trên OS; `S3` là Object Storage truy cập qua REST API/HTTP.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Giới hạn hệ điều hành:** EFS **chỉ hỗ trợ các máy chủ dựa trên Linux (POSIX)** — **KHÔNG hỗ trợ Windows** (nếu đề bài nhắc tới Windows File Share SMB, phải chọn **Amazon FSx for Windows File Server**).
  - **Tối ưu chi phí:** Bật **EFS Lifecycle Management** để tự động chuyển các tệp không truy cập sau $N$ ngày sang tầng **EFS Standard-IA (Infrequent Access)** hoặc dùng **EFS One Zone** cho môi trường dev/test để tiết kiệm tới 90% chi phí.
  - **Từ khóa gợi ý:** `"shared POSIX file system"`, `"mounted across multiple Linux EC2 instances in multiple AZs"` $\rightarrow$ **Amazon EFS**.

---

## Danh sách các bài giảng trong Section 7

| STT | Lecture ID | Tên bài học | Thời lượng | Trạng thái |
| :-: | :---: | :--- | :---: | :---: |
| 56 | `26098272` | [EBS Overview](./56-ebs-overview.md) | 04:47 | **Đã lưu** |
| 57 | `26098274` | [EBS Hands On](./57-ebs-hands-on.md) | 05:34 | **Đã lưu** |
| 58 | `26098276` | [EBS Snapshots](./58-ebs-snapshots.md) | 02:08 | **Đã lưu** |
| 59 | `26098278` | [EBS Snapshots - Hands On](./59-ebs-snapshots-hands-on.md) | 03:38 | **Đã lưu** |
| 60 | `26098280` | [AMI Overview](./60-ami-overview.md) | 02:45 | **Đã lưu** |
| 61 | `26098284` | [AMI Hands On](./61-ami-hands-on.md) | 04:59 | **Đã lưu** |
| 62 | `26098288` | [EC2 Instance Store](./62-ec2-instance-store.md) | 02:47 | **Đã lưu** |
| 63 | `26098296` | [EBS Volume Types](./63-ebs-volume-types.md) | 04:34 | **Đã lưu** |
| 64 | `26098298` | [EBS Multi-Attach](./64-ebs-multi-attach.md) | 01:45 | **Đã lưu** |
| 65 | `13528122` | [EBS Encryption](./65-ebs-encryption.md) | 03:47 | **Đã lưu** |
| 66 | `13528128` | [Amazon EFS](./66-amazon-efs.md) | 05:18 | **Đã lưu** |
| 67 | `13528130` | [Amazon EFS - Hands On](./67-amazon-efs-hands-on.md) | 13:05 | **Đã lưu** |
| 68 | `13528138` | [EFS vs EBS](./68-efs-vs-ebs.md) | 02:11 | **Đã lưu** |
| 69 | `13528132` | [EBS & EFS - Section Cleanup](./69-ebs-and-efs-section-cleanup.md) | 01:31 | **Đã lưu** |
| Quiz 4 | `5334520` | [EC2 Instance Storage and Data Management Quiz (9 Questions)](./quiz-04-ec2-data-management-quiz.md) | 9 câu hỏi | **Đã lưu** |
