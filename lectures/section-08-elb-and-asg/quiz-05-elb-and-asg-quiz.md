# Quiz 5: High Availability and Scalability - ELB & ASG Quiz (21 Câu hỏi)

- **Phần (Section):** Phần 8: High Availability and Scalability: ELB & ASG
- **Mã bài kiểm tra (Quiz ID):** `5334526`
- **Số lượng câu hỏi:** `21 câu`
- **Cheat sheet:** [topics/aws_elb_asg.html](../../topics/aws_elb_asg.html)

---

## Câu hỏi 1 (ID: `37492506`)
**Question (English):**
Scaling an EC2 instance from `r4.large` to `r4.4xlarge` is called .....................

**Câu hỏi (Tiếng Việt):**
Việc nâng cấp một EC2 instance từ loại `r4.large` lên `r4.4xlarge` được gọi là .....................

**Các phương án lựa chọn:**
- [ ] A. Horizontal Scalability (Mở rộng theo chiều ngang)
- [ ] B. Vertical Scalability (Mở rộng theo chiều dọc)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Vertical Scalability (Mở rộng theo chiều dọc)**

> [!NOTE]
> **Giải thích:**
> - Thay đổi kích thước/cấu hình của một instance (Scale Up / Scale Down) được gọi là **Vertical Scalability (Mở rộng theo chiều dọc)**.
</details>

---

## Câu hỏi 2 (ID: `37492512`)
**Question (English):**
Running an application on an Auto Scaling Group that scales the number of EC2 instances in and out is called .....................

**Câu hỏi (Tiếng Việt):**
Việc chạy một ứng dụng trên một Auto Scaling Group tự động tăng và giảm (scale out & scale in) số lượng các EC2 instances được gọi là .....................

**Các phương án lựa chọn:**
- [ ] A. Horizontal Scalability (Mở rộng theo chiều ngang / Elasticity)
- [ ] B. Vertical Scalability (Mở rộng theo chiều dọc)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Horizontal Scalability (Mở rộng theo chiều ngang / Elasticity)**

> [!NOTE]
> **Giải thích:**
> - Tăng hoặc giảm số lượng các máy chủ/instances (Scale Out / Scale In) được gọi là **Horizontal Scalability (Mở rộng theo chiều ngang)** hay **Elasticity**.
</details>

---

## Câu hỏi 3 (ID: `37492518`)
**Question (English):**
Elastic Load Balancers provide a .......................

**Câu hỏi (Tiếng Việt):**
Tất cả các bộ cân bằng tải Elastic Load Balancers đều cung cấp một .......................

**Các phương án lựa chọn:**
- [ ] A. static IPv4 we can use in our application (địa chỉ IPv4 tĩnh để dùng trong ứng dụng)
- [ ] B. static DNS name we can use in our application (tên miền DNS tĩnh để dùng trong ứng dụng)
- [ ] C. static IPv6 we can use in our application (địa chỉ IPv6 tĩnh để dùng trong ứng dụng)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. static DNS name we can use in our application (tên miền DNS tĩnh để dùng trong ứng dụng)**

> [!NOTE]
> **Giải thích:**
> - Chỉ có riêng **Network Load Balancer (NLB)** mới cung cấp cả tên DNS tĩnh lẫn địa chỉ IP tĩnh (Static IP / Elastic IP trên mỗi AZ). Còn **Application Load Balancer (ALB)** và **Classic Load Balancer (CLB)** chỉ cung cấp một **tên miền DNS tĩnh (static DNS name)** chứ KHÔNG cung cấp IP tĩnh, vì AWS quản lý và tự động thay đổi hạ tầng IP bên dưới của ALB.
</details>

---

## Câu hỏi 4 (ID: `37492530`)
**Question (English):**
You are running a website on 10 EC2 instances fronted by an Elastic Load Balancer. Your users are complaining about the fact that the website always asks them to re-authenticate when they are moving between website pages. You are puzzled because it's working just fine on your machine and in the Dev environment with 1 EC2 instance. What could be the reason?

