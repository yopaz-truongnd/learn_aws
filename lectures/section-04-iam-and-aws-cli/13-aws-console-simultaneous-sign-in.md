# Bài 13: AWS Console Simultaneous Sign-in

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `51960287` (`CCP - Console - Multi Session Support v1.mp4`)
- **Thời lượng:** `01:48`

---

## 1. Kiến thức trọng tâm (Exam Notes)

- **Multi-session Support (Đăng nhập đồng thời nhiều phiên):**
  - Tính năng mới của AWS Management Console cho phép đăng nhập **nhiều tài khoản AWS (Multiple Accounts) hoặc nhiều vai trò (Roles/Identities) khác nhau trên cùng một trình duyệt** (tối đa 5 phiên cùng lúc) mà không cần phải dùng cửa sổ ẩn danh (Private/Incognito window).
  - Cách bật: Nhấp vào menu tài khoản ở góc trên bên phải -> Bật **Multi-session support** -> Chọn **Add session** để đăng nhập thêm tài khoản hoặc IAM User khác.
  - Mỗi tab/cửa sổ sẽ làm việc độc lập với tài khoản tương ứng của tab đó.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:42` | So let me show you something cool now called the multi-session support. You click on it to turn it on, and the idea now is that I can have in this browser a specific role or account and then I can add a session, and sign into any of your identities using the same browser. So here I click on it and add a session. And now you can login again using any account ID or root. After being signed in, I have one specific account ID here and a different account ID on the other tab. | Tôi sẽ giới thiệu một tính năng rất hay gọi là **Multi-session support** (Hỗ trợ đa phiên). Khi bật tính năng này lên, bạn có thể giữ một tài khoản/role đang mở và nhấn **Add session** để đăng nhập vào bất kỳ danh tính/tài khoản nào khác ngay trên cùng một trình duyệt. |
| `00:42` - `01:48` | For example, if I go to the EC2 console under Volumes in one account and create a 1 GB EBS volume, and then check EC2 Volumes on the other account tab, I don't see any volumes because it is a different account window. That means you can have multiple accounts under the same browser without disconnecting each other. | Ví dụ, khi tôi tạo nhanh một ổ đĩa EBS 1 GB trong phần EC2 Volumes ở tab tài khoản thứ nhất, rồi chuyển sang tab của tài khoản thứ hai kiểm tra, sẽ không thấy ổ đĩa đó vì hai tab thuộc hai tài khoản khác nhau hoàn toàn độc lập trên cùng một trình duyệt. |
