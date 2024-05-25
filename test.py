# x = 10  # Biến global

# def my_function():
#     global x
#     x += 5
    


# print("Outside the function:", x)
# numbers = []
# while True:
#     number = input("Nhập một số nguyên (nhập 0 để kết thúc): ")
#     if number == '0':
#         break
#     numbers.append(int(number))

# def tong(numbers):
#     total = 0
#     for item in numbers:
#         if isinstance(item, int):
#             total += item
#         else:
#             print(f"{item} không phải là số nguyên")
#             continue
#     return total

# result = tong(numbers)
# print(f"Tổng các phần tử trong mảng là: {result}")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n=int(input("Input number: "))

print(f'First {n} prime(s): ',end=' ')
k=0
for i in range(1,n+1):
  k+=1
  while is_prime(k)!=True:
    k+=1
  print(k,end=' ')