**Câu hỏi (Tiếng Việt):**
Bạn đang chạy một trang web trên 10 EC2 instances đứng sau một Elastic Load Balancer. Người dùng phàn nàn rằng trang web liên tục bắt họ phải đăng nhập lại mỗi khi chuyển trang. Bạn thấy khó hiểu vì nó chạy hoàn toàn bình thường trên máy cá nhân của bạn và trên môi trường Dev chỉ có 1 EC2 instance. Nguyên nhân có thể là gì?

**Các phương án lựa chọn:**
- [ ] A. Your website must have an issue when hosted on multiple EC2 instances
- [ ] B. The EC2 instances log out users as they can't see their IP addresses, instead, they receive ELB IP addresses.
- [ ] C. The Elastic Load Balancer does not have Sticky Sessions enabled (Bộ cân bằng tải ELB chưa bật tính năng Sticky Sessions)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. The Elastic Load Balancer does not have Sticky Sessions enabled (Bộ cân bằng tải ELB chưa bật tính năng Sticky Sessions)**

> [!NOTE]
> **Giải thích:**
> - Tính năng **ELB Sticky Sessions (Session Affinity)** đảm bảo mọi lưu lượng từ cùng một client sẽ luôn được chuyển tiếp tới cùng một EC2 instance phía sau, giúp client không bị mất dữ liệu phiên đăng nhập (session data) lưu cục bộ trên instance đó.
</details>

---

## Câu hỏi 5 (ID: `37492542`)
**Question (English):**
You are using an Application Load Balancer to distribute traffic to your website hosted on EC2 instances. It turns out that your website only sees traffic coming from private IPv4 addresses which are in fact your Application Load Balancer's IP addresses. What should you do to get the IP address of clients connected to your website?

**Câu hỏi (Tiếng Việt):**
Bạn đang sử dụng Application Load Balancer để phân phối lưu lượng tới trang web chạy trên các EC2 instances. Hóa ra trang web của bạn chỉ nhìn thấy lưu lượng đến từ các địa chỉ IPv4 riêng (thực chất là địa chỉ IP của ALB). Bạn nên làm gì để lấy được địa chỉ IP thật của các client kết nối tới trang web?

**Các phương án lựa chọn:**
- [ ] A. Modify your website's frontend so that users send their IP in every request
- [ ] B. Modify your website's backend to get the client IP address from the `X-Forwarded-For` header
- [ ] C. Modify your website's backend to get the client IP address from the `X-Forwarded-Port` header
- [ ] D. Modify your website's backend to get the client IP address from the `X-Forwarded-Proto` header

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Modify your website's backend to get the client IP address from the `X-Forwarded-For` header**

> [!NOTE]
> **Giải thích:**
> - Khi dùng ALB, các EC2 instances chỉ thấy gói tin IP đến từ Private IP của ALB. Để lấy địa chỉ IP thật của client, ứng dụng backend cần đọc HTTP Header **`X-Forwarded-For`** (trong khi `X-Forwarded-Port` chứa cổng và `X-Forwarded-Proto` chứa giao thức).
</details>

---

## Câu hỏi 6 (ID: `37492622`)
**Question (English):**
You hosted an application on a set of EC2 instances fronted by an Elastic Load Balancer. A week later, users begin complaining that sometimes the application just doesn't work. You investigate the issue and found that some EC2 instances crash from time to time. What should you do to protect users from connecting to the EC2 instances that are crashing?

**Câu hỏi (Tiếng Việt):**
Bạn triển khai một ứng dụng trên một tập hợp các EC2 instances đứng sau một Elastic Load Balancer. Một tuần sau, người dùng phàn nàn rằng đôi khi ứng dụng không hoạt động. Bạn điều tra và phát hiện một số EC2 instances thỉnh thoảng bị sập (crash). Bạn nên làm gì để bảo vệ người dùng không bị kết nối tới các EC2 instances đang bị sập đó?

