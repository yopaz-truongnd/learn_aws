# Bài 61: AMI Hands On

- **Phần (Section):** Section 7: EC2 Instance Storage
- **Lecture ID:** `26098284`
- **Video gốc:** `CCP_-_EC2_-_AMI_Hands_On_v3.mp4`
- **Thời lượng:** `04:59`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Minh họa thực hành đóng gói phần mềm vào Custom AMI để tăng tốc khởi động
1. **Bước 1: Tạo EC2 Instance gốc và cài sẵn Apache (`httpd`):**
   - Khởi chạy EC2 `t2.micro` (Amazon Linux 2) với script **User Data** chỉ cài đặt và bật dịch vụ Apache Web Server (chưa tạo file `index.html`):
     ```bash
     #!/bin/bash
     yum update -y
     yum install -y httpd
     systemctl start httpd
     systemctl enable httpd
     ```
   - Chờ khoảng 1–2 phút để EC2 chạy xong User Data và truy cập `http://<Public-IP>` hiện trang Test Page của Apache.
2. **Bước 2: Tạo Custom AMI (`demo image`) từ EC2 Instance đang chạy:**
   - Chọn EC2 instance -> nhấp chuột phải chọn **Image and templates -> Create image**.
   - Đặt Image name: `demo image` -> nhấn **Create image**.
   - Vào menu bên trái **Images -> AMIs** để theo dõi trạng thái chuyển từ `Pending` sang `Available`.
