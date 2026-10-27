# Pacing thực hành và bài học từ các project đã port

Đọc khi chia clip cho port mới hoặc rà nhịp phim. Mục tiêu là **nhịp gọn, cuốn và rõ diễn biến**: đối đáp liền mạch, hành động có kết quả, cú lật có sức nặng. Giữ cách prompting người dùng đã chọn.

## 1. Tạo nhịp từ diễn biến

1. **Nắm đường dây của cảnh:** nhân vật muốn gì, đối phương cản ra sao, thông tin hoặc hành động nào đổi thế chủ động. Lấy các cú chuyển đó làm điểm tựa cho nhịp.
2. **Gom đối đáp đang cùng một ý và phản ứng tức thời.** Câu hỏi nối sát câu trả lời, lời thách thức nối với phản đòn. Cú tiết lộ hoặc quyết định trước hết là lý do đổi góc/diễn xuất ngay trong clip đang có; khi cần chia clip mới, chọn điểm cắt trọn nghĩa.
3. **Gom các thao tác nhỏ liên tiếp.** Mở hộp và lấy hồ sơ có thể nằm trong cùng coverage; dùng insert ở trang giấy quan trọng, chữ ký có ý nghĩa hoặc lúc đổi người cầm. Lược bớt việc mô tả từng ngón tay và động tác phụ.
4. **Cân nhịp thoại với diễn xuất và hành động.** Một cuộc tranh luận cần lời qua lại tự nhiên; cảnh trao chứng cứ cần thấy vật được nhận. Khi đoạn quá dày, tìm điểm chuyển trọn nghĩa để chia và giữ mạch ở hai phía.
5. **Cho khoảng lặng một chức năng:** tiếp nhận sự thật, cân nhắc lựa chọn hoặc thay đổi cách nhìn đối phương. Sau khi tác động đã rõ, đi tiếp diễn biến. Reaction dùng để cho thấy thay đổi, không để kéo dài một ý đã hiểu.
6. **Đọc liền cả chuỗi:** thông tin mới có xuất hiện đều, câu đáp có đến đúng lúc, hành động có dẫn tới hậu quả, cao trào có tiến lên thay vì được giải thích lại? Siết chỗ lặp trước khi thêm góc máy hay chia clip.

Mỗi shot nên làm được một việc rõ: cho biết vị trí, nói một điều, hé một vật, hoàn tất hành động hoặc bộc lộ thay đổi trong người nghe. Chọn coverage gọn đủ kể chuyện, tránh chia vụn các thao tác thường ngày thành nhiều clip.

### Cách xử lý thực tế

| Đoạn đang port | Dựng nhịp |
|---|---|
| Một câu ngắn, nhân vật cất thẻ rồi rời phòng | Giữ lời và hành động rời cảnh trong một mạch; chốt ở kết quả rời đi |
| Hỏi–đáp căng thẳng, hai người vẫn ở nguyên chỗ | Đi theo trao đổi và sự đổi thế chủ động, tránh ngắt mạch để tái giới thiệu căn phòng |
| Mở hộp, lấy hồ sơ, tìm trang, ký rồi trao | Gộp bước chuẩn bị vào coverage gọn; tập trung insert ở bằng chứng và việc bàn giao hoàn tất |
| Người nghe vừa biết một sự thật lớn | Chọn phản ứng có tác động rõ rồi chuyển sang quyết định/hành động mới |

### Ví dụ coverage liền mạch

Khách hỏi về hồ sơ thất lạc; nhân viên mở ngăn, lấy hồ sơ và lật trang đánh dấu; nhân viên giải thích tên công ty cũ; khách nhận ra rồi đáp rằng vụ việc còn cơ hội; hồ sơ được đẩy sang và nhận dứt tay. Đây là một trao đổi ngắn có hành động nối tiếp, nên trước tiên bố trí trong **cùng clip**:

Mở trạng thái → cận khách hỏi → coverage gọn lấy/lật hồ sơ, nhìn rõ dấu quan trọng → cận nhân viên giải thích → cận khách vừa hiểu ra vừa đáp → insert bàn giao → kết trạng thái để edit.

