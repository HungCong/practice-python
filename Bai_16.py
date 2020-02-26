#Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. 

count_num = 0
count_str = 0

chuoi = input("Nhập chuỗi: ")
for c in chuoi:
    if c.isdigit(): # Kiểm tra có phải là số không
        count_num += 1
    elif c.isalpha(): # Kiểm tra có phải là ký tự không
        count_str += 1
    else:
        pass
print("Số ký tự trong chuỗi: ", count_str)
print("Số chữ số trong chuỗi: ", count_num)