**Các phương án lựa chọn:**
- [ ] A. Enable ELB Health Checks (Bật kiểm tra sức khỏe ELB Health Checks)
- [ ] B. Enable ELB Stickiness
- [ ] C. Enable SSL Termination
- [ ] D. Enable Cross-Zone Load Balancing

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Enable ELB Health Checks (Bật kiểm tra sức khỏe ELB Health Checks)**

> [!NOTE]
> **Giải thích:**
> - Khi bật và cấu hình đúng **ELB Health Checks**, bộ cân bằng tải sẽ liên tục kiểm tra tình trạng ứng dụng và tự động ngừng gửi lưu lượng tới các EC2 instances bị sập (`unhealthy`).
</details>

---

## Câu hỏi 7 (ID: `37511954`)
**Question (English):**
You are working as a Solutions Architect for a company and you are required to design an architecture for a high-performance, low-latency application that will receive millions of requests per second. Which type of Elastic Load Balancer should you choose?

**Câu hỏi (Tiếng Việt):**
Bạn đang làm Kiến trúc sư Giải pháp cho một công ty và được yêu cầu thiết kế kiến trúc cho một ứng dụng hiệu năng cao, độ trễ thấp, nhận hàng triệu yêu cầu mỗi giây. Bạn nên chọn loại Elastic Load Balancer nào?

**Các phương án lựa chọn:**
- [ ] A. Application Load Balancer
- [ ] B. Network Load Balancer

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Network Load Balancer**

> [!NOTE]
> **Giải thích:**
> - **Network Load Balancer (NLB)** hoạt động ở tầng 4 (Layer 4), cung cấp hiệu năng cao nhất (xử lý hàng triệu requests/giây) với độ trễ cực thấp (ultra-low latency).
</details>

---

## Câu hỏi 8 (ID: `37511958`)
**Question (English):**
Application Load Balancers support the following protocols, **EXCEPT**:

**Câu hỏi (Tiếng Việt):**
Application Load Balancer hỗ trợ tất cả các giao thức sau đây, **NGOẠI TRỪ**:

**Các phương án lựa chọn:**
- [ ] A. HTTP
- [ ] B. HTTPS
- [ ] C. TCP
- [ ] D. WebSocket

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. TCP**

> [!NOTE]
> **Giải thích:**
> - **Application Load Balancer (ALB)** chỉ hoạt động ở tầng 7 (Layer 7) nên hỗ trợ `HTTP`, `HTTPS`, `gRPC` và `WebSocket`, **không** hỗ trợ cân bằng tải trực tiếp ở tầng `TCP` (vốn dành cho NLB).
</details>

---

## Câu hỏi 9 (ID: `37511962`)
**Question (English):**
Application Load Balancers can route traffic to different Target Groups based on the following, **EXCEPT**:

**Câu hỏi (Tiếng Việt):**
Application Load Balancer có thể định tuyến lưu lượng tới các Target Groups khác nhau dựa trên các tiêu chí sau đây, **NGOẠI TRỪ**:

**Các phương án lựa chọn:**
- [ ] A. Client's Location (Geography) (Vị trí địa lý của Client)
- [ ] B. Hostname
- [ ] C. Request URL Path
- [ ] D. Source IP Address

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Client's Location (Geography) (Vị trí địa lý của Client)**

> [!NOTE]
> **Giải thích:**
> - ALB có thể định tuyến dựa trên URL Path, Hostname (Host Header), HTTP Headers, HTTP Methods, Query Strings và Source IP Address. Nó **không** định tuyến theo vị trí địa lý (Geolocation là tính năng của **Amazon Route 53**).
</details>

---

## Câu hỏi 10 (ID: `37511966`)
**Question (English):**
Registered targets in a Target Group for an Application Load Balancer can be one of the following, **EXCEPT**:

**Câu hỏi (Tiếng Việt):**
Các mục tiêu được đăng ký trong một Target Group của Application Load Balancer có thể là một trong các loại sau đây, **NGOẠI TRỪ**:

**Các phương án lựa chọn:**
- [ ] A. EC2 Instances
- [ ] B. Network Load Balancer
- [ ] C. Private IP Addresses
- [ ] D. Lambda Functions

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Network Load Balancer**

