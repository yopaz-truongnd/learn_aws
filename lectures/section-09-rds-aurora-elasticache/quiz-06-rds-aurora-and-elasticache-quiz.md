# Quiz 6: RDS, Aurora, and ElastiCache Quiz (Bộ 24 câu hỏi trắc nghiệm Phần 9)

- **Phần (Section):** Section 9: AWS Fundamentals: RDS + Aurora + ElastiCache
- **Quiz ID:** `5336165`
- **Số lượng câu hỏi:** 24 câu hỏi trắc nghiệm

---

### Câu 1 (`id: 37559173`)
**Câu hỏi (English):** Amazon RDS supports the following databases, **EXCEPT**:
**Dịch nghĩa (Tiếng Việt):** Amazon RDS hỗ trợ các cơ sở dữ liệu sau đây, **NGOẠI TRỪ**:

- [x] **A. MongoDB**
- [ ] B. MySQL
- [ ] C. MariaDB
- [ ] D. Microsoft SQL Server

> **Giải thích:** Amazon RDS là dịch vụ cơ sở dữ liệu quan hệ (SQL), hỗ trợ MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, IBM Db2 và Amazon Aurora. **MongoDB** là cơ sở dữ liệu NoSQL nên không được hỗ trợ trên RDS (trên AWS có dịch vụ Amazon DocumentDB tương thích với MongoDB).

---

### Câu 2 (`id: 37559185`)
**Câu hỏi (English):** You're planning for a new solution that requires a MySQL database that must be available even in case of a disaster in one of the Availability Zones. What should you use?
**Dịch nghĩa (Tiếng Việt):** Bạn đang lên kế hoạch cho một giải pháp mới đòi hỏi cơ sở dữ liệu MySQL phải luôn sẵn sàng ngay cả khi xảy ra thảm họa ở một trong các Availability Zones. Bạn nên sử dụng tính năng nào?

- [ ] A. Create Read Replicas
- [ ] B. Enable Encryption
- [x] **C. Enable Multi-AZ**

> **Giải thích:** **Multi-AZ** giúp đảm bảo tính sẵn sàng cao và khôi phục sau thảm họa (Disaster Recovery) khi toàn bộ một Availability Zone gặp sự cố (nhờ sao chép đồng bộ sang Standby DB ở AZ khác và tự động failover). Read Replicas dùng để mở rộng quy mô đọc (scale reads), không phải cơ chế failover tự động cho DR cấp độ AZ.

---

### Câu 3 (`id: 37559197`)
**Câu hỏi (English):** We have an RDS database that struggles to keep up with the demand of requests from our website. Our million users mostly read news, and we don't post news very often. Which solution is **NOT** adapted to this problem?
**Dịch nghĩa (Tiếng Việt):** Chúng ta có một cơ sở dữ liệu RDS đang chật vật đáp ứng nhu cầu truy vấn từ trang web. Hàng triệu người dùng của chúng ta chủ yếu đọc tin tức, và chúng ta không đăng tin mới thường xuyên. Giải pháp nào **KHÔNG** phù hợp cho vấn đề này?

- [ ] A. An ElastiCache Cluster
- [x] **B. RDS Multi-AZ**
- [ ] C. RDS Read Replicas

> **Giải thích:** Hãy đọc kỹ câu hỏi (`NOT adapted`). Cả **ElastiCache Cluster** và **RDS Read Replicas** đều giúp mở rộng khả năng đọc (read scaling). Ngược lại, **RDS Multi-AZ** chỉ dùng cho mục đích dự phòng thảm họa (Standby instance không nhận truy vấn đọc), nên **không** giải quyết được bài toán quá tải đọc.

---

### Câu 4 (`id: 37559203`)
**Câu hỏi (English):** You have set up read replicas on your RDS database, but users are complaining that upon updating their social media posts, they do not see their updated posts right away. What is a possible cause for this?
**Dịch nghĩa (Tiếng Việt):** Bạn đã thiết lập các Read Replicas trên cơ sở dữ liệu RDS của mình, nhưng người dùng phàn nàn rằng ngay sau khi cập nhật bài đăng mạng xã hội, họ không nhìn thấy nội dung mới cập nhật ngay lập tức. Nguyên nhân có thể là gì?

- [ ] A. There must be a bug in your application
- [x] **B. Read Replicas have Asynchronous Replication, therefore it's likely your users will only read Eventual Consistency**
- [ ] C. You should have setup Multi-AZ instead

