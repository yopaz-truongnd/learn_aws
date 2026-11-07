# Bài 36: Security Groups Hands On

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098138` (`CCP_-_EC2_-_Security_Groups_Hands_On_v3.mp4`)
- **Thời lượng:** `04:45`

---

## 1. Kiến thức trọng tâm (Exam Notes)

- **Kiểm chứng thực tế lỗi Timeout do Security Group:**
  - Trong menu **Network & Security -> Security Groups**, chọn group `launch-wizard-1` đang gắn với EC2 Instance.
  - Khi **xóa Inbound rule `HTTP (Port 80)`** và lưu lại: Làm mới trình duyệt truy cập địa chỉ IP của EC2 lập tức bị xoay vòng chờ mãi rồi báo lỗi **Timeout** -> Chứng minh mọi lỗi **Timeout** khi kết nối tới EC2 là do Security Group chặn.
  - Khi **thêm lại Inbound rule `HTTP (Port 80)`** cho phép từ `Anywhere-IPv4 (0.0.0.0/0)`: Trang web lập tức tải lại bình thường.
- **Các tùy chọn Source (Nguồn) khi cấu hình Inbound Rule:**
  - `Anywhere-IPv4` (`0.0.0.0/0`) hoặc `Anywhere-IPv6` (`::/0`).
  - `Custom`: Nhập một CIDR block tùy chỉnh, một Prefix List, hoặc một Security Group ID khác (`sg-xxxx`).
  - `My IP`: Chỉ cho phép địa chỉ IP hiện tại của máy tính bạn truy cập (`x.x.x.x/32`). *(Lưu ý: nếu mạng nhà/văn phòng của bạn đổi IP động, bạn sẽ bị mất kết nối Timeout cho đến khi cập nhật lại IP mới)*.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `02:40` | Under **Network & Security -> Security Groups**, we see `default` and `launch-wizard-1`. `launch-wizard-1` has two inbound rules: `SSH` (port 22) from `0.0.0.0/0` and `HTTP` (port 80) from `0.0.0.0/0`. If we delete the `HTTP` port 80 rule and refresh our web server page, the browser hangs in an infinite loading screen and eventually fails with a **timeout**. Anytime you see a timeout connecting to an EC2 instance (SSH, HTTP, etc.), it is 100% a Security Group issue. | Vào mục **Network & Security -> Security Groups**, chọn `launch-wizard-1` đang có 2 quy tắc Inbound là `SSH` (port 22) và `HTTP` (port 80) từ `0.0.0.0/0`. Khi xóa quy tắc `HTTP` port 80 rồi tải lại trang web, trình duyệt sẽ quay vòng chờ vô tận rồi báo lỗi **Timeout**. Bất cứ khi nào gặp lỗi Timeout khi kết nối vào EC2, 100% nguyên nhân nằm ở Security Group. |
| `02:40` - `04:45` | Adding back the `HTTP` (port 80) rule from `Anywhere-IPv4` (`0.0.0.0/0`) immediately restores access to the website. When adding rules, you can choose protocol shortcuts (like `HTTPS` port 443) and set the Source to `Anywhere`, a custom CIDR/Security Group, or `My IP` (just note that if your IP changes, you'll get a timeout). Outbound rules allow all traffic (`0.0.0.0/0`) by default. Finally, remember multiple security groups can be attached to one instance (their rules are combined), and one security group can be attached to multiple instances. | Khi thêm lại quy tắc `HTTP` (port 80) từ `Anywhere-IPv4` (`0.0.0.0/0`), trang web lập tức hoạt động trở lại. Bạn có thể chọn nguồn (Source) là `Anywhere`, CIDR/Security Group tùy chỉnh, hoặc `My IP` (chỉ cho phép IP hiện tại của bạn). Outbound rules mặc định cho phép mọi lưu lượng ra ngoài. Một EC2 có thể gắn nhiều Security Groups (các quy tắc sẽ được cộng gộp lại) và một Security Group có thể gắn cho nhiều EC2. |
