# Bài 52: Elastic Network Interfaces (ENI) - Hands On

- **Phần (Section):** Section 6: EC2 - Solutions Architect Associate Level
- **Lecture ID:** `26118774`
- **Video gốc:** `SAA_-_EC2_-_ENI_-_Hands_On_v3.mp4`
- **Thời lượng:** `05:23`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Quy trình thực hành tạo, gắn và di chuyển ENI giữa 2 EC2 Instances
1. **Khởi chạy 2 EC2 Instances trong cùng 1 AZ (`us-east-2a`):**
   - Mỗi instance khi khởi chạy mặc định có **1 Primary ENI** (trạng thái `in-use`), chứa `Public IPv4`, `Private IPv4`, và `Private IPv4 DNS`.
2. **Tạo một ENI độc lập (Secondary ENI):**
   - Vào **Network & Security -> Network Interfaces -> Create network interface**.
   - Nhập Description (`demo ENI`), chọn **Subnet** nằm trong **cùng AZ (`us-east-2a`)** với 2 EC2 instances.
   - Chọn **Auto-assign** cho Private IPv4 (hoặc tự chỉ định một IP tĩnh trong dải subnet) và chọn **Security Group**.
   - Sau khi tạo xong, `demo ENI` có trạng thái `available` và mang một địa chỉ Private IPv4 riêng.
3. **Gắn (Attach) và Di chuyển (Failover) ENI giữa 2 EC2 Instances:**
   - Chọn `demo ENI` -> **Actions -> Attach** -> chọn EC2 Instance số 1. Lúc này Instance số 1 có **2 ENIs** (1 Primary ENI + 1 Secondary `demo ENI` mang thêm 1 Private IPv4 phụ).
   - Để di chuyển sang Instance số 2: Chọn `demo ENI` -> **Actions -> Detach** (có thể tick **Force detach**) -> sau đó chọn **Actions -> Attach** -> gắn sang EC2 Instance số 2. Địa chỉ Private IPv4 của `demo ENI` lập tức chuyển sang Instance số 2.
4. **Hành vi khi Terminate EC2 Instances (Lưu ý thi SAA-C03):**
   - Khi **Terminate** cả 2 EC2 instances:
     - **2 Primary ENIs** được tạo tự động cùng lúc khởi chạy EC2 sẽ **tự động bị xóa theo** (bởi thuộc tính `Delete on termination = true` mặc định trên Primary ENI).
     - **Secondary ENI (`demo ENI`)** do bạn tạo thủ công và gắn vào sau sẽ **KHÔNG bị xóa** mà chuyển về trạng thái `available` (và việc giữ ENI không gắn Elastic IP hoàn toàn không tốn phí).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So let's practice elastic network interfaces, and to do so let's go ahead and launch two instances. | Bây giờ hãy cùng thực hành với Elastic Network Interfaces (ENI), và để làm điều đó chúng ta hãy khởi chạy 2 EC2 instances. |
