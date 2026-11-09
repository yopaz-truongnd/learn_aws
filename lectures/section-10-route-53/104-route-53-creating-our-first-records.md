# Bài 104: Route 53 - Creating our first records (Tạo bản ghi DNS đầu tiên trong Route 53)

- **Section:** Phần 10 - Route 53
- **Lecture ID:** `28384312`
- **Video:** `SAA_-_Route_53_-_First_Records_v2.mp4`
- **Thời lượng:** `03:56`
- **Cheat sheet:** [topics/aws_route53.html](../../topics/aws_route53.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Tạo bản ghi `A` đầu tiên trong Hosted Zone
- Vào **Hosted Zone** của tên miền (ví dụ: `stephanetheteacher.com`) -> nhấn **Create record**:
  - **Record name:** `test.stephanetheteacher.com`
  - **Record type:** `A` – Routes traffic to an IPv4 address and some AWS resources.
  - **Value:** `11.22.33.44` (IPv4 giả định để kiểm thử phản hồi DNS).
  - **TTL (Time to Live):** `300` giây (mặc định).
  - **Routing policy:** `Simple routing`.

### 1.2. Kiểm tra phân giải DNS bằng dòng lệnh (`nslookup` & `dig`)
- Mặc dù địa chỉ IP `11.22.33.44` không có Web Server thực tế đang chạy (nên mở trên trình duyệt sẽ báo lỗi kết nối), việc phân giải DNS ở tầng dưới vẫn hoạt động bình thường.
- Có thể kiểm tra trên máy cá nhân (Windows dùng `nslookup`, macOS/Linux dùng `dig`) hoặc mở **AWS CloudShell**:
  - Cài đặt bộ công cụ DNS trên Amazon Linux trong CloudShell:
    ```bash
    sudo yum install -y bind-utils
    ```
  - Kiểm tra bằng `nslookup`:
    ```bash
    nslookup test.stephanetheteacher.com
    ```
  - Kiểm tra bằng `dig` (hiển thị chi tiết `ANSWER SECTION`, loại bản ghi `A`, giá trị **TTL** đang đếm ngược và địa chỉ IP trả về):
    ```bash
    dig test.stephanetheteacher.com
    ```

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
|---|---|---|
| `00:00:00` | So now let's go ahead and create our first records in Route 53. | Bây giờ chúng ta hãy bắt đầu tạo những bản ghi đầu tiên trong Route 53. |
| `00:00:04` | So I'm going to go into my hosted zone, and in there I'm going to create some simple records. So let's have a look. | Tôi sẽ vào Hosted Zone của mình, và tạo một vài bản ghi đơn giản. Hãy cùng xem nhé. |
| `00:00:10` | We're going to create a record by clicking on here. And in here, I can just have a record name. | Chúng ta tạo bản ghi bằng cách nhấp vào nút **Create record** ở đây. Tại đây tôi có thể nhập tên bản ghi (Record name). |
| `00:00:15` | So we want it to be test.stephanetheteacher.com. But you can enter anything you want here. This is how you would create your domain names. | Chúng ta muốn đặt là `test.stephanetheteacher.com`. Bạn có thể nhập bất cứ tên gì bạn muốn tại đây. Đó là cách bạn tạo các tên miền phụ. |
| `00:00:23` | Now you have to specify the record type. So you can see there's a lot of record types in here, but for now we'll keep it simple. We'll keep it as an A record. | Tiếp theo bạn phải chỉ định loại bản ghi (**Record type**). Có rất nhiều loại bản ghi ở đây, nhưng hiện tại chúng ta sẽ giữ ở mức đơn giản là bản ghi **A** (A record). |
| `00:00:31` | And which is to route an IPv4 address into a domain name, to an IPv4 address. | Bản ghi A dùng để ánh xạ một tên miền sang một địa chỉ IPv4. |
| `00:00:36` | So the answer is going to be value is 11.22.33.44. Which is just a value we want to have, and this is not a domain, an IP we own right now, but just to show you just a random value. | Giá trị (**Value**) trả về sẽ là `11.22.33.44`. Đây chỉ là một giá trị ngẫu nhiên mà chúng ta nhập vào để minh họa, không phải là một IP mà chúng ta thực sự sở hữu. |
| `00:00:48` | Later on, we'll be routing to a real EC2 instance. Okay. | Lát nữa, chúng ta sẽ định tuyến tới một EC2 instance thực tế. |
| `00:00:53` | TTL is time to live. We'll leave it as 300 seconds right now. And the routing policy will have a look at it later on as well. We'll leave everything as simple routing. Okay. | **TTL** là Time to Live, chúng ta sẽ để mặc định là `300` giây lúc này. Phần **Routing policy** chúng ta cũng sẽ tìm hiểu sau, hiện tại cứ để là **Simple routing**. |
| `00:01:02` | So let's go ahead and create this record. And now my record has been successfully created. | Hãy nhấn tạo bản ghi này. Và bây giờ bản ghi của tôi đã được tạo thành công. |
| `00:01:08` | So the idea is that if I go to test.stephanetheteacher.com, it is going to ask my hosted zone. What is the value of that? And the zone is going to say, well, the value of it is 11.22.33.44. | Ý tưởng là nếu tôi truy cập `test.stephanetheteacher.com`, hệ thống sẽ hỏi Hosted Zone của tôi giá trị của tên miền đó là gì, và Hosted Zone sẽ trả lời rằng giá trị là `11.22.33.44`. |
| `00:01:22` | So if you try it to do it with a web browser, so if you take your browser and you open it and you press enter, and it's not going to show you many things, because right now we don't have 11.22.33.44, there's probably no server that exists with that IP as well. | Nếu bạn thử mở URL này bằng trình duyệt web và nhấn Enter, nó sẽ không hiển thị được trang web nào cả vì hiện tại chúng ta không sở hữu IP `11.22.33.44` và có lẽ cũng không có Web Server nào đang chạy ở IP đó. |
| `00:01:38` | And if I try to just access this URL, it doesn't work. Okay. So what we want to know is what is going on behind the scenes. | Truy cập URL trên trình duyệt sẽ không hoạt động. Vậy điều chúng ta muốn kiểm tra là những gì đang diễn ra ở phía hậu trường (tầng DNS). |
| `00:01:44` | And so for this, we're going to type some command lines. Now you can be using your command line on your Windows laptop, or your Mac, | Để làm điều đó, chúng ta sẽ gõ một vài lệnh trên dòng lệnh. Bạn có thể dùng cửa sổ dòng lệnh trên máy tính Windows hoặc Mac của mình, |
| `00:01:50` | but because I want everyone to follow the same way as me, I'm going to show you how to do it using the CloudShell environment in AWS. | nhưng vì tôi muốn mọi người đều có thể thực hiện giống hệt nhau, tôi sẽ hướng dẫn bạn sử dụng môi trường **AWS CloudShell**. |
| `00:01:57` | So let me open the management console, and then I'm going to click here to open CloudShell and CloudShell is going to allow me to do some commands using a standard Linux command line interface. Okay. | Tôi mở Management Console, nhấp vào biểu tượng trên thanh công cụ để mở **CloudShell**. CloudShell cho phép tôi chạy các câu lệnh bằng giao diện dòng lệnh Linux tiêu chuẩn. |
| `00:02:09` | But this is fine, if you want to just do it with your own terminal on Windows or on Mac. | Tuy nhiên bạn hoàn toàn có thể chạy trực tiếp trên Terminal của Windows hoặc Mac nếu muốn. |
| `00:02:14` | Okay. So my terminal is now ready. And if you're on Windows, the nslookup command is going to work. If you're on Mac, the dig command is going to work as well. | Được rồi, Terminal của tôi đã sẵn sàng. Nếu bạn dùng Windows, lệnh `nslookup` sẽ hoạt động sẵn. Nếu bạn dùng Mac, lệnh `dig` cũng hoạt động sẵn. |
| `00:02:22` | But as you can see, these commands are not found on my CloudShell. So I need to install them. | Nhưng như bạn thấy, các lệnh này chưa được cài sẵn trên CloudShell của tôi. Vì vậy tôi cần cài đặt chúng. |
| `00:02:26` | So I do `sudo yum install -y bind-utils`. And it's going to install both the nslookup and the dig commands on my CloudShell. | Tôi chạy lệnh `sudo yum install -y bind-utils`. Lệnh này sẽ cài đặt cả hai công cụ `nslookup` và `dig` lên CloudShell. |
| `00:02:39` | So let's clear the screen. And now let's try to do `nslookup test.stephanetheteacher.com`. | Hãy xóa màn hình (`clear`). Bây giờ hãy thử chạy lệnh `nslookup test.stephanetheteacher.com`. |
| `00:02:48` | And as you can see, I get an answer, which is that test.stephanetheteacher.com is going to 11.22.33.44, which is corresponding to what is happening right here, which is cool. | Như bạn thấy, tôi nhận được câu trả lời rằng `test.stephanetheteacher.com` trỏ tới `11.22.33.44`, khớp hoàn toàn với bản ghi chúng ta vừa tạo. Rất tuyệt. |
| `00:03:01` | And I personally like the dig command a little bit more because I'm more familiar with it, | Cá nhân tôi thích lệnh `dig` hơn một chút vì tôi quen dùng nó hơn. |
| `00:03:05` | but if you type `dig` and then the URL that you have, okay. And press enter, you're going to see that I have the wrong command... so `stephanetheteacher.com`, so let's clear this screen and then retype the command. | Nếu bạn gõ `dig` kèm theo tên miền (không có `http://`), để tôi xóa màn hình và gõ lại lệnh `dig test.stephanetheteacher.com`. |
| `00:03:20` | Okay. What here we're going to see is that we have the ANSWER SECTION and says, `test.stephanetheteacher.com` is an A record, and this is the value of the record. | Tại đây chúng ta thấy phần **ANSWER SECTION** hiển thị `test.stephanetheteacher.com` là một bản ghi **A**, cùng với giá trị IP của bản ghi đó (`11.22.33.44`). |
| `00:03:30` | So I like it better, because it shows you the TTL, as we'll see later on, and also shows you the A record, the fact that it's an A record. Okay. | Tôi thích lệnh `dig` hơn vì nó hiển thị cả thông số **TTL** (như chúng ta sẽ học ở bài sau) và cho biết rõ loại bản ghi là `A`. |
| `00:03:39` | So we have created our first Route 53 record, and we have been able to query it using a terminal, which is cool. | Vậy là chúng ta đã tạo xong bản ghi Route 53 đầu tiên và truy vấn thành công nó từ Terminal. |
| `00:03:45` | Obviously loading it from a webpage doesn't work right now, but we'll see how we can do it later on when we have a real server. | Tất nhiên việc tải trang web trên trình duyệt hiện chưa hoạt động, nhưng chúng ta sẽ làm điều đó ngay sau đây khi thiết lập máy chủ EC2 thực tế. |
| `00:03:53` | So I hope you liked this lecture and I will see you in the next lecture. | Hy vọng bạn thích bài giảng này và hẹn gặp lại trong bài học tiếp theo. |
