# Bài 50: EC2 Placement Groups - Hands On

- **Phần (Section):** Section 6: EC2 - Solutions Architect Associate Level
- **Lecture ID:** `26118770`
- **Video gốc:** `SAA - EC2 - Placement Groups Hands On v5.mp4`
- **Thời lượng:** `01:42`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các bước tạo và sử dụng Placement Groups trên AWS Console
1. **Truy cập mục quản lý:**
   - Trong giao diện EC2 Console, cuộn xuống menu bên trái mục **Network & Security -> Placement Groups** -> nhấn **Create placement group**.
2. **Tạo 3 loại Placement Group mẫu:**
   - **`my-high-performance-group`**: Chọn Placement strategy là **Cluster** (đặt các EC2 sát nhau trong cùng 1 AZ để tối đa hóa hiệu năng mạng).
   - **`my-critical-group`**: Chọn Placement strategy là **Spread**; ở mục **Spread level**, chọn **Rack** (mặc định trên AWS Cloud; tùy chọn **Host** chỉ dành cho AWS Outposts).
   - **`my-distributed-group`**: Chọn Placement strategy là **Partition**; chọn **Number of partitions** từ **`1` đến `7`** (ví dụ: `4` partitions).
3. **Khởi chạy EC2 vào Placement Group:**
   - Nhấn **Launch instances**, cuộn xuống cuối trang mở mục **Advanced details**.
   - Tại trường **Placement group name**, chọn một trong các Placement Group đã tạo (`my-critical-group`, `my-distributed-group`, hoặc `my-high-performance-group`).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So let's go ahead and practice placement groups. | Bây giờ hãy cùng thực hành với Placement Groups. |
| `00:00:03` | To this, on the left hand side, I'm going to scroll down and find under network and security, the placement groups option. | Để làm việc này, ở thanh menu bên trái, tôi sẽ cuộn xuống và tìm tùy chọn **Placement Groups** dưới mục **Network & Security**. |
| `00:00:09` | And I will go ahead and create a placement group. So the first one is going to be `my-high-performance-group`. | Tôi sẽ tiến hành tạo một Placement Group. Nhóm đầu tiên sẽ có tên là `my-high-performance-group`. |
| `00:00:16` | And as you can guess, the placement strategy for this one is going to be cluster, because we want instances to be very close to each other so that they have maximum network capability. | Như bạn có thể đoán, chiến lược sắp xếp (Placement strategy) cho nhóm này sẽ là **Cluster**, bởi vì chúng ta muốn các instances nằm rất gần nhau để đạt năng lực mạng tối đa. |
| `00:00:27` | The second thing is going to be `my-critical-group`. | Nhóm thứ hai sẽ là `my-critical-group`. |
| `00:00:33` | And for this one, the placement strategy is going to be spread, because we want instances to be distributed as much as possible. | Với nhóm này, chiến lược sắp xếp sẽ là **Spread**, vì chúng ta muốn các instances được phân tán tách biệt nhiều nhất có thể. |
| `00:00:41` | And you can set the spread level to rack, which is a default, or host, which is outpost only, but we don't use outpost. | Bạn có thể đặt cấp độ phân tán (Spread level) là **Rack** (mặc định) hoặc **Host** (chỉ dành riêng cho AWS Outposts, mà chúng ta không dùng Outposts). |
| `00:00:46` | So for now we'll just use rack, which is what we should know about. | Vì vậy hiện tại chúng ta chỉ dùng mức **Rack**, đó là những gì chúng ta cần biết. |
| `00:00:51` | Okay. So this critical group has been done. And finally, we have `my-distributed-group`. | Được rồi, nhóm critical đã tạo xong. Và cuối cùng, chúng ta tạo nhóm `my-distributed-group`. |
| `00:00:58` | And this one, as you can guess, is going to be for the partition type. | Như bạn có thể đoán, nhóm này sẽ thuộc kiểu **Partition**. |
| `00:01:01` | And here we have the choice between one, two, seven partitions. For example, I can set four, and create this group. | Tại đây chúng ta có thể chọn số lượng từ 1 đến 7 partitions. Ví dụ tôi đặt là 4 rồi nhấn tạo nhóm này. |
| `00:01:09` | So the three groups have been created. And now, to just launch an instance in a group, you click on launch instances. | Vậy là cả 3 nhóm đã được tạo xong. Bây giờ để khởi chạy một instance vào trong một nhóm, bạn nhấn vào **Launch instances**. |
| `00:01:16` | And now, when you scroll down, at the very bottom, under the advanced details, you can have a setting for right here, the placement group name, | Khi cuộn xuống tận dưới cùng, bên trong mục **Advanced details**, bạn sẽ thấy thiết lập **Placement group name** ngay tại đây, |
| `00:01:28` | and you can select between `my-critical-group`, `my-distributed-group`, or `my-high-performance-group` based on your placement group strategy. | và bạn có thể chọn giữa `my-critical-group`, `my-distributed-group`, hoặc `my-high-performance-group` tùy theo chiến lược Placement Group của bạn. |
| `00:01:36` | So that's it. It's a very short lecture, but now you know where the options are. | Chỉ vậy thôi. Đây là một bài học rất ngắn nhưng giờ bạn đã biết các tùy chọn này nằm ở đâu. |
| `00:01:39` | I hope you liked it. And I will see you in the next lecture. | Hy vọng bạn thích bài học này. Hẹn gặp lại bạn ở bài học tiếp theo. |
