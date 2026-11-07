# Bài 62: EC2 Instance Store

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `26098288`
- **Video gốc:** `CCP_-_EC2_-_Instance_Store.mp4`
- **Thời lượng:** `02:47`

---

## 1. Kiến thức trọng tâm (Exam Notes)

> [!TIP]
> **Tóm tắt nhanh dịch vụ — EC2 Instance Store (SAA-C03 Cheat Sheet)**
> - **Là gì (1 câu):** Ổ cứng vật lý gắn trực tiếp trên máy chủ host của EC2 (Ephemeral Block Storage), cung cấp hiệu năng đọc/ghi IOPS cực đại nhưng mất dữ liệu khi dừng máy.
> - **Dùng khi nào:** Cần hiệu năng đĩa cực cao (hàng triệu IOPS, độ trễ cực thấp) cho dữ liệu tạm thời: **buffer, cache, scratch data, temporary processing** hoặc hệ thống có cơ chế nhân bản dữ liệu sẵn giữa các nodes.
> - **Khác gì dịch vụ gần giống:**
>   - **EC2 Instance Store vs Amazon EBS:** **Instance Store** gắn vật lý vào host (IOPS cao nhất, **mất dữ liệu khi EC2 Stop/Hibernate/Terminate** hoặc lỗi phần cứng host); **EBS** là ổ đĩa mạng bền vững (giữ nguyên dữ liệu khi EC2 Stop).
> - **Điểm hay bị hỏi:**
>   - **Giới hạn & Mặc định:** Dữ liệu **vẫn còn khi Reboot OS**, nhưng **mất sạch khi Stop, Hibernate hoặc Terminate** EC2. Không thể tháo rời hay dùng AWS Snapshot tự động (trách nhiệm backup thuộc về người dùng).
>   - **Từ khóa gợi ý:** `"very high IOPS / millions of IOPS"`, `"ephemeral / temporary storage / scratch data / buffer / cache"`, `"data can be recreated if lost"`.

### 1.1. EC2 Instance Store là gì?
- **Bối cảnh:** EBS volumes là ổ đĩa mạng (network drives) có hiệu năng tốt nhưng vẫn bị giới hạn bởi băng thông và độ trễ mạng. Khi bạn cần **hiệu năng đọc/ghi phần cứng cực kỳ cao (very high I/O performance)**, bạn sử dụng **EC2 Instance Store**.
- **Định nghĩa:** **EC2 Instance Store** là ổ đĩa cứng vật lý (thường là NVMe SSD) được **gắn trực tiếp về mặt vật lý (physically attached)** vào máy chủ phần cứng (host server) đang chạy máy ảo EC2 của bạn.
- **Chênh lệch hiệu năng khủng khiếp (Ví dụ minh họa):**
  - Dòng máy `i3` / `i3en` sử dụng **Local EC2 Instance Store** có thể đạt tới **3.3 triệu Read IOPS** và **1.4 triệu Write IOPS**.
  - Trong khi đó, ổ đĩa mạng EBS `gp2` chỉ đạt tối đa `16,000 IOPS`, `io1`/`io2` đạt `64,000 IOPS` (hoặc `256,000 IOPS` với `io2 Block Express`).
  - **Mẹo thi SAA-C03:** Bất cứ khi nào đề bài yêu cầu **ổ đĩa gắn trực tiếp phần cứng có hiệu năng I/O cực cao** (ví dụ: cần `> 300,000 IOPS`) hoặc **bộ nhớ đệm cục bộ siêu nhanh (high-performance local cache)**, hãy chọn **EC2 Instance Store**.

---

### 1.2. Đặc điểm lưu trữ tạm thời (Ephemeral Storage) & Trách nhiệm sao lưu
- **Mất dữ liệu khi Stop hoặc Terminate (Ephemeral Storage):**
  - Nếu bạn **Stop (Dừng)**, **Hibernate**, hoặc **Terminate (Hủy)** EC2 instance, hoặc nếu máy chủ phần cứng vật lý bên dưới bị hỏng (hardware failure), **toàn bộ dữ liệu trên EC2 Instance Store sẽ BỊ MẤT (Lost)**.
  - *(Lưu ý: Nếu chỉ **Reboot / Restart** hệ điều hành thì dữ liệu trên Instance Store vẫn còn).*
- **Không dùng cho lưu trữ dài hạn:** Tuyệt đối không dùng Instance Store làm nơi lưu trữ bền vững lâu dài (hãy dùng EBS cho mục đích đó).
- **Trường hợp sử dụng tốt nhất (Best Use Cases):**
  - **Buffer (Bộ đệm)**, **Cache (Bộ nhớ đệm)**, **Scratch data (Dữ liệu nháp xử lý trung gian)**, **Temporary content (Nội dung tạm thời)**.