> **Giải thích:** Các **Read Replicas** sử dụng cơ chế sao chép bất đồng bộ (**Asynchronous Replication**), dẫn đến tính nhất quán cuối cùng (**Eventual Consistency**). Nếu ứng dụng đọc từ Read Replica ngay trước khi dữ liệu mới từ Master kịp sao chép sang, người dùng sẽ tạm thời thấy dữ liệu cũ.

---

### Câu 5 (`id: 37559217`)
**Câu hỏi (English):** Which RDS **(NOT Aurora)** feature when used does not require you to change the SQL connection string?
**Dịch nghĩa (Tiếng Việt):** Tính năng nào của RDS **(KHÔNG phải Aurora)** khi sử dụng sẽ không yêu cầu bạn phải thay đổi chuỗi kết nối SQL (SQL connection string)?

- [x] **A. Multi-AZ**
- [ ] B. Read Replicas

> **Giải thích:** **RDS Multi-AZ** giữ nguyên một tên DNS (connection string) duy nhất bất kể Master hay Standby đang hoạt động (AWS tự động chuyển đổi DNS ngầm khi failover). Trong khi đó, mỗi **RDS Read Replica** có một DNS endpoint riêng biệt nên bạn phải sửa ứng dụng để tham chiếu tới chúng.

---

### Câu 6 (`id: 37559227`)
**Câu hỏi (English):** Your application running on a fleet of EC2 instances managed by an Auto Scaling Group behind an Application Load Balancer. Users have to constantly log back in and you don't want to enable Sticky Sessions on your ALB as you fear it will overload some EC2 instances. What should you do?
**Dịch nghĩa (Tiếng Việt):** Ứng dụng của bạn đang chạy trên một dàn EC2 instances được quản lý bởi Auto Scaling Group phía sau một Application Load Balancer. Người dùng liên tục phải đăng nhập lại và bạn không muốn bật Sticky Sessions trên ALB vì sợ làm quá tải một số EC2 instances. Bạn nên làm gì?

- [ ] A. Use your own custom Load Balancer on EC2 instances instead of using ALB
- [ ] B. Store session data in RDS
- [x] **C. Store session data in ElastiCache**
- [ ] D. Store session data in a shared EBS volume

> **Giải thích:** Lưu trữ dữ liệu phiên làm việc (**Session Data**) trong **Amazon ElastiCache** là mẫu thiết kế chuẩn để biến tầng EC2 trở thành phi trạng thái (**Stateless**), giúp bất kỳ EC2 instance nào cũng truy xuất được trạng thái đăng nhập của người dùng với hiệu năng cực cao và độ trễ cực thấp.

---

### Câu 7 (`id: 37559235`)
**Câu hỏi (English):** An analytics application is currently performing its queries against your main production RDS database. These queries run at any time of the day and slow down the RDS database which impacts your users' experience. What should you do to improve the users' experience?
**Dịch nghĩa (Tiếng Việt):** Một ứng dụng phân tích (analytics) hiện đang chạy các truy vấn trực tiếp vào cơ sở dữ liệu RDS Production chính của bạn. Các truy vấn này chạy vào bất kỳ thời điểm nào trong ngày và làm chậm cơ sở dữ liệu RDS, gây ảnh hưởng đến trải nghiệm người dùng. Bạn nên làm gì để cải thiện trải nghiệm người dùng?

- [x] **A. Setup a Read Replica**
- [ ] B. Setup Multi-AZ
- [ ] C. Run the analytics queries at night

> **Giải thích:** Thiết lập một **Read Replica** và trỏ ứng dụng phân tích (analytics) sang truy vấn trên Read Replica đó sẽ tách biệt hoàn toàn tải đọc nặng ra khỏi cơ sở dữ liệu RDS Production chính.

---

### Câu 8 (`id: 37559249`)
**Câu hỏi (English):** You would like to ensure you have a replica of your database available in another AWS Region if a disaster happens to your main AWS Region. Which database do you recommend to implement this easily?
**Dịch nghĩa (Tiếng Việt):** Bạn muốn đảm bảo có sẵn một bản sao cơ sở dữ liệu ở một AWS Region khác phòng trường hợp xảy ra thảm họa đối với AWS Region chính. Bạn khuyến nghị sử dụng giải pháp cơ sở dữ liệu nào để triển khai việc này dễ dàng và hiệu quả nhất?

