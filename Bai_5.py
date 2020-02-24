#Định nghĩa một class có ít nhất 2 method:
#getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển. 
#printString: in chuỗi vừa nhập sang chữ hoa.
#Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

class pressKey:
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input("Nhập vào một chuỗi: ")
    def printString(self):
        print ("Chuỗi vừa nhập: ", self.str.upper())

obj = pressKey()
obj.getString()
obj.printString()