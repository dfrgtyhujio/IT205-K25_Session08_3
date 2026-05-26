while True :
    print('\n+===========================================================+')
    print('|      HỆ THÔNG QUAN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS      |')
    print('+===========================================================+')
    print('|  1. Nhập dữ liệu đơn hàng và xem báo cáo thông kê         |')
    print('|  2. Chuân hóa mã đơn hàng                                 |')
    print('|  3. Ẩn số điện thoại khách hàng                           |')
    print('|  4. Tìm kiểm và thay thể từ khóa trong ghi chú đơn hàng   |')
    print('|  5. Thoát chương trình                                    |')
    print('+===========================================================+')
    
    choose = input('Mời bạn chọn chức năng (1-5): ')
    
    if choose == '1':
        sender_name = input('Nhập Tên người gửi: ').strip().title()
        if not sender_name:
            print("Tên người gửi không được để trống.")
            continue
        
        sender_phone = input('Nhập số điện thoại người gửi: ').strip()
        if not sender_phone:
            print("Số điện thoại người gửi không được để trống.")
            continue

        pickup_address = input('Nhập địa chỉ lấy hàng: ').strip()
        if not pickup_address:
            print("Địa chỉ lấy hàng không được để trống.")
            continue
        
        recipient_name = input('Nhập Tên người nhận: ').strip().title()
        if not recipient_name:
            print("Tên người nhận không được để trống.")
            continue
        
        recipient_phone = input('Nhập số điện thoại người nhận: ').strip()
        if not recipient_phone:
            print("Số điện thoại người nhận không được để trống.")
            continue

        delivery_address = input('Nhập địa chỉ giao hàng: ').strip()
        if not delivery_address:
            print("Địa chỉ giao hàng không được để trống.")
            continue
        
        delivery_notes = input('Nhập ghi chú giao hàng: ').strip()

        print(f'Tên người gửi: {sender_name}')
        print(f'Số điện thoại người gửi: {sender_phone}')
        print(f'Tên người nhận: {recipient_name}')
        print(f'Số điện thoại người nhận: {recipient_phone}')
        print(f'Địa chỉ lấy hàng: {pickup_address}')
        print(f'Địa chỉ giao hàng: {delivery_address}')
        print(f'Ghi chú giao hàng: {delivery_notes}')
        print(f'Độ dài ghi chú giao hàng: {len(delivery_notes)}')
        print(f'Số lượng từ trong ghi chú giao hàng: {len(delivery_notes.split())}')
        print(f'Ghi chú giao hàng dạng chữ thường: {delivery_notes.lower()}')
        print(f'Ghi chú giao hàng dạng chữ hoa: {delivery_notes.upper()}')
    
    elif choose == '2':
        order_code = input('Nhập mã đơn hàng: ').strip()
        if not order_code:
            print("Mã đơn hàng không được để trống.")
            continue

        print(f'Mã đơn hàng: {order_code}')
        print(f'Mã đơn hàng sau khi chuẩn hóa: GRAB-{order_code.upper().replace(" ", "-")}')
    
    elif choose == '3':
        if not sender_phone:
            print("Số điện thoại không được rỗng")
            
        elif not sender_phone.isdigit():
            print("Số điện thoại chỉ được chứa chữ số")
            
        elif len(sender_phone) != 10:
            print("Số điện thoại phải có đúng 10 ký tự")
            
        else:
            print(f'SĐT người gửi: {sender_phone[:3]}****{sender_phone[-2:]}')
            
        if not recipient_phone:
            print("Số điện thoại không được rỗng")
            
        elif not recipient_phone.isdigit():
            print("Số điện thoại chỉ được chứa chữ số")
            
        elif len(recipient_phone) != 10:
            print("Số điện thoại phải có đúng 10 ký tự")
            
        else:
            print(f'SĐT người nhận: {recipient_phone[:3]}****{recipient_phone[-2:]}')

    elif choose == '4':
        search_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")
        

        if search_keyword in delivery_notes:
            keyword_count = delivery_notes.count(search_keyword)
            
            delivery_notes = delivery_notes.replace(search_keyword, replace_keyword)
            
            print(f"Số lần xuất hiện của từ khóa: {keyword_count}")
            print(f"Ghi chú sau khi thay thế: {delivery_notes}")
        else:
            print(f"Không tìm thấy từ khóa {search_keyword} trong ghi chú giao hàng.")
    
    elif choose == '5':
        print('Thoát chương trình.')
        break
    
    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')
        
        
# 1. Phân tích Input / Output
# Chức năng 1 (Nhập đơn hàng & Thống kê):
# - Input: sender_name, sender_phone, pickup_address, recipient_name, recipient_phone, delivery_address, delivery_note
# - Output: In ra màn hình các chuỗi đã xử lý (Tên chuẩn hóa Title Case, Địa chỉ khử khoảng trắng, Ghi chú độ dài, Số từ, Viết hoa/thường).

# Chức năng 2 (Chuẩn hóa mã đơn hàng):
# - Input: order_code
# - Output: Chuỗi mã đơn hàng chuẩn hóa dạng GRAB-MÃ-ĐƠN-HÀNG

# Chức năng 3 (Ẩn số điện thoại khách hàng):
# - Input: Lấy dữ liệu sender_phone và recipient_phone đã nhập từ Chức năng 1
# - Output: Chuỗi số điện thoại bảo mật dạng 3_số_đầu*****2_số_cuối hoặc thông báo lỗi nếu dữ liệu chưa hợp lệ.

# Chức năng 4 (Tìm & Thay thế từ khóa trong ghi chú):
# - Input: search_keyword, replace_keyword
# - Output: Chuỗi ghi chú mới sau khi thay thế và số lần từ khóa xuất hiện ban đầu trong ghi chú


# 2. Đề xuất giải pháp
# Loại bỏ khoảng trắng thừa đầu cuối: .strip()
# Viết hoa chữ cái đầu mỗi từ: .title()
# Chuyển đổi hoa/thường: .upper(), .lower()
# Thay thế ký tự / chuỗi con: .replace()
# Đếm số lần xuất hiện của từ khóa: .count()
# Kiểm tra chuỗi chỉ chứa ký tự số: .isdigit()
# Kiểm tra tiền tố chuỗi: .startswith()

# 3. Mô tả luồng chương trình
# Vòng lặp while True hiển thị Menu 5 chức năng.
# Nhận lựa chọn từ người dùng:
#     Nếu không phải số nguyên từ 1 đến 5 => Báo lỗi, yêu cầu nhập lại.
# Thực thi chức năng tương ứng qua cấu trúc rẽ nhánh if...elif...else