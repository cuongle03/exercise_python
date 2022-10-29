#%% bai 10 tính tổng các chư số trong số nguyên dương
tong = 0
n = -1
def  (n)
while n <= 0:
   n =int(input("nhap so nguyen duong n"))
   tong = tong + n%10
   n =int(n%10)
  return tong

print("tổng: ",tong)