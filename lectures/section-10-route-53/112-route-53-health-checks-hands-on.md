# Bài 112: Route 53 - Health Checks Hands On (Thực hành tạo Health Checks trong Route 53)

- **Section:** Phần 10 - Route 53
- **Lecture ID:** `28384354`
- **Video:** `SAA_-_Route_53_-_Health_Checks_Hands_On_v2.mp4`
- **Thời lượng:** `04:39`
- **Cheat sheet:** [topics/aws_route53.html](../../topics/aws_route53.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Cấu hình Endpoint Health Check trong thực tế
- Vào **Route 53 Console** -> **Health checks** -> **Create health check**:
  - **What to monitor:** `Endpoint` (theo `IP address` hoặc `Domain name`).
  - **Protocol / Port / Path:** Ví dụ `HTTP`, Port `80`, Path `/` (trong ứng dụng thực tế thường dùng `/health`).
  - **Advanced Configuration:**
    - **Request interval:** `Standard (30 seconds)` hoặc `Fast (10 seconds)` (tốn phí hơn).
    - **Failure threshold:** Số lần thất bại liên tiếp trước khi chuyển sang trạng thái `Unhealthy` (mặc định là `3`).
    - **String matching:** Tìm chuỗi ký tự trong `5,120 bytes` đầu tiên của phản hồi.
    - **Latency graphs:** Vẽ biểu đồ độ trễ theo thời gian trên CloudWatch.
    - **Invert health check status:** Đảo ngược kết quả (`Healthy` <-> `Unhealthy`, rất tiện để giả lập lỗi nhanh khi kiểm thử).
    - **Health checker regions:** Giữ nguyên `Recommended` (tất cả khu vực) hoặc tùy chọn các Region cụ thể.

### 1.2. Kiểm thử lỗi Firewall / Security Group & Calculated Health Check
- Khi xóa Inbound rule cổng `80 (HTTP)` trên Security Group của EC2 instance tại `ap-southeast-1`, các Health Checkers sẽ gặp lỗi `Connection timeout` và chuyển trạng thái Health Check của `ap-southeast-1` sang **Unhealthy**.
- Khi tạo **Calculated Health Check** giám sát cả 3 Health Checks (`us-east-1`, `ap-southeast-1`, `eu-central-1`) với điều kiện `Healthy when all health checks are healthy (AND)`, Calculated Health Check cũng báo **Unhealthy** vì `ap-southeast-1` đang Unhealthy.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
|---|---|---|
| `00:00:00` | So let's go ahead and create some health checks. So on the left hand side, I'm going to go into the health checks, and we're going to create health checks for all our EC2 instances. | Hãy bắt đầu tạo một số Health Checks. Ở thanh menu bên trái, tôi vào mục **Health checks** và tạo Health Checks cho cả 3 EC2 instances của chúng ta. |
| `00:00:08` | So we're going to create three health checks. So the first one is going to be from an instance in us-east-1, and is going to be an endpoint. | Chúng ta sẽ tạo 3 Health Checks. Cái đầu tiên đặt tên là `us-east-1`, chọn loại giám sát là **Endpoint**. |
| `00:00:15` | And then you'd just specify either an IP address or a domain name. So we'll keep it as an IP address. And my instance in us-east-1 is right here. So we'll paste that in. | Bạn có thể chỉ định theo **IP address** hoặc **Domain name**. Chúng ta giữ nguyên là **IP address** và dán địa chỉ IP của instance tại `us-east-1` vào đây. |
| `00:00:26` | We have to specify a port, so we'll keep it as 80, because this is the HTTP port. And for path, we're just going to be keeping the path as slash (`/`) because while this is the same as the IP slash, which is the root of our website, | Chỉ định **Port** là `80` (cổng HTTP), và **Path** giữ nguyên là `/` (gốc của website). |
| `00:00:37` | if we had a real application, sometimes it is very common to have a path `/health`, for example, which responds with the health of the endpoint itself. Okay, so we have this ready, so I'll just remove the `/health`. | Trong các ứng dụng thực tế, người ta thường tạo một đường dẫn riêng như `/health` chuyên trả về tình trạng sức khỏe của ứng dụng. Ở đây tôi để trống để dùng đường dẫn gốc `/`. |
| `00:00:50` | And then we can look at some advanced configuration. So we can either have a standard every thirty seconds or a fast every ten seconds health check. We'll keep it as standard because this is otherwise more expensive. | Mở mục **Advanced configuration**: chúng ta có thể chọn **Standard (mỗi 30 giây)** hoặc **Fast (mỗi 10 giây)**. Chúng ta giữ ở mức Standard vì Fast sẽ đắt tiền hơn. |
| `00:01:01` | How many times does it need to fail before being considered as a failure? Do you want to do string matching so do you want to look for a string in the first 5,120 bytes? Yes or no? | **Failure threshold**: cần thất bại liên tiếp bao nhiêu lần trước khi bị coi là lỗi (mặc định là 3)? **String matching**: có muốn tìm một chuỗi văn bản trong 5.120 bytes đầu tiên không? |
| `00:01:10` | Do we want a latency graph, to see how latency evolves over time? Do we want to invert the health check status, do we want healthy to be unhealthy and vice-versa? Or disable it. | **Latency graphs**: có muốn bật biểu đồ theo dõi độ trễ theo thời gian không? **Invert health check status**: đảo ngược trạng thái (Healthy thành Unhealthy và ngược lại). |
| `00:01:23` | And then do you want to customize the regions of the health checkers? Or do you want to use the recommended and we'll just keep it as is with using recommended. | Và bạn có muốn tùy chỉnh danh sách các Region của Health Checkers hay dùng cấu hình khuyến nghị (**Recommended**)? Chúng ta giữ nguyên mặc định. |
| `00:01:32` | And do we want to be notified whenever this health check fails? Yes or no by creating an alarm? I will just say no for now. So we have created our first health check. | Bước tiếp theo hỏi có muốn nhận thông báo qua CloudWatch Alarm + SNS khi Health Check thất bại không — hiện tại tôi chọn **No** và nhấn **Create health check**. |
| `00:01:40` | Now let's create our second health check and it's going to be for ap-southeast-1. So ap-southeast-1, and then IP address right here, not host name. And then next and create. | Tiếp tục tạo Health Check thứ hai cho `ap-southeast-1`: nhập tên `ap-southeast-1`, dán địa chỉ IP tại Singapore vào, nhấn **Next** rồi **Create health check**. |
| `00:01:54` | And the last health check is for eu-central-1. So let's create this health check and I will name it eu-central-1. And then here is the IP address and click on next and create health check. | Và Health Check thứ ba cho `eu-central-1`: đặt tên `eu-central-1`, dán địa chỉ IP tại Frankfurt, nhấn **Next** rồi **Create health check**. |
| `00:02:10` | Okay. So our health checks are created. And what I'm going to do is I'm going to go to one of my instances, for example, the one in Singapore and for the security group, I'm going to start blocking the port 80, removing this rule. | Sau khi cả 3 Health Checks đã được tạo, tôi sẽ vào EC2 instance tại **Singapore (`ap-southeast-1`)**, mở **Security Group** của nó và xóa rule cổng **80 (HTTP)** để chặn kết nối. |
| `00:02:23` | And the idea is that I want to get a failing health check. So I'm going to go into the security group right here. I will do action and edit the inbound rules, and I will delete my HTTP based rules. | Mục đích là tôi muốn tạo ra một Health Check bị lỗi (`Unhealthy`). Tôi vào chỉnh sửa Inbound rules và xóa rule HTTP đi. |
| `00:02:33` | And what this will do is that the one health check for ap-southeast-1 should give me an unhealthy status. So let me wait a little bit for the health checkers to do their thing, and then we'll get back to you. | Việc này sẽ khiến Health Check `ap-southeast-1` chuyển sang trạng thái **Unhealthy**. Hãy đợi một chút để các Health Checkers kiểm tra. |
| `00:02:43` | Okay. So as we can see, we have three health checks, and one of them is unhealthy, obviously because I blocked at the security group and the other two healthy. | Như bạn thấy, trong 3 Health Checks hiện có 1 cái báo **Unhealthy** (`ap-southeast-1`) do tôi đã chặn ở Security Group, còn 2 cái kia đều báo **Healthy**. |
| `00:02:52` | So we can have a look at the health checkers and it gives you some information around when it was last checked and so on. And for the unhealthy one, we can view the error status. | Khi nhấp vào tab **Health checkers**, bạn có thể xem chi tiết thời điểm kiểm tra gần nhất của từng vị trí trên thế giới và trạng thái lỗi. |
| `00:03:00` | So if we look at view last failed check, we can see that there was a connection timeout, and maybe the requests are being blocked by my firewall and firewall is your security group. So that makes sense. | Nhấp vào **View last failed check**, hệ thống báo `Connection timeout` — do các yêu cầu bị chặn bởi tường lửa (chính là Security Group của chúng ta). Rất hợp lý! |
| `00:03:16` | And one last thing you can create is a calculated health check. And this one is going to be a calculated health check, Calculated. Here we go. And this is going to check for the status of other health checks. | Tiếp theo, hãy thử tạo một **Calculated Health Check**. Đặt tên là `Calculated` và chọn loại **Monitor other health checks**. |
| `00:03:29` | And now we can specify which health checks we want to monitor. And okay, we're saying maybe you want to report healthy when one of the three health checks are healthy or when 2, or when all of them are healthy. | Chọn cả 3 Health Checks con cần giám sát. Chúng ta có thể chọn báo cáo Healthy khi 1 trong 3, 2 trong 3, hoặc khi **tất cả (`AND`)** đều Healthy, hoặc dùng phép **`OR`**. |
| `00:03:47` | So I would just keep it as this should be healthy when all of my health checks are healthy and then click on next, next. And we have created a calculated health check. | Tôi giữ tùy chọn báo Healthy khi **tất cả** các Health Checks con đều Healthy, rồi nhấn **Next** -> **Create health check**. |
| `00:03:58` | And the last kind of a health check we can create is to monitor the state of a CloudWatch alarm. In which case we need to specify the region the alarm is going to be in, and then this alarm could be monitoring obviously the state of a private EC2 instance for example. | Loại thứ ba bạn có thể thấy trong giao diện là **Monitor the state of a CloudWatch alarm**: bạn chọn Region chứa Alarm đó, và Alarm đó có thể đang giám sát một EC2 instance nằm trong mạng nội bộ (Private). |
| `00:04:11` | And this is how we would link the health of a private resource into a Route 53 health check. Okay. But I can't create it right now because I don't have an alarm available for us. | Đó chính là cách liên kết sức khỏe của một tài nguyên riêng tư vào Route 53 Health Check. |
| `00:04:22` | Okay. So my calculated health check is now reported unhealthy because well, one of the health checks I'm trying to monitor is unhealthy, and this is how we define it. | Quay lại danh sách, bạn có thể thấy **Calculated Health Check** vừa tạo hiện báo **Unhealthy** vì 1 trong 3 Health Checks con mà nó giám sát đang bị Unhealthy. |
| `00:04:31` | So that really shows you the power of health checks. And in the next lecture, we'll be using them of course, alongside records in Route 53. So I hope you liked this lecture and I will see you in the next lecture. | Điều này cho thấy sức mạnh của Health Checks. Trong bài giảng tiếp theo, chúng ta sẽ sử dụng chúng kết hợp với các bản ghi định tuyến trong Route 53. Hẹn gặp lại bạn! |
