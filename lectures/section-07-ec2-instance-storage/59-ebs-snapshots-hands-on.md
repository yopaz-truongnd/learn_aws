# Bài 59: EBS Snapshots - Hands On

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `26098278`
- **Video gốc:** `CCP_-_EBS_-_Snapshots_Hands_On_v3.mp4`
- **Thời lượng:** `03:38`
- **Cheat sheet:** [topics/aws_storage.html](../../topics/aws_storage.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các thao tác thực hành với EBS Snapshots trên AWS Console
1. **Tạo Snapshot từ một EBS Volume:**
   - Chọn ổ đĩa EBS (`2 GiB`, `gp2` ở `eu-west-1a`) -> **Actions -> Create snapshot** -> nhập Description (`DemoSnapshots`) -> nhấn **Create snapshot**.
   - Vào menu bên trái **Elastic Block Store -> Snapshots** để xem trạng thái (`Completed`, `100% Available`).
2. **Sao chép Snapshot sang Region khác (Copy Snapshot):**
   - Chọn Snapshot -> **Actions -> Copy snapshot** -> chọn bất kỳ **Destination Region** nào (rất hữu ích cho chiến lược **Disaster Recovery**).
3. **Khôi phục EBS Volume sang một Availability Zone khác:**
   - Chọn Snapshot -> **Actions -> Create volume from snapshot** -> chọn `eu-west-1b` (khác với AZ gốc `eu-west-1a`), có thể bật mã hóa (Encrypt) -> nhấn **Create volume**.
4. **Chuyển tầng lưu trữ (Archive Snapshot):**
   - Mặc định Snapshot nằm ở **Standard storage tier**. Có thể chọn **Actions -> Archive snapshot** để chuyển sang tầng Archive tiết kiệm chi phí (mất 24–72 giờ khi cần khôi phục).
5. **Thực hành Recycle Bin cho EBS Snapshots & AMIs:**
   - Mở **Recycle Bin** -> **Create retention rule**:
     - Chọn Resource type: **EBS Snapshots** (hoặc **AMIs**).
     - Áp dụng cho tất cả tài nguyên (Apply to all resources), thời gian lưu giữ: **`1 day`**.
   - Quay lại mục **Snapshots**, xóa bản `DemoSnapshots`. Bản snapshot biến mất khỏi EC2 Console nhưng xuất hiện trong mục **Resources** của **Recycle Bin**.
   - Chọn snapshot trong Recycle Bin -> **Actions -> Recover** -> bản snapshot lập tức quay trở lại danh sách Snapshots trên EC2 Console!

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So we have this two gigabyte, GP2 EBS Volume available to us, and we can take a snapshot from it. | Hiện chúng ta đang có sẵn ổ đĩa EBS `gp2` dung lượng 2 GB này, và chúng ta có thể chụp một bản snapshot từ nó. |
| `00:00:06` | So if we do Actions, we can Create a snapshot. So we can add a Description, for example, `DemoSnapshots`, and then click on Create snapshots. | Chúng ta chọn **Actions -> Create snapshot**, nhập phần mô tả ví dụ `DemoSnapshots`, rồi nhấn **Create snapshot**. |
| `00:00:16` | So then on the left hand side menu, instead of Volumes, you can click on Snapshots. | Sau đó ở thanh menu bên trái, thay vì mục Volumes, bạn nhấn vào mục **Snapshots**. |
| `00:00:22` | And Snapshots shows you a list of all the snapshots you have. And as you can see, we have one right here. It is Completed. It is 100% Available. | Trang Snapshots hiển thị danh sách tất cả các bản snapshots của bạn. Như bạn thấy, chúng ta có một bản ngay tại đây, trạng thái `Completed` và `100% Available`. |
| `00:00:32` | For first of all, what we can do is that we can Copy this snapshot into other region. | Đầu tiên, điều chúng ta có thể làm là sao chép (Copy) bản snapshot này sang một Region khác. |
| `00:00:37` | So if you right click and do Copy Snapshots, then as you can see, you can copy the snapshot into any destination region that you want. | Nếu bạn nhấp chuột phải và chọn **Copy snapshot**, bạn có thể sao chép bản snapshot này tới bất kỳ Destination Region nào bạn muốn. |
| `00:00:45` | And this can come in very handy, in case you want for example, to have a Disaster Recovery Strategy, to make sure data is backed up in another region of AWS. | Tính năng này cực kỳ hữu ích khi bạn muốn xây dựng chiến lược Khôi phục sau thảm họa (Disaster Recovery Strategy), đảm bảo dữ liệu được sao lưu an toàn ở một Region khác của AWS. |
| `00:00:54` | So I won't do that, I won't do so, but you get the idea. Another thing I can do is take the Snapshot, and I can recreate a Volume from it. | Ở đây tôi sẽ không bấm sao chép nhưng bạn đã nắm được ý tưởng. Điều tiếp theo tôi có thể làm là chọn bản Snapshot này và tạo lại một ổ đĩa EBS mới từ nó. |
| `00:01:03` | So Action, Create volume from snapshots. And we choose a two gigabytes GP2 Volume. | Chọn **Actions -> Create volume from snapshot**. Chúng ta giữ cấu hình ổ `gp2` 2 GB. |
| `00:01:10` | And then the target AZ doesn't have to remain `eu-west-1a`, it can be, for example, `eu-west-1b`. | Và lúc này Availability Zone đích không nhất thiết phải giữ nguyên là `eu-west-1a` nữa, mà có thể đổi sang `eu-west-1b`. |
| `00:01:18` | And we can also encrypt these volumes if you wanted to and add some Tags. | Chúng ta cũng có thể mã hóa (encrypt) ổ đĩa mới này nếu muốn và gắn thêm các thẻ Tags. |
| `00:01:21` | And so as we can see, when we click on Create volume, what's going to happen is that if we go back into our Volumes, well, now we have two Volumes, as you can see. | Khi nhấn **Create volume** và quay lại danh sách **Volumes**, bây giờ chúng ta đã có 2 ổ đĩa EBS. |
| `00:01:31` | And one of them, this one was restored through a Snapshots, okay? And it is an `eu-west-1b`. | Ổ đĩa mới này được khôi phục từ Snapshot và đang nằm ở `eu-west-1b`. |
| `00:01:39` | So the idea is that thanks to Snapshots, we can quote unquote copy EBS volumes across different Availability Zones. And that's very handy. | Như vậy nhờ có Snapshots, chúng ta có thể "sao chép" các ổ đĩa EBS qua lại giữa các Availability Zones khác nhau rất tiện lợi. |
| `00:01:48` | If we look again at Snapshots, we can have a look at what's called the Recycle Bin. | Quay lại trang Snapshots, chúng ta thấy có nút dẫn tới **Recycle Bin (Thùng rác)**. |
| `00:01:53` | So the Recycle Bin is a way for you to protect your EBS Snapshots from accidental deletion, as well as your Amazon Machine Images. | Recycle Bin là công cụ giúp bạn bảo vệ cả **EBS Snapshots** lẫn **AMIs (Amazon Machine Images)** khỏi việc bị xóa nhầm. |
| `00:02:02` | So we can Create a Retention Rule and name it `DemoRetentionRule`. | Chúng ta nhấn **Create retention rule** và đặt tên là `DemoRetentionRule`. |
| `00:02:09` | I will select EBS Snapshots. I will Apply to all resources and retain them during one day. | Tôi chọn loại tài nguyên là **EBS Snapshots**, chọn áp dụng cho tất cả tài nguyên (Apply to all resources) và thời gian lưu giữ là **1 ngày (`1 day`)**. |
| `00:02:15` | And for Rule Lock Setting, I will leave this unlocked, so that I can delete this rule whenever I want to. And then click on Create Retention Rule. | Ở mục Rule lock settings, tôi để trạng thái `Unlocked` để có thể xóa quy tắc này bất cứ lúc nào sau khi demo xong, rồi nhấn **Create retention rule**. |
| `00:02:24` | And now on the Resources, we can see if we have Resources in the Recycle Bin. So let's go back into our Snapshots in the EC2 Console. | Trong mục **Resources** của Recycle Bin hiện chưa có gì. Hãy quay lại mục **Snapshots** trong EC2 Console. |
| `00:02:39` | And what I'm going to do is take the Snapshots, and first, before I delete it, I wanna show you the Storage Tiers. | Trước khi xóa bản snapshot này, tôi muốn chỉ cho bạn thấy cột **Storage tier**. |
| `00:02:44` | So right now it is a Standard Storage Tier, okay? But you can move the Storage Tier, by Archiving a snapshots, and so I need to move the Storage Tier into another Pricing Level. | Hiện tại nó đang ở tầng **Standard**. Bạn có thể chuyển tầng lưu trữ bằng cách chọn **Actions -> Archive snapshot** để đưa nó sang mức giá rẻ hơn. |
| `00:02:55` | But if you want to restore it, of course, you will have to wait 24 to 72 hours. So just to show you. | Nhưng tất nhiên nếu muốn khôi phục từ Archive, bạn sẽ phải đợi từ 24 đến 72 giờ. |
| `00:03:00` | But anyway, let's go ahead and delete the snapshot. So we'll delete the Snapshots. As you can see, it's gone. | Bây giờ hãy tiến hành xóa bản snapshot này (**Actions -> Delete snapshot**). Như bạn thấy, nó đã biến mất khỏi danh sách. |
| `00:03:06` | And before, it used to completely delete the snapshots, and you couldn't recover it, okay? As you can see, it's gone. | Trước đây, thao tác này sẽ xóa vĩnh viễn bản snapshot và bạn không có cách nào lấy lại được. |
| `00:03:12` | But now thanks to the Recycle Bin, well, if I refresh here my Resources, I can now see that my Snapshot has appeared here. | Nhưng hiện nay nhờ có **Recycle Bin**, khi tôi sang tab Recycle Bin và làm mới mục **Resources**, bản Snapshot vừa xóa đã xuất hiện ngay tại đây! |
| `00:03:21` | And what I can do is click on it and Recover it. Yes, Recover Resources, and voila, it's back into my Snapshots on my EC2 console. | Tôi chỉ việc tích chọn nó và nhấn **Recover**. Xác nhận **Recover resources**, và tuyệt vời, bản snapshot đã quay trở lại nguyên vẹn trong danh sách Snapshots trên EC2 Console! |
| `00:03:31` | Okay, that was pretty awesome, right? Okay, that's it for EBS Snapshots. I hope you liked it, and I will see you in the next lecture. | Thật tuyệt phải không? Đó là tất cả cho bài thực hành EBS Snapshots. Hẹn gặp lại bạn ở bài học tiếp theo! |
