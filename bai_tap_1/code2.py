#%% bài 2 tính tổng các số, với n là số nguyên được nhập bởi người dùng
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