> [!NOTE]
> **Giải thích:**
> - Target Group của **ALB** hỗ trợ: `EC2 Instances`, `ECS Tasks`, `Lambda Functions`, và `Private IP Addresses`. Bạn có thể đặt **NLB đứng trước ALB** (ALB là target của NLB), nhưng **không thể** đặt ALB đứng trước NLB (NLB không thể là target của ALB).
</details>

---

## Câu hỏi 11 (ID: `37512418`)
**Question (English):**
For compliance purposes, you would like to expose a fixed static IP address to your end-users so that they can write firewall rules that will be stable and approved by regulators. What type of Elastic Load Balancer would you choose?

**Câu hỏi (Tiếng Việt):**
Vì mục đích tuân thủ quy định (compliance), bạn muốn cung cấp một địa chỉ IP tĩnh cố định cho người dùng cuối để họ có thể viết các quy tắc tường lửa ổn định và được cơ quan quản lý phê duyệt. Bạn sẽ chọn loại Elastic Load Balancer nào?

**Các phương án lựa chọn:**
- [ ] A. Application Load Balancer with an Elastic IP attached to it
- [ ] B. Network Load Balancer

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Network Load Balancer**

> [!NOTE]
> **Giải thích:**
> - Bạn không thể gắn Elastic IP trực tiếp vào ALB. Chỉ có **Network Load Balancer (NLB)** mới cung cấp 1 địa chỉ Static IP cố định trên mỗi AZ và cho phép gắn **Elastic IP** vào từng AZ.
</details>

---

## Câu hỏi 12 (ID: `37512420`)
**Question (English):**
You want to create a custom application-based cookie in your Application Load Balancer. Which of the following you can use as a cookie name?

**Câu hỏi (Tiếng Việt):**
Bạn muốn tạo một cookie tùy chỉnh dựa trên ứng dụng (custom application-based cookie) trong Application Load Balancer của mình. Bạn có thể sử dụng tên nào dưới đây làm tên cookie?

**Các phương án lựa chọn:**
- [ ] A. `AWSALBAPP`
- [ ] B. `APPUSERC`
- [ ] C. `AWSALBTG`
- [ ] D. `AWSALB`

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. `APPUSERC`**

> [!NOTE]
> **Giải thích:**
> - Ba cái tên `AWSALB`, `AWSALBAPP`, và `AWSALBTG` là các tên đã được **dành riêng (reserved)** cho chính ELB sử dụng. Bạn phải đặt một tên tùy chỉnh khác như **`APPUSERC`**.
</details>

---

## Câu hỏi 13 (ID: `37512428`)
**Question (English):**
You have a Network Load Balancer that distributes traffic across a set of EC2 instances in `us-east-1`. You have 2 EC2 instances in `us-east-1b` AZ and 5 EC2 instances in `us-east-1e` AZ. You have noticed that the CPU utilization is higher in the EC2 instances in `us-east-1b` AZ. After more investigation, you noticed that the traffic is equally distributed across the two AZs. How would you solve this problem?

**Câu hỏi (Tiếng Việt):**
Bạn có một Network Load Balancer phân phối lưu lượng qua một tập hợp các EC2 instances tại vùng `us-east-1`. Bạn có 2 EC2 instances ở `us-east-1b` và 5 EC2 instances ở `us-east-1e`. Bạn nhận thấy mức sử dụng CPU trên các máy ở `us-east-1b` cao hơn hẳn. Sau khi kiểm tra kỹ hơn, bạn thấy lưu lượng đang được chia đều 50/50 giữa hai AZ. Bạn sẽ giải quyết vấn đề này như thế nào?

**Các phương án lựa chọn:**
- [ ] A. Enable Cross-Zone Load Balancing (Bật tính năng Cân bằng tải liên vùng)
- [ ] B. Enable Sticky Sessions
- [ ] C. Enable ELB Health Checks
- [ ] D. Enable SSL Termination

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Enable Cross-Zone Load Balancing (Bật tính năng Cân bằng tải liên vùng)**