- [ ] A. RDS Read Replicas
- [ ] B. RDS Multi-AZ
- [ ] C. Aurora Read Replicas
- [x] **D. Aurora Global Database**

> **Giải thích:** **Aurora Global Database** được thiết kế chuyên biệt cho bài toán khôi phục thảm họa liên vùng (Cross-Region DR) và đọc độ trễ thấp toàn cầu, cho phép sao chép sang tối đa 10 Secondary Regions với độ trễ sao chép dưới 1 giây và RTO failover dưới 1 phút.

---

### Câu 9 (`id: 37559319`)
**Câu hỏi (English):** How can you enhance the security of your ElastiCache Redis Cluster by allowing users to access your ElastiCache Redis Cluster using their IAM Identities (e.g., Users, Roles)?
**Dịch nghĩa (Tiếng Việt):** Làm thế nào để tăng cường bảo mật cho cụm ElastiCache Redis của bạn bằng cách cho phép người dùng truy cập vào cụm ElastiCache Redis thông qua danh tính IAM của họ (ví dụ: IAM Users, Roles)?

- [ ] A. Using Redis Authentication
- [x] **B. Using IAM Authentication**
- [ ] C. Use Security Groups

> **Giải thích:** Bạn có thể bật **IAM Authentication** trên ElastiCache for Redis để cho phép xác thực kết nối vào cụm Redis bằng danh tính IAM (Users/Roles) thay vì mật khẩu tĩnh của Redis AUTH.

---

### Câu 10 (`id: 37559325`)
**Câu hỏi (English):** Your company has a production Node.js application that is using RDS MySQL 5.6 as its database. A new application programmed in Java will perform some heavy analytics workload to create a dashboard on a regular hourly basis. What is the most cost-effective solution you can implement to minimize disruption for the main application?
**Dịch nghĩa (Tiếng Việt):** Công ty của bạn có một ứng dụng Node.js trên môi trường Production đang dùng RDS MySQL làm cơ sở dữ liệu. Một ứng dụng mới viết bằng Java sẽ thực hiện khối lượng công việc phân tích nặng để tạo bảng điều khiển định kỳ hàng giờ. Giải pháp tiết kiệm chi phí nhất để giảm thiểu gián đoạn cho ứng dụng chính là gì?

- [ ] A. Enable Multi-AZ for the RDS database and run the analytics workload on the standby database
- [x] **B. Create a Read Replica in a different AZ and run the analytics workload on the replica database**
- [ ] C. Create a Read Replica in a different AZ and run the analytics workload on the source database

> **Giải thích:** Tạo một **Read Replica** và chạy tác vụ phân tích (analytics workload) trên Read Replica đó sẽ không làm ảnh hưởng đến cơ sở dữ liệu nguồn (source database). Lưu ý rằng bạn không thể đọc trực tiếp từ Standby database của Multi-AZ.

---

### Câu 11 (`id: 37559337`)
**Câu hỏi (English):** You would like to create a disaster recovery strategy for your RDS PostgreSQL database so that in case of a regional outage the database can be quickly made available for both read and write workloads in another AWS Region. The DR database must be highly available. What do you recommend?
**Dịch nghĩa (Tiếng Việt):** Bạn muốn tạo chiến lược khôi phục sau thảm họa (DR) cho cơ sở dữ liệu RDS PostgreSQL sao cho trong trường hợp mất toàn bộ một Region, cơ sở dữ liệu có thể nhanh chóng sẵn sàng cho cả tải đọc và ghi ở một AWS Region khác, đồng thời cơ sở dữ liệu DR đó cũng phải có tính sẵn sàng cao (highly available). Bạn khuyến nghị phương án nào?

- [ ] A. Create a Read Replica in the same region and enable Multi-AZ on the main database
- [x] **B. Create a Read Replica in a different region and enable Multi-AZ on the Read Replica**
- [ ] C. Create a Read Replica in the same region and enable Multi-AZ on the Read Replica
- [ ] D. Enable Multi-Region option on the main database

> **Giải thích:** Để dự phòng thảm họa cấp độ Region cho RDS PostgreSQL và đảm bảo bản thân DB dự phòng cũng có tính sẵn sàng cao (HA), bạn tạo một **Cross-Region Read Replica** (ở một Region khác) và bật tính năng **Multi-AZ trên chính Read Replica đó**. Khi Region chính gặp sự cố, bạn promote Read Replica đó lên thành Master (đã có sẵn Multi-AZ).

