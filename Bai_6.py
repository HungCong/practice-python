#Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance 

class SinhVien:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    def getSV(self):
        print("Họ và tên: ", self.name)
        print("Ngày sinh: ", self.birthday)
sv = SinhVien("Đỗ Công Hưng", "15/2/1996")
sv1 = SinhVien("Trương Tam Phong", "1/1/1800")
sv.getSV()
sv1.getSV()