> [!NOTE]
> **Giải thích:**
> - Trên **NLB**, tính năng **Cross-Zone Load Balancing** mặc định bị **Tắt (Disabled)**, khiến 2 máy ở `us-east-1b` phải gánh 50% tổng tải (25%/máy) trong khi 5 máy ở `us-east-1e` chia nhau 50% (10%/máy). Khi bật **Cross-Zone Load Balancing**, lưu lượng sẽ được chia đều cho cả 7 EC2 instances trên cả hai AZ.
</details>

---

## Câu hỏi 14 (ID: `37512430`)
**Question (English):**
Which feature in both Application Load Balancers and Network Load Balancers allows you to load multiple SSL certificates on one listener?

**Câu hỏi (Tiếng Việt):**
Tính năng nào trên cả Application Load Balancer và Network Load Balancer cho phép bạn nạp nhiều chứng chỉ SSL trên cùng một Listener?

**Các phương án lựa chọn:**
- [ ] A. TLS Termination
- [ ] B. Server Name Indication (SNI)
- [ ] C. SSL Security Policies
- [ ] D. Host Headers

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Server Name Indication (SNI)**

> [!NOTE]
> **Giải thích:**
> - **Server Name Indication (SNI)** là phần mở rộng của giao thức TLS cho phép client chỉ định hostname đích trong bước SSL handshake đầu tiên, giúp ALB/NLB nạp và chọn đúng chứng chỉ SSL trong số nhiều chứng chỉ trên cùng 1 Listener.
</details>

---

## Câu hỏi 15 (ID: `37512432`)
**Question (English):**
You have an Application Load Balancer that is configured to redirect traffic to 3 Target Groups based on the following hostnames: `users.example.com`, `api.external.example.com`, and `checkout.example.com`. You would like to configure HTTPS for each of these hostnames. How do you configure the ALB to make this work?

**Câu hỏi (Tiếng Việt):**
Bạn có một Application Load Balancer được cấu hình chuyển hướng lưu lượng tới 3 Target Groups dựa trên 3 tên miền: `users.example.com`, `api.external.example.com`, và `checkout.example.com`. Bạn muốn cấu hình HTTPS riêng cho từng tên miền này. Bạn cấu hình ALB như thế nào để thực hiện điều đó?

**Các phương án lựa chọn:**
- [ ] A. Use an HTTP to HTTPS redirect rule
- [ ] B. Use a security group SSL certificate
- [ ] C. Use Server Name Indication (SNI)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. Use Server Name Indication (SNI)**

> [!NOTE]
> **Giải thích:**
> - **Server Name Indication (SNI)** cho phép bạn gắn nhiều chứng chỉ SSL cho nhiều tên miền HTTPS khác nhau trên cùng một Listener của ALB.
</details>

---

## Câu hỏi 16 (ID: `37512434`)
**Question (English):**
You have an application hosted on a set of EC2 instances managed by an Auto Scaling Group that you configured both desired and maximum capacity to 3. Also, you have created a CloudWatch Alarm that is configured to scale out your ASG when CPU Utilization reaches 60%. Your application suddenly received huge traffic and is now running at 80% CPU Utilization. What will happen?

**Câu hỏi (Tiếng Việt):**
Bạn có một ứng dụng chạy trên các EC2 instances được quản lý bởi một Auto Scaling Group với cả Desired capacity và Maximum capacity đều được cấu hình bằng `3`. Bạn cũng đã tạo một CloudWatch Alarm để Scale Out ASG khi CPU Utilization đạt 60%. Ứng dụng của bạn đột ngột nhận lượng truy cập khổng lồ và hiện đang chạy ở mức 80% CPU. Điều gì sẽ xảy ra?

**Các phương án lựa chọn:**
- [ ] A. Nothing (Không có gì xảy ra cả)
- [ ] B. The desired capacity will go up to 4 and the maximum capacity will stay at 3
- [ ] C. The desired capacity will go up to 4 and the maximum capacity will stay at 4

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Nothing (Không có gì xảy ra cả)**

