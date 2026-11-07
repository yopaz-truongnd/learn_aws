# Quiz 3: EC2 - Solutions Architect Associate Level Quiz

- **Phần (Section):** Section 6: EC2 - Solutions Architect Associate Level
- **Quiz ID:** `5334512`
- **Số lượng câu hỏi:** `5 câu`

---

## Câu hỏi 1
**You have launched an EC2 instance that will host a NodeJS application. After installing all the required software and configured your application, you noted down the EC2 instance public IPv4 so you can access it. Then, you stopped and then started your EC2 instance to complete the application configuration. After restart, you can't access the EC2 instance, and you found that the EC2 instance public IPv4 has been changed. What should you do to assign a fixed public IPv4 to your EC2 instance?**

*(Bạn đã khởi chạy một EC2 instance để lưu trữ ứng dụng NodeJS. Sau khi cài đặt mọi phần mềm cần thiết và cấu hình ứng dụng, bạn đã ghi lại địa chỉ Public IPv4 của EC2 để truy cập. Sau đó, bạn đã Stop rồi Start lại EC2 instance để hoàn tất cấu hình. Sau khi bật lại, bạn không thể truy cập vào EC2 instance nữa và phát hiện địa chỉ Public IPv4 của máy đã bị thay đổi. Bạn nên làm gì để gán một địa chỉ Public IPv4 cố định cho EC2 instance của mình?)*

- [x] **A. Allocate an Elastic IP and assign it to your EC2 instance** *(Cấp phát một địa chỉ Elastic IP và gán nó cho EC2 instance của bạn)*
- [ ] B. From inside your EC2 instance OS, change network configuration from DHCP to static and assign it a public IPv4
- [ ] C. Contact AWS Support and request a fixed public IPv4 to your EC2 instance
- [ ] D. This can't be done, you can only assign a fixed private IPv4 to your EC2 instance

> **Giải thích:**
> - **Elastic IP (EIP)** là một địa chỉ Public IPv4 tĩnh thuộc quyền sở hữu của tài khoản AWS của bạn chừng nào bạn chưa giải phóng (release) nó, và bạn có thể gắn nó vào một EC2 instance tại một thời điểm để giữ nguyên địa chỉ Public IPv4 qua các lần Stop/Start.

---

## Câu hỏi 2
**You have an application performing big data analysis hosted on a fleet of EC2 instances. You want to ensure your EC2 instances have the highest networking performance while communicating with each other. Which EC2 Placement Group should you choose?**

*(Bạn có một ứng dụng phân tích dữ liệu lớn (Big Data analysis) chạy trên một dàn máy chủ EC2. Bạn muốn đảm bảo các EC2 instances đạt hiệu năng mạng cao nhất khi giao tiếp với nhau. Bạn nên chọn loại EC2 Placement Group nào?)*

- [ ] A. Spread Placement Group
- [x] **B. Cluster Placement Group**
- [ ] C. Partition Placement Group

> **Giải thích:**
> - **Cluster Placement Group** đặt các EC2 instances sát cạnh nhau trong cùng một Availability Zone (Single AZ), mang lại khả năng tính toán hiệu năng cao (HPC) và mạng độ trễ cực thấp (low latency), băng thông lên tới 10 Gbps.
> - Spread và Partition Placement Group phân tán các EC2 instances ra các phần cứng vật lý khác nhau nên làm tăng độ trễ mạng giữa các máy.

---

## Câu hỏi 3
**You have a critical application hosted on a fleet of EC2 instances in which you want to achieve maximum availability when there's an AZ failure. Which EC2 Placement Group should you choose?**

*(Bạn có một ứng dụng trọng yếu (critical application) chạy trên một nhóm nhỏ các EC2 instances mà bạn muốn đạt độ sẵn sàng tối đa (maximum availability) khi có sự cố phần cứng hoặc lỗi AZ. Bạn nên chọn loại EC2 Placement Group nào?)*

- [ ] A. Cluster Placement Group
- [ ] B. Partition Placement Group
- [x] **C. Spread Placement Group**

> **Giải thích:**
> - **Spread Placement Group** đặt mỗi EC2 instance trên một phần cứng vật lý (rack) hoàn toàn riêng biệt trải rộng qua nhiều AZ (giới hạn tối đa 7 instances / AZ / group), giúp giảm thiểu tối đa rủi ro lỗi đồng thời cho các ứng dụng trọng yếu (critical applications).

---

## Câu hỏi 4
**Elastic Network Interface (ENI) can be attached to EC2 instances in another AZ.**

*(Elastic Network Interface - ENI có thể được gắn vào các EC2 instances nằm ở một Availability Zone khác.)*

- [ ] A. True *(Đúng)*
- [x] **B. False *(Sai)***

> **Giải thích:**
> - Các **Elastic Network Interfaces (ENIs)** bị ràng buộc chặt vào một Availability Zone (AZ) cụ thể. Bạn **không thể** gắn một ENI vào một EC2 instance nằm ở một AZ khác.

---

## Câu hỏi 5
**The following are true regarding EC2 Hibernate, EXCEPT:**

*(Các phát biểu sau đây về EC2 Hibernate đều đúng, NGOẠI TRỪ:)*

- [x] **A. EC2 Instance Root Volume must be an Instance Store volume** *(Ổ đĩa gốc Root Volume của EC2 bắt buộc phải là ổ Instance Store)*
- [ ] B. Supports On-Demand and Reserved Instances
- [ ] C. EC2 Instance RAM must be less than 150GB
- [ ] D. EC2 Instance Root Volume type must be an EBS volume

> **Giải thích:**
> - Để bật **EC2 Hibernate**, ổ đĩa gốc (**Root Volume**) của EC2 instance **bắt buộc phải là một ổ đĩa EBS (EBS volume)** (KHÔNG hỗ trợ Instance Store volume), phải có đủ dung lượng trống để chứa bản dump của RAM và **bắt buộc phải được mã hóa (encrypted)** nhằm bảo vệ dữ liệu nhạy cảm.
