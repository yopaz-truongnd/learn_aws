# Quiz 7: Amazon Route 53 Quiz (Bộ câu hỏi trắc nghiệm Phần 10)

- **Section:** Phần 10 - Route 53
- **Quiz ID:** `5336917`
- **Số lượng câu hỏi:** `7 câu`
- **Cheat sheet:** [topics/aws_route53.html](../../topics/aws_route53.html)

---

## Câu hỏi 1 (ID: `37586207`)

**Câu hỏi (English):**
You have purchased **mycoolcompany.com** on Amazon Route 53 Registrar and would like the domain to point to your Elastic Load Balancer **my-elb-1234567890.us-west-2.elb.amazonaws.com**. Which Route 53 Record type must you use here?

**Dịch nghĩa (Tiếng Việt):**
Bạn đã mua tên miền **mycoolcompany.com** trên Amazon Route 53 Registrar và muốn trỏ trực tiếp tên miền gốc này tới Elastic Load Balancer **my-elb-1234567890.us-west-2.elb.amazonaws.com**. Bạn bắt buộc phải sử dụng loại bản ghi Route 53 nào tại đây?

- [ ] A. CNAME
- [ ] B. Alias

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Alias**

> [!NOTE]
> **Giải thích:**
> Bạn **không thể** tạo bản ghi `CNAME` cho nút đỉnh của không gian tên DNS (**Zone Apex / Root Domain**), trong trường hợp này là `mycoolcompany.com`. Để trỏ một Root Domain tới tài nguyên AWS như Elastic Load Balancer, bạn bắt buộc phải sử dụng bản ghi **Alias** (kiểu `A` hoặc `AAAA`).
</details>

---

## Câu hỏi 2 (ID: `37586215`)

**Câu hỏi (English):**
You have deployed a new Elastic Beanstalk environment and would like to direct 5% of your production traffic to this new environment. This allows you to monitor for CloudWatch metrics and ensuring that there're no bugs exist with your new environment. Which Route 53 Routing Policy allows you to do so?

**Dịch nghĩa (Tiếng Việt):**
Bạn vừa triển khai một môi trường Elastic Beanstalk mới và muốn điều hướng 5% lưu lượng production sang môi trường mới này để theo dõi các chỉ số CloudWatch và đảm bảo không có lỗi phát sinh. Chính sách định tuyến (Routing Policy) nào của Route 53 cho phép bạn thực hiện việc này?

- [ ] A. Simple
- [ ] B. Weighted
- [ ] C. Latency
- [ ] D. Failover

<details><summary>👉 Xem đáp án</summary>

**Đáp án: B. Weighted**

> [!NOTE]
> **Giải thích:**
> **Weighted Routing Policy** (Chính sách định tuyến theo trọng số) cho phép bạn phân bổ một phần lưu lượng truy cập dựa trên trọng số (tỷ lệ phần trăm). Đây là use case rất phổ biến để gửi một phần nhỏ lưu lượng (như 5%) tới phiên bản ứng dụng mới nhằm kiểm thử (Canary testing).
</details>

---

## Câu hỏi 3 (ID: `37586225`)

**Câu hỏi (English):**
You have updated a Route 53 Record's **myapp.mydomain.com** value to point to a new Elastic Load Balancer, but it looks like users are still redirected to the old ELB. What is a possible cause for this behavior?

**Dịch nghĩa (Tiếng Việt):**
Bạn vừa cập nhật giá trị của bản ghi Route 53 **myapp.mydomain.com** để trỏ sang một chiếc Elastic Load Balancer mới, nhưng có vẻ như người dùng vẫn đang bị điều hướng về chiếc ELB cũ. Nguyên nhân khả dĩ gây ra hiện tượng này là gì?

- [ ] A. Because of the Alias record
- [ ] B. Because of the CNAME record
- [ ] C. Because of the TTL
- [ ] D. Because of Route 53 Health Checks

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. Because of the TTL**

> [!NOTE]
> **Giải thích:**
> Mỗi bản ghi DNS đều có một giá trị **TTL (Time To Live)** yêu cầu Client và DNS Resolver lưu kết quả phân giải vào bộ nhớ đệm (cache) trong khoảng thời gian đó để tránh làm quá tải DNS Resolver. Khi bạn đổi giá trị bản ghi, các Client vẫn sẽ kết nối tới địa chỉ cũ trong cache cho đến khi thời gian TTL hết hạn.
</details>

---

## Câu hỏi 4 (ID: `37586365`)

**Câu hỏi (English):**
You have an application that's hosted in two different AWS Regions `us-west-1` and `eu-west-2`. You want your users to get the best possible user experience by minimizing the response time from application servers to your users. Which Route 53 Routing Policy should you choose?