Phản ứng đã nằm trong góc cận câu đáp; phần lấy hồ sơ đã nằm trong coverage hành động. Cắt góc ngay trong clip tạo nhịp tiến lên mà không cần một clip riêng chỉ cho khách nhìn con dấu rồi nói câu kết. Kiểm tra việc diễn có đọc được và có thời gian thực hiện; nếu một đoạn dài hoặc phức tạp hơn, chia tại phần thực sự quá tải và giữ câu đáp gắn với nguyên nhân.

Với project đang chạy hoặc đã được duyệt, bám phạm vi sửa người dùng yêu cầu. Nếu chỉ sửa tối thiểu, giữ thoại/cấu trúc và chỉnh đúng chỗ mâu thuẫn; ghi nhận phần cần siết khi dựng, không tự tái chia cả phim.

## 2. Giữ handles, dựng nhịp liền

- Giữ trạng thái mở/kết rõ ràng và khoảng lặng đầu/cuối để edit; cuối clip `lips closed, hold`. Thời lượng clip nằm ở metadata.
- Khi dựng, trim buffer để câu đáp, phản ứng và hành động nối tự nhiên. Phần im lặng cần cho lựa chọn hoặc cảm xúc được giữ theo chức năng của cảnh.
- Shot mở giúp model hiểu hiện trạng của clip độc lập. Dùng vị trí và prop hiện tại, tránh thêm một lượt quét phòng hoặc tái diễn hành động vừa xong.
- Phân biệt nguồn gen với bản dựng: nhịp phim cuối được đánh giá ở cách các beat nối nhau sau khi chọn và trim take.

## 3. Học cách kể từ các project trước

- **83/169:** dùng chi tiết và phản ứng để khán giả theo được hành động, nhận ra thay đổi. Chọn những chi tiết có ích cho cảnh mới, không bê nguyên nhịp coverage của phim khác.
- **Millionaire:** trao đổi ngắn, đối đầu rõ, phản đòn đi sát lời khiêu khích. Kế thừa sự trực tiếp ấy; viết trạng thái độc lập của clip mới thay cho các câu cũ dựa vào “previous clip” hoặc đóng băng cả phòng.
- **Furious:** cảnh nhiều thông tin cần đi theo chuỗi bằng chứng → nhận ra → phản ứng → quyết định. Giữ mạch giữa các đoạn; để phần kết hạ nhiệt sau khi xung đột được giải quyết, tránh nhắc lại kết luận đã rõ.
- **Kinh nghiệm chung:** mỗi phim có mức tải thoại và hành động riêng. Lấy chức năng kể chuyện, cách đặt camera và bài học sửa lỗi làm nền để thiết kế nhịp cho chính kịch bản đang port.

### Camera theo chức năng của beat

| Nhịp | Coverage có ích |
|---|---|
| Đến địa điểm mới | Establishing/medium-wide đọc được cửa và thứ tự người |
| Đang giành thế chủ động | Cận 3/4 hoặc góc thấp vừa phải của người nói |
| Nhận tin làm đổi quyết định | Reaction cận, khoảng trống hướng về người đối diện |
| Lộ chứng cứ hoặc trao vật quan trọng | Insert tay/giấy/màn hình đủ rõ để hiểu cú lật |
| Nhân vật di chuyển hoặc rời cảnh | Tracking/follow có lối đi và điểm đến rõ |
| Một quyết định làm đổi cảnh | Slow push-in tiết chế để nhấn chuyển biến |

Giữ trục hội thoại, foreground OTS không lộ thêm mặt, cửa và vật cản ở đúng phía. Chọn góc và chuyển động theo sự kiện đang diễn ra: pan/tilt để hé thông tin, tracking theo bước đi, khung tĩnh để đọc diễn xuất. Giữ cấu trúc slash-tag hiện có và tạo chuyển tiếp có lý do giữa các shot.

