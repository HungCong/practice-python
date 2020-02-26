#Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.
#Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

lst = []
count = 0
s = input("Nhập chuỗi: ")
word = [word for word in s.split('')]
for i in word:
    if i == "a":
        count += 1
    else:
        lst.append(count)
        count = 0
        pass

print(",".join(lst))