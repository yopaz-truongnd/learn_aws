# Bài 53: ENI - Extra Reading

- **Phần (Section):** Section 6: EC2 - Solutions Architect Associate Level
- **Lecture ID:** `20680996`
- **Loại bài học:** Bài đọc bổ sung (Article)
- **Thời lượng ước tính:** `00:21`
- **Cheat sheet:** [topics/aws_ec2.html](../../topics/aws_ec2.html)

---

## 1. Nội dung bài đọc (Article Content)

### Làm rõ thêm về Elastic Network Interfaces (Clarification on ENI)

> Có thể đối với một số bạn, khái niệm về **ENI (Elastic Network Interface)** hiện tại vẫn chưa hoàn toàn rõ ràng.

Điều đó hoàn toàn bình thường — ENI là một khái niệm nâng cao trong AWS và cần thời gian thực hành để nắm vững.

Nếu bạn muốn tìm hiểu sâu hơn về ENI, nhiều học viên thấy bài blog chính thức sau đây của AWS rất hữu ích:
- **AWS Blog:** [New – Elastic Network Interfaces in the Virtual Private Cloud](https://aws.amazon.com/blogs/aws/new-elastic-network-interfaces-in-the-virtual-private-cloud/)

### Minh họa cấu trúc ENI trên EC2 (từ AWS Blog)
- Mỗi EC2 instance trong VPC có một **Primary ENI (`eth0`)** gắn liền với một Subnet và không thể tháo rời khỏi instance.
- Bạn có thể tạo và gắn thêm một hoặc nhiều **Secondary ENIs (`eth1`, `eth2`,...)** nằm trong cùng Availability Zone (có thể thuộc cùng Subnet hoặc khác Subnet trong cùng AZ đó) để:
  1. Xây dựng mạng quản trị tách biệt (Management & Back-end network separation).
  2. Chạy các thiết bị mạng & bảo mật ảo (Network & Security Appliances như Firewall, Load Balancer, NAT).
  3. Tạo giải pháp chuyển đổi dự phòng chi phí thấp (Low-budget High Availability / Failover) bằng cách tháo Secondary ENI từ máy chính và gắn sang máy dự phòng.

> [!TIP]
> Nếu bạn vẫn chưa hiểu hết mọi khía cạnh của ENI ngay lúc này thì cũng đừng lo lắng — **đây không phải là rào cản cho các phần tiếp theo của khóa học**. Hãy cứ tiếp tục học tiếp và quay lại ôn tập khái niệm này khi học tới phần chuyên sâu về VPC ở cuối khóa.
