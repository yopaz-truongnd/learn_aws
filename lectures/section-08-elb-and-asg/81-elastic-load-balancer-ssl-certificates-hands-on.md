# Bài 81: Elastic Load Balancer - SSL Certificates - Hands On (Thực hành cấu hình SSL/TLS trên ALB & NLB)

- **Phần (Section):** Phần 8: High Availability and Scalability: ELB & ASG
- **Mã bài học (Lecture ID):** `35136224`
- **Tệp video:** `SAA_-_ELB_-_SSL_Certificates_-_Hands_On_-_v4.mp4`
- **Thời lượng:** `01:59`
- **Cheat sheet:** [topics/aws_elb_asg.html](../../topics/aws_elb_asg.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Cấu hình HTTPS / TLS Listener trên ALB và NLB
1. **Trên Application Load Balancer (ALB):**
   - Vào tab **Listeners** -> Nhấn **Add listener**.
   - Chọn Protocol là **`HTTPS`**, Port mặc định là **`443`**.
   - Chọn **Action:** `Forward to target group` (chọn Target Group đích).
   - **Secure listener settings:**
     - **Security Policy:** Quy định phiên bản giao thức SSL/TLS và bộ mã hóa (cipher suites) để thương lượng chứng chỉ (chọn chính sách phù hợp nếu cần tương thích ngược với các client cũ).
     - **Default SSL/TLS certificate:** Chọn nguồn chứng chỉ từ:
       1. **`From ACM`** (AWS Certificate Manager — được khuyến nghị nhất).
       2. **`From IAM`** (lưu trong IAM Certificate Store — chỉ dùng khi bắt buộc, không khuyến nghị làm phương pháp chính).
       3. **`Import certificate`** (dán trực tiếp Certificate private key, Certificate body, Certificate chain để import thẳng vào ACM hoặc IAM).
2. **Trên Network Load Balancer (NLB):**
   - Vào tab **Listeners** -> Nhấn **Add listener**.
   - Chọn Protocol là **`TLS`** (Port `443`), chọn Target Group đích.
   - Thiết lập **Security Policy**, chọn nguồn chứng chỉ (**ACM**, **IAM**, hoặc **Import**), và tùy chọn cấu hình **ALPN (Application-Layer Protocol Negotiation)** nâng cao.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00.090` | So let's have a look at how we can enable SSL certificates on both the ALB and the NLB. | Hãy cùng xem cách chúng ta có thể kích hoạt chứng chỉ SSL trên cả Application Load Balancer (ALB) và Network Load Balancer (NLB). |
| `00:00:07.470` | So if I look at the ALB, I just have to add one listener, for example, I will add a listener, and the protocol will be HTTPS and the port by default will be 443. | Đầu tiên trên ALB, tôi chỉ cần thêm một Listener mới: chọn giao thức là **HTTPS** và cổng mặc định sẽ là **443**. |
| `00:00:18.600` | And then we can say, okay if the clients are using the port 443 for HTTPS protocol, then forward to a specific target group. | Sau đó chúng ta quy định hành động: nếu client kết nối qua cổng 443 bằng giao thức HTTPS, hãy chuyển tiếp (Forward) tới một Target Group cụ thể. |
| `00:00:28.620` | And then we can also have secure listener settings. So we can actually set an SSL security policy to see how to negotiate the certificates itself, and this is based on if you need, for example, previous compatibility with older versions of SSL or TLS and so on, so you can leave this as default. | Tiếp theo ở phần **Secure listener settings**, chúng ta có thể chọn một chính sách bảo mật SSL (**Security Policy**) để quy định cách thương lượng chứng chỉ — tùy thuộc vào việc bạn có cần tương thích ngược với các phiên bản SSL hoặc TLS cũ hơn hay không; thông thường bạn có thể để mặc định. |
| `00:00:49.560` | And then you need to say where this SSL or TLS certificate is located and so it can be in ACM, Amazon Certificate Manager, but I currently don't have any, so I won't see one here, or from IAM, but this is not recommended as the main method. | Sau đó, bạn cần chỉ định nơi lưu trữ chứng chỉ SSL/TLS mặc định này: có thể lấy từ **ACM (AWS Certificate Manager)**, hoặc lấy từ **IAM** (tuy nhiên IAM không được khuyến nghị làm phương pháp chính). |
| `00:01:05.790` | Or you can import it by just pasting the private key, the body and the certificate chain here if need be and then this will import the certificate itself into ACM directly. | Hoặc bạn có thể chọn **Import** chứng chỉ ngay tại đây bằng cách dán khóa bí mật (private key), nội dung chứng chỉ (certificate body) và chuỗi chứng chỉ (certificate chain) để nhập trực tiếp vào ACM. |
| `00:01:17.310` | So it's a similar process for the network load balancer. So if I go in the network load balancer right here, and have a look at the listeners, I can add a listener of it being TLS, and then we can forward to a demo target group right here. | Quy trình cũng tương tự đối với Network Load Balancer. Khi vào mục Listeners của NLB và nhấn Add listener, tôi chọn giao thức là **TLS**, cổng 443 và chọn chuyển tiếp tới Target Group của NLB. |
| `00:01:31.810` | And then for security policy, we can set whatever policy we want, as well as choose where the certificate is from: so from ACM, IAM, or import, and finally we can set an application layer protocol negotiation, which I won't go over, but this is a pretty advanced setting for TLS. | Ở phần chính sách bảo mật (Security policy), chúng ta cũng chọn chính sách mong muốn, chọn nguồn chứng chỉ từ ACM, IAM hoặc Import, và cuối cùng có thêm tùy chọn **ALPN (Application-Layer Protocol Negotiation)** — một thiết lập nâng cao cho TLS. |
| `00:01:51.270` | So that's it, you've seen how to use SSL or TLS certificates on your load balancers. I hope you liked it and I will see you in the next lecture. | Vậy là xong, bạn đã thấy cách cấu hình chứng chỉ SSL/TLS trên các bộ cân bằng tải của mình. Hy vọng bạn thích bài học này và hẹn gặp lại trong bài giảng tiếp theo. |
