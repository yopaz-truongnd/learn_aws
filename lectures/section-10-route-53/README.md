# Phần 10: Amazon Route 53

- **Khóa học:** Ultimate AWS Certified Solutions Architect Associate 2026 (`SAA-C03`)
- **Chapter ID:** `3172812`
- **Tổng số bài giảng:** 20 bài giảng (Bài 101 -> Bài 120) + 1 bài kiểm tra trắc nghiệm (Quiz 7)
- **Cheat sheet:** [topics/aws_route53.html](../../topics/aws_route53.html)

---

## Tóm tắt nhanh các dịch vụ trong Phần 10 (Service Cheat Sheet)

### 1. Amazon Route 53
- **Là gì:** Dịch vụ hệ thống phân giải tên miền có thẩm quyền (**Authoritative DNS**), nhà đăng ký tên miền (**Domain Registrar**) và kiểm tra sức khỏe tài nguyên (**Health Checks**) được quản lý hoàn toàn với cam kết **100% Availability SLA**.
- **Dùng khi nào (Use case điển hình trong đề):**
  - Định tuyến lưu lượng người dùng tới các tài nguyên AWS (ALB, CloudFront, S3 Website, API Gateway, EC2) thông qua **Public Hosted Zones** (ngoài Internet) hoặc **Private Hosted Zones** (nội bộ trong VPC).
  - Áp dụng các **Routing Policies** theo bài toán kiến trúc:
    - **`Simple`:** Trỏ tới 1 tài nguyên hoặc trả về danh sách IP ngẫu nhiên (không hỗ trợ Health Check).
    - **`Weighted`:** Phân bổ % lưu lượng theo trọng số (Canary testing 5% traffic sang bản mới).
    - **`Latency`:** Điều hướng người dùng tới AWS Region có độ trễ mạng thấp nhất (fastest response time).
    - **`Failover`:** Chuyển đổi dự phòng **Active-Passive** (`Primary` + `Secondary`) dựa trên Health Check.
    - **`Geolocation`:** Điều hướng theo **Châu lục / Quốc gia / Bang của Mỹ** của người dùng (bản địa hóa ngôn ngữ hoặc chặn truy cập theo luật pháp từng nước — luôn cần bản ghi `Default`).
    - **`Geoproximity`:** Dịch chuyển vùng phủ lưu lượng giữa các khu vực địa lý bằng cách tăng/giảm hệ số **`Bias`**.
    - **`IP-based`:** Định tuyến dựa trên dải CIDR IP của Client/ISP.
    - **`Multi-Value Answer`:** Trả về tối đa **8 bản ghi IP khỏe mạnh (có gắn Health Checks)** để cân bằng tải phía Client.
- **Khác gì dịch vụ gần giống:**
  - **Route 53 vs. Elastic Load Balancer (ELB) / Global Accelerator:** `Route 53` chỉ trả lời truy vấn ở **tầng DNS** (lưu lượng dữ liệu thực tế không đi qua Route 53 và chịu ảnh hưởng bởi bộ nhớ đệm `TTL`); `ELB` nhận và chuyển tiếp trực tiếp các gói tin mạng; `Global Accelerator` cấp **2 địa chỉ Anycast IP tĩnh** và định tuyến lưu lượng qua mạng xương sống toàn cầu của AWS (không bị ảnh hưởng bởi DNS caching TTL của client).
  - **Alias Record vs. CNAME Record:**
    - `Alias Record` (kiểu `A`/`AAAA`) trỏ tới tài nguyên AWS, **MIỄN PHÍ truy vấn**, và **dùng được cho cả Root Domain / Zone Apex (`example.com`)** lẫn Subdomain (**Lưu ý:** KHÔNG THỂ tạo Alias trỏ tới EC2 DNS Name!).
    - `CNAME Record` trỏ tới bất kỳ hostname nào nhưng **tính phí** và **CHỈ dùng được cho Subdomain (`www.example.com`)**, tuyệt đối không dùng được cho Zone Apex.
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Health Checks:**
    - Có ~15 Global Health Checkers; cần **> 18%** báo mã `2xx`/`3xx` (hoặc khớp chuỗi trong **5.120 bytes đầu tiên**) để được tính là `Healthy`.
    - Giám sát **Private Resource (trong VPC / On-premises):** Tạo **CloudWatch Metric + CloudWatch Alarm**, sau đó tạo Route 53 Health Check giám sát chính **CloudWatch Alarm** đó.
  - **Tên miền mua ở bên thứ 3 (GoDaddy):** Tạo **Public Hosted Zone** trong Route 53, sau đó lấy 4 địa chỉ NS cập nhật vào mục **NS records trên GoDaddy**.