> [!NOTE]
> **Giải thích:**
> - Auto Scaling Group **không bao giờ** tự động mở rộng vượt quá giới hạn **`Maximum capacity`** mà bạn đã cấu hình (`3`), ngay cả khi CloudWatch Alarm bị kích hoạt. Vì hiện tại đã chạy đủ 3 máy (bằng Max capacity), sẽ không có thêm máy nào được tạo ra.
</details>

---

## Câu hỏi 17 (ID: `37512438`)
**Question (English):**
You have an Auto Scaling Group fronted by an Application Load Balancer. You have configured the ASG to use ALB Health Checks, then one EC2 instance has just been reported unhealthy. What will happen to the EC2 instance?

**Câu hỏi (Tiếng Việt):**
Bạn có một Auto Scaling Group đứng sau một Application Load Balancer. Bạn đã cấu hình ASG sử dụng ALB Health Checks, và vừa có một EC2 instance bị báo cáo là không khỏe mạnh (`unhealthy`). Điều gì sẽ xảy ra với EC2 instance đó?

**Các phương án lựa chọn:**
- [ ] A. The ASG will keep the instance running and re-start the application
- [ ] B. The ASG will detach the EC2 instance and leave it running
- [ ] C. The ASG will terminate the EC2 instance (ASG sẽ chấm dứt/hủy EC2 instance đó và tạo máy mới thay thế)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. The ASG will terminate the EC2 instance (ASG sẽ chấm dứt/hủy EC2 instance đó và tạo máy mới thay thế)**

> [!NOTE]
> **Giải thích:**
> - Khi một EC2 instance trượt bài kiểm tra sức khỏe (EC2 Status Checks hoặc ELB Health Checks đã bật trên ASG), ASG sẽ đánh dấu instance đó là `unhealthy`, **Terminate** nó và tự động khởi chạy một EC2 instance mới để thay thế.
</details>

---

## Câu hỏi 18 (ID: `37512440`)
**Question (English):**
Your boss asked you to scale your Auto Scaling Group based on the **number of requests per minute** your application makes to your database. What should you do?

**Câu hỏi (Tiếng Việt):**
Sếp của bạn yêu cầu mở rộng Auto Scaling Group dựa trên **số lượng yêu cầu mỗi phút mà ứng dụng gửi tới cơ sở dữ liệu (database)**. Bạn nên làm gì?

**Các phương án lựa chọn:**
- [ ] A. Create a CloudWatch custom metric then create a CloudWatch Alarm on this metric to scale your ASG (Tạo một CloudWatch Custom Metric, sau đó tạo CloudWatch Alarm trên chỉ số này để mở rộng ASG)
- [ ] B. You politely tell him it's impossible
- [ ] C. Enable Detailed Monitoring then create a CloudWatch Alarm to scale your ASG

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Create a CloudWatch custom metric then create a CloudWatch Alarm on this metric to scale your ASG (Tạo một CloudWatch Custom Metric, sau đó tạo CloudWatch Alarm trên chỉ số này để mở rộng ASG)**

> [!NOTE]
> **Giải thích:**
> - Mặc định CloudWatch không biết ứng dụng của bạn gửi bao nhiêu truy vấn mỗi phút vào Database. Vì vậy bạn cần lập trình đẩy số liệu này lên thành một **CloudWatch Custom Metric**, sau đó tạo **CloudWatch Alarm** trên custom metric đó để kích hoạt Scaling Policy của ASG.
</details>

---

## Câu hỏi 19 (ID: `37512478`)
**Question (English):**
An application is deployed with an Application Load Balancer and an Auto Scaling Group. Currently, you manually scale the ASG and you would like to define a Scaling Policy that will ensure the average number of connections to your EC2 instances is around 1000. Which Scaling Policy should you use?

**Câu hỏi (Tiếng Việt):**
Một ứng dụng được triển khai với Application Load Balancer và Auto Scaling Group. Hiện tại bạn đang mở rộng ASG thủ công và bạn muốn định nghĩa một Scaling Policy đảm bảo số lượng kết nối trung bình tới các EC2 instances của bạn luôn duy trì quanh mức `1000`. Bạn nên sử dụng Scaling Policy nào?

