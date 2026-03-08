from Sinhvien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    # Sinh ID tự động
    def generateID(self):
        maxID = 1
        if (self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID = maxID + 1
        return maxID

    # Đếm số lượng sinh viên
    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    # Nhập sinh viên
    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten Sinh Vien: ")
        sex = input("Nhap gioi tinh Sinh Vien: ")
        major = input("Nhap chuyen nganh cua Sinh Vien: ")
        diemTB = float(input("Nhap diem trung binh cua Sinh Vien: "))

        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    # Cập nhật sinh viên
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten Sinh Vien: ")
            sex = input("Nhap gioi tinh cua Sinh Vien: ")
            major = input("Nhap chuyen nganh cua Sinh Vien: ")
            diemTB = float(input("Nhap diem trung binh cua Sinh Vien: "))

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB

            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh Vien co ID = {} khong ton tai.".format(ID))

    # Sắp xếp theo ID
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    # Sắp xếp theo tên
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    # Sắp xếp theo điểm trung bình
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    # Tìm theo ID
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult

    # Tìm theo tên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    # Xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    # Xếp loại học lực
    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"

    # Hiển thị danh sách sinh viên
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<12} {:<10} {:<10}".format(
            "ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))

        if (len(listSV) > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<12} {:<10} {:<10}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    # Lấy danh sách sinh viên
    def getListSinhVien(self):
        return self.listSinhVien