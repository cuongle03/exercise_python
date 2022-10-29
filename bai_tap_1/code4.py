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
