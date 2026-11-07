# Bài 86: Auto Scaling Groups - Scaling Policies Hands On (Thực hành cấu hình Scaling Policies trên ASG)

- **Phần (Section):** Phần 8: High Availability and Scalability: ELB & ASG
- **Mã bài học (Lecture ID):** `18078107`
- **Tệp video:** `SAA_-_ASG_-_Scaling_Policies_Hands_On_v4.mp4`
- **Thời lượng:** `09:15`

---

## 1. Kiến thức trọng tâm (Exam Notes)

### 1.1. Ba mục cấu hình trong tab `Automatic scaling` của ASG
1. **Scheduled actions (Hành động theo lịch trình):**
   - Đặt tên, chỉ định `Desired`, `Min`, `Max capacity`, tần suất lặp lại (`Once`, `Every hour`, `Every day`, `Every week`, hoặc biểu thức `Cron`), múi giờ, thời gian bắt đầu (`Start time`) và kết thúc (`End time`).
2. **Predictive scaling policies (Chính sách mở rộng dự đoán bằng ML):**
   - Chọn metric để dự báo tải (CPU utilization, Network in/out, ALB request count, hoặc Custom metric) và đặt giá trị mục tiêu (ví dụ: `50%` CPU). Dựa trên dữ liệu lịch sử (ít nhất 24h, lý tưởng là 1-2 tuần), AWS dùng Machine Learning lập lịch mở rộng trước.
3. **Dynamic scaling policies (Chính sách mở rộng động):**
   - **Simple scaling:** Chọn 1 CloudWatch Alarm tạo sẵn -> Khi Alarm kích hoạt thì thêm/bớt một số lượng hoặc tỷ lệ phần trăm capacity units nhất định, sau đó chờ hết Cooldown (300s).
   - **Step scaling:** Chọn 1 CloudWatch Alarm -> Thêm nhiều bậc (steps) mở rộng khác nhau tùy theo mức độ vượt ngưỡng của metric (ví dụ: vượt nhẹ thêm 1 máy, vượt rất cao thêm 10 máy).
   - **Target tracking scaling (Được thực hành chi tiết trong bài):**
     - Chọn Metric: `Average CPU utilization`, Target value: **`40`** (`40%`).
     - **Điều gì diễn ra ở hậu trường?** Target Tracking Policy **tự động tạo ra 2 CloudWatch Alarms**:
       1. `AlarmHigh`: Kích hoạt **Scale Out** khi `CPUUtilization > 40%` trong **3 data points liên tiếp trong vòng 3 phút**.
       2. `AlarmLow`: Kích hoạt **Scale In** khi `CPUUtilization < 28%` trong **15 data points liên tiếp trong vòng 15 phút** *(tốc độ Scale Out luôn nhanh và nhạy hơn, trong khi Scale In chậm và thận trọng hơn để tránh dao động bật/tắt liên tục)*.

---

### 1.2. Thử nghiệm Stress Test CPU thực tế
- Cập nhật ASG với `Min = 1`, `Desired = 1`, `Max = 3`.
- Kết nối vào EC2 instance qua **EC2 Instance Connect**, cài đặt công cụ `stress` trên Amazon Linux 2 và chạy lệnh:
  ```bash
  sudo amazon-linux-extras install epel -y
  sudo yum install stress -y
  stress -c 4
  ```
- Lệnh `stress -c 4` đẩy mức sử dụng CPU của EC2 instance lên **100%**.
- Sau 3 phút, `AlarmHigh` trên CloudWatch chuyển sang trạng thái `In alarm` -> ASG tự động tăng `Desired capacity` từ `1 -> 2` rồi lên `3` (tối đa bằng `Max capacity`).
- Khi dừng lệnh `stress` (hoặc Reboot các instances để CPU về `0%`), sau 15 phút dưới ngưỡng `28%`, `AlarmLow` kích hoạt và ASG tự động **Scale In** giảm số lượng máy từ `3 -> 2 -> 1` bằng cách Terminate bớt các instances dư thừa.

---

## 2. Phụ đề chi tiết theo mốc thời gian (Full Transcript & Timestamps)