**Dịch nghĩa (Tiếng Việt):**
Bạn có một ứng dụng được đặt tại hai AWS Regions khác nhau là `us-west-1` và `eu-west-2`. Bạn muốn người dùng có trải nghiệm tốt nhất bằng cách giảm thiểu thời gian phản hồi (response time) từ máy chủ ứng dụng tới người dùng. Bạn nên chọn Route 53 Routing Policy nào?

- [ ] A. Multi Value
- [ ] B. Weighted
- [ ] C. Latency
- [ ] D. Geolocation

<details><summary>👉 Xem đáp án</summary>

**Đáp án: C. Latency**

> [!NOTE]
> **Giải thích:**
> **Latency Routing Policy** sẽ đánh giá độ trễ mạng giữa người dùng và các AWS Regions, từ đó trả về phản hồi DNS giúp giảm thiểu tối đa độ trễ (thời gian phản hồi) cho người dùng.
</details>

---

## Câu hỏi 5 (ID: `37586393`)

**Câu hỏi (English):**
You have a legal requirement that people in any country but France should **NOT** be able to access your website. Which Route 53 Routing Policy helps you in achieving this?

**Dịch nghĩa (Tiếng Việt):**
Bạn có một yêu cầu pháp lý quy định rằng người dùng ở bất kỳ quốc gia nào ngoại trừ nước Pháp đều **KHÔNG** được phép truy cập vào website của bạn. Chính sách định tuyến nào của Route 53 giúp bạn đạt được điều này?

- [ ] A. Latency
- [ ] B. Simple
- [ ] C. Multi Value
- [ ] D. Geolocation

<details><summary>👉 Xem đáp án</summary>

**Đáp án: D. Geolocation**

> [!NOTE]
> **Giải thích:**
> **Geolocation Routing Policy** định tuyến dựa trên vị trí địa lý thực tế (Châu lục, Quốc gia, Tiểu bang Mỹ) của người dùng. Nó rất phù hợp cho việc bản địa hóa nội dung hoặc giới hạn phân phối nội dung theo yêu cầu pháp lý của từng quốc gia.
</details>

---

## Câu hỏi 6 (ID: `37586409`)

**Câu hỏi (English):**
You have purchased a domain on **GoDaddy** and would like to use Route 53 as the DNS Service Provider. What should you do to make this work?

**Dịch nghĩa (Tiếng Việt):**
Bạn đã mua một tên miền trên **GoDaddy** và muốn sử dụng Route 53 làm Nhà cung cấp dịch vụ DNS (DNS Service Provider). Bạn cần phải làm gì để thiết lập hoạt động?

- [ ] A. Request for a domain transfer
- [ ] B. Create a Private Hosted Zone and update the 3rd party Registrar NS records
- [ ] C. Create a Public Hosted Zone and update the Route 53 NS records
- [ ] D. Create a Public Hosted Zone and update the 3rd party Registrar NS records

<details><summary>👉 Xem đáp án</summary>

**Đáp án: D. Create a Public Hosted Zone and update the 3rd party Registrar NS records**

> [!NOTE]
> **Giải thích:**
> **Public Hosted Zones** được dùng để trả lời các truy vấn từ người dùng truy cập website qua Internet công cộng. Để dùng tên miền mua ở bên thứ 3 với Route 53, bạn tạo một **Public Hosted Zone** trong Route 53 rồi lấy 4 địa chỉ Name Servers của nó đem cập nhật vào bản ghi **NS (Name Servers)** trên trang quản trị của nhà đăng ký bên thứ 3 (GoDaddy).
</details>

---

## Câu hỏi 7 (ID: `37586421`)

**Câu hỏi (English):**
Which of the following are **NOT** valid Route 53 Health Checks?

**Dịch nghĩa (Tiếng Việt):**
Loại nào sau đây **KHÔNG** phải là một Route 53 Health Check hợp lệ?

- [ ] A. Health Check that monitors an SQS Queue
- [ ] B. Health Check that monitors an Endpoint
- [ ] C. Health Check that monitors other Health Checks
- [ ] D. Health Check that monitors CloudWatch Alarms

<details><summary>👉 Xem đáp án</summary>

**Đáp án: A. Health Check that monitors an SQS Queue**

> [!NOTE]
> **Giải thích:**
> Route 53 chỉ hỗ trợ **3 loại Health Checks**:
> 1. Giám sát một **Endpoint** công khai (`Monitor an Endpoint`).
> 2. Giám sát các **Health Checks khác** (`Calculated Health Check`).
> 3. Giám sát trạng thái của **CloudWatch Alarms** (`Monitor a CloudWatch Alarm`).
> Không có loại Health Check nào giám sát trực tiếp hàng đợi SQS Queue.
</details>
