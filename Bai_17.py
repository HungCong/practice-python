#Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường

count_lower = 0
count_upper = 0

chuoi = input("Nhập chuỗi: ")
for c in chuoi:
    if c.islower(): # Kiểm tra có phải là chữ thường không
        count_lower += 1
    elif c.isupper(): # Kiểm tra có phải là chữ hoa không
        count_upper += 1
    else:
        pass
print("Số chữ thường trong chuỗi: ", count_lower)
print("Số chữ hoa trong chuỗi: ", count_upper)
