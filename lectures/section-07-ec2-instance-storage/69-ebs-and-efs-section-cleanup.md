# Bài 69: EBS & EFS - Section Cleanup

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `13528132`
- **Video gốc:** `EFS and EBS cleanup.mp4`
- **Thời lượng:** `01:31`
- **Cheat sheet:** [topics/aws_storage.html](../../topics/aws_storage.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Danh sách kiểm tra dọn dẹp tài nguyên cuối chương (Section 7 Cleanup Checklist)
Để tránh phát sinh bất kỳ chi phí lưu trữ nào ngoài ý muốn sau khi thực hành xong Section 7, hãy kiểm tra và xóa lần lượt 5 nhóm tài nguyên sau:
1. **Amazon EFS File Systems:** Vào EFS Console -> chọn hệ thống tệp EFS -> **Actions -> Delete** (nhập File System ID để xác nhận xóa).
2. **EC2 Instances:** Vào EC2 Console -> đảm bảo **Terminate** toàn bộ các EC2 instances đang chạy.
3. **EBS Volumes:** Vào mục **Elastic Block Store -> Volumes** -> chọn tất cả các ổ đĩa đang ở trạng thái `available` -> **Actions -> Delete volume**.
4. **EBS Snapshots & AMIs:**
   - Vào mục **Images -> AMIs** -> chọn các Custom AMIs đã tạo -> **Actions -> Deregister AMI**.
   - Vào mục **Elastic Block Store -> Snapshots** -> chọn và **Delete** toàn bộ các bản snapshots (và kiểm tra xóa cả trong **Recycle Bin** nếu có).
5. **Security Groups:** Vào mục **Network & Security -> Security Groups** -> xóa các Security Groups tạo thêm trong lúc thực hành (lưu ý: chỉ xóa được sau khi các EC2 instances và EFS Mount Targets gắn với chúng đã bị xóa hoàn toàn; giữ lại `default` security group).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | Okay, so let's just clean up this entire section. | Được rồi, bây giờ chúng ta hãy dọn dẹp toàn bộ tài nguyên của chương học này. |
| `00:00:02` | So for this I'm gonna go to Action on my file system and delete it, and for this I have to enter the file system ID, so I'll just copy and paste this. And so okay, we're gonna get rid of our file system. Perfect! | Đầu tiên trong EFS Console, tôi chọn hệ thống tệp của mình, nhấn **Delete**, sao chép và dán mã File system ID vào để xóa hoàn toàn hệ thống tệp EFS. Tuyệt vời! |
| `00:00:13` | Now into our EC2 instances, make sure to terminate any running EC2 instance, so that's good. | Tiếp theo trong mục **EC2 Instances**, hãy đảm bảo bạn đã **Terminate** tất cả các EC2 instances đang chạy. |
| `00:00:20` | Then in terms of volumes, we're going to have to clear up volumes as well, so any volumes that is available you have to terminate it, so I'll right-click and delete all these volumes. Okay. | Tiếp đến là mục **EBS Volumes**: bất kỳ ổ đĩa nào đang ở trạng thái `available` thì bạn hãy nhấp chuột phải và chọn **Delete volume** để xóa hết chúng đi. |
| `00:00:30` | Now for snapshots, you've made a few snapshots, so let's just go back and delete every snapshot you have. Just so that you can get rid and not pay for any storage for snapshots. Okay. | Tiếp theo ở mục **Snapshots**: bạn đã tạo một vài bản snapshots trong lúc thực hành, hãy vào xóa tất cả các bản snapshots đang có để không phải trả phí lưu trữ snapshot. |
| `00:00:41` | And then finally, security groups. If you want to, because it's going to get a lot of security groups right here, you can basically delete so many of these security groups except the one for `default`, so just don't delete that one. | Cuối cùng là mục **Security Groups**: để giao diện gọn gàng, bạn có thể xóa các Security Groups đã tạo thêm trong lúc thực hành (ngoại trừ nhóm `default` mặc định của VPC). |
| `00:00:56` | And they will only be deleted once you have, basically, deleted all your EC2 instances associated with those. | Lưu ý rằng các Security Groups này chỉ có thể xóa được sau khi tất cả các EC2 instances và EFS Mount Targets liên kết với chúng đã bị xóa hoàn toàn. |
| `00:01:10` | So I'll delete this security group now. Yes this one works. I'll delete the load balancer security group. Yes that worked, and this EC2 for EFS, it's still used by my instances so I have to wait for my instances to be shutting down properly before I can go ahead and delete that last security group. | Tôi xóa các nhóm không còn dùng nữa; còn nhóm nào đang gắn với instance đang trong quá trình tắt (`shutting-down`) thì chỉ cần đợi thêm vài giây cho máy tắt hẳn rồi xóa nốt. |
| `00:01:28` | Once you've cleared up everything you're ready to go for the next section. | Sau khi đã dọn dẹp sạch sẽ mọi thứ, bạn đã sẵn sàng để bước sang chương học tiếp theo! |
