# Bài 46: EC2 Instances Launch Types Hands On

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `27694918` (`SOA - EC2 - Launch Types v4.mp4`)
- **Thời lượng:** `08:52`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### Thực hành các hình thức khởi chạy và đặt mua EC2 trên AWS Console
1. **Spot Requests & Pricing History:**
   - Trong menu **Spot Requests -> Pricing history**, có thể xem biểu đồ biến động giá Spot trong 3 tháng qua của từng loại máy (ví dụ `c4.large`) theo từng Availability Zone so với đường giá On-Demand cố định (tiết kiệm ~70%).
   - Khi nhấn **Request Spot Instances** (tạo Spot Fleet request):
     - Có thể đặt **Target capacity** theo số lượng **Instances**, số lượng **vCPUs**, hoặc dung lượng **Memory (MB)**.
     - Có thể chọn thủ công các loại máy hoặc lọc theo thuộc tính phần cứng (số vCPU tối thiểu/tối đa, RAM tối thiểu/tối đa).
     - Chọn chiến lược phân bổ (**Allocation strategy**): `Capacity optimized`, `Lowest price`, hoặc `Diversified`.
   - Hoặc khi tạo máy lẻ ở màn hình **Launch an instance -> Advanced details**: Tích chọn **Request Spot instances**, chọn loại request (`One-time` hoặc `Persistent`) và hành vi khi gián đoạn (`Terminate`, `Stop`, hoặc `Hibernate`).
2. **Reserved Instances:**
   - Vào **Reserved Instances -> Purchase Reserved Instances**, tìm loại máy (ví dụ `c5.large`), kỳ hạn (12 tháng hoặc 36 tháng), loại (`Standard` hoặc `Convertible`), và hình thức thanh toán (`All Upfront`, `Partial Upfront`, `No Upfront`).
3. **Savings Plans:**
   - Vào mục **Savings Plans** để cam kết mức chi tiêu `$/hour` trong 1 hoặc 3 năm (linh hoạt hơn và được khuyến nghị thay thế dần cho Reserved Instances).
4. **Dedicated Hosts:**
   - Vào **Dedicated Hosts -> Allocate Dedicated Host**, chọn Instance Family (ví dụ `c5`) và Availability Zone để cấp phát một máy chủ vật lý riêng biệt (tích hợp với **AWS License Manager** để quản lý giấy phép phần mềm).
5. **Capacity Reservations:**
   - Vào **Capacity Reservations -> Create Capacity Reservation**, chọn loại máy (ví dụ 4 máy `m5.2xlarge`) và Availability Zone cụ thể để giữ chỗ tài nguyên (vẫn tính tiền theo giá On-Demand dù có khởi chạy máy hay không).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `04:13` | In the EC2 Console under **Spot Requests**, we can check **Pricing history** (e.g., `c4.large` Linux over 3 months shows ~70% savings across AZs compared to On-Demand). Clicking **Request Spot Instances** opens the Spot Fleet request wizard, where we configure launch parameters, max price, target capacity (by instances, vCPUs, or MB of RAM), interruption behavior (terminate, stop, hibernate), instance type restrictions/attributes, and allocation strategy (Capacity optimized, Lowest price, Diversified). | Trong EC2 Console mục **Spot Requests**, ta có thể xem **Pricing history** (lịch sử giá trong 3 tháng). Khi nhấn **Request Spot Instances**, giao diện tạo Spot Fleet cho phép cấu hình thông số khởi chạy, giá tối đa, dung lượng mục tiêu (theo số lượng máy, số vCPUs hoặc MB RAM), hành vi khi gián đoạn (terminate, stop, hibernate), giới hạn loại máy và chiến lược phân bổ. |
| `04:13` - `05:47` | You can also request a single Spot instance directly from **Launch an instance -> Advanced details -> Request Spot instances**, customizing the max price (capped at On-Demand by default), request type (`One-time` vs `Persistent`), validity period, and interruption behavior (`Hibernate`, `Stop`, `Terminate`). | Bạn cũng có thể yêu cầu Spot instance trực tiếp khi tạo máy tại mục **Launch an instance -> Advanced details -> Request Spot instances**, tùy chỉnh giá tối đa, loại yêu cầu (`One-time` hoặc `Persistent`) và hành vi khi bị thu hồi. |
| `05:47` - `08:52` | Next, we explore **Reserved Instances** (searching offerings for `c5.large`, 1- or 3-year terms, Standard vs Convertible, All/Partial/No Upfront), **Savings Plans** (committing `$/hr` for 1–3 years), **Dedicated Hosts** (allocating a physical host for an instance family like `c5` in a specific AZ, integrated with AWS License Manager), and **Capacity Reservations** (reserving e.g. four `m5.2xlarge` instances in a specific AZ, billed whether launched or not). | Tiếp theo, ta xem qua giao diện mua **Reserved Instances** (chọn loại máy `c5.large`, kỳ hạn 1 hoặc 3 năm, Standard/Convertible, All/Partial/No Upfront), **Savings Plans**, **Dedicated Hosts** (cấp phát máy chủ vật lý riêng gắn với AWS License Manager), và **Capacity Reservations** (đặt giữ chỗ số lượng máy trong một AZ cụ thể). |