---

### Câu 12 (`id: 37559349`)
**Câu hỏi (English):** You have migrated the MySQL database from on-premises to RDS. You have a lot of applications and developers interacting with your database. Each developer has an IAM user in the company's AWS account. What is a suitable approach to give access to developers to the MySQL RDS DB instance instead of creating a DB user for each one?
**Dịch nghĩa (Tiếng Việt):** Bạn đã di chuyển cơ sở dữ liệu MySQL từ tại chỗ (on-premises) lên RDS. Bạn có rất nhiều ứng dụng và lập trình viên tương tác với cơ sở dữ liệu. Mỗi lập trình viên đã có một IAM user trong tài khoản AWS của công ty. Phương pháp nào phù hợp để cấp quyền truy cập cho các lập trình viên vào MySQL RDS DB instance thay vì phải tạo từng DB user/password riêng lẻ?

- [ ] A. By default IAM users have access to your RDS database
- [ ] B. Use Amazon Cognito
- [x] **C. Enable IAM Database Authentication**

> **Giải thích:** Bật **IAM Database Authentication** cho phép sử dụng IAM Users và IAM Roles để xác thực kết nối vào RDS MySQL và PostgreSQL thông qua token bảo mật ngắn hạn.

---

### Câu 13 (`id: 37559419`)
**Câu hỏi (English):** Which of the following statement is true regarding replication in both RDS Read Replicas and Multi-AZ?
**Dịch nghĩa (Tiếng Việt):** Phát biểu nào sau đây là ĐÚNG về cơ chế sao chép (replication) trong RDS Read Replicas và Multi-AZ?

- [ ] A. Read Replica uses Asynchronous Replication and Multi-AZ uses Asynchronous Replication
- [x] **B. Read Replica uses Asynchronous Replication and Multi-AZ uses Synchronous Replication**
- [ ] C. Read Replica uses Synchronous Replication and Multi-AZ uses Synchronous Replication
- [ ] D. Read Replica uses Synchronous Replication and Multi-AZ uses Asynchronous Replication

> **Giải thích:** **Read Replica** sử dụng sao chép bất đồng bộ (**Asynchronous Replication**), trong khi **Multi-AZ** sử dụng sao chép đồng bộ (**Synchronous Replication**).

---

### Câu 14 (`id: 37559435`)
**Câu hỏi (English):** How do you encrypt an unencrypted RDS DB instance?
**Dịch nghĩa (Tiếng Việt):** Làm thế nào để mã hóa một RDS DB instance hiện đang chưa được mã hóa (unencrypted)?

- [ ] A. Do it straight from AWS Console, select your RDS DB instance, choose Actions then **Encrypt using KMS**
- [ ] B. Do it straight from AWS Console, after stopping the RDS DB instance
- [x] **C. Create a snapshot of the unencrypted RDS DB instance, copy the snapshot and tick "Enable encryption", then restore the RDS DB instance from the encrypted snapshot**

> **Giải thích:** Bạn không thể bật mã hóa trực tiếp trên một RDS DB instance đang chạy hoặc đã dừng nếu lúc khởi tạo chưa bật mã hóa. Cách duy nhất là: **Chụp Snapshot** của DB chưa mã hóa $\rightarrow$ **Copy Snapshot và tích chọn "Enable encryption"** (hoặc Restore kèm bật mã hóa) $\rightarrow$ **Restore** thành một RDS DB instance mới đã được mã hóa.

---

### Câu 15 (`id: 37559563`)
**Câu hỏi (English):** For your RDS database, you can have up to ............ Read Replicas.
**Dịch nghĩa (Tiếng Việt):** Đối với cơ sở dữ liệu RDS của bạn, bạn có thể tạo tối đa ............ Read Replicas.

- [ ] A. 5
- [x] **B. 15**
- [ ] C. 7

> **Giải thích:** Cả Amazon RDS và Amazon Aurora hiện nay đều hỗ trợ tối đa **15 Read Replicas**.

---

