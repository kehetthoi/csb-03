#phan1
#bai1
# a=int(input("nhap 1 so:"))
# b=int(input("nhap 1 so:"))
# c=a+b
# print(f"tong cua {a}va {b} la:",c)

#bai2
# import cmath
# a = float(input("Input a: "))
# b = float(input("Input b: "))
# c = float(input("Input c: "))
# delta = b*b - 4*a*c
# if delta == 0:
#     print("Phương trình có nghiệm kép x1 = x2 =", -b/(2*a))
# if delta > 0:
#     print("Phương trình có 2 nghiệm x1 =", (-b + cmath.sqrt(delta))/(2*a), " và x2 =", (-b - cmath.sqrt(delta))/(2*a))
# if delta < 0:
#     print("Phương trình đã cho vô nghiệm ! ")

#bai3
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

#bai4
# def restaurant_order():
#     print("== Welcome to MindX Restaurant ==")
#     order_list = []
#     while True:
#         dish = input("Please choose a dish: ")
#         if dish in order_list:
#             print("You chose this already. Anything else? (y/n): ", end="")
#         else:
#             order_list.append(dish)
#             print("Great choice! Anything else? (y/n): ", end="")
#         more = input().strip().lower()
#         if more != 'y':
#             break
#     print("Well done! Your order:")
#     for dish in order_list:
#         print(f"- {dish}")
# restaurant_order()

#bai5
# phone_prices = {
#     "Iphone12": 28000000,
#     "Samsung N10": 16000000,
#     "Oppo 93": 7500000,
#     "Vsmart": 7400000,
#     "Vivo": 4200000
# }
# def get_phone_price():
#     phone_name = input("Input name of a phone: ").strip()
#     if phone_name in phone_prices:
#         print(f"Price of {phone_name}: {phone_prices[phone_name]}")
#     else:
#         print(f"{phone_name} is not in the list.")
# def get_phones_within_budget():
#     budget = int(input("Input your budget: "))
#     print("Phones that fit your budget:")
#     found_any = False
#     for phone, price in phone_prices.items():
#         if price <= budget:
#             print(f"- {phone}: {price}")
#             found_any = True
#     if not found_any:
#         print("No phones fit your budget.")
# get_phone_price()
# print()  
# get_phones_within_budget()

#bai6
# def count_digits(number):
#     num_str = str(number)
#     return len(num_str)
# number = int(input("nhap day so:"))
# digit_count = count_digits(number)
# print(f"so chu so trong {number} là {digit_count}.")

#bai7
# numbers = [ 5, 1, 8, 92, -1, 30]
# lenth = len(numbers)
# for i in range(0, lenth - 1):
#     for j in range(i + 1, lenth):
#         if (numbers[i] > numbers[j]):
#             tmp = numbers[i]
#             numbers[i] = numbers[j]
#             numbers[j] = tmp
# print(numbers)

#bai8
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






   

     








