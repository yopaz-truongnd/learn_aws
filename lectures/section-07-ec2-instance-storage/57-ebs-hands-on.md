# Bài 57: EBS Hands On

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `26098274`
- **Video gốc:** `CCP_-_EBS_-_Hands_On_v3.mp4`
- **Thời lượng:** `05:34`
- **Cheat sheet:** [topics/aws_storage.html](../../topics/aws_storage.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các thao tác thực hành với EBS Volume trên AWS Console
1. **Kiểm tra ổ đĩa EBS đang gắn trên EC2:**
   - Chọn EC2 instance -> tab **Storage** -> mục **Block devices** hiển thị ổ đĩa gốc (Root volume `8 GiB`, trạng thái `in-use`, thuộc tính `Delete on termination: Yes`).
2. **Tạo và gắn thêm EBS Volume thứ hai (Cùng AZ):**
   - Kiểm tra xem EC2 instance đang nằm ở Availability Zone nào (ví dụ: `eu-west-1b` trong tab **Networking**).
   - Vào menu bên trái **Elastic Block Store -> Volumes -> Create volume**.
   - Chọn loại `gp2`, dung lượng `2 GiB`, và **bắt buộc chọn đúng AZ `eu-west-1b`** trùng với EC2 instance.
   - Khi volume mới chuyển sang trạng thái `available`, chọn **Actions -> Attach volume** -> chọn EC2 instance đang chạy -> nhấn **Attach volume**.
   - Lúc này trong tab **Storage** của EC2 hiển thị **2 Block devices**: ổ Root `8 GiB` (`Delete on termination: Yes`) và ổ phụ `2 GiB` (`Delete on termination: No`).
3. **Thử tạo EBS Volume ở khác AZ (`eu-west-1a`):**
   - Tạo một ổ `2 GiB` ở `eu-west-1a`. Khi chọn **Actions -> Attach volume**, bạn sẽ **không tìm thấy EC2 instance** (vì EC2 nằm ở `eu-west-1b`), chứng minh thực tế rằng **EBS volume bị khóa chặt vào 1 Availability Zone**.
4. **Kiểm chứng hành vi khi Terminate EC2 Instance:**
   - Khi nhấn **Terminate** EC2 instance:
     - Ổ đĩa **Root volume (`8 GiB`)** tự động bị xóa biến mất.
     - Ổ đĩa **EBS phụ (`2 GiB`)** không bị xóa mà chuyển từ trạng thái `in-use` về trạng thái `available`.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So let's have a look at the EBS volumes attached to our instance. | Hãy cùng xem xét các ổ đĩa EBS đang được gắn vào EC2 instance của chúng ta. |
| `00:00:03` | So if you click on instance and then you go to the storage tab in here, you find that there is a root device and there's a block device on it. | Nếu bạn nhấp vào instance rồi chuyển sang tab **Storage** ở đây, bạn sẽ thấy thông tin Root device và danh sách Block devices bên dưới. |
| `00:00:13` | As you can see, we got one volume of eight gigabytes currently attached into our EC2 instance. | Như bạn thấy, hiện có một ổ đĩa dung lượng 8 GB đang được gắn vào EC2 instance của chúng ta. |
| `00:00:19` | So what I can do is I can click on this volume and it will take me into the volumes interface of AWS. | Tôi có thể nhấp vào ID của ổ đĩa này và nó sẽ đưa tôi tới giao diện quản lý **Volumes** của AWS. |
| `00:00:25` | And we can see that, yes, indeed, our volume exists and it's there. It's in use as shown here and it's attached to an instance right here. | Chúng ta thấy ổ đĩa của mình đang tồn tại ở đây với trạng thái `in-use` (đang sử dụng) và được gắn vào instance ngay tại đây. |
| `00:00:33` | So we have a different kind of console here and to access it, you can just go on the left hand side and click on volumes. | Để truy cập trang này bất kỳ lúc nào, bạn chỉ cần nhìn sang thanh menu bên trái và nhấp vào mục **Volumes**. |
| `00:00:39` | So as we can see, now we have one EBS of eight gigabytes and what I can do is I can create a second volume. | Hiện tại chúng ta có một ổ EBS 8 GB, và điều tôi có thể làm bây giờ là tạo thêm một ổ đĩa thứ hai. |
| `00:00:45` | So let me create a volume and I will have many options to choose from, GP2, GP3 and so on but I will just use GP2 of type of size two gigabytes. | Tôi nhấn **Create volume**; có nhiều loại ổ đĩa để chọn như `gp2`, `gp3`, v.v., ở đây tôi sẽ chọn loại `gp2` với dung lượng `2 GiB`. |
| `00:00:57` | And then for availability zone, I can choose the same one where my EC2 instance is. | Tiếp theo ở mục **Availability Zone**, tôi phải chọn đúng AZ nơi EC2 instance của tôi đang chạy. |
| `00:01:02` | So for this, I'm gonna go into my EC2 instance, in here and I will find which availability zone it is on. | Để kiểm tra, tôi quay lại tab EC2 instance và xem nó đang nằm ở Availability Zone nào. |
| `00:01:11` | So I scroll down, and it is going to be in the networking one. So I scroll down in the networking and here, availability zone, it says `eu-west-1b`. | Tôi chuyển sang tab **Networking**, cuộn xuống và thấy mục Availability Zone ghi là `eu-west-1b`. |
| `00:01:25` | Therefore, the volume I will create is going to be in `eu-west-1b` because the EBS volumes are bound by specific AZ. | Do đó, ổ đĩa tôi sắp tạo bắt buộc phải đặt ở `eu-west-1b`, bởi vì các ổ đĩa EBS bị ràng buộc vào một AZ cụ thể. |
| `00:01:34` | So that's good. I will have it done and create this volume. And now my volume is created. | Rất tốt, tôi chọn `eu-west-1b` và nhấn **Create volume**. Ổ đĩa của tôi đã được tạo. |
| `00:01:41` | And what I can do is if I can click on it, this one is currently not attached. Okay, so it's been creating so let me refresh this to see if it's created. | Ban đầu nó ở trạng thái `creating`, hãy làm mới (refresh) lại trang xem đã xong chưa. |
| `00:01:50` | Okay, it's available and it's not attached yet. So therefore, because it's available, what I can do is action and then I can attach the volume and we need to find an instance. | Được rồi, trạng thái đã chuyển sang `available` và chưa được gắn vào đâu cả. Bây giờ tôi chọn **Actions -> Attach volume** và chọn một instance. |
| `00:02:01` | So we have one running right here. And so we're going to attach this volume to my instance, click on attach volume and voila, our instance now has two EBS volumes attached to it. | Chúng ta có một instance đang chạy ngay tại đây. Tôi chọn nó, nhấn **Attach volume**, và xong! Instance của chúng ta hiện đã có 2 ổ đĩa EBS được gắn vào. |
| `00:02:10` | How do we know? Well, I can refresh this page, go to storage on my EC2 console, scroll down. | Làm sao để kiểm tra? Tôi làm mới lại trang EC2 Console, vào tab **Storage** và cuộn xuống dưới. |
| `00:02:19` | As you can see now for block devices, I have two block devices. I have the one of eight gigabytes and the one of two gigabytes. | Như bạn thấy trong mục **Block devices**, hiện tôi đã có 2 thiết bị lưu trữ khối: một ổ 8 GB và một ổ 2 GB. |
| `00:02:27` | To actually use this new block device, it's a bit more complicated and out of scope for this course, but you can go to format EBS volume attach EC2, | Để thực sự định dạng (format) và mount ổ đĩa mới này bên trong hệ điều hành Linux thì có thêm vài câu lệnh ngoài phạm vi bài thi này, nhưng bạn có thể tra tài liệu AWS *"Make an Amazon EBS volume available for use on Linux"* nếu muốn thử. |
| `00:02:47` | So now if I go into my volumes and I create a volume, I can create a volume of two gigabytes of GP2 but this time the AZ is going to be `eu-west-1a` and not `eu-west-1b`. | Bây giờ, nếu tôi quay lại mục **Volumes** và tạo thêm một ổ `gp2` dung lượng 2 GB nữa, nhưng lần này tôi cố tình chọn AZ là `eu-west-1a` thay vì `eu-west-1b` (tức là khác AZ với EC2 instance). |
| `00:03:02` | And the reason I do so is to show you that right now, we have three GP2 volumes. So let me refresh this. | Lý do tôi làm vậy là để cho bạn thấy chuyện gì xảy ra khi khác AZ. Hãy làm mới danh sách 3 ổ đĩa `gp2`. |
| `00:03:09` | So the last one is available and it's a different AZ, so `eu-west-1a`. And if I do actions and then attach volume, as you can see, I cannot attach it to my EC2 instance because my EC2 instance is in `eu-west-1b`. | Ổ đĩa thứ ba đang ở trạng thái `available` tại `eu-west-1a`. Khi tôi chọn **Actions -> Attach volume**, như bạn thấy, không có chiếc EC2 instance nào hiện ra trong danh sách để gắn cả vì EC2 của tôi nằm ở `eu-west-1b`. |
| `00:03:26` | And so therefore, we can see that the EBS volumes indeed are bound by a specific availability zone. | Qua đó chúng ta thấy rất rõ ràng rằng các ổ đĩa EBS thực sự bị ràng buộc chặt vào một Availability Zone cụ thể. |
| `00:03:33` | Lastly, what I can do is that I can take this volume, do action, delete volume, and it's gone. And that really shows you the power of the cloud. I can just request volumes, delete volumes right on the go in the matters of seconds. | Tôi sẽ chọn ổ đĩa ở `eu-west-1a` này và chọn **Actions -> Delete volume** để xóa nó đi ngay trong vài giây. |
| `00:03:47` | Okay, so we have our two EBS volumes in here and what I wanna show you now is a cool behavior. So what happens if I terminate my instance? | Bây giờ chúng ta còn 2 ổ EBS đang gắn vào EC2, và tôi muốn cho bạn quan sát một hành vi rất thú vị: điều gì sẽ xảy ra nếu tôi **Terminate** EC2 instance của mình? |
| `00:03:56` | Well remember, and I will show you again, this one root volume of eight gigabytes has the delete on termination attribute. | Hãy nhớ lại bài lý thuyết: ổ đĩa gốc (Root volume) 8 GB có thuộc tính `Delete on termination` được bật. |
| `00:04:03` | So how do we know? Well, if I go into my storage and then go to my block devices, into this table right here, and scroll all the way right, you see the first one has delete on termination `Yes` and the second one `No`. | Trong bảng **Block devices** ở tab **Storage**, khi kéo sang cột bên phải, bạn thấy ổ đầu tiên (8 GB) có `Delete on termination = Yes`, còn ổ thứ hai (2 GB) có `Delete on termination = No`. |
| `00:04:18` | So why this one is yes? Well, I don't know if you remember, but when you go through the process of launching an instance, okay? And then you scroll down to the storage, | Tại sao ổ đầu tiên lại là `Yes`? Bởi vì khi bạn khởi chạy (Launch) một EC2 instance mới và cuộn xuống mục **Storage -> Advanced**, |
| `00:04:32` | in here, if you click on advanced, you can see the fact that it is your root of eight gigabytes and by default, this delete on termination attribute is yes, which makes sense, but you could set it to no if you wanted to keep the root after terminating your instance. | bạn sẽ thấy đối với ổ Root 8 GB, thuộc tính `Delete on termination` mặc định được đặt là `Yes` (và bạn có thể đổi thành `No` nếu muốn giữ lại ổ Root sau khi hủy máy). |
| `00:04:51` | And so therefore, if I go ahead and terminate my instance which I will, so it says successfully terminated so it's going to really remove it from here. | Vì vậy bây giờ tôi sẽ tiến hành **Terminate** EC2 instance này. |
| `00:05:01` | I can go back into my EBS volumes. I can refresh them. And what's going to happen is that this one soon is going to be available so because it's going to be detached from my EC2 instance and then it's going to be terminated. | Quay lại danh sách **Volumes** và làm mới trang. Chuyện sẽ xảy ra là ổ 2 GB sẽ được tháo ra và chuyển về trạng thái `available`, trong khi ổ Root 8 GB sẽ bị xóa. |
| `00:05:19` | And here we go. So my eight gigabyte volume has now disappeared. Only my two gigabyte volume is left and if I go to my EC2 console, well, it says that my first instance has been terminated. | Và đây rồi! Ổ đĩa Root 8 GB đã hoàn toàn biến mất, chỉ còn lại duy nhất ổ đĩa 2 GB ở trạng thái `available` khi EC2 instance đã bị Terminate. |
| `00:05:29` | So that's it for this lecture. I hope you liked it and I will see you in the next lecture. | Đó là tất cả cho bài học này. Hy vọng bạn thích nó và hẹn gặp lại ở bài học tiếp theo. |
