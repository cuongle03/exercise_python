#%% 6 tìm số nguyên tố trong n số được nhập
import math
def isPrimeNumber(n) : # là số nguyên tố
  if (n < 2) :
    return False # False  không phải là số nguyên tố
  squareBoot = int(math.sqrt(n))
  for i in range(2, squareBoot +1) :
    if (n % i == 0) :
        return False
    return True              # True là số nguyên tố
n = int(input("nhập số nguyên dương n = "))
print (n, "số nguyên tố đầu tiên là: ")
dem = 0    # đếm số nguyên tố
i = 2      # tìm số nguyên tố bắt đầu
sb = " "
while ( dem < n) :
    if( isPrimeNumber(i)) :
        sb = sb + str(i)+ " " 
        dem = dem + 1 
    i = i + 1
print("các số nguyên tố đầu tiên : ", sb)
 #%% 5 tạo list  có các phần tử tăng dần, chèn B vào list vẫn có thứ tự tăng
list1 = []
n = int(input("Nhap vao so luong phan tu: n = "))
for i in range(n):
    print("\tPhan tu thu", i+1 ,"la:", end=" ")
    list1.append(int(input()))
print("Danh sach vua nhap la: ",list1)
a = int(input("nhập vị trí chèn: "))
B = int(input("nhập ký tự muốn chèn: "))
list1.insert(a, B)
print(list1 )
if a < i + 1 :
    list1.sort()
    print(list1)





 
      