### Câu 16 (`id: 37559575`)
**Câu hỏi (English):** You have an un-encrypted RDS DB instance and you want to create Read Replicas. Can you configure the RDS Read Replicas to be encrypted?
**Dịch nghĩa (Tiếng Việt):** Bạn có một RDS DB instance chưa được mã hóa và bạn muốn tạo các Read Replicas. Bạn có thể cấu hình cho các RDS Read Replicas đó được mã hóa hay không?

- [x] **A. No**
- [ ] B. Yes

> **Giải thích:** **Không (No)**. Bạn không thể tạo một Read Replica được mã hóa từ một Master RDS DB instance chưa được mã hóa.

---

### Câu 17 (`id: 37559585`)
**Câu hỏi (English):** An application running in production is using an Aurora Cluster as its database. Your development team would like to run a version of the application in a scaled-down application with the ability to perform some heavy workload on a need-basis. Most of the time, the application will be unused. Your CIO has tasked you with helping the team to achieve this while minimizing costs. What do you suggest?
**Dịch nghĩa (Tiếng Việt):** Một ứng dụng chạy trên Production đang dùng cụm Aurora làm cơ sở dữ liệu. Nhóm phát triển muốn chạy một phiên bản thu nhỏ của ứng dụng với khả năng thực hiện một số tác vụ nặng khi cần thiết, nhưng phần lớn thời gian ứng dụng sẽ không được sử dụng. CIO giao nhiệm vụ cho bạn giúp nhóm đạt được mục tiêu này đồng thời tối ưu chi phí nhất. Bạn đề xuất gì?

- [ ] A. Use an Aurora Global Database
- [ ] B. Use an RDS database
- [x] **C. Use Aurora Serverless**
- [ ] D. Run Aurora on EC2, and write a script to shut down the EC2 instance at night

> **Giải thích:** **Aurora Serverless** tự động bật/tắt và co giãn năng lực tính toán theo nhu cầu thực tế (trả tiền theo giây sử dụng), cực kỳ tiết kiệm chi phí cho các môi trường Dev/Test hoặc tải công việc ngắt quãng, phần lớn thời gian không sử dụng.

---

### Câu 18 (`id: 37559591`)
**Câu hỏi (English):** How many Aurora Read Replicas can you have in a single Aurora DB Cluster?
**Dịch nghĩa (Tiếng Việt):** Bạn có thể có tối đa bao nhiêu Aurora Read Replicas trong một cụm Aurora DB Cluster đơn lẻ?

- [ ] A. 5
- [ ] B. 10
- [x] **C. 15**

> **Giải thích:** Một cụm Aurora DB Cluster hỗ trợ tối đa **15 Aurora Read Replicas**.

---

### Câu 19 (`id: 37559593`)
**Câu hỏi (English):** Amazon Aurora supports both .......................... databases.
**Dịch nghĩa (Tiếng Việt):** Amazon Aurora tương thích và hỗ trợ cả hai hệ cơ sở dữ liệu ..........................

- [ ] A. MySQL and MariaDB
- [x] **B. MySQL and PostgreSQL**
- [ ] C. Oracle and MariaDB
- [ ] D. Oracle and MS SQL Server

> **Giải thích:** Amazon Aurora tương thích với **MySQL và PostgreSQL**.

---

### Câu 20 (`id: 37559671`)
**Câu hỏi (English):** You work as a Solutions Architect for a gaming company. One of the games mandates that players are ranked in real-time based on their score. Your boss asked you to design then implement an effective and highly available solution to create a gaming leaderboard. What should you use?
**Dịch nghĩa (Tiếng Việt):** Bạn làm Solutions Architect cho một công ty game. Một trong các trò chơi yêu cầu xếp hạng người chơi theo thời gian thực dựa trên điểm số của họ. Sếp yêu cầu bạn thiết kế và triển khai một giải pháp hiệu quả, có tính sẵn sàng cao để tạo bảng xếp hạng trò chơi (gaming leaderboard). Bạn nên sử dụng gì?

- [ ] A. Use RDS for MySQL
- [ ] B. Use an Amazon Aurora
- [ ] C. Use ElastiCache for Memcached
- [x] **D. Use ElastiCache for Redis - Sorted Sets**

> **Giải thích:** **ElastiCache for Redis — Sorted Sets** đảm bảo cả tính duy nhất lẫn thứ tự sắp xếp điểm số theo thời gian thực với độ sẵn sàng cao (Multi-AZ), là giải pháp chuẩn mực cho bài toán **Real-time Gaming Leaderboard**.

