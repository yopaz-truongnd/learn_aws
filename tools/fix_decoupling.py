import re

with open('topics/aws_decoupling.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Diagram 1
d1_old_start = content.find('<div class="mermaid-diagram">\nflowchart TD')
d1_old_end = content.find('</div>\n</div>\n\n<!-- 2. MA TRẬN', d1_old_start) + 6

d1_new = '''<div class="mermaid-diagram" id="diag-decoupling-tree">
    <div class="mermaid-src lang-vi" style="display:none">
flowchart TD
    START(["Nhu cầu tích hợp & Phân tách ứng dụng (Decoupling)"]) --> Q1{"Mô hình truyền tin là gì?"}

    %% Nhánh 1: Queue (Pull)
    Q1 -- "Hàng đợi xử lý tác vụ (1-to-1, Pull-based)" --> Q2{"Ứng dụng yêu cầu thứ tự & tính tương thích?"}
    Q2 -- "Cloud-native / Throughput vô hạn / Chấp nhận trùng lặp nhẹ" --> SQS_STD["Amazon SQS Standard<br/>• At-least-once delivery<br/>• Throughput không giới hạn<br/>• Lưu đệm & co giãn Worker"]
    Q2 -- "Bắt buộc chính xác thứ tự & không trùng lặp" --> SQS_FIFO["Amazon SQS FIFO<br/>• Exactly-once processing<br/>• Giữ nghiêm ngặt thứ tự FIFO<br/>• Bắt buộc đuôi: .fifo"]
    Q2 -- "Ứng dụng cũ on-prem (JMS, AMQP, MQTT, STOMP)" --> AMQ["Amazon MQ<br/>• Managed ActiveMQ / RabbitMQ<br/>• Không cần viết lại mã nguồn"]

    %% Nhánh 2: Pub/Sub (Push)
    Q1 -- "Phát tán thông báo (1-to-Many, Push-based)" --> Q3{"Đích đến là gì?"}
    Q3 -- "Nhiều hàng đợi SQS / Lambda / Email / SMS" --> SNS_FANOUT["Amazon SNS Topic<br/>• Pub/Sub Fan-Out Pattern<br/>• Message Filtering bằng JSON<br/>• Đẩy tin tức thì (Push)"]

    %% Nhánh 3: Streaming Big Data
    Q1 -- "Luồng dữ liệu thời gian thực (Real-time Streaming)" --> Q4{"Nhu cầu lưu trữ & Xử lý đích?"}
    Q4 -- "Phân tích tức thì (dưới 100ms) / Custom Consumers" --> KIN_STREAMS["Kinesis Data Streams<br/>• Shard throughput (1MB In / 2MB Out)<br/>• Replay dữ liệu (1–365 ngày)<br/>• Nhiều consumer đọc đồng thời"]
    Q4 -- "Nạp thẳng Serverless vào S3, Redshift, OpenSearch" --> KIN_FIREHOSE["Kinesis Data Firehose<br/>• Near real-time (buffer 60s)<br/>• Tự động co giãn 100%<br/>• Tích hợp Lambda chuyển đổi"]

    classDef awsBox fill:#E5F2FC,stroke:#2783DE,stroke-width:2px,color:#2783DE;
    classDef optBox fill:#E8F1EC,stroke:#46A171,stroke-width:2px,color:#46A171;
    classDef warnBox fill:#FBEBDE,stroke:#D5803B,stroke-width:2px,color:#D5803B;

    class SQS_STD,SQS_FIFO awsBox;
    class SNS_FANOUT,AMQ optBox;
    class KIN_STREAMS,KIN_FIREHOSE warnBox;
    </div>
    <div class="mermaid-src lang-en" style="display:none">
flowchart TD
    START(["Integration & Decoupling Requirement"]) --> Q1{"What messaging pattern is needed?"}

    %% Branch 1: Queue (Pull)
    Q1 -- "Task queue processing (1-to-1, Pull-based)" --> Q2{"Strict ordering & compatibility requirement?"}
    Q2 -- "Cloud-native / Unlimited throughput / Tolerates minor duplicates" --> SQS_STD["Amazon SQS Standard<br/>• At-least-once delivery<br/>• Unlimited throughput<br/>• Buffer & auto-scale workers"]
    Q2 -- "Strict ordering & deduplication required" --> SQS_FIFO["Amazon SQS FIFO<br/>• Exactly-once processing<br/>• Strict FIFO ordering<br/>• Requires .fifo suffix"]
    Q2 -- "Legacy on-prem apps (JMS, AMQP, MQTT, STOMP)" --> AMQ["Amazon MQ<br/>• Managed ActiveMQ / RabbitMQ<br/>• No application rewrite"]

    %% Branch 2: Pub/Sub (Push)
    Q1 -- "Message broadcast (1-to-Many, Push-based)" --> Q3{"What is the target consumer?"}
    Q3 -- "Multiple SQS queues / Lambda / Email / SMS" --> SNS_FANOUT["Amazon SNS Topic<br/>• Pub/Sub Fan-Out Pattern<br/>• JSON Message Filtering<br/>• Instant push notifications"]

    %% Branch 3: Streaming Big Data
    Q1 -- "Real-time big data streaming" --> Q4{"Storage & downstream processing requirement?"}
    Q4 -- "Real-time analytics (under 100ms) / Custom Consumers" --> KIN_STREAMS["Kinesis Data Streams<br/>• Shard throughput (1MB In / 2MB Out)<br/>• Data replay (1–365 days)<br/>• Multiple concurrent consumers"]
    Q4 -- "Serverless delivery to S3, Redshift, OpenSearch" --> KIN_FIREHOSE["Kinesis Data Firehose<br/>• Near real-time (60s buffer)<br/>• 100% autoscaling<br/>• Lambda transformation"]

    classDef awsBox fill:#E5F2FC,stroke:#2783DE,stroke-width:2px,color:#2783DE;
    classDef optBox fill:#E8F1EC,stroke:#46A171,stroke-width:2px,color:#46A171;
    classDef warnBox fill:#FBEBDE,stroke:#D5803B,stroke-width:2px,color:#D5803B;

    class SQS_STD,SQS_FIFO awsBox;
    class SNS_FANOUT,AMQ optBox;
    class KIN_STREAMS,KIN_FIREHOSE warnBox;
    </div>
    <div class="mermaid-output"></div>
  </div>'''

if d1_old_start != -1 and d1_old_end != -1:
    content = content[:d1_old_start] + d1_new + content[d1_old_end:]
    print("Replaced Diagram 1")
else:
    print("Could not find Diagram 1 boundaries")

# Replace Diagram 2
d2_old_start = content.find('<div class="mermaid-diagram">\nflowchart LR')
d2_old_end = content.find('</div>\n    </div>\n\n    <div>\n      <div class="pi pi-exam">', d2_old_start) + 6

d2_new = '''<div class="mermaid-diagram" id="diag-sns-fanout">
        <div class="mermaid-src lang-vi" style="display:none">
flowchart LR
    PUB["Order Service<br/>(Publisher)"] -->|Publish| SNS["SNS Topic<br/>(Orders Topic)"]

    SNS -->|Fan-Out Push| Q1["SQS Queue 1<br/>Fraud Detection"]
    SNS -->|Fan-Out Push| Q2["SQS Queue 2<br/>Inventory Update"]
    SNS -->|Fan-Out Push| Q3["SQS Queue 3<br/>Analytics Service"]

    Q1 -->|Poll & Process| W1["Fraud Workers"]
    Q2 -->|Poll & Process| W2["Inventory Workers"]
    Q3 -->|Poll & Process| W3["Analytics Workers"]

    classDef pubBox fill:#E5F2FC,stroke:#2783DE,stroke-width:1.5px;
    classDef snsBox fill:#FBEBDE,stroke:#D5803B,stroke-width:2px;
    classDef qBox fill:#E8F1EC,stroke:#46A171,stroke-width:1.5px;

    class PUB,W1,W2,W3 pubBox;
    class SNS snsBox;
    class Q1,Q2,Q3 qBox;
        </div>
        <div class="mermaid-src lang-en" style="display:none">
flowchart LR
    PUB["Order Service<br/>(Publisher)"] -->|Publish| SNS["SNS Topic<br/>(Orders Topic)"]

    SNS -->|Fan-Out Push| Q1["SQS Queue 1<br/>Fraud Detection"]
    SNS -->|Fan-Out Push| Q2["SQS Queue 2<br/>Inventory Update"]
    SNS -->|Fan-Out Push| Q3["SQS Queue 3<br/>Analytics Service"]

    Q1 -->|Poll & Process| W1["Fraud Workers"]
    Q2 -->|Poll & Process| W2["Inventory Workers"]
    Q3 -->|Poll & Process| W3["Analytics Workers"]

    classDef pubBox fill:#E5F2FC,stroke:#2783DE,stroke-width:1.5px;
    classDef snsBox fill:#FBEBDE,stroke:#D5803B,stroke-width:2px;
    classDef qBox fill:#E8F1EC,stroke:#46A171,stroke-width:1.5px;

    class PUB,W1,W2,W3 pubBox;
    class SNS snsBox;
    class Q1,Q2,Q3 qBox;
        </div>
        <div class="mermaid-output"></div>
      </div>'''

if d2_old_start != -1 and d2_old_end != -1:
    content = content[:d2_old_start] + d2_new + content[d2_old_end:]
    print("Replaced Diagram 2")
else:
    print("Could not find Diagram 2 boundaries")

with open('topics/aws_decoupling.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished writing topics/aws_decoupling.html")
