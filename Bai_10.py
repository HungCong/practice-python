#Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
#Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
#Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
#Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4,
#6, 8]]

m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

a = []

for i in range(0, m):
    a.append([])
    for j in range(0, n):
        a[i].append(i*j)

print("ma trận tương ứng với %d hàng và %d cột là" %(m,n))
for i in range(0, m):
    for j in range(0, n):
        print("%d " % a[i][j], end='')
    print()