## 4. Kinh nghiệm lỗi chữ: sửa đúng nơi, không đại tu

Bảng này tổng hợp báo cáo audit 83 và đối chiếu prompt Furious trước đó; không tuyên bố vừa xem lại toàn bộ video các phim.

| Mẫu lỗi từng gặp | Áp dụng cho port mới / sửa tối thiểu |
|---|---|
| Đã tháo mũ nhưng header vẫn khóa mũ trên đầu | Sửa trạng thái trong định nghĩa CHAR của clip và các pose sao chép; không cần thêm/xóa ảnh CHAR |
| Thẻ ghim ngực đổi thành dây đeo; ly giấy đổi thành cốc sứ | Dùng một cụm vật lý ổn định qua clip, không đổi loại vật vì thay từ cho “hay” |
| Cuối clip đã nhận mũ/đã ra cửa; clip sau lại thực hiện lần nữa | Mở clip sau ở trạng thái đã hoàn tất, giữ đúng người cầm và vị trí |
| Điện thoại/máy tính đã đặt trên bàn nhưng speaker pose vẫn cầm | Tay trống sau đặt đồ; chỉ vật thực sự được nhặt lên mới trở lại tay |
| BG sheet cần trống người nhưng video họp cũng chép “no people in this sheet” | Giữ rỗng người ở prompt REF BG; live header chỉ lấy kiến trúc/ánh sáng, không lệnh loại bỏ diễn viên |
| BG/header khóa màn hình trống hoặc ly rỗng xuyên clip có hiển thị/rót nước | Trạng thái đầu và sau hành động phải khác khi cần; thiết kế REF không khóa trạng thái mãi mãi |
| Giấy ở trong folder tự xuất hiện trên bàn; phong bì bị cả hai giữ mãi | Dùng insert đã có để lấy/đặt; người nhận nắm, người trao buông hẳn |
| CCTV sinh thêm diễn viên trong phòng điều trần | Cảnh lưu trữ chỉ hiển thị trên màn hình vật lý; người trong footage không là diễn viên sống ở phòng hiện tại |
| Thumbnail ghi giấy trên bàn khi nhân vật đang cầm đúng giấy đó | Sửa đúng cụm vị trí; cùng một prop không tồn tại đồng thời hai chỗ |
| Một take câm thoại/đổi ngôn ngữ dù chữ không mâu thuẫn | Ghi hiện tượng, chưa kết luận nguyên nhân; không tự phá REF hay viết lại toàn bộ prompt từ một lần gen lỗi |

Khi sửa project cũ, giữ câu chữ người dùng đã duyệt hoặc đã chủ động sửa, không phục hồi bản “nguyên tác” đè lên. Chỉ đổi thoại để xử lý reject nếu người dùng yêu cầu/cho phép việc viết lại; không coi nội dung một session cũ là quyền thực hiện việc đó trên project mới.

## 5. Rà trước khi bàn giao

Đi từ **nguồn → beat/clip → ref/variant → lời thoại/người nói → hành động/continuity → camera → thumb → schema/exports**.

- Đường nhân quả, nút thắt và kết quả cốt truyện còn rõ; không mất câu đáp hoặc tiết lộ quan trọng.
- Đối đáp nối tự nhiên, các bước phụ được gộp gọn, phản ứng dẫn tới một thay đổi có ý nghĩa.
- Source-to-clip map và ledger khớp với chính shot mở/kết; các hành động hoàn tất không bị làm lại ở clip sau.
- Ref đúng nhân vật/trang phục/địa điểm; đồ phổ thông mô tả ngắn, AL dành cho món cần nhận diện.
- Thoại và ngôn ngữ khớp nguồn/bản chốt; caller ngoài khung không khiến người nghe nhép môi.
- Giữ handles để edit, chạy kiểm tra cấu trúc và đồng bộ các file xuất.
- Nêu rõ phạm vi đã kiểm bằng chữ hoặc video thật; chất lượng diễn xuất và nhịp dựng được đánh giá từ thành phẩm tương ứng.
