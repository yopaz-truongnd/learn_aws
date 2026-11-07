# Bài 78: Elastic Load Balancer - Sticky Sessions (Phiên kết dính / Session Affinity)

- **Phần (Section):** Phần 8: High Availability and Scalability: ELB & ASG
- **Mã bài học (Lecture ID):** `13528094`
- **Tệp video:** `SOA - ELB - Sticky Sessions v3.mp4`
- **Thời lượng:** `05:51`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Sticky Sessions (Session Affinity) là gì?
- **Nguyên lý:** Mặc định, ELB phân phối các request từ một Client đều khắp các EC2 instances. Khi bật **Sticky Sessions (Session Affinity)**, mọi request tiếp theo từ **cùng một Client** sẽ luôn được chuyển tiếp tới **cùng một EC2 instance phía sau** đã xử lý request đầu tiên.
- **Các loại Load Balancer hỗ trợ:**
  - **Classic Load Balancer (CLB)**
  - **Application Load Balancer (ALB)** (bật ở cấp độ Target Group, hoạt động dựa trên HTTP **Cookie** có thời hạn hết hạn - expiration).
  - **Network Load Balancer (NLB)** (bật ở cấp độ Target Group, hoạt động dựa trên thuật toán băm nguồn/đích IP, không dùng cookie).
- **Trường hợp sử dụng (Use Case):** Đảm bảo người dùng **không bị mất dữ liệu phiên làm việc (Session Data)** lưu cục bộ trên bộ nhớ của EC2 instance (ví dụ: trạng thái đăng nhập / login session, giỏ hàng).
- **Nhược điểm:** Có thể gây **mất cân bằng tải (imbalance)** lên các backend EC2 instances nếu một số instance bị gắn với những người dùng gửi quá nhiều yêu cầu ("very sticky users").

```mermaid
flowchart LR
    C1["Client 1"] -->|Request 1 & 2<br/>(Cùng Cookie)| ALB["Application Load Balancer<br/>(Sticky Sessions = Enabled)"]
    C2["Client 2"] -->|Request 1 & 2<br/>(Cùng Cookie)| ALB
    ALB -->|Luôn định tuyến C1| EC2_1["EC2 Instance 1<br/>(Lưu Session của C1)"]
    ALB -->|Luôn định tuyến C2| EC2_2["EC2 Instance 2<br/>(Lưu Session của C2)"]
```

---

### 1.2. Phân loại Cookie trong Sticky Sessions (ALB / CLB)

