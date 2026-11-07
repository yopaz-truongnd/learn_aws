# Bài 74: Application Load Balancer (ALB) - Hands On - Part 2 (Thực hành ALB - Phần 2)

- **Phần (Section):** Phần 8: High Availability and Scalability: ELB & ASG
- **Mã bài học (Lecture ID):** `26099120`
- **Tệp video:** `SAA_-_ELB_-_Application_Load_Balancer_Hands_On_Part_2_v8.mp4`
- **Thời lượng:** `05:37`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Thắt chặt bảo mật mạng với Security Group Referencing
- **Vấn đề:** Ở Phần 1, EC2 instances dùng Security Group `launch-wizard-1` cho phép HTTP (`80`) từ `0.0.0.0/0`. Điều này khiến người dùng có thể lách qua ALB để truy cập trực tiếp vào Public IP của EC2 instance.
- **Giải pháp chuẩn SAA-C03:**
  - Chỉnh sửa Inbound Rule của EC2 Security Group (`launch-wizard-1`): Xóa rule cho phép HTTP từ `0.0.0.0/0`, thêm rule mới cho phép **HTTP (Port 80)** nhưng phần **Source** chọn **Security Group của ALB (`demo-sg-load-balancer`)**.
  - **Kết quả:** Khi truy cập trực tiếp bằng Public IP của EC2 -> **Connection Timed Out**. Khi truy cập qua DNS của ALB -> **Hoạt động bình thường**.

---

### 1.2. Cấu hình ALB Listener Rules nâng cao
Trong phần **Listeners -> View/edit rules** của ALB, ngoài **Default Rule** (luôn chạy cuối cùng nếu không khớp rule nào khác), ta có thể thêm các **Custom Listener Rules** (tối đa hàng trăm rules):
- **1. Conditions (Điều kiện khớp request):**
  - `Host header` (ví dụ: `*.example.com`, `myapp.example.com`)
  - `Path` (ví dụ: `/error`, `/users`, `/posts`)
  - `HTTP request method` (`GET`, `POST`, ...)
  - `Source IP` (lọc theo dải CIDR của người gửi)
  - `HTTP header` & `Query string`
- **2. Actions (Hành động khi khớp điều kiện):**
  - `Forward to target groups`: Chuyển tiếp tới 1 hoặc nhiều Target Groups (có thể chia trọng số).
  - `Redirect to...`: Chuyển hướng sang một URL/URI khác, đổi giao thức HTTP -> HTTPS, trả về mã `301`/`302`.
  - `Return fixed response`: Trả về trực tiếp một phản hồi cố định ngay từ ALB mà không cần gọi xuống EC2 (ví dụ: trả về mã `404 Not Found` với nội dung `text/plain`: `"Not found, custom error"` khi truy cập đường dẫn `/error`).
