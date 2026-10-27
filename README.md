# SF Board Port — Codex skill

Port kịch bản thành thư mục **`.project` có `sf-board.json` đúng cấu trúc SF Board**, giữ cách prompting Seedance single-line, có ref CHAR/BG/AL, thumbnail prompt, pacing và continuity. Mặc định **chỉ viết prompt, không tạo ảnh/video**.

Skill tự chứa schema, ví dụ giả lập và script kiểm tra; máy khác không cần kịch bản Furious/169/83/Millionaire hay lịch sử chat trên máy gốc. Các project đó là kinh nghiệm hình thành workflow, không được upload kèm repo.

## Cài trên máy khác

Cần **Python 3.10+**. Cách dùng Terminal cần thêm Git và GitHub CLI (`gh`). Repo riêng tư: đăng nhập tài khoản có quyền đọc repo.

```sh
gh auth login
gh auth setup-git
gh repo clone Ductoii/sf-board-port-skill
cd sf-board-port-skill
python3 install.py
```

Windows có thể dùng `py -3` thay `python3`. Installer dùng Python chuẩn, không tải package, mặc định cài vào `~/.agents/skills/sf-board-port`. Nếu bản Codex của bạn dùng thư mục skills riêng, chỉ định **folder mẹ**:

```sh
python3 install.py --dest ~/.codex/skills
```

Chỉ cài vào **một** nơi để tránh hiện skill trùng. Codex nhận skill mới tự động; nếu chưa xuất hiện thì khởi động lại. Vị trí `~/.agents/skills` và cách nhận skill được đối chiếu với [tài liệu Codex chính thức](https://learn.chatgpt.com/docs/build-skills).

Hoặc dán vào Codex trên máy đã có quyền GitHub:

```text
$skill-installer cài skill từ https://github.com/Ductoii/sf-board-port-skill/tree/main/skills/sf-board-port
```

Nếu installer không đọc được repo private, dùng cách `gh repo clone` ở trên để cấp quyền Git qua tài khoản của bạn; không ghi token vào skill hay file README.

## Gọi skill

```text
$sf-board-port port kịch bản đính kèm thành sf-board.json trong một folder .project,
đặt vào thư mục SF Board của máy này. Mỗi video 30s; chỉ tạo prompt ref và thumb,
không tạo ảnh. Giữ nguyên thoại và cấu trúc prompting, sửa tối thiểu.
```

Có thể chỉ định thêm project mẫu trên máy đích. Nếu không có, skill dùng ví dụ đi kèm. Với project đang làm:

```text
$sf-board-port rà continuity của project này, đặc biệt trạng thái đồ vật và tay cầm.
Giữ nguyên cấu trúc prompt, clip, thoại và khoảng lặng mở/kết. Chỉ sửa lỗi chữ cần thiết.
```

Các nguyên tắc chính:

- `.project` là folder; ref ở `scenes[0].sfs`, clip ở `scenes[].shots`.
- 30s nằm ở `dur`, không nhét giây kỹ thuật vào prompt; clip count theo beat và tải thoại, không ép mọi phim còn 60–70 video.
- Giữ khoảng lặng đầu/cuối để edit. Mỗi clip tự mô tả trạng thái, không dùng “giống video trước”.
- CHAR sheet ngang bốn cột, cận mặt 30%; BG bốn góc trống người; costume variant bám CHAR gốc.
- Khăn/ly/đĩa phổ thông mô tả ngắn. AL dành cho thiết kế khó giữ đồng nhất hoặc bằng chứng có nội dung quan trọng; xuất hiện ≥4 video không tự động đủ điều kiện tạo AL.
- Góc máy có chủ đích, chủ yếu tĩnh; tracking/push-in phục vụ hành động/cao trào. Không dùng nhãn “cinematic” thay cho thiết kế shot.
- THUMB là khoảnh khắc kể chuyện, không poster; text hậu kỳ ghi ở notes.
- Không tự tạo media, ghi đè media người dùng đã chọn hoặc can thiệp hàng chờ/tool đang chạy.

## Kiểm tra và xuất file

Chạy trong repo clone; đường dẫn project do Codex tạo trên máy đích:

```sh
python3 skills/sf-board-port/scripts/project.py "/path/to/Title.project"
python3 skills/sf-board-port/scripts/project.py "/path/to/Title.project" --export
```

`--export` chỉ chạy khi JSON qua kiểm tra, tạo `PROMPT_VIDEO.txt`, `BANGTRA.tsv`, `REF/prompts.json` và từng `<ID>.prompt.txt`. Export cũ bị thay có backup trong `.snapshots/`. Không xóa ảnh, không reset picked/status và không sửa prompt trong board. Không tự sửa usedBy: Codex phải sửa bản JSON chính rồi kiểm tra lại.

Bộ kiểm tra bắt lỗi schema, ID/ref/dependency/usedBy, VO ↔ text, single-line, shot numbering, khoảng lặng, giây kỹ thuật, chỉ dẫn nhớ clip trước và ledger continuity. **Không chứng minh** diễn xuất, độ điện ảnh, coverage ngữ nghĩa hoặc video tạo ra đã đúng; các phần đó cần đọc đối chiếu hoặc xem video thật.

## Cập nhật

```sh
cd sf-board-port-skill
git pull --ff-only
python3 install.py
```

Nếu lần đầu dùng `--dest`, dùng lại đúng tùy chọn đó khi cập nhật. Installer bỏ qua bản giống hệt; bản đang cài bị thay được lưu ở `~/.agents/skill-backups/` (hoặc folder tương ứng cạnh thư mục skills tùy chỉnh), ngoài đường quét skill để tránh hiện trùng. Muốn gỡ chỉ xóa folder `sf-board-port` trong nơi đã cài; không cần sửa cấu hình Codex.

## Tự kiểm tra bộ skill

```sh
python3 -m unittest discover -s tests -v
python3 skills/sf-board-port/scripts/project.py skills/sf-board-port/assets/example.project
```

Cấu trúc repo: `skills/sf-board-port/SKILL.md` là entrypoint, `references/` giữ quy tắc chi tiết, `assets/example.project/` là dữ liệu giả lập, `scripts/project.py` kiểm tra/xuất project, `install.py` cài skill. Không cần API key, connector hay plugin để port file local.
