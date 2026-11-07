# Bài 48: Private vs Public vs Elastic IP Hands On

- **Phần (Section):** Section 6: EC2 - Solutions Architect Associate Level
- **Lecture ID:** `13528054`
- **Video gốc:** `SAA_-_EC2_-_Private_vs_Public_vs_Elastic_IP_Hands_On_v4.mp4`
- **Thời lượng:** `06:06`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các hành vi thực tế được kiểm chứng trong bài Hands-On
1. **SSH qua Public IP vs Private IP:**
   - SSH từ máy cá nhân qua Internet bằng **Public IPv4** thành công. Khi đăng nhập vào trong máy, hostname của EC2 hiển thị **Private IPv4** (ví dụ: `ip-172-31-28-193`).
   - Nếu thoát ra và thử SSH từ máy cá nhân bằng **Private IPv4**, kết nối sẽ bị **treo/timeout** vì máy cá nhân không nằm trong mạng riêng (VPC) của AWS.
2. **Hành vi khi Stop & Start EC2 Instance:**
   - Khi thực hiện **Stop** rồi **Start** lại EC2 instance (lưu ý: khác với **Reboot**), **Public IPv4 sẽ bị đổi sang địa chỉ mới**, trong khi **Private IPv4 vẫn giữ nguyên**.
   - Nếu tiếp tục SSH bằng Public IP cũ sẽ thất bại; phải dùng Public IP mới.
3. **Cấp phát và gắn Elastic IP (Allocate & Associate Elastic IP):**
   - Vào mục **Network & Security -> Elastic IPs** -> nhấn **Allocate Elastic IP address** để lấy một địa chỉ IPv4 từ Amazon's pool.
   - Nhấn **Actions -> Associate Elastic IP address** -> chọn **Instance** (hoặc Network Interface) và chọn EC2 instance đang chạy.
   - Sau khi gắn, Public IPv4 của EC2 chính là địa chỉ Elastic IP đó. Khi **Stop** rồi **Start** lại EC2, địa chỉ Public IPv4 (Elastic IP) **vẫn được giữ nguyên không đổi**.

---

### 1.2. Chính sách tính phí Public IPv4 & Elastic IP (Lưu ý quan trọng)
- Hiện nay AWS tính phí cho mọi địa chỉ **Public IPv4** (bao gồm cả Public IPv4 thông thường gắn trên EC2 lẫn **Elastic IP** dù có đang gắn hay không gắn):
  - Mức phí: **`$0.005 / giờ`** (tương đương khoảng **`$3.50 / tháng`** cho mỗi địa chỉ Public IPv4).
  - Trong gói **AWS Free Tier**, bạn có **750 giờ/tháng** sử dụng Public IPv4 miễn phí (in-use public IPv4 address).
- **Quy trình dọn dẹp Elastic IP để không bị trừ tiền:**
  1. Chọn Elastic IP -> **Actions -> Disassociate Elastic IP address** (tháo khỏi EC2 instance).
  2. Chọn lại Elastic IP -> **Actions -> Release Elastic IP addresses** (trả lại địa chỉ IP về kho của AWS).
  3. **Terminate** EC2 instance nếu không còn sử dụng để không vượt quá 750 giờ/tháng.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | Okay, so let's have a look at the behaviors of IP in areas. | Được rồi, hãy cùng xem xét hành vi của các địa chỉ IP trên AWS. |
