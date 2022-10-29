list1 = []
n = int(input("Nhap vao so luong phan tu: n = "))
for i in range(n):
    print("\tPhan tu thu", i+1 ,"la:", end=" ")
    list1.append(int(input()))
print("Danh sach vua nhap la: ",list1)
a = int(input("nhập vị trí chèn: "))
B = int(input("nhập ký tự muốn chèn: "))
list1.insert(a, B)
if a < i + 1 :
    list1.sort()
    print(list1)




