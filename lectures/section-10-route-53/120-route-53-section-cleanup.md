# Bài 120: Route 53 - Section Cleanup (Dọn dẹp tài nguyên cuối chương Route 53)

- **Section:** Phần 10 - Route 53
- **Lecture ID:** `13528214`
- **Video:** `SAA_-_Route_53_-_Cleanup_v2.mp4`
- **Thời lượng:** `01:21`
- **Cheat sheet:** [topics/aws_route53.html](../../topics/aws_route53.html)

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Các bước dọn dẹp tài nguyên để tránh phát sinh chi phí
1. **Tên miền đã đăng ký (Registered Domain):**
   - Sẽ tồn tại trong tài khoản của bạn với chi phí khoảng **\$12/năm** (tắt Auto-renew nếu không muốn gia hạn vào năm sau).
2. **Hosted Zone trong Route 53:**
   - Mỗi Hosted Zone tốn phí **\$0.50/tháng**.
   - Nếu không sử dụng nữa, bạn có thể xóa toàn bộ các bản ghi DNS đã tạo bên trong (trừ `NS` và `SOA`) rồi xóa Hosted Zone. (Nếu vẫn giữ Hosted Zone thì việc để lại các bản ghi thường bên trong không làm tăng phí duy trì).
3. **Route 53 Health Checks:**
   - Xóa các Health Checks đã tạo trong chương học.
4. **Hạ tầng EC2 & Load Balancer ở cả 3 Regions:**
   - **Frankfurt (`eu-central-1`):** Xóa **Application Load Balancer (`DemoRoute53ALB`)**, xóa **Target Group (`demo-tg-route-53`)**, và **Terminate EC2 instance**.
   - **N. Virginia (`us-east-1`):** **Terminate EC2 instance**.
   - **Singapore (`ap-southeast-1`):** **Terminate EC2 instance**.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
|---|---|---|
| `00:00:00` | Okay, so let's clean up what we've done in Route 53 if you wanted to avoid some costs. | Được rồi, hãy dọn dẹp những tài nguyên chúng ta đã tạo trong phần Route 53 để tránh phát sinh chi phí không cần thiết. |
| `00:00:04` | So the domain name you've bought, of course stays in your account, and it will cost you $12 a year if you wanted to renew it or more if you've bought a more pricey domain name. | Tên miền bạn đã mua tất nhiên vẫn nằm trong tài khoản của bạn, và sẽ tốn khoảng \$12 một năm nếu bạn để tự động gia hạn (hoặc cao hơn tùy đuôi tên miền). |
| `00:00:15` | And the domain name itself, so the hosted zone, if you're not using it, you can delete this hosted zone by first emptying all the records. Otherwise it will cost you 50 cents per month to keep this hosted zone alive, okay. | Về phần **Hosted Zone**, nếu bạn không có nhu cầu sử dụng nữa, bạn có thể xóa Hosted Zone này đi bằng cách xóa hết các bản ghi tự tạo bên trong trước; nếu giữ lại sẽ tốn phí **\$0.50 mỗi tháng**. |
| `00:00:27` | Within it, it doesn't matter if you have many records, you can just leave them as is. This is fine. | Nếu bạn vẫn giữ Hosted Zone để dùng tiếp thì việc giữ nguyên các bản ghi bên trong cũng không sao. |
| `00:00:32` | The other thing we have to delete is all our EC2 instances in our different regions, as well as our ALB. | Điều quan trọng tiếp theo chúng ta cần xóa là toàn bộ các **EC2 instances** ở các Region khác nhau, cũng như chiếc **ALB** (và đừng quên xóa các **Route 53 Health Checks**). |
| `00:00:38` | So we had EC2 instances in three different regions. So what I'm going to do is just delete them one by one. | Chúng ta có EC2 instances ở 3 Region khác nhau, nên tôi sẽ lần lượt xóa từng cái một. |
| `00:00:43` | So there was one for me in Frankfurt, and I believe that the load balancer I had created is also here. So let me delete this load balancer as well. And we can also delete the associated target group with that load balancer, okay. This is good. | Đầu tiên tại **Frankfurt (`eu-central-1`)**, tôi Terminate EC2 instance, xóa chiếc **Application Load Balancer**, và xóa luôn **Target Group** đi kèm với Load Balancer đó. |
| `00:00:57` | And we have to perform the same kind of cleanup in other regions. So for me it was us-east-1 where I'm going to go ahead and terminate another EC2 instance, and finally do the exact same thing in ap-southeast-1. | Tiếp theo tôi chuyển sang các Region còn lại để dọn dẹp: vào **`us-east-1`** để Terminate EC2 instance tại đó, và cuối cùng vào **`ap-southeast-1`** để Terminate EC2 instance cuối cùng. |
| `00:01:12` | Okay. After this, you should not incur any costs out of these lectures. Okay, so I really hope you liked this section and I will see you in the next lecture. | Sau khi hoàn tất các bước này, bạn sẽ không bị phát sinh thêm chi phí từ các bài thực hành trên. Hy vọng bạn yêu thích chương học này và hẹn gặp lại ở chương tiếp theo! |
