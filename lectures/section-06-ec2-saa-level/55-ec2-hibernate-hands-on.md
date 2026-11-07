# Bài 55: EC2 Hibernate - Hands On

- **Phần (Section):** Section 6: EC2 - Solutions Architect Associate Level
- **Lecture ID:** `18105183`
- **Video gốc:** `SAA_-_EC2_-_Hibernate_Hands_On_v4.mp4`
- **Thời lượng:** `04:07`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các bước bật và kiểm chứng EC2 Hibernate trên AWS Console
1. **Cấu hình khi Launch EC2 Instance:**
   - Chọn AMI: **Amazon Linux 2**, Instance type: **`t2.micro`** (có `1 GiB` RAM).
   - Trong mục **Advanced details -> Stop - Hibernate behavior**: Chọn **Enable**.
   - **Cấu hình Root EBS Volume (Bắt buộc):**
     - Mở phần **Configure storage -> Advanced** của Root volume (`8 GiB` — đủ lớn để chứa `1 GiB` RAM của `t2.micro`).
     - Chọn **Encrypted: Yes** và chọn KMS key mặc định **`(default) aws/ebs`**. *(Lưu ý: Nếu không mã hóa Root EBS volume, AWS sẽ không cho phép bật Hibernate).*
2. **Kiểm chứng bằng lệnh `uptime` trên Linux:**
   - Kết nối vào EC2 qua **EC2 Instance Connect**, chạy lệnh `uptime` -> hiển thị thời gian hệ điều hành đã chạy kể từ lần khởi động gần nhất (ví dụ: `up 1 min`).
   - Quay lại EC2 Console, chọn **Instance state -> Hibernate instance**. Instance chuyển sang trạng thái `Stopping` (dump RAM xuống EBS) rồi `Stopped`.
   - Nhấn **Start instance** để bật lại máy, sau đó kết nối lại và gõ `uptime`.
   - **Kết quả:** Thay vì reset về `0 min` như khi Stop/Start thông thường, lệnh `uptime` trả về **`up 2 min` (hoặc `3 min`)**, chứng minh hệ điều hành không hề bị tắt/khởi động lại mà toàn bộ trạng thái RAM đã được khôi phục nguyên vẹn!

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So let's practice using the EC2 hibernate feature. So let's go and launch an instance. | Bây giờ hãy cùng thực hành sử dụng tính năng EC2 Hibernate. Chúng ta hãy vào khởi chạy một instance. |
| `00:00:06` | I'll choose Amazon Linux 2. I'll go `t2.micro`, I'll select a key pair. | Tôi sẽ chọn Amazon Linux 2, loại máy `t2.micro`, và chọn một key pair. |
| `00:00:11` | And then for network security I will just use an existing security group namely `launch-wizard-1` and for storage, for now we're good. | Về bảo mật mạng, tôi sẽ dùng một Security Group có sẵn là `launch-wizard-1`, còn phần lưu trữ tạm thời để đó. |
| `00:00:20` | I'll show you a few things we have to set but I will scroll down and then stop hibernate behavior. We can enable it. | Tôi sẽ chỉ cho bạn vài thứ chúng ta phải thiết lập: cuộn xuống dưới mục **Stop - Hibernate behavior** và chọn **Enable**. |
| `00:00:30` | And this will allow us to enable hibernation on our EC2 instance. And there's a warning message. | Tùy chọn này cho phép chúng ta bật tính năng ngủ đông (hibernation) trên EC2 instance. Và ở đây có một thông báo nhắc nhở: |
| `00:00:36` | You cannot really read it here but it says that if you do enable hibernation then you need to make sure that the root volume has enough storage to fit the RAM of our EC2 instance. | Nó báo rằng nếu bạn bật tính năng Hibernation, bạn cần đảm bảo ổ đĩa gốc (Root volume) có đủ dung lượng lưu trữ để chứa dữ liệu RAM của EC2 instance. |
| `00:00:50` | And on top of it, the EBS volume, the root EBS volume must be encrypted. | Và thêm vào đó, ổ đĩa **Root EBS volume bắt buộc phải được mã hóa (encrypted)**. |
| `00:00:55` | So first regarding the storage, I will go to advanced, choose my EBS volume and I will, yes I will encrypt it and I will choose the default `aws/ebs` key to encrypt it. | Vì vậy đầu tiên ở mục Storage, tôi bấm vào **Advanced**, mở chi tiết ổ đĩa EBS, chọn **Encrypted = Yes** và chọn khóa mặc định `aws/ebs` để mã hóa. |
| `00:01:06` | So now our EBS volume is correctly set up and then we have an eight gigabytes volume. | Bây giờ ổ đĩa EBS của chúng ta đã được thiết lập đúng chuẩn và có dung lượng 8 GB. |
| `00:01:12` | And that is enough of storage because if we look at this `t2.micro`, here it says there's one gigabyte of memory of RAM. | Dung lượng 8 GB là quá đủ bởi vì chiếc `t2.micro` chỉ có 1 GB bộ nhớ RAM mà thôi. |
| `00:01:20` | So all the RAM fits onto the disk and that is good for us. So we have set up everything we need to enable hibernation. | Như vậy toàn bộ RAM hoàn toàn vừa vặn trên ổ đĩa. Chúng ta đã thiết lập đầy đủ mọi điều kiện để bật Hibernation. |
| `00:01:29` | And now what I'll do, is I will just launch my instances. | Bây giờ tôi chỉ việc nhấn **Launch instance**. |
| `00:01:34` | So our instance is now created and we have enabled hibernation as a specific stop behavior. | Instance của chúng ta đã được tạo xong và đã bật Hibernation. |
| `00:01:40` | So how do we prove that hibernation works? So let's connect to our instance using the EC2 Instance Connect and I'm going to connect right now. | Làm thế nào để chứng minh rằng Hibernation thực sự hoạt động? Hãy kết nối vào instance bằng **EC2 Instance Connect** ngay bây giờ. |
| `00:01:54` | So we are connected to our instance using EC2 Instance Connect. | Chúng ta đã kết nối thành công vào instance qua EC2 Instance Connect. |
| `00:01:58` | And there is one command called `uptime` that is quite special because `uptime` allows you to know for how long the instance has been turned on. | Có một câu lệnh rất đặc biệt trên Linux là `uptime`, vì lệnh `uptime` cho bạn biết máy chủ đã được bật liên tục trong bao lâu kể từ lần khởi động cuối cùng. |
| `00:02:06` | So if you do `uptime`, it says that right now it's been up for zero minutes. | Khi gõ `uptime` lúc này, nó báo máy mới bật được `0 min` (0 phút). |
| `00:02:11` | So we just need to wait maybe a little bit to do `uptime` for it to become one minute. | Chúng ta chỉ cần đợi thêm một chút rồi gõ lại `uptime` để nó nhảy lên 1 phút. |
| `00:02:16` | But the idea is that the `uptime` is telling you how long has the instance been on since its last restart. | Ý nghĩa của lệnh `uptime` là cho biết hệ điều hành đã hoạt động liên tục bao lâu kể từ lần khởi động gần nhất. |
| `00:02:25` | So as we can see now, we do `uptime` and we are getting one minute of uptime. So that means that the instance has been up for one minute. Okay, great. | Bây giờ khi gõ lại `uptime`, chúng ta nhận được kết quả là `1 min`. Nghĩa là instance đã chạy được 1 phút. Rất tuyệt. |
| `00:02:33` | So let's disconnect from our instance and what we're going to do now is that we're going to hibernate the instance. | Bây giờ hãy đóng kết nối và tiến hành cho instance này ngủ đông (Hibernate). |
| `00:02:40` | So to do so we do instance state and then hibernate instance, and this is going to make sure that all the data on the RAM is stored onto our EBS volume. | Chúng ta chọn **Instance state -> Hibernate instance**, thao tác này sẽ đảm bảo toàn bộ dữ liệu trên RAM được lưu xuống ổ đĩa EBS. |
| `00:02:52` | So we are hibernating the instance and so we need to wait for it to be stopped. | Máy đang trong quá trình ngủ đông, chúng ta đợi một lát để nó chuyển sang trạng thái `Stopped`. |
| `00:02:57` | So our instance is now stopped and I'm going to start it again. | Hiện tại instance đã ở trạng thái `Stopped` và tôi sẽ nhấn **Start instance** để bật nó lên lại. |
| `00:03:01` | Now, if we do it a little mental exercise, if we did not have hibernation and then we stopped the instance, and then we start it again, | Hãy suy luận một chút: nếu chúng ta không dùng Hibernation mà chỉ Stop rồi Start lại instance như bình thường, |
| `00:03:10` | we expect the `uptime` command to return again zero minutes and then one minute, because we have effectively stopped and started the instance. | chúng ta sẽ thấy lệnh `uptime` quay trở về `0 min` rồi mới lên `1 min`, bởi vì hệ điều hành đã thực sự bị tắt và khởi động lại từ đầu. |
| `00:03:19` | But we have hibernated the instance and then started it. And so if that's the case then we should be able to have the `uptime` start not at zero, but start at maybe three or four minutes. | Nhưng ở đây chúng ta đã **Hibernate** instance rồi mới Start lại. Vì vậy lệnh `uptime` sẽ không bắt đầu lại từ 0 mà sẽ tiếp tục ở mức 2, 3 hoặc 4 phút. |
| `00:03:30` | So let's connect to the instance and do `uptime`. And yes, we get up for two minutes because I was really quick. | Hãy kết nối lại vào instance và gõ `uptime`. Và vâng! Kết quả hiển thị là **`up 2 min`** vì tôi thao tác rất nhanh. |
| `00:03:36` | So the idea is that even though we have stopped, quote unquote stopped the instance by hibernating it, and restarted it from an operating system perspective, the instance was never stopped. It was hibernated. | Điều này chứng minh rằng mặc dù chúng ta đã đưa máy về trạng thái "Stopped" bằng lệnh Hibernate rồi bật lại, nhưng dưới góc nhìn của hệ điều hành (OS), máy chủ chưa bao giờ bị tắt mà chỉ ngủ đông. |
| `00:03:47` | And therefore the `uptime` command gives you two or three minutes because it has never quote unquote been stopped from an operating system perspective which is the whole idea behind hibernation. | Do đó lệnh `uptime` vẫn báo 2 hoặc 3 phút liên tục — đó chính là toàn bộ ý nghĩa cốt lõi của tính năng EC2 Hibernate. |
| `00:03:58` | So that's it. It's a really cool demo, I think. And to finish this hands on, just take your instance and terminate it. | Đó là tất cả. Một bản demo rất thú vị phải không? Để kết thúc bài thực hành này, bạn chỉ cần chọn instance và **Terminate** nó đi. |
| `00:04:05` | That's it, I will see you in the next lecture. | Hẹn gặp lại bạn ở bài học tiếp theo! |