| `00:00:05` | So I can just scroll down, Amazon Linux 2, `t2.micro`. I'll just choose whatever key pair, doesn't matter. | Tôi sẽ cuộn xuống chọn Amazon Linux 2, `t2.micro`. Tôi chọn một key pair bất kỳ, không quan trọng lắm. |
| `00:00:11` | For network settings, I will just use an existing security group which is my `launch-wizard-1`. | Đối với thiết lập mạng, tôi sẽ dùng một Security Group có sẵn là `launch-wizard-1`. |
| `00:00:17` | This is great. And then I will launch two instances in here, and then click on launch instances. | Rất tốt. Sau đó tôi nhập số lượng là 2 instances ở đây rồi nhấn **Launch instances**. |
| `00:00:24` | So what I wanna show you is that from these instances we're going to get these two, and under networking, if we scroll down, we're going to look at the network interfaces. | Điều tôi muốn cho bạn thấy là từ hai instances vừa tạo này, khi vào tab **Networking** và cuộn xuống dưới, chúng ta sẽ thấy mục **Network interfaces**. |
| `00:00:36` | So each of these instances is going to have one network interface, and we have an interface ID. So there's an ENI and an ID right here. | Mỗi instance trong số này sẽ có một card mạng (Network Interface), kèm theo một Interface ID (`eni-...`) ngay tại đây. |
| `00:00:43` | And each interface contains a public IPv4, a private IPv4 and a private IPv4 DNS. | Và mỗi interface chứa một địa chỉ Public IPv4, một Private IPv4 và một tên miền Private IPv4 DNS. |
| `00:00:50` | So as we can see, if we go on the left hand side, so on the two instances, we're gonna have two different network interfaces. | Như vậy trên hai instances chúng ta có hai Network Interfaces khác nhau. |
| `00:00:57` | And if you go on the left hand side, under network and security, we're also going to have the network interfaces. | Nếu bạn nhìn sang thanh menu bên trái dưới mục **Network & Security**, chúng ta cũng có mục **Network Interfaces**. |
| `00:01:04` | So here we can find the two ENIs, one of each is going to be attached to our EC2 instances, | Tại đây chúng ta tìm thấy 2 ENI, mỗi cái đang được gắn vào một trong hai EC2 instances của chúng ta, |
| `00:01:10` | and we can know it by going to the right hand side, and the status is `in-use`, and we can see that they are linked to different instance IDs. | và khi kéo sang bên phải, chúng ta thấy trạng thái (Status) là `in-use` và chúng được liên kết tới hai Instance ID khác nhau. |
| `00:01:19` | The one thing we can do is that we can create a new network interface. So in this instance, we can give our description. So `demo ENI`. | Một điều chúng ta có thể làm là tạo mới một Network Interface. Chúng ta đặt phần mô tả (Description) là `demo ENI`. |
| `00:01:29` | We can to select a subnet for our ENI to be in. So it is linked to a specific AZ, and I will choose the AZ my EC2 instances are in, so `us-east-2a`. | Chúng ta cần chọn một Subnet cho ENI này. Vì Subnet gắn liền với một AZ cụ thể, tôi sẽ chọn đúng AZ mà các EC2 instances của tôi đang nằm trong đó, tức là `us-east-2a`. |
| `00:01:43` | Then we want to auto assign a private IPv4, but we could also customize and say, which IPv4 we want within the subnets, so we'll use auto assign. | Tiếp theo chúng ta chọn tự động gán (Auto-assign) địa chỉ Private IPv4, hoặc bạn cũng có thể tùy chỉnh chỉ định cụ thể địa chỉ IPv4 nào trong Subnet; ở đây chúng ta chọn Auto-assign. |
| `00:01:53` | And then we can attach a security group to our ENI. So here we go and then create this network interface. | Sau đó chúng ta gắn một Security Group cho ENI này rồi nhấn **Create network interface**. |
| `00:02:00` | So now we have created a new network interface and it is right here, the `demo ENI`, and it is available. | Bây giờ chúng ta đã tạo xong một Network Interface mới nằm ngay đây (`demo ENI`), và trạng thái của nó là `available`. |
| `00:02:06` | So as we can see right now, we have created basically a secondary private IPv4. | Như bạn thấy, về cơ bản chúng ta vừa tạo ra một địa chỉ Private IPv4 phụ (secondary private IPv4). |
| `00:02:13` | And what we can do is that we can attach this to our instance so we can do action, attach and choose an instance to attach it to. So I'll choose this one and attach it. | Bây giờ chúng ta có thể gắn ENI này vào instance bằng cách chọn **Actions -> Attach** và chọn một EC2 instance. Tôi sẽ chọn instance đầu tiên và nhấn Attach. |
| `00:02:27` | And now if we go to our instance and refresh, let's go back to our instances and refresh. So we'll go into networking and scroll down. | Quay trở lại màn hình Instances và làm mới trang, vào tab **Networking** và cuộn xuống dưới. |
| `00:02:38` | So this one, I got lucky. This one has two network interfaces. | Instance này hiện đã có 2 Network Interfaces. |
| `00:02:43` | And one of them was the primary one, which gives us a public IPv4 and a private IPv4. And this `demo ENI` gives us a secondary, private IPv4. | Một cái là Primary ENI ban đầu cung cấp Public IPv4 và Private IPv4 chính; còn chiếc `demo ENI` cung cấp thêm cho chúng ta một địa chỉ Secondary Private IPv4. |
| `00:02:53` | So why would you do this? Well, this ENI we have control over, so we could take it, and we could actually move it from one EC2 instance to another, | Tại sao bạn lại làm như vậy? Bởi vì chiếc ENI phụ này nằm dưới quyền kiểm soát độc lập của chúng ta, nên chúng ta có thể tháo nó ra và di chuyển từ EC2 instance này sang EC2 instance khác, |
| `00:03:02` | imagining that the two EC2 instances are running the same application and we want to access them using the private IPv4. Then we can move the ENI over. | hãy tưởng tượng hai EC2 instances đang chạy cùng một ứng dụng và các client truy cập vào thông qua địa chỉ Private IPv4 đó — khi máy 1 gặp sự cố, chúng ta chỉ cần chuyển ENI sang máy 2. |
| `00:03:10` | And the reason for doing so is that we can do a very quick and easy network failover between the two instances by moving an ENI, because we can attach an IPv4 from one instance to another. | Lý do thực hiện việc này là để chuyển đổi dự phòng mạng (network failover) cực kỳ nhanh chóng và dễ dàng giữa hai instances bằng cách di chuyển ENI mang theo địa chỉ Private IPv4 đó. |
| `00:03:22` | So let's do a demo of that. So I'm going to take this ENI. I'm going to detach it. Yes, detach. | Hãy làm thử ngay nhé. Tôi chọn chiếc `demo ENI` này và nhấn **Detach**. |
| `00:03:29` | And then once it's going to be detached in a few seconds we can reattach it to the other instance, and to do so, by the way, maybe it's going to be an issue to detach it like this. | Sau khi nó được tháo ra trong vài giây, chúng ta có thể gắn lại nó sang instance còn lại. Nếu tháo thông thường mất thời gian, |
| `00:03:41` | So what I can do is just click on it, and to action detach with a force detach. So here we go. | tôi có thể chọn nó trong danh sách ENI và chọn **Actions -> Detach** kèm tùy chọn **Force detach**. |
| `00:03:50` | So after refresh, all the error messages are gone. We can do action, attach, and then we can choose the other instance to attach it to, | Sau khi làm mới trang, chúng ta chọn **Actions -> Attach**, rồi chọn chiếc EC2 instance thứ hai để gắn vào, |
| `00:04:00` | so then make sure yes, that's the other one. So I'm going to attach it to the other instance and now it's being attached. | kiểm tra chắc chắn đúng là máy thứ hai rồi nhấn Attach. |
| `00:04:05` | And so, as we can see now, if I refresh this, from two network interfaces, there's going to be only one. | Bây giờ nếu tôi làm mới lại thông tin máy thứ nhất, từ 2 Network Interfaces giờ chỉ còn lại 1. |
| `00:04:11` | And the other instance now has two network interfaces. And this `demo ENI` has moved to my other instance, | Còn máy thứ hai bây giờ đã có 2 Network Interfaces, chiếc `demo ENI` đã được chuyển sang máy thứ hai thành công, |
| `00:04:17` | so we can see how we could do some failover between the instances with the ENI, which I think is really, really cool, but it is advanced, okay. | qua đó chúng ta thấy rõ cách thực hiện failover giữa các instances bằng ENI — một kỹ thuật nâng cao rất thú vị. |
| `00:04:27` | So finally, if we go ahead and terminate these instances, so let's terminate them and see what happens. | Cuối cùng, nếu chúng ta tiến hành Terminate cả hai instances này, hãy xem điều gì sẽ xảy ra với các ENIs. |
| `00:04:35` | So they're shutting down, and now from the ENIs, what do you think is going to happen? | Hai máy đang tắt dần. Theo bạn điều gì sẽ xảy ra với 3 chiếc ENIs của chúng ta? |
| `00:04:39` | So we have three ENI right now, two were created alongside my EC2 instances, and one was created manually. | Hiện tại chúng ta có 3 ENIs: 2 cái được tạo tự động cùng lúc với 2 EC2 instances, và 1 cái được tạo thủ công. |
| `00:04:45` | Well, maybe you guess right? So what's going to happen is that my ENI that was created manually is going to stay. | Có lẽ bạn đã đoán đúng! Chiếc ENI được tạo thủ công (`demo ENI`) sẽ vẫn được giữ lại. |
| `00:04:51` | Whereas the two ENIs that were created alongside the instances are going to be automatically deleted. | Trong khi đó, 2 chiếc Primary ENI được tạo tự động kèm theo 2 instances sẽ tự động bị xóa đi. |
| `00:04:57` | So by creating your own ENIs, you have more control over your private IPv4s, and more control over your networking. And that could be a helpful in some type of advanced use cases. | Vì vậy, bằng cách tự tạo ENI riêng, bạn có quyền kiểm soát tốt hơn đối với địa chỉ Private IPv4 và cấu hình mạng trong các trường hợp nâng cao. |
| `00:05:08` | So we can see when ENI is gone and the other one should be gone very soon. | Chúng ta thấy một ENI đã biến mất và cái thứ hai cũng sắp được xóa xong. |
| `00:05:13` | So that's it for this hands-on. You can leave the ENI on if you want, or you can delete it. It will not cost you any money. | Đó là tất cả cho bài thực hành này. Bạn có thể giữ lại chiếc `demo ENI` hoặc xóa nó đi tùy ý, việc để ENI trống không hề tốn chi phí nào cả. |
| `00:05:20` | So that's it for this hands-on. I hope you liked it. And I will see you in the next lecture. | Hy vọng bạn thích bài thực hành này và hẹn gặp lại ở bài học tiếp theo. |