- **3. Priority (Độ ưu tiên):**
  - Giá trị từ **`1` đến `50,000`**.
  - **Số càng nhỏ thì độ ưu tiên càng cao** (`1` là ưu tiên cao nhất, được đánh giá trước tiên).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00.000` | So let's have a look at a few more advanced concepts for our load balancer. Number one is around network security. | Hãy cùng xem xét một vài khái niệm nâng cao hơn cho bộ cân bằng tải của chúng ta. Đầu tiên là về bảo mật mạng (network security). |
| `00:00:07.110` | So currently we access this load balancer through a security group here. This is my load balancer security group. And then we access our EC2 instances through their own security group. | Hiện tại chúng ta truy cập bộ cân bằng tải này thông qua một Security Group ở đây (Security Group của Load Balancer). Và sau đó chúng ta truy cập các EC2 instance thông qua Security Group riêng của chúng. |
| `00:00:20.100` | So right now if I look at the public IP and access it, as you can see I can access my EC2 instance directly or I can access it, of course, through my load balancer. | Ngay lúc này, nếu tôi lấy địa chỉ Public IP của EC2 và truy cập nó, như bạn thấy tôi có thể truy cập trực tiếp vào EC2 instance hoặc tất nhiên là truy cập thông qua bộ cân bằng tải. |
| `00:00:30.870` | But it may be preferable to only access my EC2 instance through my load balancer. So how do we do this? | Nhưng tốt hơn hết là chúng ta chỉ cho phép truy cập vào EC2 instance thông qua bộ cân bằng tải mà thôi. Vậy làm thế nào để thực hiện điều này? |
| `00:00:37.950` | Well under instances, let's go for Security Groups, so right here. And we're going to look at the launch-wizard-1 security group. | Dưới mục Instances, hãy vào phần Security Groups ngay tại đây. Chúng ta sẽ xem xét Security Group `launch-wizard-1`. |
| `00:00:47.550` | And in here for the inbound rules, we're going to edit them and we're going to look at the HTTP rule. Right now we allow everything from everywhere on this security group. | Trong phần Inbound rules, chúng ta nhấn chỉnh sửa (Edit inbound rules) và nhìn vào quy tắc HTTP. Hiện tại chúng ta đang cho phép mọi lưu lượng HTTP từ bất kỳ đâu (`0.0.0.0/0`). |
| `00:00:58.410` | But what we wanna say is that no, the only traffic allowed into our EC2 instance should be traffic coming from the load balancer. | Nhưng điều chúng ta muốn quy định là: không, lưu lượng duy nhất được phép đi vào EC2 instance của chúng ta phải là lưu lượng đến từ bộ cân bằng tải. |
| `00:01:06.420` | So how do we change this? Well, let's first delete this rule. You have to first delete it and then you add a new rule. And so again, we want HTTP. | Làm sao để thay đổi? Trước tiên hãy xóa quy tắc cũ đi, sau đó nhấn thêm quy tắc mới (Add rule) và chọn lại giao thức HTTP. |
| `00:01:15.090` | But this time instead of having a CIDR block, you can scroll down and you can see that you can have security groups in there. So the security group we want to allow in is the security group of my load balancer. | Nhưng lần này, thay vì nhập một dải CIDR block, bạn có thể cuộn xuống và thấy danh sách các Security Group. Security Group mà chúng ta muốn cho phép đi vào chính là Security Group của bộ cân bằng tải (`demo-sg-load-balancer`). |
| `00:01:28.140` | So if you just type load as well it is going to filter the list. So then you select the security group of the load balancer. | Bạn chỉ cần gõ chữ `load` để lọc danh sách, sau đó chọn Security Group của bộ cân bằng tải. |
| `00:01:35.160` | And the effect of this is that if we save this rule and have a look at it, now if we have a look at our EC2 instance directly and I refresh this page, as you can see it's timing out | Kết quả của việc này là khi chúng ta lưu quy tắc lại, bây giờ nếu tôi quay sang tab truy cập trực tiếp vào Public IP của EC2 instance và nhấn refresh, như bạn thấy nó đang bị chờ quá hạn (timing out) |
| `00:01:48.210` | because it's not being able to access the instance because I'm not allowed to access directly the instance. | bởi vì trình duyệt của tôi không còn được phép kết nối trực tiếp tới EC2 instance nữa. |
| `00:01:54.570` | But if you refresh the load balancer, well the load balancer can still access my instances because in the rule that we have created in our security group, we allow inbound coming from the security group of the application load balancer. So here we have tightened network security. | Nhưng nếu bạn làm mới (refresh) tab của bộ cân bằng tải, bộ cân bằng tải vẫn truy cập được các instance của tôi bình thường, vì trong quy tắc Security Group mới tạo, chúng ta đã cho phép lưu lượng Inbound đến từ Security Group của ALB. Như vậy chúng ta đã thắt chặt bảo mật mạng thành công. |
| `00:02:16.050` | The second thing I want to show you is around application load balancer rules. So currently if you go into this ALB right here, and we go under listeners and I click on it. | Điều thứ hai tôi muốn chỉ cho bạn là về các quy tắc (rules) của Application Load Balancer. Nếu bạn vào ALB này, chuyển sang tab Listeners và nhấp vào listener hiện tại. |
| `00:02:27.270` | So as you can see I have my listener right here. There are some details over it and then I scroll down and we have the rules, listener rules. So here we can add some rules. | Bạn sẽ thấy thông tin chi tiết của Listener, và khi cuộn xuống dưới chúng ta có phần Listener rules. Tại đây chúng ta có thể thêm các quy tắc mới. |
| `00:02:37.020` | So we have the default rule right now which is saying that, "Hey, for every request, send it to my demo target group for my ALB." But we can add rules and make it as complex as we want. | Hiện tại chúng ta đang có quy tắc mặc định (Default rule) nói rằng: "Với mọi yêu cầu, hãy gửi nó tới `demo-tg-alb`." Nhưng chúng ta có thể thêm các quy tắc riêng phức tạp tùy ý. |
| `00:02:47.160` | So this one is going to be a DemoRule, that's the name I want to give it. And next we need to add conditions. | Tôi nhấn Add rule và đặt tên cho quy tắc này là `DemoRule`. Tiếp theo chúng ta cần thêm các điều kiện (Conditions). |
| `00:02:54.060` | So conditions is what do we want to filter in terms of requests for this rule? So do we want to look at host headers or, for example, have a look at if we are on the *.example.com or myapp.example.com or whatever you want. | Điều kiện là những tiêu chí chúng ta muốn dùng để lọc yêu cầu cho quy tắc này. Ví dụ chúng ta có thể kiểm tra `Host header` xem người dùng đang gọi vào `*.example.com` hay `myapp.example.com`. |
| `00:03:09.270` | Path is for the path. So we'll use /error and saying, "Okay if in the path we have /error then this rule should come in." | Hoặc lọc theo `Path` (đường dẫn). Chúng ta sẽ dùng đường dẫn `/error`, nghĩa là nếu trong đường dẫn URL có `/error` thì quy tắc này sẽ được kích hoạt. |
| `00:03:16.410` | We can also have the HTTP request method to be GET or POST whatever you want. You can filter and condition based on the source IP and then you can have query string and HTTP header as well. | Chúng ta cũng có thể lọc theo phương thức HTTP (`GET`, `POST`,...), lọc dựa trên địa chỉ `Source IP`, hoặc dựa trên `Query string` và `HTTP header`. |
| `00:03:27.960` | So, quite a lot of different possibilities but for now I'm going to use path and the path is going to be /error. Okay, confirm. | Có rất nhiều khả năng kết hợp khác nhau, nhưng hiện tại tôi sẽ chọn `Path` với giá trị là `/error` và nhấn Confirm. |
| `00:03:36.780` | So we can add multiple conditions if we wanted to. Right now in the rules limit you can see the types of limits you can have. So let's click on Next. We have one condition, that's enough. | Chúng ta có thể thêm nhiều điều kiện cùng lúc nếu muốn. Ở đây một điều kiện là đủ rồi, hãy nhấn Next. |
| `00:03:46.050` | And then what is the action? So once we match on the condition, what do we want to do with it? Do we want to forward to specific target groups? | Tiếp theo là Hành động (Action): một khi yêu cầu khớp với điều kiện, chúng ta muốn làm gì với nó? Chúng ta muốn chuyển tiếp (Forward) tới các Target Group cụ thể? |
| `00:03:53.220` | For example, if you had more than one target group then we could define one or more applications based on path or based on host domain. | Ví dụ nếu bạn có nhiều hơn một Target Group, bạn có thể định tuyến tới các ứng dụng khác nhau dựa trên đường dẫn hoặc tên miền. |
| `00:04:00.630` | Or we can redirect to a specific URL, for example, with a URI parts or full URL on the protocol HTTP or HTTPS, and then a specific status code. And then as well customize the host, the path, and the query. | Hoặc chúng ta có thể chuyển hướng (Redirect) tới một URL cụ thể với giao thức HTTP hoặc HTTPS cùng mã trạng thái phản hồi, tùy chỉnh cả host, path và query. |
| `00:04:13.500` | Or we can return a fixed response, and this is the one I'm going to do right now. So we can say, "Hey, 404, it's not found. So not found, custom error." | Hoặc chúng ta có thể trả về một phản hồi cố định (Return fixed response), và đây là lựa chọn tôi sẽ thực hiện ngay bây giờ. Tôi nhập mã phản hồi là `404` và nội dung văn bản là `"Not found, custom error."` |
| `00:04:24.150` | So this is what we're going to return when we go to /error. You'll see in a second that will make more sense to you. | Đó là những gì ALB sẽ trả về khi chúng ta truy cập vào `/error`. Bạn sẽ thấy kết quả ngay sau đây. |
| `00:04:29.820` | Then what is the priority of this rule? So right now it is pending. And so we have rules and we can have maybe a hundred rules in here. | Tiếp theo, độ ưu tiên (Priority) của quy tắc này là gì? Chúng ta có thể có tới hàng trăm quy tắc ở đây. |
| `00:04:36.990` | So we can define priorities and the 1 is going to be the highest priority, 5 is going to be a bit lower, up to 50,000. | Vì vậy chúng ta định nghĩa độ ưu tiên: `1` là độ ưu tiên cao nhất, `5` thấp hơn một chút, tối đa lên tới `50,000`. |
| `00:04:44.250` | So, of course based on like, for example, if a condition is matched by multiple rules, it is the rule with the highest priority that will win. So we're going to use priority of 5 just to give it as an example. | Nếu một yêu cầu khớp với nhiều quy tắc cùng lúc, quy tắc nào có độ ưu tiên cao hơn (số nhỏ hơn) sẽ thắng. Tôi sẽ đặt độ ưu tiên là `5` làm ví dụ. |
| `00:04:55.860` | And now we can see both our listener rules. Let's click on Next. Everything looks good for this demo rule and it has been created. So we can see now we have two rules, the default rule and the demo rule. | Nhấn Next, kiểm tra lại cấu hình và nhấn Create. Bây giờ chúng ta có hai quy tắc: `DemoRule` (ưu tiên 5) và `Default` rule. |
| `00:05:10.650` | Now let's test it out. So if I go into my load balancer detail, look at the DNS name, copy it and add /error, then this is going to trigger my rule and the result is not found, custom error. | Hãy kiểm tra thử. Tôi sao chép DNS name của bộ cân bằng tải, dán vào trình duyệt và thêm `/error` ở cuối. Ngay lập tức quy tắc mới của tôi được kích hoạt và kết quả trả về là `"Not found, custom error."` |
| `00:05:24.300` | Which means that yes, indeed, this request was matching the path pattern of /error and so therefore 404 and text/plain was returned. So, okay, that's it. I hope you liked it and I will see you in the next lecture. | Điều đó chứng tỏ yêu cầu này đã khớp với mẫu đường dẫn `/error` và phản hồi cố định `404` dạng `text/plain` đã được trả về trực tiếp từ ALB. Đó là tất cả cho bài học này, hẹn gặp lại bạn trong bài giảng tiếp theo. |
