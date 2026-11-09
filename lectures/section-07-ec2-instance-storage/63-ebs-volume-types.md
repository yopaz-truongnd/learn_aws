# Bài 63: EBS Volume Types

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `26098296`
- **Video gốc:** `SAA - EBS Volume Types v5.mp4`
- **Thời lượng:** `04:34`
- **Cheat sheet:** [topics/aws_storage.html](../../topics/aws_storage.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Phân loại 6 dòng ổ đĩa EBS (6 EBS Volume Types)
Hiện nay EBS được chia làm **4 nhóm lớn (6 loại ổ đĩa)**, định nghĩa theo 3 yếu tố: **Size (Dung lượng)**, **Throughput (Thông lượng MB/s)** và **IOPS (Số thao tác đọc/ghi mỗi giây)**:
1. **`gp2` / `gp3` (General Purpose SSD):** Ổ đĩa SSD đa dụng cân bằng giữa chi phí và hiệu năng cho đa số các tác vụ.
2. **`io1` / `io2 Block Express` (Provisioned IOPS SSD):** Ổ đĩa SSD hiệu năng cao nhất dành cho các ứng dụng trọng yếu (mission-critical), cơ sở dữ liệu lớn cần độ trễ cực thấp và IOPS duy trì ổn định cao.
3. **`st1` (Throughput Optimized HDD):** Ổ đĩa từ HDD chi phí thấp, thiết kế cho các tác vụ truy cập thường xuyên và cần thông lượng tuần tự lớn (Big Data, Data Warehousing, Log Processing).
4. **`sc1` (Cold HDD):** Ổ đĩa từ HDD chi phí rẻ nhất, thiết kế cho dữ liệu ít khi truy cập (Archive / Infrequently accessed data).

> [!IMPORTANT]
> **Quy tắc Boot Volume (Ổ đĩa khởi động hệ điều hành) trong đề thi SAA-C03:**
> - **CHỈ các ổ đĩa SSD (`gp2`, `gp3`, `io1`, `io2`)** (cùng chuẩn Magnetic cũ) mới có thể dùng làm **Boot Volume** (Root volume chạy OS).
> - **`st1` và `sc1` TUYỆT ĐỐI KHÔNG THỂ dùng làm Boot Volume!**

---

### 1.2. Bảng so sánh chi tiết các loại EBS Volumes (Trọng tâm thi SAA-C03)

| Loại EBS | Nhóm | Đặc điểm IOPS & Throughput | Dung lượng | Use Cases điển hình |
| :--- | :--- | :--- | :--- | :--- |
| **`gp3`** | General Purpose SSD (Thế hệ mới) | - Baseline: **`3,000 IOPS`** và **`125 MB/s`**.<br>- Tăng **độc lập (independently)** IOPS lên tới **`80,000 IOPS`** và Throughput lên tới **`2,000 MB/s`** không phụ thuộc dung lượng ổ. | `1 GiB` – `16 TiB` | System boot volumes, Virtual desktops, Dev/Test, Medium-sized DBs. |
| **`gp2`** | General Purpose SSD (Thế hệ cũ) | - **Dung lượng và IOPS gắn liền với nhau:** Cứ mỗi `1 GB` được cộng **`3 IOPS`**.<br>- Ổ nhỏ có thể burst lên `3,000 IOPS`.<br>- Đạt tối đa **`16,000 IOPS`** tại mức dung lượng **`5,334 GB`**. | `1 GiB` – `16 TiB` | System boot volumes, Dev/Test, ứng dụng độ trễ thấp đa dụng. |
| **`io1`** | Provisioned IOPS SSD | - Tăng IOPS độc lập với dung lượng (tỷ lệ tối đa `50 IOPS : 1 GiB`).<br>- Tối đa **`64,000 IOPS`** (trên **EC2 Nitro**) hoặc `32,000 IOPS` (trên các dòng EC2 khác).<br>- Hỗ trợ **EBS Multi-Attach**. | `4 GiB` – `16 TiB` | Cơ sở dữ liệu trọng yếu (Mission-critical Databases), ứng dụng cần `> 16,000` hoặc `> 80,000 IOPS` ổn định. |
| **`io2 Block Express`** | Provisioned IOPS SSD (Cao cấp nhất) | - Độ trễ dưới mili-giây (**Sub-millisecond latency**).<br>- Tối đa **`256,000 IOPS`** (tỷ lệ `1,000 IOPS : 1 GiB`).<br>- Độ bền `99.999%`, hỗ trợ **EBS Multi-Attach**. | `4 GiB` – `64 TiB` | Workloads cơ sở dữ liệu khổng lồ đòi hỏi IOPS cực cao (`up to 256,000 IOPS`). |
| **`st1`** | Throughput Optimized HDD | - **Không làm Boot volume**.<br>- Max Throughput: **`500 MB/s`**.<br>- Max IOPS: **`500 IOPS`**. | `125 GiB` – `16 TiB` | Big Data, Data Warehouses, Log Processing, Apache Kafka. |
| **`sc1`** | Cold HDD | - **Không làm Boot volume**.<br>- Max Throughput: **`250 MB/s`**.<br>- Max IOPS: **`250 IOPS`**. | `125 GiB` – `16 TiB` | Dữ liệu lưu trữ ít truy cập (Infrequently accessed data), cần chi phí lưu trữ EBS thấp nhất. |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So now let's talk about EBS volumes, and there are different volume types. | Bây giờ hãy cùng tìm hiểu về các loại ổ đĩa EBS (EBS volume types). |
| `00:00:04` | They come in six different types today, and we can group them in several categories. | Hiện nay chúng có 6 loại khác nhau, được chia thành 4 nhóm chính. |
| `00:00:08` | The first one is `gp2`/`gp3`, which is a general purpose SSD volume that will balance price and performance for a wide variety of workloads. And this is something we've been using so far in this course. | Nhóm đầu tiên là **`gp2` / `gp3`** — dòng ổ đĩa SSD đa dụng (General Purpose SSD) cân bằng giữa giá thành và hiệu năng cho nhiều loại tải công việc khác nhau. Đây là loại chúng ta đã dùng từ đầu khóa học tới giờ. |
| `00:00:19` | Then we have `io1` and `io2 Block Express`. They're highest-performance SSD volumes that will be used for mission-critical low-latency and high-throughput workloads. | Tiếp theo là **`io1` và `io2 Block Express`** — các ổ đĩa SSD có hiệu năng cao nhất, được dùng cho các hệ thống trọng yếu (mission-critical) đòi hỏi độ trễ cực thấp và thông lượng/IOPS cao. |
| `00:00:29` | Then we have `st1` volumes and they're low-cost HDD volume designed for frequently accessed throughput-intensive workloads. | Thứ ba là **`st1`** — ổ đĩa cứng từ (HDD) chi phí thấp được thiết kế cho các tác vụ truy cập thường xuyên và thiên về thông lượng tuần tự cao (throughput-intensive). |
| `00:00:36` | We have `sc1` volume, which are going to be the lowest cost HDD volume, and they will be designed for less frequently accessed workloads. | Thứ tư là **`sc1`** — ổ đĩa HDD có chi phí thấp nhất, được thiết kế cho các dữ liệu ít được truy cập hơn. |
| `00:00:43` | Now, how do you define an EBS volume? Well, you can have several factors, for example, size, throughputs, and IOPS, which means I/O operations per second. | Làm thế nào để đặc tả một ổ đĩa EBS? Chúng ta dựa trên các thông số: dung lượng (Size), thông lượng truyền tải (Throughput), và **IOPS** (số lượng thao tác đọc/ghi I/O mỗi giây). |
| `00:00:58` | Now, for your EC2 instances, only `gp2` and `gp3` and `io1` and `io2` can be used as boot volumes. That means where the root OS is going to be running. | Lưu ý quan trọng cho EC2 instances của bạn: **chỉ có `gp2`, `gp3`, `io1` và `io2` mới có thể được dùng làm ổ đĩa khởi động (Boot volumes)** — tức là nơi cài đặt và chạy hệ điều hành gốc (Root OS). |
| `00:01:09` | So let's do a deeper dive into the different EBS volume types. | Hãy cùng đi sâu vào từng nhóm ổ đĩa EBS này. |
| `00:01:13` | The first one is the General Purpose or GP SSD. So we have the cost effective storage and low latency. | Đầu tiên là **General Purpose SSD (`gp2` / `gp3`)**: lưu trữ tiết kiệm chi phí với độ trễ thấp. |
| `00:01:19` | They can be used as system boot volumes, virtual desktops, Development and test environments, medium sized databases, and transactional workloads. | Chúng được dùng làm ổ khởi động hệ thống, máy tính ảo (virtual desktops), môi trường Dev/Test, cơ sở dữ liệu quy mô vừa và các tác vụ giao dịch. |
| `00:01:28` | We have the `gp3` type of volume, which gives you a baseline of 3,000 IOPS and a throughput of 125 megabytes per second. | Với loại **`gp3`** (thế hệ mới hơn), bạn có sẵn mức cơ sở (baseline) là **3.000 IOPS** và thông lượng **125 MB/giây**. |
| `00:01:37` | And you can increase the IOPS up to 80,000 and the throughput up to 2,000 megabytes per second independently. | Và bạn có thể tăng IOPS lên tới **80.000 IOPS** cũng như tăng thông lượng lên tới **2.000 MB/giây** một cách hoàn toàn **độc lập (independently)** với dung lượng ổ đĩa. |
| `00:01:45` | The `gp2` volume will give you small `gp2` volumes that can burst up to 3,000 IOPS, and there is the size and the IOPS capacity that are linked. | Ngược lại với loại **`gp2`** (thế hệ cũ hơn), các ổ `gp2` nhỏ có thể bứt tốc (burst) lên tới 3.000 IOPS, và **dung lượng ổ đĩa (size) gắn liền chặt chẽ với mức IOPS**. |
| `00:01:56` | So as you increase the size of your `gp2` volume, the IOPS will increase and the max IOPS you can ever get is 16,000. | Khi bạn tăng dung lượng của ổ `gp2`, số IOPS sẽ tăng theo, và mức IOPS tối đa bạn có thể đạt được trên `gp2` là **16.000 IOPS**. |
| `00:02:04` | So in `gp3`, you can set them independently. In `gp2`, they are linked together. You get 3 IOPS per gigabyte. That means that at 5,300 something gigabytes, we are at the max IOPS. | Tóm lại: ở `gp3` bạn cấu hình IOPS và dung lượng độc lập; còn ở `gp2` chúng gắn liền nhau theo tỷ lệ **3 IOPS cho mỗi GB** — nghĩa là ở mức `5.334 GB` bạn sẽ chạm trần 16.000 IOPS. |
| `00:02:16` | Next we get the Provisioned IOPS SSD. So this is when you have a critical business application with sustained IOPS performance or applications that will need more than 80,000 IOPS. | Tiếp theo là nhóm **Provisioned IOPS SSD (`io1` / `io2`)**: dùng khi bạn có các ứng dụng kinh doanh trọng yếu cần hiệu năng IOPS duy trì ổn định liên tục hoặc các ứng dụng cần nhiều hơn 80.000 IOPS. |
| `00:02:28` | This is great for very good database workloads that will be sensitive to storage performance and consistency. | Dòng này cực kỳ phù hợp cho các tải cơ sở dữ liệu lớn rất nhạy cảm với hiệu năng và tính nhất quán của lưu trữ. |
| `00:02:35` | So we have the `io1` volume where you get a max IOPS of 64,000. PIOPS is Provisioned IOPS. 64,000 for Nitro EC2 instances and 32,000 for others. | Với ổ **`io1`** (`4 GiB` – `16 TiB`), bạn đạt tối đa **64.000 PIOPS** đối với các **Nitro EC2 instances** và **32.000 PIOPS** đối với các dòng máy khác. |
| `00:02:46` | And you can increase the IOPS independently from the storage size with a ratio of about 50 to 1. | Bạn có thể tăng PIOPS độc lập với dung lượng lưu trữ theo tỷ lệ tối đa 50 IOPS trên mỗi GiB. |
| `00:02:54` | And the `io2 Block Express` volumes give you sub-millisecond latency, give you a much greater IOPS max capacity. So 256,000 IOPS with a ratio of 1,000 IOPS per gigabyte maximum. | Còn ổ **`io2 Block Express`** (`4 GiB` – `64 TiB`) mang lại độ trễ dưới 1 mili-giây (sub-millisecond latency) và mức IOPS tối đa lớn hơn rất nhiều: lên tới **256.000 IOPS** với tỷ lệ tối đa 1.000 IOPS trên mỗi GiB. |
| `00:03:10` | Also, they support EBS Multi-attach feature. | Ngoài ra, cả `io1` và `io2` đều hỗ trợ tính năng **EBS Multi-Attach**. |
| `00:03:14` | So now let's quickly touch upon `st1` and `sc1`. So they cannot be boot volumes, this is only for the previous types of volumes. You can get the size up to 16 terabytes and we get two kinds of volumes here. | Cuối cùng hãy điểm qua hai loại ổ HDD là **`st1` và `sc1`**. Hãy nhớ rằng **chúng KHÔNG THỂ làm ổ đĩa khởi động (cannot be boot volumes)**. Dung lượng của chúng từ `125 GiB` đến `16 TiB`: |
| `00:03:28` | We have the throughput optimized HDD, so `st1`, which is great for big data, data warehousing, and log processing, which gives you a max throughput of 500 megabytes per second and a max IOPS of 500. | Thứ nhất là **Throughput Optimized HDD (`st1`)**: rất tốt cho Big Data, Data Warehousing và xử lý Log, cung cấp thông lượng tối đa **500 MB/giây** và IOPS tối đa là 500. |
| `00:03:39` | And then for cold HDD so, `sc1`, this is for archive data, so data that is infrequently accessed. And this is when you would use it when you need to have the lowest possible cost. Here, the max throughput is 250 megabytes per second and the max IOPS is 250 as well. | Thứ hai là **Cold HDD (`sc1`)**: dành cho dữ liệu lưu trữ ít khi được truy cập (infrequently accessed data) khi bạn cần chi phí lưu trữ thấp nhất có thể; thông lượng tối đa là **250 MB/giây** và IOPS tối đa là 250. |
| `00:03:55` | Now you don't have to remember all these details going into the exam. You just need to understand the differences at a high level of all these volumes. | Khi đi thi, bạn không cần nhớ từng con số chi tiết nhỏ lẻ mà chỉ cần hiểu rõ sự khác biệt cốt lõi giữa các loại ổ đĩa này: |
| `00:04:02` | So the General Purpose SSD versus the Provisioned IOPS SSD in case you need a database versus some `st1` and `sc1` in case you need to have high throughput and lowest cost. | Khi nào dùng General Purpose SSD (`gp2`/`gp3`), khi nào dùng Provisioned IOPS SSD (`io1`/`io2`) cho database khắt khe về IOPS, và khi nào dùng `st1`/`sc1` cho thông lượng tuần tự cao hoặc chi phí thấp nhất. |
| `00:04:19` | So don't need to remember the details again, but remember that if you wanna get also over 32,000 IOPS, you need EC2 Nitro with `io1` or `io2`. And that will be it for this lecture. | Cũng hãy nhớ rằng nếu đề bài cần trên `32,000 IOPS` trên EBS (và lên tới `64,000` hay `256,000 IOPS`), bạn cần dùng **EC2 Nitro** kết hợp với **`io1` hoặc `io2`**. Hẹn gặp lại bạn ở bài học tiếp theo! |
