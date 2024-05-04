'''
a=int(input("nhap so duong"))
for i in range(1,a+1):
    print("#"*i)
    '''

'''
while True:
    
        a = int(input("nhap so thuc duong "))
        if a <= 0:
            print("so nay sai roi nhap lai")
        else:
            print("cam on")
            break
'''
'''
def tinhgiaithua(n):
    giai_thua = 1
    if n == 0 or n == 1:
        return giai_thua
    else:
        for i in range(1, n + 1):
            giai_thua *= i
        return giai_thua

n = int(input("nhap so nguyen duong n = "))
print(f"giai thua cua {n} là {tinhgiaithua(n)}")
'''
'''
a = input("nhap so: ")
b = 0

for i in a:
    b += int(i)

print("tong cac so", a, "=", b)
'''
print("cac so co tong chu so la 9:")
a = 0

for i in range(1000, 10000):
    if sum(int(b) for b in str(i)) == 9:
        print(i)
        a += 1
    if a == 10:
        break



        










