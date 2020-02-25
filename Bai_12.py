#Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, 
#chuyển các dòng này thành chữ in hoa và in ra màn hình. 

lst = []

while(1):
    string = input("Nhập một chuỗi: ")
    if string != "ok":
        lst.append(string.upper())
    else:
        break

print(', '.join(lst))