### 2. Route 53 Resolver & Hybrid DNS (Inbound / Outbound Endpoints)
- **Là gì:** Tính năng mở rộng của bộ phân giải DNS trong VPC giúp kết nối và chuyển tiếp truy vấn DNS hai chiều giữa mạng **AWS VPC** và mạng **On-Premises Data Center** (qua VPN hoặc Direct Connect).
- **Dùng khi nào (Use case điển hình trong đề):**
  - Xây dựng kiến trúc **Hybrid DNS** khi máy chủ dưới On-premises cần phân giải các tên miền trong **Route 53 Private Hosted Zone**, hoặc khi EC2 trong VPC cần phân giải các tên miền nội bộ thuộc máy chủ DNS dưới On-premises.
- **Khác gì giữa hai loại Endpoint (Rất hay bẫy ngược chiều trong đề thi):**
  - **`Resolver Inbound Endpoint`:** Cho phép truy vấn DNS đi **TỪ On-Premises VÀO AWS VPC** (On-premises DNS Resolver chuyển tiếp truy vấn tới IP của Inbound Endpoint).
  - **`Resolver Outbound Endpoint` (+ Forwarding Rules):** Cho phép truy vấn DNS đi **TỪ AWS VPC RA On-Premises** (Route 53 Resolver dùng Forwarding Rule đẩy truy vấn qua Outbound Endpoint về On-premises DNS Server).
- **Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa gợi ý):**
  - **Từ khóa gợi ý:** `"on-premises servers need to resolve domains in Route 53 Private Hosted Zone"` $\rightarrow$ **Inbound Endpoint**; `"EC2 instances in VPC need to resolve on-premises corporate domains"` $\rightarrow$ **Outbound Endpoint + Resolver Forwarding Rule**.

---

## Danh sách bài học trong Phần 10

| STT | Lecture ID | Tên bài giảng | Loại | Thời lượng | Trạng thái |
| :---: | :---: | :--- | :---: | :---: | :--- |
| 101 | `28384280` | [What is a DNS ?](./101-what-is-a-dns.md) | Video | 06:24 | **Đã lưu** |
| 102 | `13528180` | [Route 53 Overview](./102-route-53-overview.md) | Video | 06:18 | **Đã lưu** |
| 103 | `28384290` | [Route 53 - Registering a domain](./103-route-53-registering-a-domain.md) | Video | 03:24 | **Đã lưu** |
| 104 | `28384312` | [Route 53 - Creating our first records](./104-route-53-creating-our-first-records.md) | Video | 03:56 | **Đã lưu** |
| 105 | `13528186` | [Route 53 - EC2 Setup](./105-route-53-ec2-setup.md) | Video | 05:40 | **Đã lưu** |
| 106 | `13528188` | [Route 53 - TTL](./106-route-53-ttl.md) | Video | 05:28 | **Đã lưu** |
| 107 | `13528190` | [Route 53 CNAME vs Alias](./107-route-53-cname-vs-alias.md) | Video | 07:00 | **Đã lưu** |
| 108 | `13528192` | [Routing Policy - Simple](./108-routing-policy-simple.md) | Video | 04:05 | **Đã lưu** |
| 109 | `13528194` | [Routing Policy - Weighted](./109-routing-policy-weighted.md) | Video | 05:02 | **Đã lưu** |
| 110 | `13528196` | [Routing Policy - Latency](./110-routing-policy-latency.md) | Video | 04:39 | **Đã lưu** |
| 111 | `13528200` | [Route 53 - Health Checks](./111-route-53-health-checks.md) | Video | 04:54 | **Đã lưu** |
| 112 | `28384354` | [Route 53 - Health Checks Hands On](./112-route-53-health-checks-hands-on.md) | Video | 04:39 | **Đã lưu** |
| 113 | `13528204` | [Routing Policy - Failover](./113-routing-policy-failover.md) | Video | 04:12 | **Đã lưu** |
| 114 | `13528206` | [Routing Policy - Geolocation](./114-routing-policy-geolocation.md) | Video | 04:15 | **Đã lưu** |
| 115 | `26099214` | [Routing Policy - Geoproximity](./115-routing-policy-geoproximity.md) | Video | 03:21 | **Đã lưu** |
| 116 | `37045728` | [Routing Policy - IP-based](./116-routing-policy-ip-based.md) | Video | 01:45 | **Đã lưu** |
| 117 | `13528210` | [Routing Policy - Multi Value](./117-routing-policy-multi-value.md) | Video | 03:42 | **Đã lưu** |
| 118 | `13528212` | [3rd Party Domains & Route 53](./118-third-party-domains-and-route-53.md) | Video | 02:24 | **Đã lưu** |
| 119 | `51771513` | [Route 53 Resolvers & Hybrid DNS](./119-route-53-resolvers-and-hybrid-dns.md) | Video | 02:56 | **Đã lưu** |
| 120 | `13528214` | [Route 53 - Section Cleanup](./120-route-53-section-cleanup.md) | Video | 01:21 | **Đã lưu** |
| Quiz 7 | `5336917` | [Amazon Route 53 Quiz](./quiz-07-amazon-route-53-quiz.md) | Quiz | 7 câu | **Đã lưu** |