---

### Câu 21 (`id: 51042560`)
**Câu hỏi (English):** You need full customization of an Oracle Database on AWS. You would like to benefit from using the AWS services. What do you recommend?
**Dịch nghĩa (Tiếng Việt):** Bạn cần toàn quyền tùy chỉnh (full customization) một cơ sở dữ liệu Oracle trên AWS nhưng vẫn muốn hưởng lợi từ các tính năng dịch vụ được quản lý của AWS. Bạn khuyến nghị gì?

- [ ] A. RDS for Oracle
- [x] **B. RDS Custom for Oracle**
- [ ] C. Deploy Oracle on EC2

> **Giải thích:** **RDS Custom for Oracle** (và Microsoft SQL Server) vừa mang lại lợi ích tự động hóa của dịch vụ RDS được quản lý, vừa cấp toàn quyền quản trị viên (SSH / SSM Session Manager) vào hệ điều hành và cơ sở dữ liệu bên dưới để tùy chỉnh sâu.

---

### Câu 22 (`id: 51042570`)
**Câu hỏi (English):** You need to store long-term backups for your Aurora database for disaster recovery and audit purposes. What do you recommend?
**Dịch nghĩa (Tiếng Việt):** Bạn cần lưu trữ các bản sao lưu dài hạn (long-term backups) cho cơ sở dữ liệu Aurora để phục vụ mục đích khôi phục thảm họa và kiểm toán. Bạn khuyến nghị gì?

- [ ] A. Enable Automated Backups
- [x] **B. Perform On Demand Backups**
- [ ] C. Use Aurora Database Cloning

> **Giải thích:** Automated Backups chỉ lưu giữ được tối đa **35 ngày**. Để lưu trữ sao lưu dài hạn vô thời hạn (long-term retention), bạn cần thực hiện các bản sao lưu thủ công theo yêu cầu (**On-Demand Backups / Manual DB Snapshots**).

---

### Câu 23 (`id: 51042840`)
**Câu hỏi (English):** Your development team would like to perform a suite of read and write tests against your production Aurora database because they need access to production data as soon as possible. What do you advise?
**Dịch nghĩa (Tiếng Việt):** Nhóm phát triển của bạn muốn thực hiện một bộ kiểm thử cả đọc và ghi (read and write tests) dựa trên dữ liệu của cơ sở dữ liệu Aurora Production vì họ cần truy cập dữ liệu Production càng sớm càng tốt. Bạn khuyên họ nên làm gì?

- [ ] A. Create an Aurora Read Replica for them
- [ ] B. Do the test against the production database
- [ ] C. Make a DB Snapshot and Restore it into a new database
- [x] **D. Use the Aurora Cloning feature**

> **Giải thích:** **Aurora Database Cloning** sử dụng giao thức `Copy-on-Write` giúp tạo một cụm Aurora độc lập mới (hỗ trợ cả Read và Write) từ dữ liệu Production gần như tức thì, nhanh hơn nhiều so với việc chụp Snapshot rồi Restore và không làm ảnh hưởng đến Production DB. (Read Replica không dùng được vì nhóm cần chạy cả Write tests).

---

### Câu 24 (`id: 51042852`)
**Câu hỏi (English):** You have 100 EC2 instances connected to your RDS database and you see that upon a maintenance of the database, all your applications take a lot of time to reconnect to RDS, due to poor application logic. How do you improve this?
**Dịch nghĩa (Tiếng Việt):** Bạn có 100 EC2 instances kết nối tới cơ sở dữ liệu RDS và nhận thấy rằng mỗi khi bảo trì cơ sở dữ liệu, tất cả các ứng dụng mất rất nhiều thời gian để kết nối lại vào RDS do logic xử lý kết nối kém của ứng dụng. Làm thế nào để cải thiện vấn đề này?

- [ ] A. Fix all the applications
- [ ] B. Disable Multi-AZ
- [ ] C. Enable Multi-AZ
- [x] **D. Use an RDS Proxy**

> **Giải thích:** **Amazon RDS Proxy** duy trì và gộp các kết nối từ ứng dụng, đồng thời tự động xử lý chuyển đổi dự phòng ở phía sau khi cơ sở dữ liệu bảo trì hoặc failover, giúp giảm thời gian failover lên tới **66%** mà không cần sửa lại mã nguồn của 100 ứng dụng.
