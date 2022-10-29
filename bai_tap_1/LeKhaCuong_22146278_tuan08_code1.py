#%% bài 1 tính tổng số phân số dương
N = -3
while N < 0:
  N =int(input("nhập số nguyên dương: "))
i = 1
tổng = 0
mẫu_số = 0
phân_số = 1
while i <= N:
  mẫu_số += i
  phân_số = 1/(mẫu_số)
  tổng += phân_số
  i += 1
print("tổng số bằng: ", tổng)

#%% bài 4 tính tổng các số, với n là số nguyên được nhập bởi người dùng
N = -2
while N < 0:
    N =int(input("nhập số nguyên dương: "))
i = 0
tử_số = 0
mẫu_số = 0
tổng = 0

while i <3= N:
    tử_số = (2*i + 1)
    mẫu_số = (2*i + 2)
    phân_số = (tử_số / mẫu_số)
    tổng += phân_số
    i +=1
print("tổng phân số: ", tổng)

#%% tìm ước số lẻ của số n được nhập
n = -1
while n < 0:
    n =int(input("nhập số nguyên dương: "))
for i in range(1, n+1):
    if (n % i ==0):
     if (i %2 !=0): 
        print(i)
#%% tính tổng các chữ số trong số n được nhập bởi người dùng
def totalDigitsOfNumber(n):
    tong = 0
    while (n > 0):
        tong = tong + n % 10
        n = int(n / 10)
    return tong
n = int(input("Nhập số nguyên dương n = "))
print("Tổng các chữ số của", n , "là",totalDigitsOfNumber(n))
""""
* totalDigitOfNumber : tổng các số của số
* def dùng để gọi hàm
* return trả về các giá trị của hàm được gọi