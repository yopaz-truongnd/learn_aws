#!/usr/bin/env python3
"""
tools/enrich_topics_study_mode.py
Implements T2.1 and T2.2:
Adds '⚡ 5-minute Review' Card and Study Mode (toggle buttons, kw-target, pi-exam)
to all topic cheat sheets in topics/aws_*.html.
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_DIR = os.path.join(BASE_DIR, 'topics')

# Define the 5-minute review card for each topic
CARDS = {
    'aws_global_infra.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>&ge; 3 AZs:</b> Mỗi AWS Region chuẩn luôn có tối thiểu 3 Availability Zones độc lập.<br>
          • <b>&lt; 10ms:</b> Độ trễ mạng cáp quang riêng siêu tốc kết nối giữa các AZs trong cùng Region.<br>
          • <b>$0.00 / GB:</b> Miễn phí Inbound Data Transfer từ Internet vào AWS và truyền dữ liệu nội bộ qua Private IP trong cùng 1 AZ.<br>
          • <b>$0.01 / GB:</b> Chi phí Data Transfer giữa 2 AZ khác nhau trong cùng Region (tính cả 2 chiều gửi và nhận).<br>
          • <b>AZ ID vs AZ Name:</b> Tên AZ (<code>us-east-1a</code>) được ánh xạ ngẫu nhiên cho từng AWS Account; để đồng bộ đúng AZ vật lý giữa các tài khoản bắt buộc phải dùng <b>AZ ID</b> (ví dụ <code>use1-az1</code>).
        </span>
        <span class="lang-en">
          • <b>&ge; 3 AZs:</b> Every standard AWS Region contains a minimum of 3 isolated Availability Zones.<br>
          • <b>&lt; 10ms:</b> Ultra-low latency private fiber network interconnecting AZs within a Region.<br>
          • <b>$0.00 / GB:</b> Free Inbound Data Transfer from Internet and free intra-AZ traffic using Private IPs.<br>
          • <b>$0.01 / GB:</b> Inter-AZ data transfer cost per GB in each direction within the same Region.<br>
          • <b>AZ ID vs AZ Name:</b> AZ Names (<code>us-east-1a</code>) are dynamically mapped per account; multi-account physical alignment strictly requires <b>AZ ID</b> (e.g. <code>use1-az1</code>).
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Chạy hạ tầng AWS trực tiếp tại On-premises Data Center của công ty</span>
              <span class="lang-en">Run AWS infrastructure physically inside on-premises datacenter</span>
            </td>
            <td><span class="kw-target">AWS Outposts</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Độ trễ mili-giây cực thấp cho ứng dụng di động mạng 5G</span>
              <span class="lang-en">Ultra-low single-digit ms latency for mobile 5G applications</span>
            </td>
            <td><span class="kw-target">AWS Wavelength</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Mở rộng tính toán gần các trung tâm dân cư lớn (đô thị lớn)</span>
              <span class="lang-en">Low latency compute near large metropolitan population centers</span>
            </td>
            <td><span class="kw-target">AWS Local Zones</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Đường truyền cáp quang vật lý riêng biệt bỏ qua hoàn toàn Internet</span>
              <span class="lang-en">Dedicated private physical fiber connection bypassing public Internet</span>
            </td>
            <td><span class="kw-target">AWS Direct Connect</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Đồng bộ vị trí AZ vật lý chuẩn xác giữa nhiều tài khoản AWS</span>
              <span class="lang-en">Consistent physical AZ mapping across multiple AWS Accounts</span>
            </td>
            <td><span class="kw-target">AZ ID (not AZ Name)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Kiến trúc sẵn sàng cao chịu được sự cố sập cả một Data Center</span>
              <span class="lang-en">High availability compute architecture resilient to datacenter loss</span>
            </td>
            <td><span class="kw-target">Multi-AZ Deployment</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Quy định luật pháp yêu cầu dữ liệu không được rời khỏi biên giới quốc gia</span>
              <span class="lang-en">Compliance requirement stating data must remain within national borders</span>
            </td>
            <td><span class="kw-target">Data Sovereignty (Choose Region)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Truyền dữ liệu chi phí thấp nhất giữa 2 EC2 instances trong cùng 1 AZ</span>
              <span class="lang-en">Least cost data transfer between two EC2 instances in same AZ</span>
            </td>
            <td><span class="kw-target">Private IPv4 Address ($0/GB)</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_ec2.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>AZ-Scoped:</b> Mỗi EC2 Instance gắn chặt vào 1 AZ duy nhất; không thể span qua AZ khác.<br>
          • <b>Max 7 instances / AZ:</b> Giới hạn cứng của <b>Spread Placement Group</b> để tránh rủi ro sập đồng thời.<br>
          • <b>15 phút:</b> Thời gian chạy tối đa của AWS Lambda; tác vụ tính toán dài hơn bắt buộc dùng <b>Amazon EC2</b>.<br>
          • <b>5 EIP / Region:</b> Giới hạn mặc định Elastic IP; chỉ miễn phí khi gắn vào 1 EC2 đang Running.<br>
          • <b>User Data chỉ chạy 1 lần:</b> Tự động thực thi dưới quyền <code>root</code> khi instance khởi tạo lần đầu tiên.
        </span>
        <span class="lang-en">
          • <b>AZ-Scoped:</b> Each EC2 instance is locked to a single AZ; cannot span across AZs.<br>
          • <b>Max 7 instances / AZ:</b> Strict hard limit for <b>Spread Placement Groups</b> to isolate hardware racks.<br>
          • <b>15 minutes:</b> AWS Lambda maximum execution timeout; longer compute tasks require <b>Amazon EC2</b>.<br>
          • <b>5 EIPs / Region:</b> Default soft limit for Elastic IPs; free only when attached to a running instance.<br>
          • <b>User Data runs once:</b> Bootstraps automatically under <code>root</code> exclusively on the very first boot.
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Tác vụ xử lý dữ liệu chịu lỗi, chạy theo mẻ, tiết kiệm chi phí tối đa (giảm tới 90%)</span>
              <span class="lang-en">Stateless, fault-tolerant batch jobs at maximum discount (up to 90% off)</span>
            </td>
            <td><span class="kw-target">Spot Instances</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Tải ổn định liên tục với cam kết dài hạn 1 hoặc 3 năm</span>
              <span class="lang-en">Long-term steady-state workload with 1 or 3 year commitment</span>
            </td>
            <td><span class="kw-target">Reserved Instances / Savings Plans</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Phần mềm yêu cầu bản quyền tính theo phần cứng vật lý Socket / Core (BYOL)</span>
              <span class="lang-en">Server-bound software licenses per socket / core (BYOL compliance)</span>
            </td>
            <td><span class="kw-target">Dedicated Hosts</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Tính toán hiệu năng cao (HPC), mạng 10 Gbps, độ trễ cực thấp trong 1 AZ</span>
              <span class="lang-en">HPC, ultra-low network latency, 10 Gbps interconnect in single AZ</span>
            </td>
            <td><span class="kw-target">Cluster Placement Group</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cách ly tối đa máy chủ trọng yếu trên các tủ rack vật lý khác nhau (tối đa 7/AZ)</span>
              <span class="lang-en">Critical instances isolated on separate hardware racks (max 7 per AZ)</span>
            </td>
            <td><span class="kw-target">Spread Placement Group</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Hệ thống phân tán lớn (Hadoop, Kafka, Cassandra) trải rộng hàng trăm máy</span>
              <span class="lang-en">Hadoop, Kafka, Cassandra hundreds of instances rack-aware</span>
            </td>
            <td><span class="kw-target">Partition Placement Group</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Địa chỉ IPv4 công khai tĩnh cố định không đổi khi Stop/Start EC2</span>
              <span class="lang-en">Fixed static public IPv4 retained across EC2 Stop/Start cycles</span>
            </td>
            <td><span class="kw-target">Elastic IP (EIP)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Đăng nhập terminal bảo mật không cần mở port 22, không cần Public IP</span>
              <span class="lang-en">Secure terminal access with NO open port 22 and NO public IP</span>
            </td>
            <td><span class="kw-target">SSM Session Manager</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Bảo toàn trạng thái bộ nhớ RAM khi tạm dừng máy chủ để khởi động lại nhanh</span>
              <span class="lang-en">Preserve in-memory RAM state during planned instance stop for fast boot</span>
            </td>
            <td><span class="kw-target">EC2 Hibernate</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_storage.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>16.000 IOPS:</b> Ngưỡng chuyển giao hiệu năng giữa <code>gp3</code> và <code>io2</code> (Provisioned IOPS SSD).<br>
          • <b>Max 16 instances:</b> Giới hạn gắn đồng thời của <b>EBS Multi-Attach</b> (chỉ <code>io1/io2</code> trong <b>CÙNG 1 AZ</b>).<br>
          • <b>Delete on Termination:</b> Mặc định Root Volume bị xóa (<code>Yes</code>), Additional Volume được giữ lại (<code>No</code>).<br>
          • <b>EBS là AZ-locked:</b> Không thể gắn trực tiếp ổ EBS sang AZ khác (phải tạo Snapshot rồi Restore sang AZ đích).<br>
          • <b>Instance Store = Ephemeral:</b> Ổ đĩa vật lý gắn trực tiếp máy chủ, IOPS tối đa nhưng mất sạch dữ liệu khi Stop/Terminate.
        </span>
        <span class="lang-en">
          • <b>16,000 IOPS:</b> Cut-off performance threshold transitioning from <code>gp3</code> to <code>io2</code> SSD.<br>
          • <b>Max 16 instances:</b> Maximum attachment concurrency for <b>EBS Multi-Attach</b> (<code>io1/io2</code> in <b>SAME AZ</b> only).<br>
          • <b>Delete on Termination:</b> Root volume deleted by default (<code>Yes</code>); secondary volumes preserved (<code>No</code>).<br>
          • <b>EBS is AZ-locked:</b> Cannot attach an EBS volume directly to another AZ (must Snapshot &rarr; Restore to new AZ).<br>
          • <b>Instance Store is Ephemeral:</b> Physical host-attached drive, maximum IOPS but loses all data upon Stop/Terminate.
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Ổ đĩa hệ điều hành chuẩn, tùy chỉnh độc lập IOPS và Throughput với dung lượng</span>
              <span class="lang-en">Standard OS root drive, independent IOPS and throughput scaling from volume size</span>
            </td>
            <td><span class="kw-target">EBS gp3</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cơ sở dữ liệu trọng yếu yêu cầu trên 16.000 IOPS hoặc tính năng Multi-Attach</span>
              <span class="lang-en">Mission-critical DB requiring &gt;16,000 IOPS or EBS Multi-Attach</span>
            </td>
            <td><span class="kw-target">EBS io2 Block Express</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Dữ liệu lớn tuần tự (Big Data, Data Warehouse) không thể làm Boot Volume</span>
              <span class="lang-en">Sequential throughput big data workload (cannot be an OS boot volume)</span>
            </td>
            <td><span class="kw-target">EBS st1 (Throughput Optimized)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Hệ thống tệp mạng POSIX chia sẻ đồng thời cho hàng trăm máy Linux qua nhiều AZ</span>
              <span class="lang-en">Multi-AZ POSIX network filesystem shared concurrently by hundreds of Linux EC2s</span>
            </td>
            <td><span class="kw-target">Amazon EFS</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Bộ nhớ đệm tạm thời yêu cầu IOPS phần cứng cực đại, chấp nhận mất dữ liệu</span>
              <span class="lang-en">Ultra-high IOPS buffer/cache where data loss on stop/terminate is acceptable</span>
            </td>
            <td><span class="kw-target">EC2 Instance Store (Ephemeral)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Di chuyển dữ liệu một ổ đĩa EBS từ Availability Zone này sang Availability Zone khác</span>
              <span class="lang-en">Migrate an EBS volume from one Availability Zone to another</span>
            </td>
            <td><span class="kw-target">EBS Snapshot &rarr; Restore in new AZ</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Bảo vệ và khôi phục EBS Snapshots bị xóa nhầm trong khoảng từ 1 đến 365 ngày</span>
              <span class="lang-en">Recover accidentally deleted EBS Snapshots within 1 to 365 days</span>
            </td>
            <td><span class="kw-target">AWS Recycle Bin</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Loại bỏ độ trễ khởi tạo lần đầu khi tạo ổ EBS dung lượng lớn từ Snapshot</span>
              <span class="lang-en">Instantly restore full EBS snapshot IOPS performance without initial latency</span>
            </td>
            <td><span class="kw-target">Fast Snapshot Restore (FSR)</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_elb_asg.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>Layer 7 vs Layer 4:</b> ALB định tuyến thông minh theo HTTP path/host/headers; NLB định tuyến siêu tốc TCP/UDP với độ trễ micro-giây.<br>
          • <b>Static IP:</b> Chỉ <b>NLB</b> cung cấp 1 Public Static IPv4 cố định cho mỗi AZ; ALB luôn sử dụng DNS Name động.<br>
          • <b>Port 6081 GENEVE:</b> Cổng giao thức chuẩn mà Gateway Load Balancer (GWLB) sử dụng để đóng gói gói tin Layer 3.<br>
          • <b>SNI:</b> Cho phép gắn nhiều chứng chỉ SSL/TLS trên cùng một Load Balancer cho nhiều hostname khác nhau.<br>
          • <b>Deregistration Delay:</b> Cho phép các request đang xử lý hoàn thành trước khi terminate máy chủ (mặc định 300 giây).
        </span>
        <span class="lang-en">
          • <b>Layer 7 vs Layer 4:</b> ALB routes intelligently on HTTP path/host/headers; NLB routes ultra-fast TCP/UDP with microsecond latency.<br>
          • <b>Static IP:</b> Only <b>NLB</b> provides a single public static IPv4 per AZ; ALB always uses dynamic DNS names.<br>
          • <b>Port 6081 GENEVE:</b> Standard encapsulation protocol port used by Gateway Load Balancer (GWLB) at Layer 3.<br>
          • <b>SNI:</b> Allows hosting multiple SSL/TLS certificates on the same listener for different hostnames.<br>
          • <b>Deregistration Delay:</b> Grace period allowing in-flight requests to complete before instance termination (default 300s).
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Định tuyến HTTP/HTTPS dựa theo đường dẫn URL path, host header, hoặc query string</span>
              <span class="lang-en">HTTP/HTTPS routing based on URL path, host header, or query parameters</span>
            </td>
            <td><span class="kw-target">Application Load Balancer (ALB)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Hàng triệu request/giây, độ trễ micro-giây, yêu cầu địa chỉ IP tĩnh cố định</span>
              <span class="lang-en">Ultra-high throughput, millions of requests/sec, microsecond latency, static IP</span>
            </td>
            <td><span class="kw-target">Network Load Balancer (NLB)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Mở rộng và điều hướng luồng qua dàn thiết bị ảo tường lửa bên thứ ba (Virtual Appliances)</span>
              <span class="lang-en">Deploy and scale a fleet of 3rd party inline virtual firewalls / appliances</span>
            </td>
            <td><span class="kw-target">Gateway Load Balancer (GWLB)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Tải nhiều chứng chỉ SSL/TLS trên cùng một Load Balancer cho nhiều tên miền</span>
              <span class="lang-en">Serve multiple domains with different SSL certificates on same listener</span>
            </td>
            <td><span class="kw-target">Server Name Indication (SNI)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Ghim client luôn gửi request về đúng 1 instance backend bằng cookie</span>
              <span class="lang-en">Send client to the exact same backend EC2 instance using a cookie</span>
            </td>
            <td><span class="kw-target">Sticky Sessions (Session Affinity)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Phân phối lưu lượng đều tới tất cả các instance trong mọi AZ đã đăng ký</span>
              <span class="lang-en">Distribute incoming traffic evenly across all instances in all registered AZs</span>
            </td>
            <td><span class="kw-target">Cross-Zone Load Balancing</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Duy trì mức sử dụng CPU trung bình của toàn bộ ASG ở mức cố định 50%</span>
              <span class="lang-en">Maintain average ASG aggregate CPU utilization at exactly 50%</span>
            </td>
            <td><span class="kw-target">Target Tracking Scaling Policy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Chờ hoàn tất ghi dữ liệu hoặc backup trước khi máy chủ bị ASG tiêu hủy</span>
              <span class="lang-en">Custom actions or pause instance termination before state cleanup completes</span>
            </td>
            <td><span class="kw-target">ASG Lifecycle Hooks</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_databases.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>6 copies across 3 AZs:</b> Amazon Aurora luôn tự động sao chép 6 bản sao dữ liệu trải đều trên 3 AZ.<br>
          • <b>Max 15 Read Replicas:</b> Aurora hỗ trợ tối đa 15 bản sao đọc (so với chỉ 5 của RDS thông thường).<br>
          • <b>Multi-AZ = HA / DR:</b> Multi-AZ là Standby thụ động, KHÔNG tăng tốc độ đọc; muốn tăng tốc đọc phải dùng <b>Read Replicas</b> hoặc <b>ElastiCache</b>.<br>
          • <b>Database Ports:</b> MySQL/MariaDB (3306), PostgreSQL (5432), MSSQL (1433), Oracle (1521). Security Group của RDS tuyệt đối không mở port 80/443 hay 0.0.0.0/0.<br>
          • <b>RDS Proxy:</b> Giải quyết triệt để sự cố cạn kiệt Connection Pool khi hàng nghìn hàm Lambda kết nối đồng thời.
        </span>
        <span class="lang-en">
          • <b>6 copies across 3 AZs:</b> Amazon Aurora automatically replicates 6 storage copies across 3 availability zones.<br>
          • <b>Max 15 Read Replicas:</b> Aurora scales up to 15 read replicas (compared to 5 for standard RDS).<br>
          • <b>Multi-AZ is HA/DR:</b> Standby is passive and rejects reads; to scale reads use <b>Read Replicas</b> or <b>ElastiCache</b>.<br>
          • <b>Database Ports:</b> MySQL/MariaDB (3306), PostgreSQL (5432), MSSQL (1433), Oracle (1521). Never open port 80/443 or 0.0.0.0/0 on RDS SGs.<br>
          • <b>RDS Proxy:</b> Eliminates connection pool exhaustion from thousands of concurrent serverless Lambda invocations.
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Cơ sở dữ liệu quan hệ cần tự động failover sang AZ khác khi gặp sự cố thảm họa</span>
              <span class="lang-en">Relational DB with automatic failover across AZs for high availability (no read scale)</span>
            </td>
            <td><span class="kw-target">RDS Multi-AZ Deployment</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Giảm tải truy vấn đọc nặng cho báo cáo phân tích ban ngày ra khỏi Master DB</span>
              <span class="lang-en">Offload read-heavy reporting / analytics queries from production master DB</span>
            </td>
            <td><span class="kw-target">RDS Read Replicas</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cơ sở dữ liệu quan hệ Cloud-native, hiệu năng gấp 5 lần MySQL, 6 bản sao trên 3 AZ</span>
              <span class="lang-en">Cloud-native SQL, 5x MySQL performance, 6 copies across 3 AZs, up to 15 replicas</span>
            </td>
            <td><span class="kw-target">Amazon Aurora</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Tải cơ sở dữ liệu không thường xuyên, khó đoán, tự động bật/tắt để tối ưu chi phí</span>
              <span class="lang-en">Infrequent, unpredictable database workload that auto-starts and stops automatically</span>
            </td>
            <td><span class="kw-target">Aurora Serverless v2</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Hàng nghìn hàm Lambda Serverless gây cạn kiệt Connection Pool của RDS</span>
              <span class="lang-en">Serverless Lambda functions exhausting database connection pool on RDS</span>
            </td>
            <td><span class="kw-target">Amazon RDS Proxy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Bộ nhớ đệm In-memory độ trễ dưới 1 mili-giây hỗ trợ cấu trúc dữ liệu phức tạp &amp; Pub/Sub</span>
              <span class="lang-en">Sub-millisecond in-memory cache supporting complex data structures and pub/sub</span>
            </td>
            <td><span class="kw-target">Amazon ElastiCache for Redis</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cơ sở dữ liệu NoSQL Serverless độ trễ đọc/ghi dưới 10ms ở mọi quy mô</span>
              <span class="lang-en">Serverless NoSQL key-value with single-digit millisecond latency at any scale</span>
            </td>
            <td><span class="kw-target">Amazon DynamoDB</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Bộ nhớ đệm đọc siêu tốc cấp độ micro-giây (&mu;s) cho bảng DynamoDB</span>
              <span class="lang-en">Microsecond read latency cache for hot DynamoDB keys</span>
            </td>
            <td><span class="kw-target">DynamoDB Accelerator (DAX)</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_route53.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>Zone Apex (Root Domain):</b> Tên miền gốc (<code>example.com</code>) BẮT BUỘC dùng <b>Alias Record</b> (CNAME bị cấm theo chuẩn DNS).<br>
          • <b>Alias Record = $0:</b> Route 53 hoàn toàn miễn phí truy vấn DNS đối với các bản ghi Alias trỏ vào tài nguyên AWS.<br>
          • <b>KHÔNG Alias vào EC2 DNS:</b> Bản ghi Alias không thể trỏ tới tên DNS của EC2 (phải dùng bản ghi A trỏ IP hoặc đặt EC2 sau ALB).<br>
          • <b>5120 bytes:</b> Health Check của Route 53 chỉ kiểm tra chuỗi phản hồi trong 5120 bytes đầu tiên của trang web.<br>
          • <b>Route 53 Resolver:</b> Inbound Endpoints cho On-Prem giải quyết DNS của AWS; Outbound Endpoints cho AWS giải quyết DNS On-Premises.
        </span>
        <span class="lang-en">
          • <b>Zone Apex (Root Domain):</b> Top-level domain (<code>example.com</code>) strictly mandates <b>Alias Record</b> (CNAME forbidden by DNS RFC).<br>
          • <b>Alias Record is Free:</b> Route 53 queries pointing to AWS resources via Alias are completely free of charge.<br>
          • <b>NO Alias to EC2 DNS:</b> Alias records cannot target EC2 instance hostnames directly (use A record to IP or place EC2 behind ALB).<br>
          • <b>5,120 bytes:</b> Route 53 string-matching health checks inspect only the first 5,120 bytes of response payload.<br>
          • <b>Route 53 Resolver:</b> Inbound endpoints allow on-premises to resolve AWS DNS; Outbound endpoints allow AWS to resolve on-prem DNS.
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Trỏ tên miền gốc (Zone Apex mydomain.com) trực tiếp tới Elastic Load Balancer</span>
              <span class="lang-en">Map root domain (zone apex mydomain.com) directly to Elastic Load Balancer</span>
            </td>
            <td><span class="kw-target">Alias Record (Type A)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Trỏ hostname tới một hostname khác bất kỳ mà không hỗ trợ tên miền gốc</span>
              <span class="lang-en">Point hostname to another hostname anywhere without supporting root domain</span>
            </td>
            <td><span class="kw-target">CNAME Record</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Gửi 10% lưu lượng truy cập sang phiên bản phần mềm mới để thử nghiệm (Canary)</span>
              <span class="lang-en">Send 10% of traffic to new software version for canary testing</span>
            </td>
            <td><span class="kw-target">Weighted Routing Policy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Điều hướng người dùng tới AWS Region có độ trễ mạng thấp nhất</span>
              <span class="lang-en">Direct users to the AWS Region that provides the lowest network latency</span>
            </td>
            <td><span class="kw-target">Latency Routing Policy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Tự động chuyển đổi dự phòng Active-Passive sang trang dự phòng khi kiểm tra sức khỏe lỗi</span>
              <span class="lang-en">Active-Passive automatic failover to backup site upon health check failure</span>
            </td>
            <td><span class="kw-target">Failover Routing Policy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Chặn hoặc phân luồng người dùng dựa trên quốc gia / châu lục xuất phát của họ</span>
              <span class="lang-en">Restrict access or route users based on their country / continent location</span>
            </td>
            <td><span class="kw-target">Geolocation Routing Policy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Trả về ngẫu nhiên tối đa 8 bản ghi IP khỏe mạnh để client tự cân bằng tải</span>
              <span class="lang-en">Return up to 8 healthy IP records randomly for client-side load balancing</span>
            </td>
            <td><span class="kw-target">Multi-Value Answer Policy</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Phân giải tên miền lai kết nối giữa mạng nội bộ On-Premises và AWS VPC</span>
              <span class="lang-en">Hybrid DNS resolution between On-Premises DNS servers and AWS VPC</span>
            </td>
            <td><span class="kw-target">Route 53 Resolver (Inbound/Outbound)</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_s3.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>11 con số 9 (99.999999999%):</b> Độ bền dữ liệu (Durability) của mọi tầng lưu trữ S3 (kể cả S3 One Zone-IA).<br>
          • <b>5 TB / Object:</b> Dung lượng tối đa của một Object đơn lẻ; tệp trên <b>5 GB</b> bắt buộc phải dùng <b>Multipart Upload</b>.<br>
          • <b>100 MB+:</b> Ngưỡng khuyến nghị bắt đầu dùng Multipart Upload để tăng tốc độ truyền tải.<br>
          • <b>Versioning không thể xóa:</b> Khi đã kích hoạt Versioning thì chỉ có thể Tạm dừng (Suspend), không thể tắt vĩnh viễn.<br>
          • <b>Object Lock Compliance:</b> Chế độ WORM nghiêm ngặt nhất, ngăn chặn tuyệt đối việc xóa tệp kể cả với tài khoản root.
        </span>
        <span class="lang-en">
          • <b>11 9s (99.999999999%):</b> Data durability across all S3 storage tiers (including S3 One Zone-IA).<br>
          • <b>5 TB / Object:</b> Maximum size of a single S3 object; files over <b>5 GB</b> strictly mandate <b>Multipart Upload</b>.<br>
          • <b>100 MB+:</b> Recommended threshold to adopt Multipart Upload for parallel transfer speed and reliability.<br>
          • <b>Versioning cannot be disabled:</b> Once enabled on a bucket, versioning can only be Suspended, never disabled.<br>
          • <b>Object Lock Compliance Mode:</b> Strict WORM compliance where nobody, including the AWS root account, can delete objects.
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Dữ liệu truy cập thường xuyên yêu cầu sẵn sàng 99.99% và truy xuất tức thì</span>
              <span class="lang-en">Frequently accessed data requiring 99.99% availability with instant retrieval</span>
            </td>
            <td><span class="kw-target">S3 Standard</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Dữ liệu ít truy cập, cần lấy ra ngay lập tức, tiết kiệm chi phí, Multi-AZ</span>
              <span class="lang-en">Infrequently accessed data needing millisecond access, lower cost, multi-AZ</span>
            </td>
            <td><span class="kw-target">S3 Standard-IA</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Bản sao lưu thứ cấp có thể tạo lại được, lưu trong 1 AZ duy nhất để giảm 20% chi phí</span>
              <span class="lang-en">Reproducible non-critical secondary backups stored in a single AZ to save 20%</span>
            </td>
            <td><span class="kw-target">S3 One Zone-IA</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Mô hình truy cập dữ liệu không thể dự đoán trước, tự động chuyển tầng không tính phí truy xuất</span>
              <span class="lang-en">Unknown or unpredictable access patterns with automatic tier shifting and no fee</span>
            </td>
            <td><span class="kw-target">S3 Intelligent-Tiering</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Lưu trữ lưu trữ lâu năm (1-2 lần/năm), thời gian lấy dữ liệu từ vài phút đến vài giờ</span>
              <span class="lang-en">Archive data accessed 1-2 times/year with retrieval time of minutes to hours</span>
            </td>
            <td><span class="kw-target">S3 Glacier Flexible Archive</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Lưu trữ tuân thủ pháp lý nhiều năm với chi phí thấp nhất, thời gian lấy dữ liệu 12-48 giờ</span>
              <span class="lang-en">Long-term compliance data rarely accessed with lowest cost and 12-48 hour retrieval</span>
            </td>
            <td><span class="kw-target">S3 Glacier Deep Archive</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Tuân thủ quy chuẩn WORM nghiêm ngặt cấm tuyệt đối việc xóa tệp kể cả tài khoản root</span>
              <span class="lang-en">Enforce strict WORM compliance where even AWS root account cannot delete objects</span>
            </td>
            <td><span class="kw-target">S3 Object Lock (Compliance Mode)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cung cấp quyền tải về hoặc tải lên tạm thời có giới hạn thời gian cho một đối tượng riêng tư</span>
              <span class="lang-en">Give temporary time-limited download or upload access to a private S3 object</span>
            </td>
            <td><span class="kw-target">S3 Pre-signed URLs</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',

    'aws_cloudfront.html': '''<!-- ⚡ 5-MINUTE REVIEW: ÔN NHANH TRƯỚC PHÒNG THI -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--orb)">⚡</div>
    <div>
      <div class="ct">
        <span class="lang-vi">⚡ Ôn nhanh 5 phút trước giờ thi (5-Minute SAA-C03 Review)</span>
        <span class="lang-en">⚡ 5-Minute Exam Quick Review (SAA-C03 High-Yield)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">Bẫy đề thi cốt lõi · Bảng ánh xạ Từ khóa &rarr; Đáp án · 5 con số vàng phải thuộc</span>
        <span class="lang-en">Essential Exam Traps · Keyword &rarr; Answer Mapping · Critical Numbers to Memorize</span>
      </div>
    </div>
  </div>

  <!-- Study Mode Toolbar -->
  <div class="study-toolbar">
    <button class="study-btn" onclick="toggleExamFocus(this)">
      <span>🎯</span>
      <span class="lang-vi">Chỉ hiện Điểm hay bị hỏi</span>
      <span class="lang-en">Focus Exam Traps Only</span>
    </button>
    <button class="study-btn" onclick="toggleHideAnswers(this)">
      <span>👁️</span>
      <span class="lang-vi">Chế độ Flashcard (Ẩn đáp án)</span>
      <span class="lang-en">Flashcard Mode (Blur Answers)</span>
    </button>
  </div>

  <div class="g2">
    <div>
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 5 Con số vàng &amp; Bẫy đề cốt lõi</span>
          <span class="lang-en">🔴 5 Golden Numbers &amp; Core Exam Traps</span>
        </b>
        <span class="lang-vi">
          • <b>CloudFront vs Global Accelerator:</b> CloudFront cache nội dung web tĩnh/động tại Edge PoP (HTTP/HTTPS); Global Accelerator KHÔNG cache mà dùng 2 Anycast IP định tuyến TCP/UDP qua mạng cáp quang AWS Backbone.<br>
          • <b>OAC (Origin Access Control):</b> Phương thức chuẩn hiện nay để bảo vệ S3 Origin, thay thế hoàn toàn OAI cũ.<br>
          • <b>Dưới 1ms:</b> Thời gian thực thi của <b>CloudFront Functions</b> viết bằng JavaScript tại 450+ Edge Locations (chỉnh headers, URL rewrite).<br>
          • <b>Signed URL vs Signed Cookies:</b> Signed URL dùng khi truy cập 1 tệp tin đơn lẻ; Signed Cookies dùng khi truy cập nhiều tệp tin hoặc toàn bộ nội dung thành viên trả phí.<br>
          • <b>Origin Shield:</b> Tầng bộ nhớ đệm phụ tập trung nằm giữa Regional Edge Cache và Origin giúp giảm thiểu tối đa tải truy vấn về máy chủ gốc.
        </span>
        <span class="lang-en">
          • <b>CloudFront vs Global Accelerator:</b> CloudFront caches web content at Edge PoPs (HTTP/HTTPS); Global Accelerator does NOT cache, routing TCP/UDP over AWS backbone via 2 Anycast IPs.<br>
          • <b>OAC (Origin Access Control):</b> The modern security standard to lock down S3 origins, superseding legacy OAI.<br>
          • <b>Sub-1ms:</b> Execution latency of lightweight <b>CloudFront Functions</b> written in JavaScript across 450+ Edge Locations.<br>
          • <b>Signed URL vs Signed Cookies:</b> Signed URL for single file access; Signed Cookies for accessing multiple files or premium member areas.<br>
          • <b>Origin Shield:</b> Centralized secondary caching layer between Regional Edge Caches and Origin to minimize origin database load.
        </span>
      </div>
    </div>

    <div style="overflow-x:auto">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>
              <span class="lang-vi">Tình huống / Từ khóa trong đề thi</span>
              <span class="lang-en">Exam Scenario / Keyword</span>
            </th>
            <th>
              <span class="lang-vi">Dịch vụ / Đáp án cốt lõi</span>
              <span class="lang-en">Target Service / Answer</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="lang-vi">Lưu bộ nhớ đệm nội dung web toàn cầu tại các Edge Locations để giảm độ trễ HTTP/HTTPS</span>
              <span class="lang-en">Cache web content globally at edge locations to reduce latency for HTTP/HTTPS</span>
            </td>
            <td><span class="kw-target">Amazon CloudFront</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Hai địa chỉ Anycast IP tĩnh tăng tốc luồng giao thức mạng non-HTTP (TCP/UDP) qua mạng AWS</span>
              <span class="lang-en">Two static Anycast IPs to accelerate non-HTTP TCP/UDP traffic via AWS backbone</span>
            </td>
            <td><span class="kw-target">AWS Global Accelerator</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Chặn truy cập trực tiếp từ Internet vào S3 bucket, chỉ cho phép đi qua CloudFront</span>
              <span class="lang-en">Restrict S3 bucket access strictly to CloudFront and block direct internet access</span>
            </td>
            <td><span class="kw-target">Origin Access Control (OAC)</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cung cấp quyền truy cập có thời hạn vào một tệp tải về hoặc video đơn lẻ</span>
              <span class="lang-en">Provide time-limited access to a single video or file download</span>
            </td>
            <td><span class="kw-target">CloudFront Signed URL</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Cấp quyền truy cập cho người dùng trả phí xem nhiều tệp nội dung số cao cấp</span>
              <span class="lang-en">Provide authorized access to multiple premium media files or an entire website section</span>
            </td>
            <td><span class="kw-target">CloudFront Signed Cookies</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Chuyển hướng URL và chỉnh sửa HTTP headers siêu tốc độ trễ dưới 1 mili-giây tại Edge</span>
              <span class="lang-en">Sub-millisecond lightweight URL rewrites and HTTP header manipulations at Edge PoPs</span>
            </td>
            <td><span class="kw-target">CloudFront Functions</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Xử lý tính toán phức tạp tại biên yêu cầu gọi API mạng bên thứ ba bằng Node.js / Python</span>
              <span class="lang-en">Complex edge compute requiring network access or third-party API validation</span>
            </td>
            <td><span class="kw-target">Lambda@Edge</span></td>
          </tr>
          <tr>
            <td>
              <span class="lang-vi">Chặn người dùng ở các quốc gia địa lý cụ thể không được xem trang web của bạn</span>
              <span class="lang-en">Prevent users in specific geographic countries from viewing your website</span>
            </td>
            <td><span class="kw-target">CloudFront Geographic Restriction</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>''',
}

def inject_review_card(file_name, card_html):
    fpath = os.path.join(TOPICS_DIR, file_name)
    if not os.path.isfile(fpath):
        print(f"Skipping {file_name}: not found")
        return
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already injected
    if '5-Minute SAA-C03 Review' in content or '5-MINUTE REVIEW' in content:
        print(f"{file_name}: Review card already present.")
        return
    
    grid_pattern = r'(<div class="grid">\s*)'
    if not re.search(grid_pattern, content):
        print(f"Error: Could not find <div class=\"grid\"> in {file_name}")
        return
    
    replacement = r'\1' + card_html + '\n\n'
    new_content = re.sub(grid_pattern, replacement, content, count=1)
    
    # Also attach pi-exam to existing important exam trap / golden rule .pi elements
    # e.g., <div class="pi"> that contains "Bẫy" or "Trap" or "Nguyên tắc vàng" or "Golden Rule"
    def mark_pi_exam(match):
        pi_body = match.group(0)
        if 'pi-exam' in pi_body:
            return pi_body
        keywords = ['bẫy', 'trap', 'nguyên tắc vàng', 'golden rule', 'hotspot', 'điểm hay bị hỏi']
        if any(kw in pi_body.lower() for kw in keywords):
            return pi_body.replace('<div class="pi"', '<div class="pi pi-exam"')
        return pi_body
    
    new_content = re.sub(r'<div class="pi"[^>]*>.*?(?=\n\s*<(?:div|/div|b|span|ul|ol|table))', mark_pi_exam, new_content, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully enriched {file_name}!")

def main():
    for fname, card in CARDS.items():
        inject_review_card(fname, card)

if __name__ == '__main__':
    main()
