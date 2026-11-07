# Bài 31: AWS Budget Setup

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098410` (`CCP - Creating an AWS Budget v5.mp4`)
- **Thời lượng:** `05:05`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Cấp quyền cho IAM User xem thông tin Billing
- Mặc định, ngay cả khi một IAM User có quyền **`AdministratorAccess`**, User đó vẫn bị **`AccessDenied`** khi truy cập **Billing and Cost Management Console**.
- **Cách khắc phục:**
  1. Đăng nhập bằng **Root Account** -> Nhấp vào tên tài khoản ở góc phải -> Chọn **Account**.
  2. Cuộn xuống mục **IAM user and role access to Billing information** -> Chọn **Edit** -> Tích chọn **Activate IAM access** -> Update.
  3. Sau khi bật, các IAM Users có quyền Admin (hoặc Billing policy) mới xem được dữ liệu chi phí.

### 1.2. Các công cụ theo dõi chi phí trong Billing Console
- **Bills:** Xem chi tiết hóa đơn theo từng tháng, phân rã chi phí theo từng dịch vụ (**Charges by service**) và từng Region (ví dụ: chi phí EC2, NAT Gateway, EBS, Elastic IP tại Region Ireland).
- **Free Tier Dashboard:** Theo dõi mức sử dụng hiện tại (Current usage) và dự báo (Forecasted usage) so với hạn mức miễn phí của AWS Free Tier.
- **AWS Budgets:** Thiết lập ngân sách và gửi cảnh báo qua email khi chi phí vượt ngưỡng:
  1. **Zero spend budget:** Cảnh báo ngay khi phát sinh chi phí chỉ từ `$0.01` (`1 cent`).
  2. **Monthly cost budget:** Đặt hạn mức chi tiêu hàng tháng (ví dụ: `$10/tháng`) và gửi email tại 3 mốc:
     - Chi phí thực tế (Actual spend) chạm **85%**.
     - Chi phí thực tế (Actual spend) chạm **100%**.
     - Chi phí dự báo (Forecasted spend) dự kiến chạm **100%**.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:21` | Let's set up a budget and an alarm in the Billing and Cost Management console. Notice that when logged in as IAM user `Stephane` (even with `AdministratorAccess`), we get `AccessDenied` on billing data. To fix this, log into the **Root account**, go to **Account**, scroll down to **IAM user and role access to Billing information**, and activate IAM access. Refreshing the Billing console now displays all cost data. | Hãy thiết lập ngân sách (Budget) và cảnh báo trong Billing Console. Lưu ý rằng khi đăng nhập bằng IAM user `Stephane` (dù có quyền `AdministratorAccess`), ta vẫn bị báo lỗi `AccessDenied`. Để mở quyền này, phải đăng nhập **Root account** -> vào **Account** -> cuộn xuống mục **IAM user and role access to Billing information** và bật **Activate IAM access**. |
| `01:21` - `03:05` | In the Billing console, you can view month-to-date cost, forecasted cost, and under **Bills**, see **Charges by service** broken down by region (e.g., EC2 NAT Gateway, EBS, Elastic IP costs). Under **Free Tier** on the left menu, you can track current and forecasted usage against AWS Free Tier limits. | Trong Billing Console, bạn có thể xem chi phí từ đầu tháng, chi phí dự báo, và vào mục **Bills** để xem chi tiết **Charges by service** theo từng dịch vụ và Region. Tại mục **Free Tier**, bạn theo dõi được mức sử dụng hiện tại và dự báo so với hạn mức miễn phí. |
| `03:05` - `05:05` | Under **Budgets -> Create budget**, we can use simplified templates: 1) **Zero spend budget** (`My Zero Spend Budget`), which sends an email alert as soon as spending reaches `$0.01`; and 2) **Monthly cost budget** (e.g., `$10/month`), which sends three email alerts: when actual spend reaches 85%, when actual spend reaches 100%, and when forecasted spend is expected to reach 100%. | Vào **Budgets -> Create budget**, chọn mẫu đơn giản hóa: 1) **Zero spend budget** — gửi email cảnh báo ngay khi tiêu tốn `1 cent` (`$0.01`); và 2) **Monthly cost budget** (ví dụ `$10/tháng`) — tự động gửi 3 email cảnh báo khi chi tiêu thực tế đạt 85%, đạt 100%, hoặc khi chi tiêu dự báo chạm mức 100%. |
