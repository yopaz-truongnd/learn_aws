# Bài 34: EC2 Instance Types Basics

- **Phần:** Phần 5: EC2 Fundamentals
- **Lecture ID:** `26098128` (`CCP - EC2 - Instance Types Basics v4.mp4`)
- **Thời lượng:** `04:51`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Quy ước đặt tên EC2 Instance (Naming Convention)
Ví dụ với loại máy **`m5.2xlarge`**:
- **`m`**: **Instance Class** (Nhóm/dòng máy, ví dụ General Purpose).
- **`5`**: **Generation** (Thế hệ phần cứng thứ 5 của AWS).
- **`2xlarge`**: **Size** (Kích thước máy trong dòng đó — càng lớn càng nhiều CPU và RAM).

---

### 1.2. Bốn nhóm EC2 Instance chính cần nhớ cho kỳ thi SAA-C03

| Nhóm Instance (Category) | Ký hiệu dòng máy (Family) | Đặc điểm & Trường hợp sử dụng điển hình (Use Cases) |
| :--- | :---: | :--- |
| **1. General Purpose** *(Đa dụng)* | **`T`** (`t2`, `t3`), **`M`** (`m5`, `m6i`...) | Cân bằng tốt giữa **Compute (CPU), Memory (RAM) và Networking**.<br>- **Use cases:** Web servers, kho lưu trữ mã nguồn (code repositories), các tác vụ đa dạng.<br>- `t2.micro` / `t3.micro` thuộc gói Free Tier (1 vCPU, 1 GB RAM). |
| **2. Compute Optimized** *(Tối ưu tính toán / CPU)* | **`C`** (`c5`, `c6g`, `c5d`...) | Tối ưu cho các tác vụ đòi hỏi **CPU hiệu năng rất cao (compute-intensive)**.<br>- **Use cases:** Xử lý dữ liệu theo lô (**Batch processing**), chuyển mã đa phương tiện (**Media transcoding**), Web servers hiệu năng cao, Tính toán hiệu năng cao (**HPC - High Performance Computing**), mô hình khoa học & **Machine Learning**, Dedicated gaming servers. |
| **3. Memory Optimized** *(Tối ưu bộ nhớ / RAM)* | **`R`** (*RAM* - `r5`, `r6i`), **`X1`**, **`High Memory`**, **`z1d`** | Hiệu năng nhanh cho các tác vụ **xử lý tập dữ liệu lớn ngay trong bộ nhớ RAM (in-memory)**.<br>- **Use cases:** Cơ sở dữ liệu quan hệ / phi quan hệ hiệu năng cao, bộ nhớ đệm phân tán quy mô web (**Distributed web scale cache stores** như ElastiCache), **In-memory databases** cho BI (Business Intelligence), xử lý thời gian thực dữ liệu lớn phi cấu trúc (real-time big unstructured data). |
| **4. Storage Optimized** *(Tối ưu lưu trữ)* | **`I`**, **`D`**, **`H1`** | Tối ưu cho các tác vụ đòi hỏi **truy xuất đọc/ghi tuần tự tốc độ cao trên tập dữ liệu rất lớn tại ổ đĩa cục bộ (local storage)**.<br>- **Use cases:** Hệ thống xử lý giao dịch trực tuyến tần suất cao (**High-frequency OLTP systems**), cơ sở dữ liệu **Relational & NoSQL**, Cache cho in-memory databases (như Redis), ứng dụng **Data Warehousing**, hệ thống tệp phân tán (**Distributed file systems**). |

### 1.3. Ví dụ so sánh thông số thực tế
- **`t2.micro`** (*General Purpose*): `1 vCPU`, `1 GiB RAM`.
- **`r5.16xlarge`** (*Memory Optimized*): `64 vCPU`, `512 GiB RAM` (tập trung mạnh vào RAM).
- **`c5d.4xlarge`** (*Compute Optimized*): `16 vCPU`, `32 GiB RAM` (tập trung vào CPU).
- Trang tra cứu nhanh bảng giá và cấu hình EC2: `https://instances.vantage.sh` (trước đây là `ec2instances.info`).

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :---: | :--- | :--- |
| `00:00` - `00:45` | Let's talk about the different EC2 instance types. AWS uses a naming convention like **`m5.2xlarge`**: **`m`** is the instance class, **`5`** is the generation, and **`2xlarge`** is the size within the instance class. | Hãy tìm hiểu về các loại EC2 instance. AWS đặt tên theo quy ước như **`m5.2xlarge`**: trong đó **`m`** là phân lớp (instance class), **`5`** là thế hệ (generation), và **`2xlarge`** là kích cỡ (size) trong phân lớp đó. |
| `00:45` - `01:21` | **General Purpose** instances are great for a diversity of workloads such as web servers or code repositories. They have a good balance between compute, memory, and networking (e.g., `t2.micro`). | Nhóm **General Purpose** (Đa dụng) rất phù hợp cho các tác vụ đa dạng như web servers hoặc kho chứa code (code repositories), nhờ sự cân bằng giữa Compute, Memory và Networking (ví dụ `t2.micro`). |
| `01:21` - `02:06` | **Compute Optimized** instances (starting with **`C`**, like `C5`, `C6`) are optimized for compute-intensive tasks requiring high-performance processors: batch processing data, media transcoding, high-performance web servers, High Performance Computing (HPC), machine learning, and dedicated gaming servers. | Nhóm **Compute Optimized** (bắt đầu bằng chữ **`C`** như `C5`, `C6`) tối ưu cho các tác vụ nặng về tính toán cần CPU mạnh: xử lý dữ liệu theo lô (batch processing), chuyển mã video/media (media transcoding), web servers hiệu năng cao, tính toán hiệu năng cao (HPC), học máy (Machine Learning) và máy chủ game chuyên dụng. |
| `02:06` - `02:57` | **Memory Optimized** instances (`R` series for RAM, `X1`, High Memory, `z1d`) deliver fast performance for workloads processing large data sets in memory (RAM): high-performance relational/non-relational databases, distributed web-scale cache stores (like ElastiCache), in-memory databases optimized for BI, and real-time processing of big unstructured data. | Nhóm **Memory Optimized** (dòng **`R`**, `X1`, High Memory, `z1d`) mang lại tốc độ cao cho các tác vụ xử lý tập dữ liệu lớn trong bộ nhớ RAM: CSDL quan hệ/phi quan hệ hiệu năng cao, bộ nhớ đệm phân tán (như ElastiCache), CSDL in-memory cho BI, và xử lý thời gian thực dữ liệu lớn phi cấu trúc. |
| `02:57` - `04:51` | **Storage Optimized** instances (`I`, `D`, `H1`) are great for high, sequential read/write access to large data sets on local storage: high-frequency online transaction processing (**OLTP** systems), relational & NoSQL databases, cache for in-memory databases (e.g., Redis), data warehousing applications, and distributed file systems. You can compare all EC2 instance specs and pricing on `ec2instances.info`. | Nhóm **Storage Optimized** (`I`, `D`, `H1`) phù hợp khi cần truy xuất đọc/ghi tuần tự tốc độ cao vào tập dữ liệu lớn trên ổ lưu trữ cục bộ: hệ thống giao dịch trực tuyến tần suất cao (**OLTP**), CSDL quan hệ & NoSQL, cache cho CSDL in-memory (Redis), kho dữ liệu (Data Warehousing) và hệ thống file phân tán. |
