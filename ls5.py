'''
hs=["huy","tai","ngoc"]
hs.append("hieu")
print(hs)
'''
'''
hs=["huy","tai","ngoc"]
hs.pop(1)
print(hs)
'''
'''
hs=["huy","tai","ngoc"]
hs.clear()
'''
'''
hs=["huy","tai","ngoc"]
del hs
'''
'''
mon = ["pho", "bun bo", "hu tiu"]  
for i in range(len(mon)):
    print(mon[i])
   
a = input("ban muon an gi: ")
mon.append(a)-
print(a)
'''
# mon = ["pho", "bun bo", "hu tiu"]  
# for i in range(len(mon)):
#     print(mon[i])
   
# a = input("ban muon bo mon nao: ")
# print(a)
# if a==mon:
#     mon.remove(a)
#     print(a)
'''
mon = ["pho", "bun bo", "hu tiu"]
for i in range(len(mon)):
    print(mon[i])
a = input("ban muon bo mon nao: ")
print(a)

if a in mon:
    mon.remove(a)
    print("ban da bo:",a)
    print(mon)
else:
    print("mon nay ko co trong menu")
'''
'''
a = input("nhap cac so cach nhau : ").split()
a = [int(num) for num in a]
b = sum(a)
print("tong cac so la:", b)
'''

a = input("nhap cac so cach nhau : ").split()
a = [int(num) for num in a]
b = max(a)
print("so lon nhat la: ",b)

a = input("nhap cac so cach nhau : ").split()
b=len(a)
for i in range(0,b-1):
    for z in range(i+1,b):
        if(a[i]>a[z]):
            n=a[i]
            a[i]=a[z]
            a[z]=n
print(a)

a = input("nhap cac so cach nhau ").split()
a = [int(i) for i in a]
b = None


for i in a:
    
    if b is None or i > b:
       b = i

print("Số lớn nhất trong danh sách là:", b)









