# Bài 29: IAM Best Practices

- **Phần:** Phần 4: IAM & AWS CLI
- **Lecture ID:** `26098082` (`CCP_-_IAM_-_Best_Practices_v3.mp4`)
- **Thời lượng:** `01:29`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 8 Nguyên tắc thực hành tốt nhất (Best Practices) trong IAM
1. **Không sử dụng Root Account** cho công việc hàng ngày — chỉ dùng khi mới khởi tạo tài khoản AWS lần đầu.
2. **Một người thật = Một IAM User** (*One physical user = One AWS user*). Không dùng chung tài khoản; nếu có người mới, hãy tạo IAM User riêng cho họ.
3. **Gán Users vào Groups và phân quyền ở cấp độ Group** (*Assign users to groups and assign permissions to groups*).
4. **Thiết lập chính sách mật khẩu mạnh** (*Create a strong password policy*).
5. **Sử dụng và bắt buộc bật xác thực đa yếu tố (MFA)** (*Use and enforce Multi-Factor Authentication*).
6. **Tạo và sử dụng IAM Roles** khi cấp quyền cho các dịch vụ AWS (như EC2 Instances, Lambda...).
7. **Sử dụng Access Keys cho Programmatic Access (CLI / SDK)** và bảo mật chúng tuyệt đối như mật khẩu.
8. **Kiểm toán quyền hạn định kỳ** của tài khoản bằng **IAM Credentials Report** và **IAM Access Advisor**.
9. **TUYỆT ĐỐI KHÔNG BAO GIỜ chia sẻ IAM Users và Access Keys.**

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:47` | Here are the general guidelines and best practices for IAM: 1) Do not use the root account except for initial account setup. 2) One physical user equals one AWS user — do not share credentials, create another user instead. 3) Assign users to groups and assign permissions to groups. 4) Create a strong password policy and enforce Multi-Factor Authentication (MFA). | Dưới đây là các nguyên tắc thực hành tốt nhất (Best Practices) cho IAM: 1) Không dùng Root account ngoại trừ lúc thiết lập tài khoản ban đầu. 2) Một người thật tương ứng với một AWS user — không chia sẻ thông tin đăng nhập mà hãy tạo user riêng. 3) Đưa users vào groups và gán quyền ở cấp group. 4) Tạo chính sách mật khẩu mạnh và bật MFA. |
| `00:47` - `01:29` | 5) Create and use Roles whenever giving permissions to AWS services (like EC2 instances). 6) For programmatic access (CLI or SDK), generate Access Keys and keep them secret. 7) Audit permissions using IAM Credentials Report and IAM Access Advisor. 8) Never, ever share your IAM users and Access Keys! | 5) Tạo và dùng IAM Roles khi cấp quyền cho dịch vụ AWS (như EC2 instances). 6) Dùng Access Keys khi truy cập qua CLI hoặc SDK và giữ bí mật tuyệt đối. 7) Kiểm toán quyền bằng IAM Credentials Report và IAM Access Advisor. 8) Không bao giờ chia sẻ IAM users và Access Keys! |
