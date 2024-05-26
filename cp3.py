# def chan_le(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# a=int(input("nhap so :"))
# if chan_le(a):
#     print(f"{a} la so chan")
# else:
#     print(f"{a} la so le")

# def dtht(x):
#     return  x*x*3.14
# x=float(input("nhap ban kinh:"))
# print("dien tich hinh tron la:",dtht(x))

# def daochuoi(x):
#     return x[::-1]
# a=input("nhap 1 chuoi:")
# print("chuoi dao nguoc la:",daochuoi(a))

# def dao(x):
#     if x[:-1]:
#         return True
#     else:
#         return False
# a=input("nhap 1 Palindrome:")
# if dao(a):
#     print(f"{a} la Palindrome")
# else:
#     print(f"{a} ko phai la Palindrome")

# def gt(x):
#     return 1 if x==0 else x*gt(x-1)
# a=float(input("nhap 1 so nguyen:"))
# print(f"giai thua cua {a} la:",gt(a))

# l = [5, 1, 8, 92, -1, 30] 
# print("Original List:", *l)
# def sort_ascending(l1):
#     for i in range(0, len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i] >= l1[j]:
#                 l1[i], l1[j] = l1[j],l1[i]
#     return l1
# print("Sorted List", *sort_ascending(l))

# def fibonacci(n):
#     if (n < 0):
#         return -1
#     elif (n == 0 or n == 1):
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# a=int(input("nhap so nguyen:"))
# print(f"{a} so dau tien cua day fibonacci: ")
# sb = ""
# for i in range(0, a):
#     sb = sb + str(fibonacci(i)) + ", "
# print(sb)

# def hieu(x):
#  if x>17:
#     return x-17
#  else:
#    abs(x)
# a=int(input("nhap so:"))
# if hieu(a):
#   print((a-17)*2)
# else:
#   print(abs(a))

# def ngay(x, a):
#     if x[2] > a[2]:
#         return x[2]-a[2]
#     else:
#         return a[2]-x[2]
# x = (2024, 7, 2) 
# a = (2024, 7, 9)  
# print(ngay(x, a))  

# def dem(x):
#     return x.count(4)
# list = [4, 5, 6, 4, 7, 9, 4]
# so = dem(list)
# print(f"so lan xuat hien cua s4 la: {so}")

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 
#     717, 958, 743, 527
# ]

# def chan(numbers):
#     for x in numbers:
#         if x == 237:
#             break
#         if x % 2 == 0:
#             print(x)

# chan(numbers)

def histogram(numbers, char):
    for x in numbers:
        print(char * x)
numbers = [2, 3, 6, 5]
a = '@'
histogram(numbers, a)

    

    



    