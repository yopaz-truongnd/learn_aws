# Quiz 2: EC2 Fundamentals Quiz

- **Phần:** Phần 5: EC2 Fundamentals
- **Quiz ID:** `5334510`
- **Số lượng câu hỏi:** 12 câu hỏi trắc nghiệm

---

## Câu hỏi 1
**Which EC2 Purchasing Option can provide you the biggest discount, but it is not suitable for critical jobs or databases?**
*(Tùy chọn mua EC2 nào mang lại mức giảm giá lớn nhất, nhưng không phù hợp cho các tác vụ quan trọng hoặc cơ sở dữ liệu?)*

- [ ] A. Convertible Reserved Instances
- [ ] B. Dedicated Hosts
- [x] **C. Spot Instances**

> **Giải thích:** **Spot Instances** phù hợp cho các tác vụ ngắn hạn và là tùy chọn mua EC2 rẻ nhất (giảm tới 90%), nhưng kém tin cậy hơn vì bạn có thể bị thu hồi máy bất cứ lúc nào khi giá Spot vượt mức giá tối đa.

---

## Câu hỏi 2
**What should you use to control traffic in and out of EC2 instances?**
*(Bạn nên sử dụng công cụ nào để kiểm soát lưu lượng đi vào và đi ra khỏi các EC2 instances?)*

- [ ] A. Network Access Control List (NACL)
- [x] **B. Security Groups**
- [ ] C. IAM Policies

> **Giải thích:** **Security Groups** hoạt động ở cấp độ EC2 instance để kiểm soát lưu lượng mạng ra/vào máy ảo (trong khi NACL hoạt động ở cấp độ Subnet, còn IAM Policies quản lý quyền gọi API dịch vụ AWS).

---

## Câu hỏi 3
**How long can you reserve an EC2 Reserved Instance?**
*(Bạn có thể đặt trước một EC2 Reserved Instance trong thời hạn bao lâu?)*

- [x] **A. 1 or 3 years**
- [ ] B. 2 or 4 years
- [ ] C. 6 months or 1 year
- [ ] D. Anytime between 1 and 3 years

> **Giải thích:** EC2 Reserved Instances chỉ có thể đặt trước với kỳ hạn cố định là **1 năm hoặc 3 năm**.

---

## Câu hỏi 4
**You would like to deploy a High-Performance Computing (HPC) application on EC2 instances. Which EC2 instance type should you choose?**
*(Bạn muốn triển khai một ứng dụng Tính toán Hiệu năng Cao (HPC) trên các EC2 instances. Bạn nên chọn loại EC2 instance nào?)*

- [ ] A. Storage Optimized
- [x] **B. Compute Optimized**
- [ ] C. Memory Optimized
- [ ] D. General Purpose

> **Giải thích:** Các máy **Compute Optimized** (dòng `C`) được thiết kế tối ưu cho các tác vụ tính toán chuyên sâu đòi hỏi bộ vi xử lý hiệu năng cao như Batch processing, Media transcoding, High-Performance Computing (HPC), Scientific modeling & Machine Learning, và Dedicated gaming servers.

---

## Câu hỏi 5
**Which EC2 Purchasing Option should you use for an application you plan to run on a server continuously for 1 year?**
*(Bạn nên sử dụng tùy chọn mua EC2 nào cho một ứng dụng dự kiến chạy liên tục trên một máy chủ trong 1 năm?)*

- [x] **A. Reserved Instances**
- [ ] B. Spot Instances
- [ ] C. On-Demand Instances

> **Giải thích:** **Reserved Instances** rất phù hợp cho các tác vụ chạy ổn định, dài hạn (cam kết 1 hoặc 3 năm) để tiết kiệm chi phí lớn so với On-Demand.

---

## Câu hỏi 6
**You are preparing to launch an application that will be hosted on a set of EC2 instances. This application needs some software installation and some OS packages need to be updated during the first launch. What is the best way to achieve this when you launch the EC2 instances?**
*(Bạn đang chuẩn bị khởi chạy một ứng dụng trên một nhóm các EC2 instances. Ứng dụng này cần cài đặt một số phần mềm và cập nhật các gói hệ điều hành trong lần khởi chạy đầu tiên. Cách tốt nhất để thực hiện việc này khi khởi chạy các EC2 instances là gì?)*

- [ ] A. Connect to each EC2 instance using SSH, then install the required software and update your OS packages manually
- [ ] B. Write a bash script that installs the required software and updates to your OS, then contact AWS Support and provide them with the script. They will run it on your EC2 instances at launch
- [x] **C. Write a bash script that installs the required software and updates to your OS, then use this script in EC2 User Data when you launch your EC2 instances**

> **Giải thích:** **EC2 User Data** được dùng để bootstrap (khởi tạo tự động) các EC2 instances bằng một bash script chạy tự động trong lần khởi động đầu tiên.

---

