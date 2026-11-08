import os

iam_html_path = os.path.join(os.getcwd(), 'topics', 'aws_iam.html')

with open(iam_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# New enriched Cheat Sheet block with balanced lang-vi / lang-en
new_cheat_sheet = """<!-- 0. Tóm tắt nhanh dịch vụ (Service Cheat Sheet - 4 tiêu chí SAA-C03) -->
<div class="card full">
  <div class="ch">
    <div class="ci" style="background:var(--grb)">🧭</div>
    <div>
      <div class="ct">
        <span class="lang-vi">Tóm tắt nhanh dịch vụ — Section 4 (SAA-C03 Service Cheat Sheet)</span>
        <span class="lang-en">Quick Service Cheat Sheet — Section 4 (SAA-C03 4-Point Summary)</span>
      </div>
      <div class="cs">
        <span class="lang-vi">4 tiêu chí cốt lõi: Là gì (Xanh dương) · Dùng khi nào (Xanh lá) · Khác gì (Cam) · Bẫy thi (Đỏ)</span>
        <span class="lang-en">4 core exam criteria: Definition (Blue) · When to use (Green) · Differences (Amber) · Traps & Keywords (Red)</span>
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

  <div class="cols">
    <!-- COL 1: AWS IAM -->
    <div class="col">
      <div class="colt">
        <span class="lang-vi">👤 1. AWS IAM (Identity &amp; Access Management)</span>
        <span class="lang-en">👤 1. AWS IAM (Identity &amp; Access Management)</span>
      </div>

      <!-- 1. Là gì -->
      <div class="pi pi-def">
        <b>
          <span class="lang-vi">🔵 Là gì (1 câu)</span>
          <span class="lang-en">🔵 What is it (1 sentence)</span>
        </b>
        <span class="lang-vi">Dịch vụ toàn cầu (<b>Global Service</b>) quản lý danh tính người dùng và kiểm soát phân quyền truy cập an toàn vào các tài nguyên AWS.</span>
        <span class="lang-en">A <b>Global Service</b> that manages user identities and securely controls permissions to AWS resources.</span>
      </div>

      <!-- 2. Dùng khi nào -->
      <div class="pi pi-use">
        <b>
          <span class="lang-vi">🟢 Dùng khi nào (Use Case điển hình)</span>
          <span class="lang-en">🟢 When to use (Canonical Use Cases)</span>
        </b>
        <span class="lang-vi">
          <ul class="pts">
            <li>Cấp quyền theo nguyên tắc đặc quyền tối thiểu (<b>Least Privilege</b>) cho Users/Groups.</li>
            <li>Cho phép dịch vụ AWS (<code>EC2</code>, <code>Lambda</code>, <code>ECS</code>) gọi dịch vụ khác (<code>S3</code>, <code>DynamoDB</code>) mà <b>không lưu Access Keys trong code</b> bằng <b>IAM Roles</b>.</li>
            <li>Kiểm toán bảo mật định kỳ bằng <b>Credentials Report</b> (toàn account) và <b>Access Advisor</b> (từng user).</li>
          </ul>
        </span>
        <span class="lang-en">
          <ul class="pts">
            <li>Grant least privilege permissions to IAM Users and Groups.</li>
            <li>Allow AWS compute (<code>EC2</code>, <code>Lambda</code>, <code>ECS</code>) to securely call other services <b>without embedding static credentials</b> using <b>IAM Roles</b>.</li>
            <li>Audit security compliance using <b>Credentials Report</b> (account-wide) and <b>Access Advisor</b> (per entity).</li>
          </ul>
        </span>
      </div>

      <!-- 3. Khác gì -->
      <div class="pi pi-diff">
        <b>
          <span class="lang-vi">🟠 Khác gì dịch vụ gần giống</span>
          <span class="lang-en">🟠 How it differs from similar concepts</span>
        </b>
        <span class="lang-vi">
          <table class="diff-table">
            <thead>
              <tr><th>Khái niệm</th><th>Đặc điểm A</th><th>Đặc điểm B</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Policy vs Bucket Policy</b></td>
                <td><code>IAM Policy</code> gắn vào Identity (User/Group/Role)</td>
                <td><code>Bucket Policy</code> gắn trực tiếp vào S3 Bucket (Cross-account, Public)</td>
              </tr>
              <tr>
                <td><b>IAM Role vs Access Key</b></td>
                <td><code>IAM Role</code> cấp <b>Temporary Credentials</b> tự xoay qua STS</td>
                <td><code>Access Keys</code> là khóa dài hạn, tĩnh gắn với IAM User</td>
              </tr>
              <tr>
                <td><b>Report vs Access Advisor</b></td>
                <td><code>Credentials Report</code> xuất CSV toàn Account (MFA, password age)</td>
                <td><code>Access Advisor</code> xem dịch vụ truy cập lần cuối để cắt quyền dư</td>
              </tr>
            </tbody>
          </table>
        </span>
        <span class="lang-en">
          <table class="diff-table">
            <thead>
              <tr><th>Concept</th><th>Service A</th><th>Service B</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Policy vs Bucket Policy</b></td>
                <td><code>IAM Policy</code> attached to Identities</td>
                <td><code>Bucket Policy</code> attached directly to S3 (Cross-account, Public)</td>
              </tr>
              <tr>
                <td><b>IAM Role vs Access Key</b></td>
                <td><code>IAM Role</code> temporary short-lived STS credentials</td>
                <td><code>Access Keys</code> long-term static credentials on IAM User</td>
              </tr>
              <tr>
                <td><b>Report vs Access Advisor</b></td>
                <td><code>Credentials Report</code> account-wide CSV (MFA, key age)</td>
                <td><code>Access Advisor</code> last-accessed services to trim unused permissions</td>
              </tr>
            </tbody>
          </table>
        </span>
      </div>

      <!-- 4. Điểm hay bị hỏi -->
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa)</span>
          <span class="lang-en">🔴 Exam Hotspots (Limits, Defaults, Keywords)</span>
        </b>
        <span class="lang-vi">
          <ul class="pts">
            <li><b>Mặc định:</b> Mọi thao tác là <b>Implicit Deny</b> trừ khi có <code>Allow</code>; một <b>Explicit Deny</b> luôn phủ quyết mọi <code>Allow</code>.</li>
            <li><b>Giới hạn:</b> <code>IAM Groups</code> chỉ chứa Users, <b>không thể lồng Group trong Group</b> (No nested groups).</li>
          </ul>
          <div style="margin-top:8px;font-weight:600;font-size:12px;color:var(--mu);">TỪ KHÓA ĐỀ THI &rarr; ĐÁP ÁN:</div>
          <div class="kw-chip"><span>"without hardcoding credentials"</span> &rarr; <span class="kw-target">IAM Role</span></div>
          <div class="kw-chip"><span>"least operational overhead / rotate keys"</span> &rarr; <span class="kw-target">IAM Role</span></div>
          <div class="kw-chip"><span>"audit unused permissions / last accessed"</span> &rarr; <span class="kw-target">Access Advisor</span></div>
          <div class="kw-chip"><span>"simultaneous sign-in up to 5 accounts"</span> &rarr; <span class="kw-target">Multi-session support</span></div>
        </span>
        <span class="lang-en">
          <ul class="pts">
            <li><b>Defaults:</b> All actions default to <b>Implicit Deny</b>; an <b>Explicit Deny</b> always overrides any <code>Allow</code>.</li>
            <li><b>Limits:</b> <code>IAM Groups</code> only contain Users, <b>cannot contain nested groups</b>.</li>
          </ul>
          <div style="margin-top:8px;font-weight:600;font-size:12px;color:var(--mu);">EXAM KEYWORDS &rarr; ANSWER:</div>
          <div class="kw-chip"><span>"without hardcoding credentials"</span> &rarr; <span class="kw-target">IAM Role</span></div>
          <div class="kw-chip"><span>"least operational overhead / rotate keys"</span> &rarr; <span class="kw-target">IAM Role</span></div>
          <div class="kw-chip"><span>"audit unused permissions / last accessed"</span> &rarr; <span class="kw-target">Access Advisor</span></div>
          <div class="kw-chip"><span>"simultaneous sign-in up to 5 accounts"</span> &rarr; <span class="kw-target">Multi-session support</span></div>
        </span>
      </div>
    </div>

    <!-- COL 2: CLI, SDK & CLOUDSHELL -->
    <div class="col">
      <div class="colt">
        <span class="lang-vi">💻 2. AWS CLI, AWS SDK &amp; AWS CloudShell</span>
        <span class="lang-en">💻 2. AWS CLI, AWS SDK &amp; AWS CloudShell</span>
      </div>

      <!-- 1. Là gì -->
      <div class="pi pi-def">
        <b>
          <span class="lang-vi">🔵 Là gì (1 câu)</span>
          <span class="lang-en">🔵 What is it (1 sentence)</span>
        </b>
        <span class="lang-vi">Bộ công cụ dòng lệnh (<code>AWS CLI</code>), thư viện lập trình (<code>AWS SDK</code>) và terminal trực tiếp trên trình duyệt (<code>AWS CloudShell</code>) giúp quản trị và gọi API của AWS.</span>
        <span class="lang-en">Command-line tools (<code>AWS CLI</code>), programming libraries (<code>AWS SDK</code>), and web terminal (<code>AWS CloudShell</code>) to manage and invoke AWS APIs.</span>
      </div>

      <!-- 2. Dùng khi nào -->
      <div class="pi pi-use">
        <b>
          <span class="lang-vi">🟢 Dùng khi nào (Use Case điển hình)</span>
          <span class="lang-en">🟢 When to use (Canonical Use Cases)</span>
        </b>
        <span class="lang-vi">
          <ul class="pts">
            <li>Tự động hóa quản trị tài nguyên AWS bằng bash/powershell script (<code>AWS CLI</code>).</li>
            <li>Gọi trực tiếp các API AWS bên trong code Python, Java, Node.js, Go (<code>AWS SDK</code>).</li>
            <li>Chạy lệnh CLI ngay trên trình duyệt mà không cần cài đặt phần mềm hay cấu hình khóa truy cập (<code>AWS CloudShell</code>).</li>
          </ul>
        </span>
        <span class="lang-en">
          <ul class="pts">
            <li>Automate cloud infrastructure provisioning and management via scripts (<code>AWS CLI</code>).</li>
            <li>Programmatically interact with AWS services inside application source code (<code>AWS SDK</code>).</li>
            <li>Run commands inside browser without installing tooling or configuring access keys (<code>AWS CloudShell</code>).</li>
          </ul>
        </span>
      </div>

      <!-- 3. Khác gì -->
      <div class="pi pi-diff">
        <b>
          <span class="lang-vi">🟠 Khác gì dịch vụ gần giống</span>
          <span class="lang-en">🟠 How it differs from similar concepts</span>
        </b>
        <span class="lang-vi">
          <table class="diff-table">
            <thead>
              <tr><th>Tiêu chí</th><th>AWS CLI cá nhân</th><th>AWS CloudShell</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Cài đặt</b></td>
                <td>Tự cài trên máy cục bộ, quản lý phiên bản</td>
                <td>Có sẵn trên Console trình duyệt, zero-setup</td>
              </tr>
              <tr>
                <td><b>Xác thực</b></td>
                <td>Chạy <code>aws configure</code> nhập Access Key tĩnh</td>
                <td>Tự kế thừa phiên đăng nhập Console của User</td>
              </tr>
              <tr>
                <td><b>Lưu trữ</b></td>
                <td>Ổ cứng máy cá nhân</td>
                <td>Miễn phí <b>1 GB bộ nhớ bền vững (<code>$HOME</code>)</b>/Region</td>
              </tr>
            </tbody>
          </table>
        </span>
        <span class="lang-en">
          <table class="diff-table">
            <thead>
              <tr><th>Criteria</th><th>Local AWS CLI</th><th>AWS CloudShell</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Setup</b></td>
                <td>Manual local installation &amp; version maintenance</td>
                <td>Pre-installed in browser Console, zero setup</td>
              </tr>
              <tr>
                <td><b>Auth</b></td>
                <td>Manual <code>aws configure</code> with static Access Keys</td>
                <td>Inherits logged-in Console session automatically</td>
              </tr>
              <tr>
                <td><b>Storage</b></td>
                <td>Local disk space</td>
                <td>Free <b>1 GB persistent storage (<code>$HOME</code>)</b> per Region</td>
              </tr>
            </tbody>
          </table>
        </span>
      </div>

      <!-- 4. Điểm hay bị hỏi -->
      <div class="pi pi-exam">
        <b>
          <span class="lang-vi">🔴 Điểm hay bị hỏi (Giới hạn, Mặc định, Từ khóa)</span>
          <span class="lang-en">🔴 Exam Hotspots (Limits, Defaults, Keywords)</span>
        </b>
        <span class="lang-vi">
          <ul class="pts">
            <li><b>Mặc định:</b> Nếu không khai báo Region trong AWS SDK, một số SDK mặc định chọn <b><code>us-east-1</code></b>.</li>
            <li><b>Bẫy bảo mật:</b> Trên máy chủ EC2, <b>tuyệt đối KHÔNG chạy <code>aws configure</code></b> lưu static key &mdash; bắt buộc gắn <b>IAM Role</b> để EC2 tự nhận STS Temporary Credentials từ IMDS.</li>
          </ul>
          <div style="margin-top:8px;font-weight:600;font-size:12px;color:var(--mu);">TỪ KHÓA ĐỀ THI &rarr; ĐÁP ÁN:</div>
          <div class="kw-chip"><span>"browser-based shell with 1 GB persistent storage in $HOME"</span> &rarr; <span class="kw-target">AWS CloudShell</span></div>
          <div class="kw-chip"><span>"EC2 needs to access S3 / DynamoDB securely"</span> &rarr; <span class="kw-target">Attach IAM Role to EC2</span></div>
          <div class="kw-chip"><span>"CLI pagination control"</span> &rarr; <span class="kw-target">--max-items, --page-size</span></div>
        </span>
        <span class="lang-en">
          <ul class="pts">
            <li><b>Defaults:</b> If no Region is set in AWS SDK, some SDKs default to <b><code>us-east-1</code></b>.</li>
            <li><b>Security Trap:</b> Inside an EC2 instance, <b>NEVER run <code>aws configure</code></b> with static user keys &mdash; always attach an <b>IAM Role</b> so it fetches short-lived STS tokens via IMDS.</li>
          </ul>
          <div style="margin-top:8px;font-weight:600;font-size:12px;color:var(--mu);">EXAM KEYWORDS &rarr; ANSWER:</div>
          <div class="kw-chip"><span>"browser-based shell with 1 GB persistent storage in $HOME"</span> &rarr; <span class="kw-target">AWS CloudShell</span></div>
          <div class="kw-chip"><span>"EC2 needs to access S3 / DynamoDB securely"</span> &rarr; <span class="kw-target">Attach IAM Role to EC2</span></div>
          <div class="kw-chip"><span>"CLI pagination control"</span> &rarr; <span class="kw-target">--max-items, --page-size</span></div>
        </span>
      </div>
    </div>
  </div>
</div>"""

# Find and replace the old cheat sheet block
start_marker = "<!-- 0. Tóm tắt nhanh dịch vụ (Service Cheat Sheet - 4 tiêu chí SAA-C03) -->"
end_marker = "<!-- 1. Identities -->"

if start_marker in content and end_marker in content:
    idx_start = content.index(start_marker)
    idx_end = content.index(end_marker)
    new_content = content[:idx_start] + new_cheat_sheet + "\n\n" + content[idx_end:]
    with open(iam_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: aws_iam.html cheat sheet updated.")
else:
    print("ERROR: Markers not found in aws_iam.html")
