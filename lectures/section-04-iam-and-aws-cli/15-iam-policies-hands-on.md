# Bài 15: IAM Policies Hands On

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098018` (`CCP_-_IAM_-_Policies_Hands_On_v4.mp4`)
- **Thời lượng:** `08:01`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Kiểm chứng quyền hạn thực tế trên IAM
- Khi xóa User `stephane` khỏi group `admin`: User lập tức mất quyền và nhận lỗi `AccessDenied` (không có quyền `iam:ListUsers`).
- Khi gắn trực tiếp policy **`IAMReadOnlyAccess`** cho User `stephane`:
  - User có thể **xem (Read/List)** danh sách Users và Groups.
  - Khi thử **tạo Group mới (`developers`)** -> Bị từ chối (`AccessDenied`) vì chỉ có quyền Read-Only, không có quyền Write/Create.

### 1.2. Ý nghĩa ký tự đại diện `*` (Wildcard) trong JSON Policy
- Trong policy **`AdministratorAccess`**:
  ```json
  {
    "Effect": "Allow",
    "Action": "*",
    "Resource": "*"
  }
  ```
  - Dấu `*` nghĩa là **bất kỳ / tất cả (anything)**: Cho phép mọi hành động (`Action: "*"`) trên mọi tài nguyên (`Resource: "*"`).
- Trong policy **`IAMReadOnlyAccess`**:
  - Sử dụng tiền tố kết hợp dấu sao như `iam:Get*`, `iam:List*`, `iam:Generate*` trên `Resource: "*"` để gom nhóm tất cả các lệnh API bắt đầu bằng `Get` hoặc `List`.

### 1.3. Công cụ tạo Policy tùy chỉnh (Custom Policy)
- Có 2 cách tạo Policy mới trong IAM Console:
  1. **Visual Editor:** Chọn dịch vụ (ví dụ: `IAM`), chọn các Actions cụ thể (ví dụ: `ListUsers`, `GetUser`) và chọn Resource (`All resources` hoặc ARN cụ thể).
  2. **JSON Editor:** Viết hoặc chỉnh sửa trực tiếp tài liệu JSON.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:06` | Let's have a look at IAM policies in depth. Currently user `Stephane` is part of the `admin` group and has `AdministratorAccess`. If I go to the `admin` group using my root account and remove `Stephane` from that group, then on the right window `Stephane` loses permissions. Refreshing the page gives an `AccessDenied` error saying it doesn't have permission to do `iam:ListUsers`. | Hãy thực hành chi tiết về IAM Policies. Ban đầu user `Stephane` thuộc group `admin` nên có toàn quyền. Khi dùng tài khoản Root xóa `Stephane` khỏi group `admin` và làm mới trang bên cửa sổ của `Stephane`, lập tức xuất hiện lỗi `AccessDenied` báo không có quyền thực hiện `iam:ListUsers`. |
| `01:06` - `02:38` | Let's attach the policy `IAMReadOnlyAccess` directly to user `Stephane`. Refreshing the page now allows viewing users and user groups. But if we try to create a `developers` group using `Stephane`, it fails because we only have read-only access on IAM, not permission to create groups. | Bây giờ ta gắn trực tiếp policy `IAMReadOnlyAccess` cho user `Stephane`. Làm mới lại trang, `Stephane` đã xem lại được danh sách users và groups. Tuy nhiên khi thử tạo một group mới tên là `developers`, hệ thống báo lỗi từ chối vì `IAMReadOnlyAccess` chỉ cho phép đọc chứ không cho phép tạo mới. |
| `02:38` - `03:51` | Next, using Root, let's create the `developers` group, add `Stephane`, and attach a policy (e.g., `AlexaForBusinessFullAccess`), and also re-add `Stephane` to the `admin` group. Looking at `Stephane` now, there are 3 policies attached: `AdministratorAccess` (via group `admin`), `AlexaForBusiness` (via group `developers`), and `IAMReadOnlyAccess` (attached directly). | Tiếp theo, dùng tài khoản Root tạo group `developers` (gắn một policy bất kỳ như `AlexaForBusiness`) và thêm `Stephane` vào cả `developers` lẫn `admin`. Lúc này trong mục Permissions của `Stephane` hiển thị đồng thời cả 3 policies: 2 kế thừa từ 2 groups và 1 gắn trực tiếp. |
| `03:51` - `06:06` | Let's inspect policies in the Policies menu. Looking at `AdministratorAccess` under the JSON tab, we see `"Effect": "Allow", "Action": "*", "Resource": "*"`. Star (`*`) in AWS means anything — allowing any action on any resource. Looking at `IAMReadOnlyAccess` JSON, it has `"Effect": "Allow"` with actions like `"iam:Get*"`, `"iam:List*"` on `"Resource": "*"`. Using `*` groups all API calls starting with `Get` or `List`. | Khi mở menu Policies và xem tab JSON của `AdministratorAccess`, ta thấy `"Effect": "Allow", "Action": "*", "Resource": "*"`. Dấu sao (`*`) có nghĩa là tất cả mọi thứ (mọi hành động trên mọi tài nguyên). Còn trong JSON của `IAMReadOnlyAccess`, các Action dùng `"iam:Get*"`, `"iam:List*"` để gom tất cả các lệnh API bắt đầu bằng `Get` hoặc `List`. |
| `06:06` - `08:01` | You can also create your own policy using either the **Visual Editor** or **JSON Editor**. In the Visual Editor, we select service `IAM`, actions `ListUsers` and `GetUser`, and `All resources`, then name it `MyIAMPermissions`. Checking the JSON shows `iam:ListUsers` and `iam:GetUser` on `Resource: "*"`. Finally, we clean up by deleting the `developers` group and removing the direct `IAMReadOnlyAccess` policy from `Stephane`. | Bạn cũng có thể tự tạo Policy riêng bằng **Visual Editor** hoặc **JSON Editor**. Ví dụ trong Visual Editor: chọn dịch vụ `IAM`, chọn 2 quyền `ListUsers` và `GetUser` trên tất cả tài nguyên (`*`), đặt tên là `MyIAMPermissions`. Cuối cùng, dọn dẹp bằng cách xóa group `developers` và gỡ policy gắn trực tiếp để `Stephane` chỉ còn thuộc group `admin`. |