**Các phương án lựa chọn:**
- [ ] A. Simple Scaling Policy
- [ ] B. Step Scaling Policy
- [ ] C. Target Tracking Policy
- [ ] D. Scheduled Scaling Policy

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. Target Tracking Policy**

> [!NOTE]
> **Giải thích:**
> - Khi đề bài yêu cầu duy trì một chỉ số trung bình luôn xoay quanh một giá trị mục tiêu cụ thể (ví dụ: giữ số kết nối trung bình / `RequestCountPerTarget` quanh mức `1000` hoặc giữ CPU quanh mức `40%`), **Target Tracking Scaling Policy** luôn là lựa chọn chính xác và đơn giản nhất.
</details>

---

## Câu hỏi 20 (ID: `51042542`)
**Question (English):**
You have an ASG and a Network Load Balancer. The application on your ASG supports the HTTP protocol and is integrated with the Load Balancer health checks. You are currently using the TCP health checks. You would like to migrate to using HTTP health checks, what do you do?

**Câu hỏi (Tiếng Việt):**
Bạn có một ASG và một Network Load Balancer. Ứng dụng trên ASG của bạn hỗ trợ giao thức HTTP và được tích hợp với kiểm tra sức khỏe của Load Balancer. Hiện tại bạn đang dùng TCP health checks và muốn chuyển sang dùng HTTP health checks, bạn cần làm gì?

**Các phương án lựa chọn:**
- [ ] A. Migrate to an Application Load Balancer
- [ ] B. Migrate the health check to HTTP (Chỉ cần đổi giao thức Health Check trên Target Group của NLB sang HTTP)

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Migrate the health check to HTTP (Chỉ cần đổi giao thức Health Check trên Target Group của NLB sang HTTP)**

> [!NOTE]
> **Giải thích:**
> - Target Group của **Network Load Balancer (NLB)** hỗ trợ đầy đủ cả 3 giao thức Health Check là **`TCP`**, **`HTTP`**, và **`HTTPS`**. Bạn chỉ cần chuyển cấu hình Health Check sang `HTTP` mà không cần phải đổi sang ALB.
</details>

---

## Câu hỏi 21 (ID: `51457322`)
**Question (English):**
You have a website hosted in EC2 instances in an Auto Scaling Group fronted by an Application Load Balancer. Currently, the website is served over HTTP, and you have been tasked to configure it to use HTTPS. You have created a certificate in ACM and attached it to the Application Load Balancer. What can you do to force users to access the website using HTTPS instead of HTTP?

**Câu hỏi (Tiếng Việt):**
Bạn có một trang web chạy trên các EC2 instances trong một Auto Scaling Group đứng sau một Application Load Balancer. Hiện tại trang web đang chạy qua HTTP, và bạn được giao nhiệm vụ cấu hình nó sang sử dụng HTTPS. Bạn đã tạo chứng chỉ trong ACM và gắn vào ALB. Bạn có thể làm gì để bắt buộc người dùng truy cập trang web bằng HTTPS thay vì HTTP?

**Các phương án lựa chọn:**
- [ ] A. Send an email to all customers to use HTTPS instead of HTTP
- [ ] B. Configure the Application Load Balancer to redirect HTTP to HTTPS (Cấu hình Listener Rule trên ALB để tự động Redirect từ HTTP sang HTTPS)
- [ ] C. Configure the DNS record to redirect HTTP to HTTPS

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Configure the Application Load Balancer to redirect HTTP to HTTPS (Cấu hình Listener Rule trên ALB để tự động Redirect từ HTTP sang HTTPS)**

> [!NOTE]
> **Giải thích:**
> - **Application Load Balancer (ALB)** hỗ trợ tính năng **HTTP-to-HTTPS Redirect** trực tiếp trong Listener Rules (nhận request ở cổng 80 HTTP và tự động trả về mã chuyển hướng `301` sang cổng 443 HTTPS).
</details>
