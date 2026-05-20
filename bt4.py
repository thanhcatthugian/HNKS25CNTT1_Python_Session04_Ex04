count = 0
lucky_number = 369

while count < 6 :
    print(f"Bạn đang còn {5-count} lượt nhập")
    check_lucky_number = int(input("Nhập số may mắn có chứa 3 chữ số: "))
    if check_lucky_number < lucky_number:
        print("Số bạn vừa nhập đang nhỏ hơn số may mắn!")
        count+=1
    elif check_lucky_number > lucky_number:
        print("Số bạn vừa nhập đang lớn hơn số may mắn!")
        count+=1
    if count > 5 :
        print("Bạn đã hết lượt và chúc may mắn lần sau!")
        print("--- Trò chơi kết thúc ---")
    else:
        print("Bạn đã đoán chính xác số may mắn!")
        count = 6
        print("--- Trò chơi kết thúc ---")
