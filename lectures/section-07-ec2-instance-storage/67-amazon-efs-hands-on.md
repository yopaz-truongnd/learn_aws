# Bài 67: Amazon EFS - Hands On

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `13528130`
- **Video gốc:** `SAA_-_EFS_-_Hands_On_v6.mp4`
- **Thời lượng:** `13:05`
- **Cheat sheet:** [topics/aws_storage.html](../../topics/aws_storage.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Tóm tắt quy trình thực hành tạo và mount EFS lên nhiều EC2 ở các AZ khác nhau
1. **Tạo EFS File System (Customize):**
   - **File system type:** Chọn **Regional** (Multi-AZ cho Production) thay vì *One Zone* (Single AZ cho Dev).
   - **Automatic backups:** Bật (`Enabled`).
   - **Lifecycle management:**
     - Chuyển sang **IA (Infrequent Access):** `30 days since last access`.
     - Chuyển sang **Archive:** `90 days since last access`.
     - Chuyển ngược về **Standard:** `On first access` (ngay trong lần truy cập đầu tiên).
   - **Encryption:** Bật mã hóa dữ liệu tĩnh (`Enable encryption of data at rest`).
   - **Throughput mode:** Chọn **Enhanced -> Elastic** (khuyến nghị cho tải không đoán trước được; hoặc chọn *Provisioned* hay *Bursting*).
   - **Performance mode:** **General Purpose** (hoặc *Max I/O* khi dùng Bursting/Provisioned).
   - **Network access (Mount Targets):** Chọn Default VPC, tạo các Mount Targets tại cả 3 AZs (`eu-west-1a`, `eu-west-1b`, `eu-west-1c`) gắn kèm Security Group.
2. **Khởi chạy 2 EC2 Instances ở 2 AZ khác nhau và tự động Mount EFS:**
   - Tạo **Instance A** ở `eu-west-1a` và **Instance B** ở `eu-west-1b` (Amazon Linux 2, `t2.micro`).
   - Trong phần **Configure storage -> File systems -> Edit -> EFS**: Chọn hệ thống tệp EFS vừa tạo.
   - Điểm gắn (Mount point): `/mnt/efs/fs1`.
   - Tích chọn **Automatically create and attach security groups** và **Automatically mount shared file system by attaching required user data script**:
     - AWS tự động tạo Security Group mở cổng **TCP 2049 (NFS)** cho phép EC2 truy cập vào EFS Mount Targets, và tự động điền script User Data để mount ổ mạng `/mnt/efs/fs1` lúc khởi động.
3. **Kiểm chứng chia sẻ dữ liệu xuyên AZ:**
   - Trên **Instance A (`eu-west-1a`)**: Chạy lệnh `sudo su` rồi `echo "hello world" > /mnt/efs/fs1/hello.txt`.
   - Trên **Instance B (`eu-west-1b`)**: Chạy lệnh `cat /mnt/efs/fs1/hello.txt` -> hiển thị ngay lập tức nội dung `"hello world"`, chứng minh cả 2 EC2 ở 2 AZ khác nhau đang đọc/ghi chung trên cùng một hệ thống tệp mạng EFS!

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So let's go ahead and practice using the Amazon Elastic File System Service. | Bây giờ hãy cùng thực hành sử dụng dịch vụ **Amazon Elastic File System (EFS)**. |
| `00:00:05` | So let's create our file system and here we can give it an optional name, but I'll leave it empty and we have to choose a VPC where we want to connect to our file system. | Chúng ta nhấn **Create file system**; ở đây có thể đặt tên (không bắt buộc) và chọn VPC nơi chúng ta muốn kết nối tới hệ thống tệp này. |
| `00:00:13` | So we'll leave it as the default VPC as well, and we could just click on create and be done. But I wanna show you the options. So let's click on Customize. | Chúng ta giữ nguyên Default VPC, và thay vì bấm Create ngay, hãy nhấn vào **Customize** để xem chi tiết tất cả các tùy chọn. |
| `00:00:24` | Next, we need to choose a file system type. So we have two options. We have Regional, which gives you a file system within the region across multiple availability zones, which gives you very high availability and durability of the data. | Tiếp theo chúng ta chọn **File system type** với 2 tùy chọn: **Regional** giúp lưu trữ hệ thống tệp qua nhiều Availability Zones (Multi-AZ) trong Region, mang lại độ sẵn sàng và độ bền dữ liệu rất cao. |
| `00:00:37` | But if you need to reduce costs, you could use the One Zone option, in which case you have to choose one specific availability zone. And this is going to be good for development environments | Còn nếu muốn giảm chi phí, bạn có thể chọn **One Zone** (chỉ nằm trong 1 AZ cụ thể), phù hợp cho môi trường Development nhưng không tốt cho Production vì nếu AZ đó gặp sự cố thì dữ liệu sẽ không truy cập được. |
| `00:00:53` | So definitely, you want to use Regional in production settings and we'll use Regional right now for this hands-on. | Vì vậy trong môi trường Production bạn luôn nên dùng **Regional**, và chúng ta cũng sẽ chọn Regional cho bài thực hành này. |
| `00:00:59` | Next we can enable or disable automatic backups, but it's recommended to keep it enabled. | Tiếp theo là tính năng **Automatic backups** (Sao lưu tự động), được khuyến nghị giữ nguyên trạng thái bật. |
| `00:01:04` | Next we have lifecycle management. So this is to move data across different storage tiers to save costs. | Tiếp đến là **Lifecycle management** (Quản lý vòng đời) để tự động chuyển dữ liệu giữa các tầng lưu trữ nhằm tiết kiệm chi phí. |
| `00:01:12` | So it turns out that you can transition into Infrequent Access or Archive and then back to Standard. | Bạn có thể cấu hình chuyển tệp sang tầng **Infrequent Access (IA)**, tầng **Archive**, và chuyển ngược về **Standard**. |
| `00:01:18` | So we're saying that hey, if a file hasn't been accessed for 30 days, then move it to the Infrequent Access storage tier and it's going to be cheaper for you except when you access the file. | Ví dụ mặc định ở đây: nếu một tệp không được truy cập trong **30 ngày**, hệ thống sẽ chuyển nó sang tầng **Infrequent Access (IA)** có chi phí lưu trữ rẻ hơn. |
| `00:01:37` | And then if the file was not accessed, for example, in 90 days since the last access, then moving into the Archive, which is going to be even cheaper as a storage class. | Và nếu tệp đó tiếp tục không được truy cập trong **90 ngày**, nó sẽ được chuyển xuống tầng **Archive** có chi phí lưu trữ còn rẻ hơn nữa. |
| `00:01:47` | And then for example, you say that here when the file is accessed the first time, so `On first access`, transition back into Standard because for example, we assume that it's going to be reused a lot more. | Đồng thời ở tùy chọn Transition into Standard, nếu chọn **`On first access`**, ngay khi tệp được mở lại lần đầu tiên nó sẽ được chuyển ngược về tầng Standard. |
| `00:02:01` | So we can keep this on as is. Encryption, we leave it enabled, that's perfect. | Chúng ta giữ nguyên phần Lifecycle và giữ bật **Encryption** (mã hóa dữ liệu tĩnh). |
| `00:02:06` | And then we have performance settings. So for performance settings we have throughput mode and you should have three options: Bursting, Elastic, and Provisioned. | Tiếp theo là **Performance settings**. Ở mục **Throughput mode**, thực chất chúng ta có 3 chế độ chính: **Bursting**, **Elastic** và **Provisioned** (trong giao diện mới, Elastic và Provisioned được gom dưới nhóm *Enhanced*). |
| `00:02:25` | So let's start with Bursting. Bursting is a way for you to have the throughput scale with the amount of storage you're actually using and going a little bit over. | Với **Bursting**, thông lượng sẽ tăng tỷ lệ thuận theo dung lượng lưu trữ bạn đang dùng (1 TB có thông lượng cao hơn 1 GB) kèm khả năng bứt tốc ngắn hạn. |
| `00:02:44` | Then there is Enhanced mode, and now **Elastic** is recommended, which is saying: Hey, regardless of the size of your EFS file system, we're going to give you all the I/O you need and we'll scale automatically and you're going to only pay for what you use. | Với **Elastic** (chế độ được khuyến nghị): bất kể kích thước hệ thống tệp EFS của bạn lớn hay nhỏ, AWS sẽ cung cấp toàn bộ thông lượng I/O bạn cần, tự động co giãn và bạn chỉ trả tiền cho mức thực tế sử dụng — lý tưởng nhất cho các tải không đoán trước được (**unpredictable I/O**). |
| `00:03:15` | And the last one is **Provisioned**. This is when you know in advance the throughput you're going to be needing. | Và chế độ thứ ba là **Provisioned**: dùng khi bạn biết chắc chắn trước mức thông lượng mình cần (ví dụ cố định 100 MB/s) và trả tiền trước cho mức thông lượng đã cấp phát đó. |
| `00:03:39` | And then if you look at the additional settings, we have **General Purpose** and **Max I/O**. | Mở phần **Additional settings (Performance mode)**, chúng ta có **General Purpose** (độ trễ thấp cho đa số ứng dụng, là tùy chọn duy nhất khi dùng Elastic throughput) và **Max I/O** (chấp nhận độ trễ cao hơn để đổi lấy tổng thông lượng song song tối đa cho Big Data khi dùng Bursting/Provisioned). |
| `00:04:21` | Okay, let's click on Next now. Next we have the network access settings and they're very important, we have to choose a VPC. | Nhấn **Next** để sang bước **Network access**. Chúng ta chọn Default VPC, và vì chọn kiểu Regional nên hệ thống tạo ra các **Mount targets** tại cả 3 AZs (`eu-west-1a`, `eu-west-1b`, `eu-west-1c`). |
| `00:05:05` | And we need to assign a security group. So I'll go into the EC2 console and then I will go into Security Groups. I will create a security group and I will call it `EFS demo`. | Chúng ta cần gán một Security Group cho các Mount targets này. Tôi sang EC2 Console tạo một Security Group tên là `EFS demo` (tạm thời chưa cần thêm Inbound rule nào) rồi gắn vào cả 3 Mount targets của EFS. |
| `00:06:10` | I will click on Next. We have a file system policy that is optional and we will not touch it right now. I will click on Next, review and click on Create. | Nhấn **Next** bỏ qua phần File system policy (không bắt buộc), xem lại cấu hình và nhấn **Create**. |
| `00:06:30` | My file system is now available and I can go in it and see that there is six kilobytes of size that is being used right now. And when you have an EFS file system, you only pay for the storage you use, so right now my costs are zero. | Hệ thống tệp EFS hiện đã ở trạng thái `Available`, dung lượng ban đầu chỉ là 6 KB nên chi phí lúc này gần như bằng 0. |
| `00:06:46` | And now we want to mount this onto EC2 instances. So let's launch some instance. And I will name this one `Instance A`, because we will launch it in subnet of AZ A (`eu-west-1a`). | Bây giờ chúng ta sẽ khởi chạy 2 EC2 instances để mount hệ thống tệp EFS này lên. Chiếc đầu tiên đặt tên là **`Instance A`**, chọn Amazon Linux 2, `t2.micro`, không dùng key pair (để kết nối qua EC2 Instance Connect). |
| `00:07:52` | So we go to Network Settings, we Edit it, and in subnet I'm going to choose `eu-west-1a`. | Trong phần **Network settings**, tôi chọn Subnet thuộc **`eu-west-1a`**. |
| `00:08:00` | So now that my subnet is selected, I can go back into Configure storage -> File systems -> Edit. And as you can see, I can add an EFS or an FSx file system. | Tiếp theo ở phần **Configure storage**, bấm **Edit** tại mục **File systems**, nhấn **Add shared file system** và chọn loại **EFS** cùng hệ thống tệp EFS vừa tạo. |
| `00:08:16` | The mount point is `/mnt/efs/fs1`. This is going to automatically create and attach security groups for us, which is amazing. And then it's automatically going to mount shared file system by attaching the required user data scripts. | Đường dẫn mount mặc định là **`/mnt/efs/fs1`**. Rất tuyệt vời là EC2 Console hiện nay có 2 ô tích chọn tự động: **Automatically create and attach security groups** và **Automatically mount shared file system by attaching required user data script**. Nhấn **Launch instance** để khởi chạy `Instance A`. |
| `00:08:56` | I'm going to launch a new one. I will call this one `Instance B`. Amazon Linux 2, proceed without a key pair, I will go into `eu-west-1b`. | Tiếp theo tôi khởi chạy chiếc máy thứ hai đặt tên là **`Instance B`**, đặt tại Subnet thuộc **`eu-west-1b`** (khác AZ với Instance A), và cũng gắn cùng hệ thống tệp EFS vào đường dẫn `/mnt/efs/fs1` tương tự như trên. |
| `00:09:48` | So now they're both running. And the interesting thing is that if we go into the EFS console and go to the Network tab, each availability zone now has multiple security groups (`efs-sg-1`, `efs-sg-2`). | Khi cả hai máy đã chạy (`Running`), nếu kiểm tra tab **Network** của EFS và kiểm tra Security Group `efs-sg-1`/`efs-sg-2` do AWS tự tạo, bạn sẽ thấy Inbound rule mở giao thức **NFS trên cổng 2049** cho phép lưu lượng từ Security Group của EC2 đi vào EFS. |
| `00:10:53` | So now if I go into one of these instances, we're going to connect using EC2 Instance Connect on this tab, and then connecting to `Instance B` over EC2 Instance Connect. | Bây giờ tôi mở 2 tab kết nối vào cả `Instance A` và `Instance B` thông qua **EC2 Instance Connect**. |
| `00:11:12` | So now I can verify that in `ls /mnt/efs/fs1` there is an EFS file system. I will type `sudo su` and then `echo "hello world" > /mnt/efs/fs1/hello.txt`. | Trên **`Instance A` (`eu-west-1a`)**, tôi chuyển sang quyền root bằng `sudo su` và tạo một tệp tin bằng lệnh: `echo "hello world" > /mnt/efs/fs1/hello.txt`. Khi kiểm tra bằng `cat /mnt/efs/fs1/hello.txt`, nội dung hiển thị là `hello world`. |
| `00:11:54` | But now if I go into my second EC2 instance (`Instance B` in `eu-west-1b`) and do `ls /mnt/efs/fs1`, we also see this `hello.txt` file in it! And if I do `cat /mnt/efs/fs1/hello.txt`, it says `hello world` as well! | Bây giờ chuyển sang cửa sổ của **`Instance B` (`eu-west-1b`)**, khi gõ `ls /mnt/efs/fs1`, chúng ta thấy ngay tệp `hello.txt` xuất hiện ở đó! Và khi gõ `cat /mnt/efs/fs1/hello.txt`, nó cũng in ra `hello world`! |
| `00:12:12` | So as you can see, the EFS file system is indeed mounted as a network drive onto both my EC2 instances and they are in different AZs and they share the same EFS. | Như bạn thấy, hệ thống tệp EFS thực sự đã được gắn làm ổ đĩa mạng dùng chung cho cả 2 EC2 instances nằm ở 2 Availability Zones khác nhau! |
| `00:12:31` | Now to just clean it up, you can terminate these two EC2 instances, go into the EFS file system and delete it, and delete the extra security groups. | Để dọn dẹp sau khi thực hành, bạn hãy Terminate 2 EC2 instances, xóa hệ thống tệp EFS và xóa các Security Groups đã tạo. Hẹn gặp lại bạn ở bài học tiếp theo! |
