'''
a = input("nhap vao mot chu so: ")
if a.isdigit():
    print(a,"la chu so")
else:
    print(a,"ko phai la chu so")
    '''
'''
a = int(input("nhập số: "))
if a % 2 == 0:
    print(a,"là số chẵn")
else:
    print(a," là số lẻ")
'''
'''
a = float(input("nhập số: "))
if a == a // 1:
    print(a," là số nguyên ")
else:
    print(a," ko là số nguyên")
    '''
'''
a = int(input("nhập số: "))

if a % 3 == 0 and a % 5 == 0:
    print(a," chia hết cho 3 và 5")
elif a % 3 == 0:
    print(a," chia hết cho 3")
elif a % 5 == 0:
    print(a," chia hết cho 5")
else:
    print(a," chia hết cho 3 hoặc 5")
    '''
'''
a = "admin"
b = "12345"

c = input("Username: ")
d = input("Password: ")

if c == a and d == b:
    print(f"Bạn đã đăng nhập, {c}.")
else:
    print("Tên người dùng hoặc mật khẩu sai.")
    '''
'''
a = float(input("nhập cạnh 1: "))
b = float(input("nhập cạnh 2: "))
c = float(input("nhập cạnh 3: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("3 đoạn thẳng không thể tạo thành hình tam giác.")
else:
    print("3 đoạn thẳng có thể tạo thành một hình tam giác.")
    '''
'''
a = float(input('Nhap vao so thuc 1: '))
b = float(input('Nhap vao so thuc 2: '))
c = float(input('Nhap vao so thuc 3: '))

k = [a,b,c]
if a + b > c and a + c > b and b + c > a:
    if a==b==c:
        print('la tam giac can')
        from turtle import *
        pen()
        backward(a)
        left(60)
        forward(a)
        left(60)
        backward(a)
        right(60)
        mainloop()
    elif a*a+b*b == c*c or a*a+c*c == b*b or c*c+b*b == a*a:
        print('la tam giac vuong')
    else:
        print('la tam giac thuong')
else:
    print('khong phai la tam giac')
    '''
'''
for i in range(21):
    if i % 3 == 0:
        print(i)
        '''
a = int(input("nhap so: "))
b = len(str(a))

print("So chu so cua so la: ",b)