| `00:00:03` | So we have a public IPv4 for our instance, and this is the IPv4 we can use to SSH into our machine and it works great, okay? | Chúng ta có một địa chỉ Public IPv4 cho instance của mình, và đây là địa chỉ IPv4 chúng ta có thể dùng để SSH vào máy chủ và nó hoạt động rất tốt. |
| `00:00:13` | So once we're logged in, remember, we see that there is a private IP attached as a host name of my instance. | Khi đã đăng nhập vào bên trong, hãy nhớ rằng chúng ta thấy có một địa chỉ Private IP được gắn làm tên máy (hostname) của instance. |
| `00:00:20` | So once we are in, we can start using the private IP. But if we disconnect from our instance and we try to do the SSH command, | Khi đã ở bên trong mạng nội bộ, chúng ta có thể dùng Private IP. Nhưng nếu chúng ta ngắt kết nối khỏi instance và thử chạy lại lệnh SSH |
| `00:00:27` | but this time using the private IPv4 address, as we can see, it will not work well. | nhưng lần này lại dùng địa chỉ Private IPv4, như chúng ta có thể thấy, nó sẽ không hoạt động được. |
| `00:00:32` | Well let's have a look. So I'm going to press Enter. As you can see, this does not work. And why? | Hãy thử xem nhé. Tôi sẽ nhấn Enter. Như bạn thấy đấy, nó không kết nối được. Tại sao vậy? |
| `00:00:37` | Well, private IPv4s belong to a private network, but right now I'm not connected to the private network of AWS. | Bởi vì các địa chỉ Private IPv4 thuộc về một mạng riêng (private network), mà hiện tại máy tôi không kết nối vào mạng riêng của AWS. |
| `00:00:43` | I can only connect to AWS with the Internet. And this is why private IPs do not work. | Tôi chỉ có thể kết nối tới AWS thông qua mạng Internet. Và đó là lý do tại sao Private IP không hoạt động. |
| `00:00:48` | And this is why you have to use a public IP because the public IP allows you to access AWS from a public network, | Đó cũng là lý do bạn bắt buộc phải dùng Public IP, bởi vì Public IP cho phép bạn truy cập vào AWS từ một mạng công cộng, |
| `00:00:55` | and therefore the public network being the Internet. | mà mạng công cộng ở đây chính là Internet. |
| `00:00:58` | Okay, so now let's have a look at the behavior of our instance just to observe it once. When we start it, stop it and restart it. | Được rồi, bây giờ hãy cùng quan sát hành vi của instance khi chúng ta chạy, dừng (Stop) và bật lại (Start) nó. |
| `00:01:05` | So we're going to stop our instance and the instance is not stopping. And let's just save the IPv4 address right here just to have it on my screen. | Chúng ta sẽ dừng instance lại, và trước đó hãy lưu lại địa chỉ Public IPv4 hiện tại ngay trên màn hình để tiện đối chiếu. |
| `00:01:16` | So we're going to stop our instance. So my instance is now stopped and I'm going to start my instance, | Chúng ta tiến hành Stop instance. Bây giờ instance của tôi đã ở trạng thái Stopped và tôi sẽ nhấn Start lại instance, |
| `00:01:23` | which is different, by the way, from rebooting an instance. So you need to stop and start the instance to observe the behavior of the public IPv4 changing. | nhân tiện thì thao tác này khác với việc khởi động lại (Reboot) một instance nhé. Bạn cần phải Stop rồi Start lại instance thì mới quan sát được hiện tượng địa chỉ Public IPv4 bị thay đổi. |
| `00:01:31` | So now that I've stopped it and started it, in a few seconds, we're going to obtain a new public IPv4. | Bây giờ sau khi tôi đã Stop và Start lại nó, chỉ trong vài giây nữa chúng ta sẽ nhận được một địa chỉ Public IPv4 mới. |
| `00:01:39` | So here we go. This one right here, I'm going to copy it and paste it here. | Đây rồi. Địa chỉ mới ngay tại đây, tôi sẽ sao chép và dán nó vào đây. |
| `00:01:44` | And so as we can see, yes indeed, in this console, the two IPs are different. | Và như chúng ta có thể thấy trên màn hình terminal này, quả thực hai địa chỉ IP hoàn toàn khác nhau. |
| `00:01:49` | So if I use the previous IP to SSH, this is not going to go anywhere because my instance has changed its IPv4. | Vì vậy nếu tôi dùng địa chỉ IP cũ để SSH, lệnh sẽ không thể đi tới đâu cả vì instance của tôi đã đổi địa chỉ IPv4 rồi. |
| `00:01:56` | But if I use the new IP to do my SSH command, then I can SSH again in my instance. | Nhưng nếu tôi dùng địa chỉ IP mới cho lệnh SSH, tôi có thể SSH vào lại instance của mình bình thường. |
| `00:02:03` | But the private IP has not changed because it doesn't need to. | Tuy nhiên địa chỉ Private IP thì không hề thay đổi vì nó không cần phải đổi. |
| `00:02:06` | Okay, so how do we solve this problem? Because maybe we want to stop and start our instance, but we don't want the public IPv4 to change. | Vậy làm thế nào để chúng ta giải quyết vấn đề này? Bởi vì có thể chúng ta muốn Stop và Start instance nhưng không muốn địa chỉ Public IPv4 bị thay đổi. |
| `00:02:14` | In this case, what we have to use is an elastic IP. So right now you see elastic IP address here is zero. | Trong trường hợp này, thứ chúng ta phải sử dụng là một Elastic IP. Hiện tại bạn thấy mục Elastic IP address ở đây đang trống. |
| `00:02:21` | So on the left hand side you can find elastic IPs. I'm going to open this in a new tab. | Ở thanh menu bên trái, bạn có thể tìm thấy mục Elastic IPs. Tôi sẽ mở nó trong một tab mới. |
| `00:02:25` | And we're going to allocate a new IP address from Amazon's pool of IPv4 address. | Và chúng ta sẽ cấp phát (Allocate) một địa chỉ IP mới từ kho địa chỉ IPv4 của Amazon. |
| `00:02:31` | And what this will do is that it will create an IPv4 address that we own now at least for the time we rent it. | Thao tác này sẽ tạo ra một địa chỉ IPv4 mà chúng ta sở hữu ít nhất là trong khoảng thời gian chúng ta thuê nó. |
| `00:02:37` | And this can be allocated to a specific EC2 instance and they will keep the elastic IP as long as it's attached. | Địa chỉ này có thể được gán cho một EC2 instance cụ thể và instance đó sẽ giữ nguyên địa chỉ Elastic IP này chừng nào nó còn được gắn vào. |
| `00:02:45` | So now just a quick note about pricing of IPv4 addresses. | Bây giờ là một lưu ý nhanh về chi phí của các địa chỉ IPv4. |
| `00:02:49` | So now in AWS, if you use a public IPv4, or if you don't use a public IPv4, whereas it is a public IPv4 or an elastic IP, | Hiện nay trên AWS, dù bạn đang dùng hay không dùng một địa chỉ Public IPv4 — bất kể đó là Public IPv4 thông thường hay là một Elastic IP — |
| `00:03:00` | you have an hourly charge of about `$0.005` per hour, okay? | bạn sẽ bị tính phí theo giờ khoảng `$0.005` mỗi giờ, được chứ? |
| `00:03:05` | Which represents about `$3.50` every month for a public IPv4 if you use it or if you don't use it. | Tương đương khoảng `$3.50` mỗi tháng cho một địa chỉ Public IPv4 dù bạn đang gắn sử dụng hay để không. |
| `00:03:13` | So bottom line is you need to terminate your instances and your elastic IPs if you don't use them so that you don't pay that charge. | Vì vậy điểm mấu chốt là bạn cần phải Terminate các instance và giải phóng (Release) các Elastic IP nếu không sử dụng để không phải trả khoản phí đó. |
| `00:03:21` | So in your account, if you started with me, then you have 750 hours per month of free public IPv4 addresses. | Trong tài khoản của bạn, nếu bạn mới tạo tài khoản cùng tôi (Free Tier), bạn sẽ có 750 giờ mỗi tháng sử dụng địa chỉ Public IPv4 miễn phí. |
| `00:03:29` | So that means that if you go ahead and create EC2 instances, please make sure to terminate them, so that you don't go over the 750 hours per month of IPv4 and you'll be good to go. | Điều đó có nghĩa là nếu bạn tạo các EC2 instance, hãy nhớ Terminate chúng sau khi thực hành xong để không vượt quá 750 giờ Public IPv4 mỗi tháng, như vậy bạn sẽ hoàn toàn yên tâm không mất phí. |
| `00:03:41` | We can right click, we can do action, and associate elastic IP address. | Bây giờ chúng ta có thể nhấp chuột phải hoặc chọn Actions -> Associate Elastic IP address. |
| `00:03:47` | So if we do so, then we need to say what we want to attach it to. So is it an instance or a network interface? | Khi chọn mục này, chúng ta cần chỉ định muốn gắn nó vào đâu: vào một Instance hay một Network Interface (ENI)? |
| `00:03:52` | So it's going to be an instance. And I'm going to choose the instance that is running and then the private IP | Ở đây chúng ta chọn Instance. Tôi sẽ chọn instance đang chạy và chọn địa chỉ Private IP |
| `00:03:59` | to which to associate the elastic IP address. So there's only one private IP for my instance. So we're good to go. | mà chúng ta muốn liên kết với địa chỉ Elastic IP này. Instance của tôi chỉ có duy nhất một Private IP nên chúng ta có thể nhấn Associate ngay. |
| `00:04:04` | Okay, so we associate it. And now let's have a look at what happens. | Được rồi, chúng ta đã liên kết xong. Bây giờ hãy xem chuyện gì xảy ra. |
| `00:04:11` | So if we go back to our EC2 instance, I'm going to refresh this window and close these. | Quay trở lại màn hình EC2 instance, tôi sẽ làm mới (refresh) cửa sổ này. |
| `00:04:17` | So as you can see now, the public IPv4 address is now equal to the value of the elastic IP address. | Như bạn thấy bây giờ, địa chỉ Public IPv4 của máy đã bằng đúng giá trị của địa chỉ Elastic IP vừa gắn. |
| `00:04:24` | And if I scroll down and refresh this fully, as we can see now, the elastic IP addresses field also has an elastic IP address right here, which is a public address. | Và nếu tôi cuộn xuống dưới và làm mới toàn bộ, trường Elastic IP address hiện đã hiển thị địa chỉ Elastic IP ngay tại đây. |
| `00:04:37` | And now we can click on this elastic IP and this takes us directly into the elastic IP console from EC2, where we can get more information around this elastic IP. | Chúng ta có thể nhấp vào địa chỉ Elastic IP này và nó sẽ đưa chúng ta tới thẳng trang quản lý Elastic IP của EC2 để xem thêm thông tin chi tiết. |
| `00:04:49` | So this is good. So now let's have a look and see if that works. | Rất tốt. Bây giờ hãy thử kiểm tra xem nó hoạt động thế nào. |
| `00:04:51` | So we're going to copy the address right here, and I'm going to run the SSH command and this one will not work, so we have to use the new one. And yes, indeed we can do an SSH. | Chúng ta sao chép địa chỉ Elastic IP này và chạy lệnh SSH với địa chỉ mới. Vâng, chúng ta đã SSH vào thành công. |
| `00:05:02` | But now in case we stop the instance. So let's stop this instance and see what happens. | Bây giờ giả sử chúng ta dừng (Stop) instance này. Hãy nhấn Stop instance và xem điều gì xảy ra. |
| `00:05:10` | So as we can see now, the instance is in stop state, but it still has a public IPv4 because the elastic IP is still attached to it. | Như chúng ta thấy lúc này, dù instance đang ở trạng thái Stopped nhưng nó vẫn giữ nguyên địa chỉ Public IPv4 bởi vì Elastic IP vẫn đang được gắn vào nó. |
| `00:05:18` | So that means that if we start our instance again, then our instance is back in the running state and the elastic IP address is still attached and the public IPv4 has not changed. | Điều đó có nghĩa là nếu chúng ta Start lại instance một lần nữa, khi instance quay lại trạng thái Running thì địa chỉ Elastic IP vẫn được gắn ở đó và địa chỉ Public IPv4 hoàn toàn không bị thay đổi. |
| `00:05:29` | So we can also check this by doing one more time the SSH command. And yes, it works using the same command as before. | Chúng ta có thể kiểm chứng bằng cách chạy lại đúng lệnh SSH lúc nãy. Và vâng, nó hoạt động ngay với cùng câu lệnh cũ. |
| `00:05:35` | So to finish this, we can go into this elastic IP and we can disassociate it to remove it from our instance. | Để kết thúc bài thực hành này, chúng ta vào mục Elastic IP và chọn Disassociate để tháo nó khỏi instance. |
| `00:05:43` | And then to not leave it running, please make sure to release this elastic IP address, to not be billed for it. | Sau đó, để không bỏ quên gây phát sinh phí, hãy nhớ nhấn Release địa chỉ Elastic IP này để không bị tính tiền. |
| `00:05:50` | And then back into our EC2 instance. If we refresh it, it has obtained a new public IPv4 address because it has been released from the elastic IP. | Quay trở lại màn hình EC2 instance, khi làm mới lại trang, bạn sẽ thấy máy đã tự động nhận một địa chỉ Public IPv4 ngẫu nhiên mới sau khi tháo Elastic IP ra. |
| `00:05:58` | And to finish this hands-on, I can just terminate my instance and be good to go. | Và để hoàn tất bài thực hành này, tôi chỉ cần Terminate instance của mình là xong. |
| `00:06:02` | So that's it for this lecture. I hope you liked it, and I will see you in the next lecture. | Đó là tất cả nội dung của bài học này. Hy vọng bạn thích nó, và hẹn gặp lại bạn ở bài học tiếp theo. |
