# Pacing thực hành và bài học từ các project đã port

Đọc trước khi chia clip cho một port mới hoặc khi người dùng hỏi về pacing. Đây là kinh nghiệm của workflow này, không phải công thức bảo đảm model tạo đúng video. Các ví dụ dưới đây diễn giải lỗi chữ và lựa chọn dựng; không thay cho việc xem video thành phẩm.

## 1. Chọn điểm cắt clip như thế nào?

**Mặc định là 30s ở `dur`, không có mặc định/mục tiêu/trần 65 từ thoại mỗi clip.** Cũng không có quy tắc mọi kịch bản phải ra 72 clip. Số từ là tín hiệu để rà tải, không phải máy chia kịch bản. Nếu người dùng đặt một ngân sách thoại cụ thể cho lần port đó thì áp dụng yêu cầu ấy riêng, không biến nó thành mặc định cho các phim sau.

Làm theo chuỗi quyết định:

1. **Đánh dấu thay đổi của câu chuyện:** ai muốn gì trong cảnh; thông tin/hành động nào làm người khác đổi quyết định hoặc thế chủ động. Giữ đường nhân quả, thứ tự tiết lộ và câu đáp cần thiết.
2. **Gom trao đổi có cùng ý và cùng trạng thái sân khấu.** Một câu hỏi và câu trả lời thường nên ở cùng clip nếu còn đủ chỗ cho diễn xuất/hành động. Không cắt một câu thoại dở dang để đạt số từ.
3. **Kiểm tra tổng tải:** độ dài và nhịp câu thoại, số lượt đổi người nói, mức khó của hành động tay, khoảng nhìn phản ứng và handles. Clip chỉ tranh luận khác clip phải mở hộp, lấy giấy, đọc, ký rồi trao. Không đánh giá tải chỉ bằng số từ hay số shot.
4. **Nếu quá tải, tách tại nhịp trọn nghĩa:** xong một lượt thoại, lộ bằng chứng, hoàn tất thao tác, đổi mục tiêu, chuyển địa điểm/thời gian. Mỗi phần có trạng thái mở/kết mô tả được. Chia lại các beat lân cận thay vì đọc nhanh bất thường, lược mất thoại hoặc giấu thao tác sau một góc cận mặt.
5. **Nếu quá loãng, xác định vì sao:** im lặng để tiếp nhận mất mát/quyết định là nội dung; im lặng do chia một thao tác nhỏ thành một clip riêng là dấu hiệu có thể gộp khi đang tạo port mới. Một clip ít thoại vẫn có thể cần thiết vì hành động hoặc cảm xúc.
6. **Đọc lại cả chuỗi, không từng clip rời:** lời đe dọa có câu đáp đúng lúc không, bằng chứng có được thấy trước kết luận không, cao trào có bị giải thích lại nhiều lần không, kết phim có đủ hạ nhiệt không?

Ở một **project đang chạy/đã được duyệt**, việc đổi số clip hay thoại là thay đổi cấu trúc. Nếu yêu cầu chỉ sửa tối thiểu thì giữ chúng, sửa trạng thái sai bằng vài từ và báo phần pacing cần lưu ý khi dựng. Không tự tái chia cả project.

### Ba quyết định mẫu

| Đoạn đang port | Quyết định hợp lý | Điều không được suy ra máy móc |
|---|---|---|
| Một câu ngắn, sau đó nhân vật cất thẻ, đóng cửa và rời đi | Giữ thoại cùng chuỗi rời cảnh nếu tải vừa; mô tả được thẻ ở đâu và ai đã ra khỏi phòng | Ít từ không có nghĩa cần kéo thêm một clip hoặc thêm thoại |
| Một lượt hỏi–đáp khá dài, hai người đứng yên | Ưu tiên giữ mạch đối đáp; nếu tổng tải quá dày, tách sau một lượt có ý nghĩa hoàn chỉnh | Vượt một con số từ tùy ý không tự động buộc cắt |
| Mở hộp, lấy hồ sơ, tìm trang, ký, gấp, trao | Bố trí insert cho các bước quyết định và hoàn tất bàn giao; tách nếu không còn chỗ để thấy rõ | Ít thoại không có nghĩa mọi động tác chắc chắn vừa một clip |

Một clip không cần “đủ 6–10 shot” để hợp lệ. Một câu nói có thể cần một cận riêng; một động tác có thể cần insert; phản ứng phải có thông tin mới. Không thêm reaction trống chỉ để đủ shot.

## 2. Handles để edit khác nhịp phim cuối

- Giữ khoảng lặng mở/kết đã yêu cầu, mô tả đúng trạng thái tại chỗ; cuối clip `lips closed, hold`.
- Khi dựng, có thể trim các buffer rồi nối đối đáp/phản ứng. Vì vậy hai handle im lặng ở ranh giới **không bắt buộc** thành hai khoảng dừng dài trong bản phim cuối.
- Không xóa handle trong prompt để chữa một nhận xét “111 clip hơi chậm”. Không viết giây vào prompt để điều khiển handle; thời lượng khai báo ở metadata.
- Phân biệt tái lập vị trí để model hiểu clip độc lập với **lặp lại sự kiện**: đứng ở cửa từ đầu không có nghĩa clip sau lại bước vào từ ngoài; đồ đã trao không được trao lần hai.
- `111 × 30 = 3330s` là tổng nguồn gen nếu lấy đủ, không phải cam kết phim dựng dài 55 phút 30 giây. Chỉ báo runtime cuối khi có bản dựng thực tế.

