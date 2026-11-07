# Quiz 4: EC2 Instance Storage and Data Management Quiz

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Quiz ID:** `5334520`
- **Số lượng câu hỏi:** `9 câu`

---

## Câu hỏi 1
**You have just terminated an EC2 instance in `us-east-1a`, and its attached EBS volume is now available. Your teammate tries to attach it to an EC2 instance in `us-east-1b` but he can't. What is a possible cause for this?**

*(Bạn vừa Terminate một EC2 instance ở `us-east-1a`, và ổ đĩa EBS gắn kèm hiện đang ở trạng thái `available`. Đồng nghiệp của bạn cố gắn ổ đĩa này vào một EC2 instance ở `us-east-1b` nhưng không được. Nguyên nhân có thể là gì?)*

- [ ] A. He's missing IAM permissions
- [ ] B. EBS volumes are locked to an AWS Region
- [x] **C. EBS volumes are locked to an Availability Zone** *(Các ổ đĩa EBS bị khóa chặt vào một Availability Zone cụ thể)*

> **Giải thích:**
> - Các ổ đĩa **EBS Volumes** được tạo cho một **Availability Zone (AZ) cụ thể** và không thể gắn trực tiếp sang một AZ khác. Để di chuyển một ổ EBS giữa các AZ khác nhau, bạn phải chụp một bản **EBS Snapshot** rồi khôi phục (restore) thành ổ EBS mới tại AZ đích.

---

## Câu hỏi 2
**You have launched an EC2 instance with two EBS volumes, Root volume type and the other EBS volume type to store the data. A month later you are planning to terminate the EC2 instance. What's the default behavior that will happen to each EBS volume?**

*(Bạn đã khởi chạy một EC2 instance với 2 ổ đĩa EBS: một ổ Root volume và một ổ EBS phụ dùng để lưu trữ dữ liệu. Một tháng sau bạn dự định Terminate chiếc EC2 instance này. Hành vi mặc định sẽ xảy ra với từng ổ đĩa EBS là gì?)*

- [ ] A. Both the root volume type and the EBS volume type will be deleted
- [x] **B. The Root volume type will be deleted and the EBS volume type will not be deleted** *(Ổ đĩa Root volume sẽ bị xóa và ổ đĩa EBS phụ sẽ không bị xóa)*
- [ ] C. The root volume type will not be deleted and the EBS volume type will be deleted
- [ ] D. Both the root volume type and the EBS volume type will not be deleted

> **Giải thích:**
> - Theo mặc định, ổ đĩa **Root volume** sẽ bị xóa khi EC2 bị Terminate vì thuộc tính **`Delete on Termination`** của nó được tích chọn (`Enabled`) mặc định.
> - Ngược lại, bất kỳ ổ đĩa **EBS gắn thêm** nào khác mặc định có thuộc tính **`Delete on Termination`** bị tắt (`Disabled`), nên chúng sẽ được giữ lại.

---

## Câu hỏi 3
**You can use an AMI in N.Virginia Region `us-east-1` to launch an EC2 instance in any AWS Region.**

*(Bạn có thể sử dụng trực tiếp một AMI ở Region N. Virginia `us-east-1` để khởi chạy một EC2 instance ở bất kỳ AWS Region nào khác.)*

- [ ] A. True *(Đúng)*
- [x] **B. False *(Sai)***

> **Giải thích:**
> - Các **AMIs** được xây dựng cho một **AWS Region cụ thể** và là duy nhất trong từng Region. Bạn không thể khởi chạy một EC2 instance bằng một AMI đang nằm ở Region khác, nhưng bạn có thể **sao chép (copy) AMI đó sang AWS Region đích** rồi sử dụng bản sao đó để khởi chạy EC2.

---

## Câu hỏi 4
**Which of the following EBS volume types can be used as boot volumes when you create EC2 instances?**

*(Những loại ổ đĩa EBS nào sau đây có thể được sử dụng làm ổ đĩa khởi động (boot volumes) khi bạn tạo các EC2 instances?)*

- [ ] A. `gp2`, `gp3`, `st1`, `sc1`
- [x] **B. `gp2`, `gp3`, `io1`, `io2`**
- [ ] C. `io1`, `io2`, `st1`, `sc1`

> **Giải thích:**
> - Khi tạo các EC2 instances, bạn chỉ có thể sử dụng các loại ổ đĩa EBS dòng SSD sau làm **Boot volumes**: **`gp2`, `gp3`, `io1`, `io2`** (và chuẩn Magnetic Standard cũ). Hai dòng ổ HDD là `st1` và `sc1` không thể làm ổ khởi động.

---

## Câu hỏi 5
**What is EBS Multi-Attach?**

*(Tính năng EBS Multi-Attach là gì?)*

- [ ] A. Attach the same EBS volume to multiple EC2 instances in multiple AZs
- [ ] B. Attach multiple EBS volumes in the same AZ to the same EC2 instance
- [x] **C. Attach the same EBS volume to multiple EC2 instances in the same AZ** *(Gắn cùng một ổ đĩa EBS vào nhiều EC2 instances trong cùng một Availability Zone)*
- [ ] D. Attach multiple EBS volumes in multiple AZs to the same EC2 instance

