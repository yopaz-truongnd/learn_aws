# Bài 12: IAM Users & Groups Hands On

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098012` (`CCP - IAM - Users Groups Hands On v7.mp4`)
- **Thời lượng:** `06:23`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Nhận diện dịch vụ Global trên AWS Console
- Khi truy cập vào **IAM Console**, góc trên bên phải hiển thị **Global** (không thể chọn Region như N. Virginia hay Ireland).
- Điều này khẳng định mọi IAM Users, Groups, Policies, Roles được tạo đều mang tính toàn cầu.

### 1.2. Quy trình tạo IAM User & Group thực tế
1. **Tạo IAM User (`stephane`):**
   - Tích chọn **Provide user access to the AWS Management Console**.
   - Chọn **I want to create an IAM user** (thay vì IAM Identity Center — trong phạm vi bài thi SAA-C03 cần nắm vững IAM User chuẩn).
   - Thiết lập mật khẩu (Custom password hoặc Auto-generated password) và tùy chọn bắt buộc đổi mật khẩu ở lần đăng nhập kế tiếp.
2. **Gán quyền qua Group (`admin`):**
   - Tạo group `admin` và đính kèm policy **`AdministratorAccess`**.
   - Thêm user `stephane` vào group `admin` -> User sẽ **kế thừa (inherit)** quyền `AdministratorAccess` từ group mà không cần gán trực tiếp.
3. **Tags (Thẻ):**
   - Các cặp `Key-Value` tùy chọn (ví dụ: `Department = Engineering`) dùng để gắn metadata quản lý tài nguyên trên khắp AWS.

### 1.3. Account Alias & Đăng nhập song song
- **Account Alias:** Tên định danh duy nhất toàn cầu giúp rút gọn URL đăng nhập IAM (thay thế dãy 12 chữ số Account ID).
- **Phân biệt trên góc phải màn hình Console:**
  - Nếu chỉ hiển thị Account ID / tên tài khoản gốc -> Đang đăng nhập bằng **Root User**.
  - Nếu hiển thị `username @ account-id/alias` -> Đang đăng nhập bằng **IAM User**.
- Có thể dùng cửa sổ ẩn danh (Private/Incognito Window) hoặc tính năng Multi-session để đăng nhập cả Root User và IAM User cùng lúc.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:50` | So let's go ahead and practice using the IAM service to create users in AWS. In the search bar, I just type IAM and I go into the IAM console. First, let's notice something. If you go to the top right corner and click on Global, you can see that the region selection is not active. That means that IAM as an entire service is a global service and therefore there is no region to be selected. When you create a user in IAM, it will be available everywhere, but some other consoles we'll see in this course will be region-specific. | Hãy thực hành sử dụng dịch vụ IAM để tạo người dùng trên AWS. Gõ IAM vào thanh tìm kiếm để mở IAM Console. Lưu ý ở góc trên bên phải hiển thị **Global** và không cần chọn Region — nghĩa là toàn bộ dịch vụ IAM là dịch vụ toàn cầu (Global Service). Khi tạo một user trong IAM, user đó sẽ khả dụng ở mọi nơi. |
| `00:50` - `02:03` | Why do we create users? Because right now, we are using what's called the root user. It's not best practice to use the root account. Therefore, we want to create users such as admin users that will allow us to use our accounts more safely. Let's create a user, and I will provide a username, `Stephane`. I want to provide myself access to the Management Console. We have the option to use Identity Center or to create an IAM user. I will choose the second option because from an exam perspective, this is the one you need to know about. Now we set a custom password and untick requiring password change at next login. | Tại sao ta tạo user? Vì hiện tại ta đang dùng Root user, và dùng Root cho công việc hàng ngày không phải là best practice. Hãy tạo một user tên là `Stephane`, tích chọn cấp quyền truy cập Management Console, chọn "I want to create an IAM user", đặt mật khẩu tùy chỉnh và bỏ tích yêu cầu đổi mật khẩu ở lần đăng nhập tới. |
| `02:03` - `03:40` | Next, we have to add permissions to this user. Let's create a group named `admin` and attach the policy `AdministratorAccess`. Now we add the user into the `admin` group. We also have tags (optional metadata, e.g. `Department = Engineering`). Now the user is created successfully. If we look at the `admin` group, it has `Stephane` in it and `AdministratorAccess` attached. If we look at the user `Stephane`, it has `AdministratorAccess` inherited via the group `admin`. This is why we put users in groups — it is simpler to manage permissions this way. | Tiếp theo, thêm quyền cho user bằng cách tạo group `admin` có gắn policy `AdministratorAccess`, rồi thêm `Stephane` vào group này. Ta cũng có thể gắn Tags (metadata tùy chọn, ví dụ `Department = Engineering`). Sau khi tạo xong, kiểm tra user `Stephane` sẽ thấy quyền `AdministratorAccess` được kế thừa (inherited) thông qua group `admin`. |
| `03:40` - `06:23` | Now we want to sign in with our user `Stephane`. On the IAM dashboard, we see our Account ID and Sign-in URL. You can customize this Sign-in URL by creating an **Account Alias** (must be globally unique, e.g., `aws-stephane-v5`). To use two accounts at the same time (Root on the left, IAM user on the right), we can open a Private Window, paste the Sign-in URL, enter the Account ID/Alias, username `Stephane`, and password. Now on the top right corner of the private window, it shows the IAM user and Account ID, whereas the left window shows the Root account. Please make sure not to lose your root and admin logins! | Để đăng nhập vào user `Stephane`, trên IAM Dashboard có Sign-in URL. Bạn có thể tùy chỉnh URL này bằng cách tạo một **Account Alias** (tên định danh duy nhất toàn cầu). Để mở song song tài khoản Root và IAM user, ta mở cửa sổ ẩn danh (Private Window), dán Sign-in URL và đăng nhập bằng IAM user `Stephane`. Hãy bảo quản cẩn thận thông tin đăng nhập của cả Root và Admin user. |