## 3. Các project mẫu cho thấy gì?

Số liệu đo từ `shots[].text` trong JSON tại lần đối chiếu 27/10/2026, bỏ nhãn vai và đếm từ theo khoảng trắng; đây là **quan sát**, không phải định mức mới. Bản chỉnh sau này hoặc cách đếm khác có thể lệch nhẹ.

| Project | Clip | Từ thoại | Trung bình/clip | Min–max | Shot/clip quan sát |
|---|---:|---:|---:|---:|---:|
| 83 | 72 | 1201 | 16,7 | 0–35 | 7–11 |
| Millionaire | 72 | 1112 | 15,4 | 0–33 | 1–5 |
| 169 | 72 | 1641 | 22,8 | 5–39 | 8–10 |
| Furious | 111 | 4524 | 40,8 | 7–54 | 3–10 |

- 83/169: cách bao phủ hành động, chi tiết, phản ứng có nhiều shot; không có nghĩa phải bê mọi insert sang phim khác.
- Millionaire: một số beat dùng ít shot và thoại ngắn. Lấy sự rõ ràng của trao đổi, không lấy 72 làm chỉ tiêu; cũng không sao chép các câu cũ như “opens on the exact final frame of the previous clip” hoặc “everyone holding still”.
- Furious: nhiều thoại hơn đáng kể. 111 clip tự nó không chứng minh chậm; cũng không dùng 40,8 hay 54 làm mục tiêu/trần cho phim sau. Số lần đổi người nói và thao tác quan trọng hơn một phép chia tổng số từ.
- Mẫu có điểm mạnh lẫn lỗi lịch sử. Kế thừa **ngôn ngữ prompting và bài học đã sửa**, không copy toàn bộ câu chữ hay mặc định coi mọi prompt mẫu đều chuẩn.

## 4. Chọn góc máy theo chức năng của beat

| Nhịp | Góc có ích | Lý do |
|---|---|---|
| Bắt đầu địa điểm mới | Establishing/medium-wide, đọc được cửa và thứ tự người | Định vị trước đối thoại |
| Người đang ép đối phương | Cận 3/4 hoặc góc thấp vừa phải, đúng người nói | Làm rõ quyền chủ động |
| Người nghe nhận tin làm đổi quyết định | Reaction cận, khoảng trống về phía người đối diện | Cho thấy tác động thay vì lặp lại lời |
| Chứng cứ/trao đồ quyết định | Insert tay/giấy/màn hình | Khán giả thấy nguyên nhân của cú lật |
| Nhân vật đổi vị trí/rời đi | Tracking/follow có lối đi rõ | Theo hành động thực sự |
| Lời chốt/quyết định lớn | Một slow push-in tiết chế, tối đa một lần/clip | Nhấn cú chuyển, không mặc định câu nào cũng đẩy |

Giữ trục hội thoại, foreground OTS không lộ thêm mặt, cửa/vật cản không tự đổi phía. Đa dạng góc máy phải có lý do: không xoay vòng 50/65/75/85mm chỉ theo số thứ tự câu thoại, không ép tỷ lệ chuyển động máy. Pan/tilt chỉ khi cần bộc lộ một thông tin, vẫn dùng cấu trúc slash-tag đang áp dụng.

Trong lần kiểm tra Furious bằng chữ, chỉ có 6 tracking và 2 push-in trên 718 shot, dù có nhiều góc tĩnh đa dạng. Điều rút ra là phải **đếm chuyển động thực sự và mô tả đúng mức độ**, không được quảng cáo “lia máy phong phú” dựa vào chữ cinematic/ARRI/35mm. Đây không phải tỷ lệ mẫu bắt mọi phim phải theo.

## 5. Kinh nghiệm lỗi chữ: sửa đúng nơi, không đại tu

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

## 6. Trước khi bàn giao

Kiểm theo thứ tự **nguồn → beat/clip → ref/variant → lời thoại/người nói → thao tác/continuity → camera → thumb → schema/exports**.

- Các nút thắt và kết quả cốt truyện đã được giữ, không chỉ đủ tổng số từ.
- Source-to-clip map chỉ rõ sự kiện nào được đưa vào clip; ledger khớp chính shot mở/kết, không chỉ tự khớp với nhau.
- Không ép 65 từ, 72 clip hay một số shot cố định; giữ nguyên handles được yêu cầu.
- Ref đúng nhân vật/trang phục/địa điểm đang dùng; đồ phổ thông mô tả ngắn, AL dành cho món cần nhận diện.
- Mọi thoại và ngôn ngữ đã đối chiếu với nguồn/bản chốt; lời qua điện thoại ngoài khung không bắt người nghe nhép môi.
- Chạy bộ kiểm tra cấu trúc và xuất lại các file liên quan; đọc lại các trường trạng thái do copy-paste dễ sót.
- Nêu rõ mới kiểm prompt hay đã xem video thật. Không có tỷ lệ phần trăm “đúng kịch bản” được chứng minh chỉ nhờ JSON hợp lệ.