> **Giải thích:**
> - Với **EBS Multi-Attach** (chỉ hỗ trợ trên dòng `io1` và `io2`), bạn có thể gắn **cùng một ổ đĩa EBS** vào tối đa **16 EC2 instances nằm trong CÙNG một Availability Zone (same AZ)**. Mỗi EC2 instance đều có toàn quyền đọc/ghi (full read/write permissions).

---

## Câu hỏi 6
**You would like to encrypt an unencrypted EBS volume attached to your EC2 instance. What should you do?**

*(Bạn muốn mã hóa một ổ đĩa EBS hiện chưa được mã hóa đang gắn trên EC2 instance của mình. Bạn nên làm gì?)*

- [x] **A. Create an EBS snapshot of your EBS volume. Copy the snapshot and tick the option to encrypt the copied snapshot. Then, use the encrypted snapshot to create a new EBS volume** *(Tạo một bản EBS snapshot của ổ đĩa EBS. Sao chép bản snapshot đó và tích chọn mã hóa bản sao. Sau đó dùng bản snapshot đã mã hóa để tạo một ổ đĩa EBS mới)*
- [ ] B. Select your EBS volume, choose **Edit Attributes**, then tick the **Encrypt using KMS** option
- [ ] C. Create a new encrypted EBS volume, then copy data from your unencrypted EBS volume to the new EBS volume.
- [ ] D. Submit a request to AWS Support to encrypt your EBS volume

> **Giải thích:**
> - Bạn không thể bật mã hóa trực tiếp trên một ổ EBS đang tồn tại. Quy trình chuẩn của AWS là chụp **EBS Snapshot** từ ổ chưa mã hóa -> **Copy Snapshot** kèm tùy chọn **Encrypt** (hoặc chọn **Create Volume from Snapshot** kèm tùy chọn **Encrypt**) để tạo ra ổ EBS mới đã được mã hóa rồi gắn vào EC2.

---

## Câu hỏi 7
**You have a fleet of EC2 instances distributed across AZs that process a large data set. What do you recommend to make the same data to be accessible as an NFS drive to all of your EC2 instances?**

*(Bạn có một dàn máy chủ EC2 phân bổ qua nhiều Availability Zones cùng xử lý một tập dữ liệu lớn. Bạn khuyến nghị giải pháp nào để cùng một nguồn dữ liệu đó có thể được truy cập dưới dạng ổ đĩa mạng NFS bởi tất cả các EC2 instances của bạn?)*

- [ ] A. Use EBS
- [x] **B. Use EFS** *(Sử dụng Amazon EFS)*
- [ ] C. Use an Instance Store

> **Giải thích:**
> - **Amazon EFS (Elastic File System)** là hệ thống tệp tin mạng (**NFS**) cho phép bạn mount cùng một hệ thống tệp lên hàng trăm/hàng nghìn EC2 instances(Linux) nằm ở các Availability Zones khác nhau.
> - EBS bị khóa vào 1 AZ, còn Instance Store là ổ đĩa vật lý cục bộ của riêng từng máy chủ EC2.

---

## Câu hỏi 8
**You would like to have a high-performance local cache for your application hosted on an EC2 instance. You don't mind losing the cache upon the termination of your EC2 instance. Which storage mechanism do you recommend as a Solutions Architect?**

*(Bạn muốn có một bộ nhớ đệm cục bộ hiệu năng cao (high-performance local cache) cho ứng dụng chạy trên một EC2 instance. Bạn không ngại việc mất dữ liệu cache này khi EC2 instance bị Terminate. Với vai trò Solutions Architect, bạn khuyến nghị cơ chế lưu trữ nào?)*

- [ ] A. EBS
- [ ] B. EFS
- [x] **C. Instance Store** *(Sử dụng EC2 Instance Store)*

> **Giải thích:**
> - **EC2 Instance Store** là ổ đĩa gắn vật lý trực tiếp vào máy chủ host nên cung cấp hiệu năng đọc/ghi I/O ổ đĩa cao nhất, cực kỳ lý tưởng cho dữ liệu tạm thời như **local cache, buffer, scratch data** (dữ liệu sẽ mất khi Stop/Terminate instance).

---

## Câu hỏi 9
**You are running a high-performance database that requires an IOPS of 310,000 for its underlying storage. What do you recommend?**

*(Bạn đang vận hành một cơ sở dữ liệu hiệu năng cao đòi hỏi mức IOPS lên tới `310,000 IOPS` cho tầng lưu trữ bên dưới. Bạn khuyến nghị giải pháp nào?)*

- [ ] A. Use an EBS `gp2` drive
- [ ] B. Use an EBS `io1` drive
- [x] **C. Use an EC2 Instance Store** *(Sử dụng EC2 Instance Store)*
- [ ] D. Use an EBS `io2` Block Express drive

> **Giải thích:**
> - Mức IOPS tối đa của các dòng ổ đĩa mạng EBS là:
>   - `gp2`: tối đa **`16,000 IOPS`**.
>   - `io1` / `io2`: tối đa **`64,000 IOPS`** (trên Nitro EC2).
>   - `io2 Block Express`: tối đa **`256,000 IOPS`**.
> - Vì yêu cầu lên tới **`310,000 IOPS`** (vượt quá giới hạn `256,000 IOPS` của `io2 Block Express`), giải pháp duy nhất đáp ứng được là sử dụng **EC2 Instance Store** (có thể đạt tới hàng triệu IOPS, đi kèm cơ chế nhân bản/sao lưu dữ liệu ở tầng ứng dụng).