| Thời gian | Nội dung lời giảng gốc (English) | Bản dịch tiếng Việt sát nghĩa |
| :--- | :--- | :--- |
| `00:00:00.710` | Okay, so now let's have a look at automatic scaling for your ASG. As you can see we have three categories, dynamic scaling policies, predictive scaling policies, and scheduled actions. | Bây giờ hãy cùng khám phá tab **Automatic scaling** trên Auto Scaling Group của bạn. Như bạn thấy chúng ta có ba danh mục: **Dynamic scaling policies**, **Predictive scaling policies**, và **Scheduled actions**. |
| `00:00:10.400` | So let's start with the simplest. So scheduled actions is when you want to schedule a scaling action in the future, so you can create one and then you say what you want the desired capacity or the min or the max to be, | Hãy bắt đầu với mục đơn giản nhất: **Scheduled actions**. Đây là nơi bạn lên lịch một hành động mở rộng trong tương lai: nhấn Create, nhập giá trị Desired, Min hoặc Max capacity mong muốn, |
| `00:00:22.300` | and then is it once, every week, every hour, is it based on a specific schedule and so on? And then a start time and an end time if you wanted it to be done. | sau đó chọn chu kỳ lặp lại (chạy 1 lần, mỗi tuần, mỗi giờ, hoặc theo lịch cron cụ thể), kèm theo thời gian bắt đầu và thời gian kết thúc. |
| `00:00:31.769` | So this is pretty cool and this is allowing you to schedule based on events that you can predict and that you know in advance. Because you know, for example that you're going to run a big promotion next Saturday. | Tính năng này rất tuyệt vời vì nó cho phép bạn lên lịch mở rộng dựa trên các sự kiện mà bạn biết trước — chẳng hạn bạn biết chắc thứ Bảy tuần tới công ty sẽ chạy một chương trình khuyến mãi lớn. |
| `00:00:42.840` | Next, predictive scaling policies is where it's going to be machine learning driven. So you need to scale it based on a forecast. | Tiếp theo là **Predictive scaling policies** — mở rộng dựa trên trí tuệ nhân tạo / học máy (Machine Learning) thông qua bản dự báo tải (forecast). |
| `00:00:49.830` | So you need to have a look at the actual policy and the actual scaling based on the past and then it will have a look at a metric to look at. For example, CPU utilization or network in, network out, the application load balancer request counts or a custom metric that you want. | Hệ thống sẽ phân tích dữ liệu lịch sử trong quá khứ dựa trên chỉ số mà bạn chọn (ví dụ: CPU utilization, Network in/out, ALB request count hoặc Custom metric) cùng mức mục tiêu (như `50%` CPU). |
| `00:01:14.450` | And based on this, and based on the actual scheduled utilization for the past week, for example, then a forecast is going to be created and your ASG is going to be scaling based on that forecast. | Dựa vào dữ liệu sử dụng thực tế trong tuần qua chẳng hạn, một bản dự báo sẽ được tạo ra và ASG của bạn sẽ chủ động mở rộng theo dự báo đó. |
| `00:01:24.860` | So it's not something I can demonstrate with you because I would need to enable this for a very long time (a week) and then make sure I have some usage on my application. | Tôi không thể chạy demo trực tiếp tính năng này ngay trong video vì cần phải bật nó và chạy tải thực tế ít nhất vài ngày đến một tuần để có dữ liệu lịch sử. |
| `00:01:42.230` | So the one policy I can demonstrate to you is the dynamic scaling policy. So let's go ahead and create a dynamic scaling policy. So here we have three options: we have target tracking, step scaling and simple scaling. | Chính sách mà tôi sẽ demo trực tiếp cho bạn ngay bây giờ là **Dynamic scaling policy**. Khi nhấn **Create dynamic scaling policy**, chúng ta có 3 lựa chọn: `Target tracking scaling`, `Step scaling`, và `Simple scaling`. |
| `00:01:54.650` | So let's have a look at simple scaling first. So here we have to specify a name, then a CloudWatch alarm, which is an alarm that can scale capacity whenever it is being triggered. | Hãy xem qua **Simple scaling** trước: bạn cần đặt tên, chọn một **CloudWatch Alarm** đã tạo sẵn từ trước, và quy định hành động khi cảnh báo đó bị kích hoạt: |
| `00:02:07.840` | And so in case the alarm is being triggered, maybe you want to add two capacity units, or maybe you want to add 10% of your group. And then add capacity units in increments of at least two capacity units. | Ví dụ thêm `2` đơn vị dung lượng (instances), hoặc thêm `10%` quy mô nhóm, hoặc đặt cứng bằng một con số cụ thể. Bạn có thể tạo chính sách để thêm máy (Scale Out) hoặc bớt máy (Scale In). |
| `00:02:35.930` | And next we have step scaling. So this is allowing you to set up an alarm and based on the alarm value to have different steps: for example, if the alarm is very, very high in terms of the value, then add 10 capacity units. But if it's high, but not too high, add one. | Tiếp theo là **Step scaling**: cho phép bạn gắn một CloudWatch Alarm và chia thành nhiều bậc (steps) dựa trên mức độ vi phạm ngưỡng của cảnh báo — ví dụ nếu chỉ số vượt quá cao thì thêm 10 máy, còn nếu mới vượt nhẹ thì chỉ thêm 1 máy. |
| `00:02:50.370` | This is the idea behind step scaling, but we'll set up a target tracking scaling policy because this is going to create CloudWatch alarms for us. | Còn bây giờ chúng ta sẽ thiết lập một **Target tracking scaling policy**, vì chính sách này sẽ tự động tạo luôn các CloudWatch Alarms cho chúng ta. |
| `00:02:58.100` | So here's the name Target Tracking Policy and it will track the average CPU utilization of a target value of 40, and then I will go ahead and create my policy. | Tôi giữ tên mặc định `Target Tracking Policy`, chọn chỉ số là **Average CPU utilization**, đặt giá trị mục tiêu (**Target value**) là **`40`** (`40%`), rồi nhấn **Create**. |
| `00:03:09.260` | So now what we're saying is that, hey, the goal of this ASG is to maintain the CPU utilization to 40. And in case you go over, then please add capacity units. | Điều chúng ta vừa quy định là: mục tiêu của ASG này là duy trì mức sử dụng CPU trung bình ở mức `40%`; nếu vượt quá mức này, hãy tự động thêm các EC2 instance mới. |
| `00:03:20.220` | So to see this in action, we need to change a few things. So right now the min and the desired is one which is good, but let's set the max capacity to be three. | Để thấy chính sách này hoạt động thực tế, chúng ta cần cập nhật lại Group size của ASG: giữ `Min = 1`, `Desired = 1`, nhưng tăng **`Max capacity` lên `3`** để ASG có không gian tăng từ 1 lên 2 rồi lên 3 instance. |
| `00:03:39.670` | And so the idea now is that we want the CPU utilization of my auto scaling group to be at a target value of 40. Right now the CPU utilization is going to be close to zero because my EC2 instance is not doing anything. | Hiện tại mức sử dụng CPU của EC2 instance gần như bằng `0%` vì máy chủ không phải xử lý tác vụ nặng nào cả. |
| `00:04:01.150` | So what I want to do is to go to my EC2 instance, and I'm going to stress it to make the CPU utilization skyrocket to 100%. So I'm going to connect to my EC2 instance using EC2 Instance Connect, | Vì vậy tôi sẽ kết nối vào EC2 instance đang chạy thông qua **EC2 Instance Connect**, và dùng công cụ tạo tải giả lập để đẩy mức sử dụng CPU vọt lên **100%**. |
| `00:04:12.850` | and then I'll Google "install stress Amazon Linux 2"... I'll copy the first command (`sudo amazon-linux-extras install epel -y`), and then I'll copy the second command (`sudo yum install stress -y`) to install stress. | Tôi chạy hai lệnh cài đặt gói `epel` và cài đặt công cụ `stress` trên Amazon Linux 2. |
| `00:04:36.543` | So stress is installed. And then I just run the command `stress -c 4` and this is going to make the CPU go to 100% by leveraging four CPU workers at a time. | Sau khi cài xong, tôi chạy lệnh `stress -c 4`. Lệnh này sẽ làm cho CPU của máy chủ tăng vọt lên **100%** ngay lập tức. |
| `00:04:53.940` | So what's going to happen is that in my monitoring of my ASG in here, what I want to happen is to see the CPU utilization go to something very, very high. And then in activities, I want to see a scaling action. | Bây giờ trong phần Monitoring của ASG, mức CPU sẽ tăng lên rất cao, và trong tab **Activity**, chúng ta sẽ chờ xem hành động tự động mở rộng (Scale Out) từ 1 lên 2 instance được kích hoạt. |
| `00:05:25.440` | So now I went into activity and under Activity history, it says that an alarm has been triggered and due to the target tracking policy, then the capacity went from one instance to two instances. | Chỉ sau vài phút, trong mục **Activity history** đã xuất hiện thông báo: một cảnh báo CloudWatch đã bị kích hoạt, và nhờ Target Tracking Policy, dung lượng (`Desired capacity`) đã tự động tăng từ **1 lên 2 instances**! |
| `00:05:37.870` | So if I go into instance management, as you can see, now I have two EC2 instances due to the scaling. And if I go into monitoring and look at the EC2 level monitoring, as we can see the CPU utilization went to a very high value and therefore scaling happened. | Chuyển sang tab **Instance management**, bạn thấy hiện có 2 EC2 instances. Trong biểu đồ **Monitoring**, đường biểu diễn CPU Utilization đã vọt lên mức rất cao và kích hoạt quá trình mở rộng. |
| `00:05:51.690` | So how do we know that the scaling happens? What I want to show you is the backend. So if we go into the CloudWatch service in here and go into Alarms. | Hãy cùng xem điều gì diễn ra ở hậu trường bằng cách mở dịch vụ **CloudWatch** và vào mục **Alarms** ở menu bên trái. |
| `00:06:14.830` | As you can see, two alarms are created directly by the target tracking policy. And one of them is called AlarmHigh, which is to scale out (add instances). And one of them is called AlarmLow, which is to scale in (less instances). | Bạn sẽ thấy có **2 cảnh báo (Alarms)** đã được Target Tracking Policy tự động tạo ra: một cái tên là **`AlarmHigh`** dùng để **Scale Out** (thêm máy), và một cái tên là **`AlarmLow`** dùng để **Scale In** (bớt máy). |
| `00:06:31.650` | And so this one (`AlarmHigh`) is looking at if the CPU utilization is more than 40% for 3 data points within 3 minutes, then go into the alarm state. | Cảnh báo `AlarmHigh` kiểm tra điều kiện: nếu `CPUUtilization > 40%` trong **3 điểm dữ liệu liên tiếp trong vòng 3 phút**, nó sẽ chuyển sang trạng thái `In alarm` và thêm máy ngay. |
| `00:06:40.810` | And this one (`AlarmLow`) is looking at if CPU utilization is less than 28% for 15 data points within 15 minutes, then scale in. | Trong khi đó, cảnh báo `AlarmLow` kiểm tra điều kiện: nếu `CPUUtilization < 28%` trong **15 điểm dữ liệu liên tiếp (15 phút)** thì mới thực hiện Scale In bớt máy. |
| `00:07:07.680` | And so now if I go here and I stop this command... I can go to my EC2 instances and reboot it. So this should make my CPU utilization go back to zero and this would trigger a scale in action within 15 minutes. | Bây giờ để dừng lệnh `stress`, tôi vào giao diện EC2 và nhấn **Reboot** instance đó để mức sử dụng CPU quay trở về `0%`, từ đó kích hoạt hành động Scale In sau 15 phút. |
| `00:07:59.360` | And actually just because I wasn't quick enough because the CPU still was high, then the desired capacity went from two to three. So as we can see yet another instance has been added. | Thậm chí vì trước khi tôi kịp reboot thì mức CPU trung bình vẫn còn cao hơn 40%, nên ASG đã tự động tăng tiếp `Desired capacity` từ **2 lên 3 instances**! |
| `00:08:19.690` | So now let's go back into activity and as you can see, more activities have been going on. So some instances have been terminated. Because the alarm went from the lower CPU and then the capacity was set from three to two and then one more time from two to one. | Sau khi đợi CPU hạ về 0% đủ 15 phút, quay lại tab **Activity history**, bạn có thể thấy cảnh báo `AlarmLow` đã kích hoạt và ASG tự động giảm dung lượng từ **3 xuống 2**, rồi từ **2 xuống 1 instance** bằng cách Terminate các instance dư thừa. |
| `00:09:04.240` | So that really shows the power of target tracking policies. When you're done, please make sure to delete this policy and you'll be good to go for the cleanup. That's it, I will see you in the next lecture. | Điều đó minh chứng rõ ràng sức mạnh tự động hóa của Target Tracking Policy. Khi thực hành xong, bạn hãy xóa chính sách này (và dọn dẹp ASG/ALB nếu không dùng nữa). Hẹn gặp lại bạn ở bài tiếp theo! |
