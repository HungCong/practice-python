import math

print("Nhap so a: ")
a = float(input())
print("Nhap so b: ")
b = float(input())
print("Nhap so c: ")
c = float(input())
delta = math.pow(b, 2) - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem!!")
elif delta == 0:
    x = -math.pow(b, 2) / 2*a
    print("phuong trinh co nghiem: x = ", x)
else:
    x1 = (-math.pow(b, 2) + math.sqrt(delta))/2*a
    x2 = (-math.pow(b, 2) - math.sqrt(delta))/2*a
    print("phuong trinh co nghiem: x1 = ", x1)
    print("va x2 = ", x2)