| Loại Cookie | Ai tạo ra Cookie? | Ai kiểm soát thời hạn (Expiration)? | Tên Cookie (Cookie Name) | Ghi chú đặc biệt cho kỳ thi SAA-C03 |
| :--- | :--- | :--- | :--- | :--- |
| **1. Application-based Cookies -> Custom Cookie** | **Target (Ứng dụng trên EC2)** tự tạo | Do **Ứng dụng** quy định | Tên tùy chỉnh riêng cho từng Target Group (ví dụ: `MYCUSTOMCOOKIEAPP`, `APPUSERC`) | **TUYỆT ĐỐI KHÔNG ĐƯỢC DÙNG** 3 tên dành riêng (reserved names): **`AWSALB`**, **`AWSALBAPP`**, **`AWSALBTG`**. |
| **2. Application-based Cookies -> Application Cookie** | **Load Balancer (ALB)** tạo để hỗ trợ cookie của ứng dụng | Tuân theo thời hạn của cookie ứng dụng | **`AWSALBAPP`** | Do ALB tự sinh ra đi kèm với custom cookie của ứng dụng. |
| **3. Duration-based Cookies (Load Balancer generated)** | **Load Balancer (ALB / CLB)** tự tạo | Do **Load Balancer** quy định (từ **1 giây đến 7 ngày**, mặc định 1 ngày) | **`AWSALB`** (trên ALB)<br/>**`AWSELB`** (trên CLB) | Cấu hình đơn giản nhất trực tiếp trên Target Group mà không cần sửa code ứng dụng. |

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00.150` | Let's talk about sticky sessions or so-called session affinity for your elastic load balancer. | Hãy nói về tính năng phiên kết dính (Sticky Sessions), hay còn gọi là Session Affinity cho Elastic Load Balancer của bạn. |
| `00:00:06.180` | So it's possible to implement what's called stickiness or sticky sessions. And the idea is that the client doing two requests to the load balancer will have the same instance in the backend to respond to the request. | Khi triển khai tính năng Stickiness (Sticky Sessions), ý tưởng cốt lõi là một client thực hiện hai hay nhiều yêu cầu tới bộ cân bằng tải sẽ luôn được cùng một instance ở phía backend phản hồi. |
| `00:00:18.600` | So the idea is that, for example, you have the ALB with two EC2 instances and you have three clients. If the client one makes a request and it goes to the first EC2 instance, that means that when it does a second request to the load balancer, it will go to the same instance, | Ví dụ bạn có một ALB đứng trước hai EC2 instance và có ba client. Nếu Client 1 gửi yêu cầu đầu tiên và được đưa tới EC2 instance thứ nhất, thì khi nó gửi yêu cầu thứ hai tới bộ cân bằng tải, yêu cầu đó vẫn sẽ đi tới chính instance thứ nhất đó, |
| `00:00:33.390` | which is a different behavior where usually the application balancer will do a spread of all the requests across all the EC2 instances. | đây là hành vi khác với thông thường (vốn phân bổ luân phiên các yêu cầu qua tất cả các EC2 instance). |
| `00:00:42.300` | Now for client two, if it goes to the ALB and talks to the second instance, then all the requests will go there. And same for client three, okay? | Tương tự đối với Client 2, nếu lần đầu nó kết nối qua ALB tới instance thứ hai, thì mọi yêu cầu tiếp theo của nó đều sẽ đi tới instance thứ hai. Và Client 3 cũng vậy. |
| `00:00:49.800` | So this can be enabled for the Classic Load Balancer, Application Load Balancer and Network Load Balancer. | Tính năng này có thể được bật cho cả Classic Load Balancer (CLB), Application Load Balancer (ALB) và Network Load Balancer (NLB). |
| `00:00:55.530` | And how it works, well, there is a cookie that is sent as part of the request from the clients to the load balancer and it has stickiness and it has an expiration date. | Cách thức hoạt động (trên ALB/CLB) là có một cookie được gửi kèm trong yêu cầu từ phía client tới bộ cân bằng tải, mang thông tin gắn kết phiên và có thời hạn hết hạn (expiration date). |
| `00:01:04.830` | That means that when the cookie expires, then the client may be redirected to another EC2 instance. | Điều đó có nghĩa là khi cookie hết hạn, client có thể sẽ được chuyển hướng sang một EC2 instance khác. |
| `00:01:10.470` | The use case for this is to make sure that the user is connected to the same backend instance in order not to lose his session data, which can take some important information such as the login of the user, for example. | Trường hợp sử dụng phổ biến của tính năng này là đảm bảo người dùng luôn kết nối tới cùng một backend instance để không bị mất dữ liệu phiên làm việc (session data) — nơi chứa các thông tin quan trọng như trạng thái đăng nhập (login) của người dùng. |
| `00:01:22.260` | But if you enable stickiness, it may bring imbalance to the load over the backend EC2 instances in case some instances have a very, very sticky user. | Tuy nhiên, việc bật stickiness có thể gây ra sự mất cân bằng tải (imbalance) giữa các backend EC2 instance trong trường hợp một số instance gặp phải những người dùng gửi lượng yêu cầu quá lớn. |
| `00:01:31.260` | Okay, now to go a little bit deeper, how about the cookie itself? Well, there are two types of cookie that you can have for sticky sessions. The first one is application-based cookie and the second one is duration-based cookie. | Đi sâu hơn một chút về bản thân các cookie: có hai loại cookie mà bạn có thể sử dụng cho Sticky Sessions. Loại thứ nhất là **Application-based cookie** (cookie dựa trên ứng dụng) và loại thứ hai là **Duration-based cookie** (cookie dựa trên khoảng thời gian). |
| `00:01:43.770` | So for application-based cookies, well, it's a custom cookie that is generated by the target, so by your application itself. And you can include any custom attributes you want required by your application. | Đối với Application-based cookies, nhánh đầu tiên là **Custom cookie** được tạo ra bởi chính mục tiêu (Target) — tức là bởi ứng dụng của bạn. Bạn có thể đưa vào bất kỳ thuộc tính tùy chỉnh nào mà ứng dụng cần. |
| `00:01:54.870` | The cookie name must be specified individually for each target group, okay? And you must not use the following names, so AWSALB, AWSALBAPP or AWSALBTG, because they are already reserved for use by the ELB itself. | Tên của custom cookie phải được chỉ định riêng cho từng Target Group. Và bạn **không được phép** sử dụng các tên sau: `AWSALB`, `AWSALBAPP`, hoặc `AWSALBTG`, bởi vì chúng đã được dành riêng (reserved) cho chính ELB sử dụng. |
| `00:02:12.180` | Or it could be an application cookie. And this time will be generated by the load balancer itself, and the cookie name used by the ALB will be AWSALBAPP, okay? | Ngoài ra trong Application-based cookies còn có một cookie ứng dụng do chính bộ cân bằng tải tạo ra, và tên cookie được ALB sử dụng sẽ là `AWSALBAPP`. |
| `00:02:23.940` | Now the second type of cookies is duration-based cookie and it's a cookie generated by the load balancer, and the name is AWSALB for the ALB and AWSELB for the CLB, okay? | Loại cookie lớn thứ hai là **Duration-based cookie** — đây là cookie được tạo hoàn toàn bởi bộ cân bằng tải, với tên cố định là `AWSALB` đối với ALB và `AWSELB` đối với CLB. |
| `00:02:35.100` | And the idea is this one will have an expiry based on a specific duration, and the duration is generated by the load balancer itself, okay? Whereas before, when there is an application-based cookie, the duration can be specified by the application itself. | Cookie này sẽ hết hạn dựa trên một khoảng thời gian cụ thể do chính bộ cân bằng tải quản lý; trong khi ở loại Application-based cookie trước đó, thời hạn có thể được quy định bởi chính ứng dụng. |
| `00:02:48.090` | So that's how it works, okay? You don't need to remember exactly the name of the cookies or the fact that you have custom and application, but you remember there's application-based cookies and duration-based, and they have a specific name. And this will be coming into account when we talk about CloudFront. | Hãy nhớ có hai loại: Application-based cookies và Duration-based cookies cùng với các tên dành riêng của AWS. Kiến thức này cũng sẽ liên quan khi chúng ta học tới CloudFront. |
| `00:03:05.040` | Okay, so if I look at my load balancer right now and I open it in the new tab, as you can see, it goes between my two/three instances in my load balancer. So that's perfect. | Bây giờ nếu tôi mở đường dẫn bộ cân bằng tải trong tab mới và nhấn refresh, như bạn thấy nó chuyển đổi luân phiên giữa các instance của tôi. |
| `00:03:13.283` | But now I'm going to enable sticky sessions. So to do so, I'm going to go at the target group level, open my target group and then Actions, and I can edit the attributes of my target group. | Bây giờ tôi sẽ bật tính năng Sticky Sessions. Để làm điều đó, tôi vào cấp độ Target Group, mở Target Group của mình, nhấn **Actions -> Edit target group attributes**. |
| `00:03:24.570` | So here, let's scroll down and we have the target selection configuration, and here we have stickiness. So here for stickiness, we can turn it on. | Cuộn xuống phần **Target selection configuration**, chúng ta thấy mục **Stickiness** và có thể bật nó lên (`Turn on stickiness`). |
| `00:03:36.120` | And we have two types of stickiness available to us. We have a load balancer generated cookie or the application based cookie. | Chúng ta thấy hai loại Stickiness hiển thị ngay trên giao diện: `Load balancer generated cookie` (Duration-based) hoặc `Application-based cookie`. |
| `00:03:44.670` | So let's look at the first one. So here we're able to set a duration. So between one second to seven days, you can modify it here. | Ở loại thứ nhất (`Load balancer generated cookie`), chúng ta có thể đặt khoảng thời gian duy trì (`Stickiness duration`) từ **1 giây đến 7 ngày**. |
| `00:03:52.920` | Or if you wanted to have your own application cookie, again, they are the same settings, but you need to add an app cookie name, for example, MYCUSTOMCOOKIEAPP. | Hoặc nếu bạn chọn `Application-based cookie`, bạn vẫn có khoảng thời gian tương tự nhưng cần nhập thêm tên cookie của ứng dụng (`App cookie name`), ví dụ `MYCUSTOMCOOKIEAPP`. |
| `00:04:04.920` | And this is just a name that you would give your cookie so that you know how to apply stickiness at the load balancer level. Now, to keep things simple, we're going to choose Load balancer generated cookie and have everything as the default, so one day. And let's click on Save changes. | Để giữ mọi thứ đơn giản trong bài thực hành, chúng ta sẽ chọn `Load balancer generated cookie` với thời hạn mặc định là `1 days` và nhấn **Save changes**. |
| `00:04:22.770` | So now let's have a look. So I'm going to go and open the debugger as well, so we can have a look at the network and see what happens. | Bây giờ hãy kiểm tra kết quả. Tôi sẽ mở công cụ Developer Tools (Debugger) trên trình duyệt và chuyển sang tab **Network** để quan sát những gì diễn ra. |
| `00:04:29.790` | So if you have a look at the network and then I refresh this page, as we can see, I refresh multiple times, okay? You get access to the same instance. So .71.76 is the one that's coming back, back and back and back. | Khi tôi làm mới (refresh) trang web này nhiều lần liên tiếp, bạn có thể thấy chúng ta luôn truy cập vào cùng một instance duy nhất (địa chỉ IP đuôi `.71.76` lặp lại liên tục). |
| `00:04:43.500` | And now what's going to happen is that when you look at the GET request made to the load balancer... if you go to Cookies, as you can see here, there is a response cookie, okay, that is saying that your cookie expires tomorrow. Here is the path and here is the value of the cookie. | Và khi nhấp vào yêu cầu `GET` gửi tới bộ cân bằng tải rồi chuyển sang tab **Cookies**, bạn sẽ thấy một cookie tên là `AWSALB` được gửi về trong Response với thời hạn hết hạn vào ngày mai, kèm theo đường dẫn và giá trị mã hóa của cookie. |
| `00:05:04.200` | And then in the request cookie, when the browser makes a request to the load balancer, it sends again the cookie it has right here. And so because of the cookie being passed and sent, this is how stickiness works, okay? | Và trong phần Request Cookies của các lần tải trang tiếp theo, trình duyệt tự động gửi kèm lại cookie `AWSALB` đó lên bộ cân bằng tải. Nhờ cookie này được truyền đi, bộ cân bằng tải biết phải gửi yêu cầu về đúng EC2 instance cũ. |
| `00:05:15.630` | So just a little bit of a deeper dive into how stickiness works. But that's it for this lecture. I hope you liked it. | Đó là cái nhìn sâu sắc và trực quan về cách hoạt động của Sticky Sessions. |
| `00:05:38.340` | And finally, just go back to your target group, and then you edit the attributes itself and you can disable stickiness to come back to a normal behavior, which should be good to go. So that's it for this lecture, I hope you liked it. And I will see you in the next lecture. | Cuối cùng, hãy quay lại Target Group của bạn, vào Edit attributes và tắt tính năng Stickiness đi để đưa bộ cân bằng tải trở về hành vi phân phối luân phiên bình thường. Hẹn gặp lại bạn ở bài giảng tiếp theo. |
