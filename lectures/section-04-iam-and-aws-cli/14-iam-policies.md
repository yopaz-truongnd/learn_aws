# Bài 14: IAM Policies

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26623458` (`CCP - IAM - Policies v1.mp4`)
- **Thời lượng:** `02:50`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Cơ chế kế thừa IAM Policy (Policy Inheritance)
- **Gán ở cấp độ Group:** Mọi User trong Group đều tự động kế thừa Policy của Group đó (ví dụ: Alice, Bob, Charles kế thừa Policy của nhóm `Developers`).
- **User thuộc nhiều Groups:** Sẽ kế thừa và cộng gộp tất cả Policies từ các Groups mà User đó tham gia (ví dụ: Charles thuộc cả `Developers` và `Audit` nên nhận cả 2 Policies; David thuộc cả `Operations` và `Audit` nên nhận cả 2 Policies).
- **Inline Policy (Chính sách nội tuyến):** Policy được gắn trực tiếp riêng cho một User duy nhất (dù User đó có thuộc Group nào hay không, như Fred).

### 1.2. Cấu trúc JSON của một IAM Policy (Bắt buộc nhớ khi thi)

```json
{
  "Version": "2012-10-17",
  "Id": "S3-Account-Permissions",
  "Statement": [
    {
      "Sid": "1",
      "Effect": "Allow",
      "Principal": {
        "AWS": ["arn:aws:iam::123456789012:root"]
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": ["arn:aws:s3:::mybucket/*"],
      "Condition": {}
    }
  ]
}
```

#### Phân biệt phần tử cấp Policy và phần tử cấp Statement:
- **Thuộc cấp độ Policy (ngoài Statement):**
  - `Version`: Phiên bản ngôn ngữ chính sách (thường là `"2012-10-17"`). *(Lưu ý bẫy đề thi: `Version` thuộc Policy, KHÔNG phải là thành phần nằm bên trong `Statement`)*.
  - `Id`: Định danh cho Policy *(tùy chọn - optional)*.
  - `Statement`: Một hoặc nhiều câu lệnh quy định quyền.
- **6 thành phần bên trong một `Statement`:**
  1. **`Sid` (Statement ID):** Mã định danh cho câu lệnh *(tùy chọn - optional)*.
  2. **`Effect`:** Cho phép (`Allow`) hoặc Từ chối (`Deny`) quyền truy cập API.
  3. **`Principal`:** Tài khoản (Account), người dùng (User) hoặc vai trò (Role) mà chính sách này áp dụng.
  4. **`Action`:** Danh sách các lệnh gọi API (API calls) được phép hoặc bị từ chối dựa trên `Effect`.
  5. **`Resource`:** Danh sách các tài nguyên AWS (ví dụ S3 bucket) mà `Action` tác động lên.
  6. **`Condition`:** Điều kiện để `Statement` có hiệu lực *(tùy chọn - optional)*.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `01:07` | Okay, so now let's discuss IAM policies in depth. Imagine we have a group of developers (Alice, Bob, Charles) and we attach a policy at the group level. Every single member of the group will inherit this policy. If you have a second group (`Operations`) with a different policy, David and Edward will have that policy. If Fred does not belong to a group, we can create an **inline policy** attached only to that user. And if Charles and David both belong to the `Audit` team with its own policy, Charles inherits policies from both `Developers` and `Audit`, while David inherits policies from both `Audit` and `Operations`. | Hãy thảo luận sâu về IAM Policies. Khi gắn một policy ở cấp độ nhóm `Developers` (Alice, Bob, Charles), mọi thành viên trong nhóm sẽ kế thừa policy đó. Nhóm `Operations` (David, Edward) sẽ có policy riêng. Với user không thuộc nhóm nào như Fred (hoặc bất kỳ user nào), ta có thể tạo **Inline Policy** gắn trực tiếp cho riêng user đó. Nếu Charles và David cùng tham gia thêm nhóm `Audit`, họ sẽ kế thừa đồng thời các policies từ tất cả các nhóm mà họ thuộc về. |
| `01:07` - `01:45` | Now, in terms of the policy structure, this is a JSON document. An IAM policy structure consists of: a **Version** number (usually `2012-10-17`, the policy language version); an **Id** to identify that policy (optional); and one or more **Statements**. Inside a Statement: **Sid** is the Statement ID (optional). | Về cấu trúc của một IAM Policy (tài liệu JSON), ở cấp độ Policy gồm có: **Version** (phiên bản ngôn ngữ policy, thường là `2012-10-17`), **Id** (định danh của policy - tùy chọn), và một hoặc nhiều **Statements**. Bên trong mỗi Statement có **Sid** (Statement ID - tùy chọn). |
| `01:45` - `02:50` | **Effect** is whether the statement allows or denies access (`Allow` or `Deny`). **Principal** consists of which account, user, or role this policy is applied to. **Action** is the list of API calls that will be allowed or denied based on the effect. **Resource** is the list of resources to which the actions apply. And finally, **Condition** (optional) specifies when this statement should be applied. Going into the exam, make sure you really understand Effect, Principal, Action, and Resource. | **Effect** xác định cho phép (`Allow`) hay từ chối (`Deny`). **Principal** chỉ định tài khoản, user hoặc role được áp dụng policy. **Action** là danh sách các lệnh gọi API được phép hoặc bị từ chối. **Resource** là danh sách tài nguyên mà các hành động áp dụng lên. Cuối cùng là **Condition** (tùy chọn) quy định điều kiện áp dụng. Khi đi thi, bạn cần nắm thật chắc `Effect`, `Principal`, `Action` và `Resource`. |
