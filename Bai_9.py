#Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) 
#(bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. Với giá trị cố định của C là 50,
#H là 30. D là dãy giá trị tùy biến, 
#được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.

from math import sqrt
C = 50
H = 30

lst = []
while(1):
    D = float(input("Nhập D: "))
    if D == 0:
        break
    Q = float(sqrt((2*C*D)/H))
    lst.append(str(int(round(Q))))

print(", ".join(lst))