## Câu hỏi 7
**Which EC2 Instance Type should you choose for a critical application that uses an in-memory database?**
*(Bạn nên chọn loại EC2 Instance nào cho một ứng dụng quan trọng sử dụng cơ sở dữ liệu trong bộ nhớ (in-memory database)?)*

- [ ] A. Compute Optimized
- [ ] B. Storage Optimized
- [x] **C. Memory Optimized**
- [ ] D. General Purpose

> **Giải thích:** Các máy **Memory Optimized** (dòng `R`, `X1`, `z1d`) được tối ưu hóa cho các tác vụ xử lý tập dữ liệu lớn trực tiếp trong bộ nhớ RAM như In-memory databases.

---

## Câu hỏi 8
**You have an e-commerce application with an OLTP database hosted on-premises. This application has popularity which results in its database has thousands of requests per second. You want to migrate the database to an EC2 instance. Which EC2 Instance Type should you choose to handle this high-frequency OLTP database?**
*(Bạn có một ứng dụng thương mại điện tử với cơ sở dữ liệu OLTP đang đặt tại chỗ (on-premises) có hàng nghìn yêu cầu mỗi giây. Bạn muốn di chuyển cơ sở dữ liệu này lên một EC2 instance. Bạn nên chọn loại EC2 Instance nào để xử lý cơ sở dữ liệu OLTP tần suất cao này?)*

- [ ] A. Compute Optimized
- [x] **B. Storage Optimized**
- [ ] C. Memory Optimized
- [ ] D. General Purpose

> **Giải thích:** Các máy **Storage Optimized** (dòng `I`, `D`, `H1`) rất lý tưởng cho các tác vụ đòi hỏi truy xuất đọc/ghi tuần tự tốc độ cao trên tập dữ liệu lớn tại ổ đĩa cục bộ, điển hình là các hệ thống **High-frequency OLTP (Online Transaction Processing)**.

---

## Câu hỏi 9
**Security Groups can be attached to only one EC2 instance.**
*(Security Groups chỉ có thể được gắn vào một EC2 instance duy nhất. Đúng hay Sai?)*

- [x] **A. False**
- [ ] B. True

> **Giải thích:** **Sai (False)**. Một Security Group có thể được gắn vào nhiều EC2 instances khác nhau trong cùng một AWS Region/VPC (và một EC2 instance cũng có thể gắn nhiều Security Groups).

---

## Câu hỏi 10
**You're planning to migrate on-premises applications to AWS. Your company has strict compliance requirements that require your applications to run on dedicated servers. You also need to use your own server-bound software license to reduce costs. Which EC2 Purchasing Option is suitable for you?**
*(Bạn đang lên kế hoạch đưa các ứng dụng on-premises lên AWS. Công ty của bạn có yêu cầu tuân thủ nghiêm ngặt bắt buộc ứng dụng phải chạy trên các máy chủ vật lý riêng biệt, đồng thời bạn cần sử dụng giấy phép phần mềm gắn theo máy chủ (server-bound software license) sẵn có để giảm chi phí. Tùy chọn mua EC2 nào phù hợp với bạn?)*

- [ ] A. Convertible Reserved Instances
- [x] **B. Dedicated Hosts**
- [ ] C. Spot Instances

> **Giải thích:** **Dedicated Hosts** phù hợp cho các doanh nghiệp có yêu cầu tuân thủ (compliance) nghiêm ngặt hoặc có mô hình bản quyền phần mềm gắn chặt với máy chủ vật lý (BYOL).

---

## Câu hỏi 11
**You would like to deploy a database technology on an EC2 instance and the vendor license bills you based on the physical cores and underlying network socket visibility. Which EC2 Purchasing Option allows you to get visibility into them?**
*(Bạn muốn triển khai một công nghệ cơ sở dữ liệu trên EC2 instance mà nhà cung cấp bản quyền tính phí dựa trên số nhân vật lý (physical cores) và khả năng quan sát socket mạng bên dưới. Tùy chọn mua EC2 nào cho phép bạn nhìn thấy các thông số này?)*

- [ ] A. Spot Instances
- [ ] B. On-Demand
- [x] **C. Dedicated Hosts**
- [ ] D. Reserved Instances

> **Giải thích:** Chỉ có **Dedicated Hosts** mới cung cấp quyền kiểm soát và khả năng nhìn thấy trực tiếp số lượng **physical cores** và **sockets** của máy chủ vật lý bên dưới.

---

## Câu hỏi 12
**Spot Fleet is a set of Spot Instances and optionally ...............**
*(Spot Fleet là một tập hợp các Spot Instances và tùy chọn bao gồm thêm ...............)*

- [ ] A. Reserved Instances
- [x] **B. On-Demand Instances**
- [ ] C. Dedicated Hosts
- [ ] D. Dedicated Instances

> **Giải thích:** **Spot Fleet** là một tập hợp các **Spot Instances** và tùy chọn kết hợp thêm **On-Demand Instances** để đáp ứng dung lượng mục tiêu với chi phí tối ưu nhất.
