# Bài 103: Route 53 - Registering a domain (Đăng ký tên miền trên Route 53)

- **Section:** Phần 10 - Route 53
- **Lecture ID:** `28384290`
- **Video:** `SAA_-_Route_53_-_Registering_Domains_v3.mp4`
- **Thời lượng:** `03:24`
- **Cheat sheet:** [topics/aws_route53.html](../../topics/aws_route53.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Quy trình đăng ký tên miền trên Amazon Route 53 (Hands-on)
1. Truy cập **Route 53 Console** -> mục **Registered domains** -> nhấn **Register domains**.
2. Nhập tên miền mong muốn (chưa có ai sở hữu) và kiểm tra tính khả dụng cùng mức giá (thường từ **\$12 - \$13/năm** cho đuôi `.com`).
3. Chọn **Duration** (thời hạn đăng ký, mặc định 1 năm) và cấu hình **Auto-renew**:
   - **Bật Auto-renew:** Nếu dùng tên miền lâu dài cho thực tế để tránh bị người khác mua mất khi hết hạn.
   - **Tắt Auto-renew:** Nếu chỉ đăng ký tạm thời để học tập/thực hành trong khóa học.
4. Điền thông tin liên hệ (**Contact information** cho Registrant, Admin, Tech) và bật **Privacy protection** để ẩn thông tin cá nhân (địa chỉ, số điện thoại, email) khỏi cơ sở dữ liệu WHOIS công khai nhằm tránh spam.
5. Xác nhận điều khoản và hoàn tất thanh toán.

### 1.2. Kết quả sau khi đăng ký tên miền
- Khi đăng ký tên miền thành công trên Route 53, AWS sẽ **tự động tạo một Public Hosted Zone** tương ứng với tên miền đó.
- Trong Hosted Zone mới tạo luôn có sẵn **2 bản ghi mặc định**:
  - **`NS` (Name Server) record:** Chỉ định 4 máy chủ DNS của AWS Route 53 chịu trách nhiệm trả lời các truy vấn DNS cho tên miền này (Route 53 là Source of Truth).
  - **`SOA` (Start of Authority) record:** Chứa thông tin quản trị của Hosted Zone.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
|---|---|---|
| `00:00:00` | Okay, so we are in Route 53 and we're going to be registering domains. | Được rồi, chúng ta đang ở trong Route 53 và sẽ tiến hành đăng ký tên miền. |
| `00:00:04` | So as you can see, I have one hosted zone and one domain. You should have none right now. It's just because I've been using my accounts before. | Như bạn thấy, tôi đang có một Hosted Zone và một tên miền. Hiện tại tài khoản của bạn có thể chưa có cái nào, đây là do tôi đã dùng tài khoản này từ trước. |
| `00:00:11` | But let's go and register a domain. So on the left hand side, click on register domains and you have a new console experience. | Hãy đi đăng ký một tên miền. Ở phía bên trái, nhấp vào **Registered domains** và bạn sẽ thấy giao diện Console mới. |
| `00:00:18` | If you don't have it, you can click on somewhere to use the new console and I will use this because this is what's going to happen moving forward. | Nếu bạn chưa thấy giao diện mới, bạn có thể bật tùy chọn sử dụng Console mới, tôi sẽ dùng giao diện này vì đây là giao diện chuẩn về sau. |
| `00:00:25` | So here we have a domain name. This is stephanetheteacher.com. It's something I have registered a while ago and you will have nothing. | Ở đây tôi có tên miền `stephanetheteacher.com` đã đăng ký từ trước, còn bạn sẽ chưa có gì. |
| `00:00:32` | So what we need to do to get started with Route 53 is to actually register our own domain. | Để bắt đầu thực hành với Route 53, chúng ta cần đăng ký tên miền của riêng mình. |
| `00:00:38` | So this is going to cost you money and if you don't want to pay say $12 a year to have a domain name, just don't do this and watch this section entirely. | Việc này sẽ tốn phí, và nếu bạn không muốn trả khoảng \$12 một năm để có một tên miền, bạn không cần làm bước này mà chỉ cần xem hết các video trong chương này là được. |
| `00:00:47` | So I'm going to follow the step you would follow. So register domain, and here you just enter a domain name. | Tôi sẽ làm theo đúng các bước mà bạn sẽ thực hiện. Nhấp vào **Register domain**, và tại đây bạn chỉ cần nhập một tên miền. |
| `00:00:52` | So something that no one else has chosen before whatever you want. Okay? The idea is that you choose a domain name. So hopefully no one has registered domain name. | Hãy chọn một tên miền mà chưa ai từng đăng ký trước đó, tùy ý bạn. Hy vọng là chưa có ai đăng ký tên miền này. |
| `00:01:03` | Okay, perfect. So I can buy this one for US $13 a year. So I will select it and it's in my basket. So I'm going to proceed to checkout. | Tuyệt vời. Tôi có thể mua tên miền này với giá \$13 Mỹ một năm. Tôi sẽ chọn nó để thêm vào giỏ hàng, rồi nhấn **Proceed to checkout**. |
| `00:01:13` | So here is my domain name. I can choose Duration, for example, one year and I can autorenew or not autorenew. | Đây là tên miền của tôi. Tôi có thể chọn **Duration** (thời hạn), ví dụ 1 năm, và chọn bật hoặc tắt **Auto-renew** (tự động gia hạn). |
| `00:01:19` | So if you intend on keeping a domain, please leave autorenew on. If you don't want it at the end of the year, click it so that it's off. | Nếu bạn có ý định giữ tên miền này lâu dài, hãy để **Auto-renew** bật. Nếu bạn không muốn giữ nó sau khi hết 1 năm, hãy bỏ chọn để tắt nó đi. |
| `00:01:27` | But of course, if you use the domain, it's much better to keep autorenew on. Otherwise someone will be able to buy the domain when you lose it. And this is not good, so up to you to keep it on or off. | Tất nhiên nếu bạn thực sự sử dụng tên miền đó thì nên bật Auto-renew, nếu không người khác sẽ có thể mua mất tên miền khi nó hết hạn. Nhưng nếu bạn chỉ định mua để học khóa này thì hãy tắt nó đi. |
| `00:01:41` | Okay, click on Next. Then we have contact information. So this is the information that you have part of the account that has been pre-populated. | Nhấp vào **Next**. Tiếp theo là phần thông tin liên hệ (**Contact information**). Thông tin từ tài khoản của bạn đã được điền sẵn vào đây. |
| `00:01:51` | And so you can enter your own information if you wanted to. And so the admin contact and the tech contact can be the same as the registrant contact. | Bạn có thể nhập thông tin của mình vào. Liên hệ quản trị (Admin contact) và liên hệ kỹ thuật (Tech contact) có thể để giống với người đăng ký (Registrant contact). |
| `00:02:00` | And finally, you should enable privacy protection so that you don't receive spam. And so that the real contact information, your own personal address, phone number, et cetera is hidden from the internet. | Cuối cùng, bạn nên bật **Privacy protection** (Bảo vệ quyền riêng tư) để không bị nhận thư rác (spam), và để thông tin liên hệ thật như địa chỉ cá nhân, số điện thoại của bạn được ẩn khỏi Internet. |
| `00:02:11` | You click on Next and then you have the review page. So make sure everything is correct and you check the terms and condition. | Nhấp vào **Next** để tới trang kiểm tra lại (Review). Hãy đảm bảo mọi thứ đều chính xác và tích chọn đồng ý với điều khoản & điều kiện. |
| `00:02:19` | And if you submit, just so you know, you will pay these $13. So please don't do this if you don't want to pay that amount of money. | Lưu ý rằng nếu bạn nhấn **Submit**, bạn sẽ phải thanh toán \$13 này. Vì vậy đừng nhấn nếu bạn không muốn chi trả khoản tiền đó. |
| `00:02:26` | Then your domain is going to be registered after a little bit of time. It can take a few minutes or a few hours but you'll be good to go. | Sau đó tên miền của bạn sẽ được đăng ký sau một khoảng thời gian ngắn — có thể mất vài phút hoặc vài giờ là sẵn sàng. |
| `00:02:33` | And to confirm everything, just go on the left hand side to hosted zones and then you click on stephanetheteacher.com or whatever domain name you have registered. | Để kiểm tra lại mọi thứ, hãy nhìn sang thanh bên trái, vào mục **Hosted zones** rồi nhấp vào `stephanetheteacher.com` hoặc bất kỳ tên miền nào bạn vừa đăng ký. |
| `00:02:42` | And you will have a few records and you should have two records. I have four because I've been using this before. But you should have the NS record and the SOA record. | Bạn sẽ thấy có sẵn **2 bản ghi** (tôi có 4 bản ghi vì đã dùng từ trước). Bạn sẽ có bản ghi **NS** và bản ghi **SOA**. |
| `00:02:53` | And the NS record is simply saying that you should use the AWS DNS to answer DNS queries. And this is Route 53. | Bản ghi **NS** đơn giản chỉ định rằng hệ thống sẽ sử dụng AWS DNS (chính là Route 53) để trả lời các truy vấn DNS cho tên miền này. |
| `00:03:01` | So what this means that now that we have a hosted zone, anytime we will insert DNS records such as this one or that one and I will teach you in the next lecture is how to do it. | Điều này có nghĩa là khi đã có Hosted Zone, bất cứ khi nào chúng ta thêm các bản ghi DNS (tôi sẽ hướng dẫn trong bài giảng tiếp theo), |
| `00:03:10` | Then the source of truth for these DNS records will be Route 53 itself. So what we're configuring in here, so that's perfect. | thì nguồn chân lý (Source of Truth) cho các bản ghi DNS đó chính là Route 53. Mọi thứ chúng ta cấu hình tại đây đã hoàn hảo. |
| `00:03:17` | We're good to go. We have a domain name and we can get started with the hands-on. I hope you liked it and I will see you in the next lecture. | Chúng ta đã sẵn sàng. Chúng ta đã có tên miền và có thể bắt đầu thực hành. Hy vọng bạn thích bài học này và hẹn gặp lại ở bài giảng tiếp theo. |