3. **Bước 3: Khởi chạy EC2 Instance mới từ Custom AMI (`demo image`):**
   - Nhấn **Launch instances** -> tại phần chọn AMI, chuyển sang tab **My AMIs -> Owned by me** và chọn `demo image`.
   - Trong phần **User Data** của máy mới, vì `httpd` đã được cài sẵn trong `demo image`, ta chỉ cần truyền lệnh ghi file `index.html`:
     ```bash
     #!/bin/bash
     echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
     ```
   - **Kết quả:** Máy mới khởi chạy và hiển thị ngay trang web *"Hello World"* **nhanh hơn rất nhiều** vì không phải tốn thời gian `yum update` và `yum install httpd` lại từ đầu!

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00` | So let's go ahead and practice using AMIs. For this, I'm going to launch an instance, and I'm going to go into this new experience. | Bây giờ hãy cùng thực hành sử dụng AMI. Đầu tiên tôi sẽ khởi chạy một EC2 instance mới. |
| `00:00:09` | So I will scroll down. We'll choose Amazon Linux 2. I will scroll down again. We'll use the `t2.micro`. | Tôi cuộn xuống chọn Amazon Linux 2, loại máy `t2.micro`. |
| `00:00:16` | I will select the `ec2-tutorial` as my key pair but it doesn't really matter. | Tôi chọn key pair của mình (không quá quan trọng vì chúng ta không cần SSH trong bài này). |
| `00:00:20` | Then I will scroll down. I would edit the network settings and I will select an existing security group being my `launch-wizard-1` from before. | Tiếp theo tôi chỉnh sửa Network settings và chọn Security Group có sẵn từ trước là `launch-wizard-1` (đã mở cổng 80 HTTP). |
| `00:00:30` | Then we'll have the same storage and for advanced details, I will scroll down and I will go for user data, | Giữ nguyên cấu hình lưu trữ, cuộn xuống mục **Advanced details** tới ô **User data**, |
| `00:00:36` | but this time you're going to copy everything, but the last line. | nhưng lần này chúng ta sẽ sao chép toàn bộ script User Data ngoại trừ dòng cuối cùng. |
| `00:00:41` | So, in the first four lines, we actually install `httpd` which is the Apache web server. | Trong 4 dòng đầu tiên, chúng ta cài đặt và khởi chạy dịch vụ `httpd` (Apache web server). |
| `00:00:47` | In the last line, we create an index file but right now we don't want to create an index file, we want to do everything but that to create an AMI out of it. | Ở dòng cuối cùng là lệnh tạo file `index.html`, nhưng hiện tại chúng ta chưa muốn tạo file `index.html` mà chỉ muốn cài sẵn Apache để đóng gói thành một AMI. |
| `00:00:55` | So we just copy everything. Remember, the last line is the `systemctl` command. And then we launch our instance. | Vì vậy dòng cuối cùng trong User Data lúc này là lệnh `systemctl enable httpd`. Sau đó chúng ta nhấn **Launch instance**. |
| `00:01:05` | So our instance is launched and what's going to happen is that the instance is going to launch that's right here. And then it's going to run through the EC2 user data script and it's going to install the Apache web server. | Instance của chúng ta đang khởi chạy, và nó sẽ thực thi script EC2 User Data để cài đặt Apache web server. |
| `00:01:19` | So if I'm too quick and I try to open right now, this public IPv4 and try to enter into it, as you can see, it doesn't work. I'll get a connection refused and so on. | Nếu tôi mở địa chỉ Public IPv4 quá sớm ngay lúc này trên trình duyệt, nó sẽ báo lỗi từ chối kết nối (connection refused). |
| `00:01:35` | Because you need to give it a bit of time. Even if it says 'running', you need to give it time for the EC2 user data script to run for the first time. | Bởi vì ngay cả khi trạng thái báo `Running`, bạn vẫn cần đợi khoảng 1–2 phút để script EC2 User Data chạy xong lần đầu tiên. |
| `00:01:54` | So let me pause the video. And it took about two minutes, but now I have my test page and this is the basic page from the Apache web server. And therefore we are good to go. | Sau khoảng 2 phút chờ đợi, khi làm mới lại trang tôi đã thấy trang Test Page mặc định của Apache web server. Như vậy máy đã cài đặt xong. |
| `00:02:05` | So what we're going to do out of it is we're going to create an AMI because we want to just save the state of our EC2 instance and reuse that. | Bây giờ những gì chúng ta sẽ làm là tạo một **AMI** từ máy chủ này, vì chúng ta muốn lưu lại trạng thái đã cài sẵn Apache của EC2 instance để tái sử dụng. |
| `00:02:13` | So I right click and I will do image and templates and then I will create an image. | Tôi nhấp chuột phải vào instance và chọn **Image and templates -> Create image**. |
| `00:02:19` | So we'll call this one `demo image` and we're going to create our own AMI. | Chúng ta đặt tên là `demo image` để tạo AMI của riêng mình. |
| `00:02:25` | And then we have these settings right here. We'll just leave it as is. Go here and click on create image. | Giữ nguyên các thiết lập mặc định bên dưới và nhấn **Create image**. |
| `00:02:32` | So now what's going to happen is that an AMI is going to be created. So if I go to the left-hand side and click on AMIs, as we can see here, my `demo image` AMI is registered. | Bây giờ nếu nhìn sang thanh menu bên trái và nhấp vào mục **AMIs**, chúng ta thấy `demo image` đã được đăng ký. |
| `00:02:42` | And right now the status is `pending` because it is being created. So what I need to do is to be a little bit patient and wait for it to go into the available state. | Hiện tại trạng thái đang là `Pending` vì hệ thống đang tạo snapshot và đóng gói AMI. Chúng ta cần kiên nhẫn đợi một chút để nó chuyển sang trạng thái `Available`. |
| `00:02:52` | So my Amazon AMI is now created. And what I can do now is I can launch instances from this AMI by clicking here. | AMI của tôi hiện đã được tạo xong (`Available`). Bây giờ tôi có thể khởi chạy các instances mới trực tiếp từ AMI này bằng nút **Launch instance from AMI**, |
| `00:03:01` | Or if you are in the instance creation page, we can launch instances. And this one is called `From AMI`. | hoặc vào trang **Launch an instance** thông thường và đặt tên máy là `From AMI`. |
| `00:03:08` | And in here in the quick start we get access to the ones we know but you can also go into the `My AMIs` tab. | Tại phần chọn AMI, thay vì chọn trong Quick Start, bạn chuyển sang tab **My AMIs**. |
| `00:03:14` | Okay. And you have the ones owned by me and you can choose the `demo image` that you just created from before. | Trong mục **Owned by me**, bạn chọn chính bản `demo image` vừa tạo lúc nãy. |
| `00:03:20` | So in that case, you scroll down, you select a key pair or not, just up to you. Network settings, again, we edit them and we just select the existing `launch-wizard-1` security group. | Cuộn xuống dưới, chọn key pair, và trong phần Network settings chọn lại Security Group `launch-wizard-1`. |
| `00:03:32` | And what I'm going to do is that in the advanced, at the very bottom, I'm going to enter some user data. | Sau đó mở phần **Advanced details** ở dưới cùng và nhập đoạn script **User data** rút gọn. |
| `00:03:39` | So I copy the first three lines, okay. Which are starting with the hash. And then the last line, which is the `echo` on the new line. | Tôi chỉ giữ lại dòng khai báo `#!/bin/bash` và dòng cuối cùng là lệnh `echo "<h1>Hello World...</h1>" > /var/www/html/index.html`. |
| `00:03:47` | And so what we do is that we only just write a new file. So we don't need to reinstall `httpd` because this AMI already contains `httpd` which is why we will speed up in the boot up time. This is why you would create an AMI. | Như vậy chúng ta chỉ việc ghi thêm đúng 1 file `index.html` mới mà không cần phải cài đặt lại `httpd` nữa, bởi vì bản AMI này đã chứa sẵn `httpd` rồi — giúp tăng tốc thời gian khởi động lên rất nhiều. Đó chính là lý do thực tế người ta tạo Custom AMI! |
| `00:04:02` | So we launch an instance and now the instance is launched. So I can just click on it. This is the one `From AMI`. I need to wait for it to be fully created. | Nhấn **Launch instance** và chờ chiếc máy `From AMI` chuyển sang trạng thái `Running`. |
| `00:04:14` | My instance from my AMI is now running. I take the public IP address and then I see the 'Hello World' from this. | Ngay khi máy `From AMI` vừa báo `Running`, tôi sao chép địa chỉ Public IP mở lên trình duyệt và thấy ngay dòng chữ **"Hello World"** hiện ra tức thì! |
| `00:04:21` | And as you can see, this was much quicker because we didn't have to install `httpd` again. So this is the whole power of AMIs. | Như bạn thấy, quá trình này nhanh hơn rất nhiều vì chúng ta không phải tốn thời gian cài đặt lại `httpd`. Đó chính là sức mạnh của AMI. |
| `00:04:28` | And you can imagine, well, it could be just more than that. It could be security software, a lot of prerequisite software, and so on, you install it, it maybe it takes two, three minutes to do it. Then you package it as an AMI, and then you just start from the AMI, maybe do some end customization at the end but you have a much faster boot-up. | Bạn có thể hình dung trong thực tế có rất nhiều phần mềm bảo mật, thư viện phụ thuộc tốn hàng chục phút để cài đặt — bạn chỉ cần cài một lần rồi đóng gói thành AMI, sau đó mọi máy mới khởi chạy từ AMI sẽ sẵn sàng cực nhanh. |
| `00:04:47` | So that's it for this demo. Now to get back from this what you do is that you take your two instances and you can terminate them. And that's it. I will see you in the next lecture. | Để dọn dẹp sau bài demo này, bạn hãy chọn cả 2 EC2 instances và **Terminate** chúng đi. Hẹn gặp lại bạn ở bài học tiếp theo! |
