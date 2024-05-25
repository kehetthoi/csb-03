# import mymodule

# a=int(input("nha 1 so:"))
# b=int(input("nhap 1 so:"))
# mymodule.sum(a,b)

numbers = []
while True:
    number = str(input("Nhập một số nguyên (nhập 0 để kết thúc): "))
    if number == '0':
        break  
    numbers.append(number)

def tong(numbers):
    total = 0
    for item in numbers:
        if type(item) == int:
            total += item
        if type(item) == str:
            print(f"{item} không phải là số nguyên")
            continue
    return total

result = tong(numbers)
print(f"Tổng các phần tử trong mảng là: {result}")

       




