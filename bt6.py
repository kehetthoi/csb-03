# def nguyen(x):
#     if x==int(x):
#         return True
#     else:
#         return False

# a=float(input("nhap 1 so nguyen:"))
# if nguyen(a):
#     print(f"{a} la so nguyen")
# else:
#     print(f"{a} ko phai so nguyen")


# def is_prime(n):
#     if n <= 1:
#         return False 
#     for i in range(2, n):
#         if n % i == 0: 
#             return False  
#     return True

# n = int(input(" nhap so tu nhien: "))

# if is_prime(n):
#     print(f"{n} la so nguyen to")
# else:
#     print(f"{n} khong phai so nguyen to")


# def is_prime(n):
#     if n <= 1:
#         return False 
#     for i in range(2, n):
#         if n % i == 0: 
#             return False  
#     return True

# n = int(input(" nhap mot so n: "))
# print(f"{n} so nguyen to dau tien la:",end="")
# for i in range(n):
#     if is_prime(i):
#         print(i, end=" ")

# def gt(n):
#     return 1 if n == 0 else n * gt(n - 1)
# n = int(input("nhap so nguyen duong: "))
# a = sum(gt(i) * i for i in range(1, n + 1))
# print("tong:",a)

# from datetime import datetime

# now = datetime.now()
# print("Today is", now.strftime('%d/%m/%Y'))
# print("Time right now:", now.strftime('%H:%M:%S'))