- **Trách nhiệm của người dùng:** Bạn phải tự chịu trách nhiệm sao lưu (**Backups**) và nhân bản dữ liệu (**Replication** sang EC2 khác) nếu muốn bảo vệ dữ liệu trên Instance Store.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So we've seen a way to attach a network drive onto our EC2 Instances but they have limited performance | Chúng ta đã thấy cách gắn một ổ đĩa mạng (EBS) vào các EC2 instances, nhưng chúng vẫn có giới hạn nhất định về hiệu năng. |
| `00:00:07` | and I said with cause because it's a really good performance but sometimes you want something even higher performance and that is going to be a hardware disk attached onto your EC2 Instance. | Hiệu năng của EBS thực ra đã rất tốt rồi, nhưng đôi khi bạn cần một thứ có hiệu năng còn cao hơn gấp nhiều lần — đó chính là một **ổ đĩa phần cứng (hardware disk)** gắn trực tiếp vào máy chủ chứa EC2 instance của bạn. |
| `00:00:18` | So the EC2 Instance is a virtual machine but it is obviously attached to a real hardware server. | EC2 instance là một máy ảo (virtual machine), nhưng hiển nhiên nó phải chạy trên một máy chủ phần cứng vật lý thực sự (physical server). |
| `00:00:25` | And some of these servers do have disk space that is attached directly you know, with a physical connection onto the server. | Và một số máy chủ vật lý này có không gian ổ đĩa được kết nối vật lý trực tiếp vào bo mạch của máy chủ đó. |
| `00:00:33` | And so a special type of EC2 Instance can leverage something called an EC2 Instance Store, which is the name of the hardware, the hard drive attached to the physical server. | Do đó, một số dòng EC2 instance đặc biệt có thể tận dụng thứ gọi là **EC2 Instance Store** — tên gọi của ổ cứng vật lý gắn trực tiếp vào máy chủ host. |
| `00:00:44` | So what we do with EC2 Instance Store, we use them for better I/O performance. We also make sure that they have good throughput and so on, so they're a great choice when you want to have extremely high disk performance. | Chúng ta sử dụng EC2 Instance Store để đạt hiệu năng đọc/ghi (**I/O performance**) và thông lượng (**throughput**) vượt trội — đây là lựa chọn tuyệt vời khi bạn cần hiệu năng ổ đĩa cực kỳ cao. |
| `00:00:56` | But the caveat is that if you stop or you terminate your EC2 Instance, that has an Instance Store, then the storage will be lost. | Tuy nhiên điểm đánh đổi cần lưu ý là: nếu bạn **Stop** hoặc **Terminate** một EC2 instance dùng Instance Store, toàn bộ dữ liệu trên ổ đĩa đó sẽ **bị mất sạch**. |
| `00:01:06` | And therefore it's called an ephemeral storage so that means that the EC2 Instance Store can not be used as a durable long term place to store your data. | Vì vậy nó được gọi là **lưu trữ tạm thời (ephemeral storage)**, nghĩa là EC2 Instance Store không thể được dùng làm nơi lưu trữ bền vững lâu dài cho dữ liệu của bạn. |
| `00:01:16` | So what is a good use case for it then? Well if you have a buffer, a cache, you want to have scratch data or temporary content, this would be a great place to do these things | Vậy trường hợp sử dụng (use case) phù hợp cho nó là gì? Nếu bạn cần làm **bộ đệm (buffer)**, **bộ nhớ tạm (cache)**, **dữ liệu nháp xử lý trung gian (scratch data)** hoặc **nội dung tạm thời (temporary content)** thì đây là nơi tuyệt vời nhất, |
| `00:01:26` | but not for long term storage. For long term storage, EBS for example is a great use case. | chứ không phải để lưu trữ lâu dài. Đối với lưu trữ lâu dài, hãy dùng EBS. |
| `00:01:31` | Finally, in case the underlying server of the EC2 Instance does fail, then you'll risk to have a data loss because the hardware attached to the EC2 Instance will fail as well. | Ngoài ra, trong trường hợp máy chủ vật lý bên dưới của EC2 instance gặp sự cố hỏng phần cứng, bạn cũng sẽ có nguy cơ mất dữ liệu vì ổ cứng gắn trực tiếp vào máy chủ đó cũng hỏng theo. |
| `00:01:43` | So if you do decide to use an EC2 Instance Store, then it is your entire responsibility to make sure that you back it up and that you replicate it correctly based on your needs. | Vì vậy nếu quyết định sử dụng EC2 Instance Store, bạn phải hoàn toàn tự chịu trách nhiệm sao lưu (back up) và nhân bản dữ liệu (replicate) ở tầng ứng dụng theo nhu cầu của mình. |
| `00:01:54` | So what I mean by better performance, this is just an example to illustrate it, don't need to know it. But if you look at for example, the Instance size of `i3` dot something, there is an Instance Store attached to these kinds of instances | Để minh họa cụ thể thế nào là hiệu năng vượt trội (bạn không cần thuộc lòng bảng số liệu này): nếu nhìn vào dòng máy `i3`, chúng có gắn kèm các ổ đĩa Instance Store (NVMe SSD), |
| `00:02:09` | and if you look at the Read IOPS and the Write IOPS which correspond to how many I/O operations we can do per second. | và khi nhìn vào cột Read IOPS và Write IOPS (số lượng thao tác đọc/ghi mỗi giây), |
| `00:02:15` | Then you can see at some of these random Read IOPS and Write IOPS can reach 3.3 million or 1.4 million, for the most performant one. | bạn sẽ thấy tốc độ đọc ngẫu nhiên có thể đạt tới **3,3 triệu IOPS** và ghi đạt **1,4 triệu IOPS** trên cấu hình mạnh nhất (`i3.16xlarge` / `i3.metal`). |
| `00:02:24` | And to put this in comparison with an EBS volume of type `gp2` for example, you can reach 32,000 IOPS. So this is a lot more. | Nếu đặt lên bàn cân so sánh với một ổ EBS thông thường đạt khoảng 16.000 – 32.000 IOPS, bạn sẽ thấy Instance Store nhanh hơn gấp hàng trăm lần. |
| `00:02:33` | But again, it's just to illustrate my point from an exam perspective anytime you see very high performance hardware attached volume for your EC2 Instances, think local EC2 Instance Store. | Dưới góc độ kỳ thi SAA-C03: bất cứ khi nào bạn thấy yêu cầu về một ổ đĩa gắn trực tiếp phần cứng có hiệu năng I/O cực cao cho EC2 instance, hãy nghĩ ngay tới **Local EC2 Instance Store**. |
| `00:02:45` | That's it. I will see you in the next lecture. | Đó là tất cả cho bài học này. Hẹn gặp lại bạn ở bài học tiếp theo! |
