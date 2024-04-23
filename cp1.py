'''
a = "mai co"
b = "do dan"
print("ten day du cua ban la: "+a,b)
'''
'''
a = "mindx school"
b = a.upper()
print(b)
'''
'''
a=int(input("nhap so: "))
b=a**2
print(b)
'''
'''
a=int(input("nhap ban kinh: "))
import turtle
pen = turtle.Turtle()
pen.circle(a)
turtle.done()
'''
'''
for i in range(3,13,1):
    print(i)
    '''
'''
a =int(input("nhap so:"))
for i in range(0,a+1,1):
 if a > 0:
  print(i)
  '''
'''
a=int(input("nhap so:"))
i=0
for i in range(i,a):
     if i<=a and a>0 and i % 2 == 1:
        print(i)
        i+=1
        '''
'''
a=int(input("nhap canh:"))
goc=360/a
from turtle import*
pen()
for i in range(a):
    forward(100)
    left(goc)
mainloop()
'''
'''
a=int(input("nhap so:"))
if a>13:
    print(a,"lon hon 13")
else:
    print(a,"ko lon hon 13")
'''
'''
a=int(input("nhap so: "))
if a%2==0:
    print(a,"la so chan")
else:
    print(a,"ko phai so chan")
    '''
'''
a = int(input("Nhập tháng: "))

if a in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", a, "có 31 ngày")
elif a in [4, 6, 9, 11]:
    print("Tháng", a, "có 30 ngày")
elif a == 2:
    print("Tháng 2 có 28 hoặc 29 ngày")
else:
    print("Tháng không hợp lệ")
    '''
'''
a=input("nhap ten")
b=input("nhap mat khau")
c=input("nhap email")
print("ten:",a)
print("mat khau:",b)
print("email:",c)
print("Registered successfully")
'''
'''
a=input("nhap ten")
b=input("nhap mat khau")
c=input("nhap email")
d=input("nhap lai mat khau")
print("ten:",a)
if d==b:
  print("mat khau:",b)
  print("mat khau nhap lai:",d)
else:
  print("mat khau ko chinh xac")
print("email:",c)
'''


a=input("nhap ten:")
c=input("nhap email:")
b=input("nhap mat khau:")
x=len(b)
d=input("nhap lai mat khau:")
print("ten:",a)
if x <= 8:
 print("mat khau khong hop le(phai nhieu hon 8 ky tu)")
elif x>8:
 print("mat khau:",b)
if d==b:
  print("mat khau:",b)
  print("mat khau nhap lai:",d)
else:
  print("mat nhap lai khau ko chinh xac")
y=c.find("@")
z=c.find(".")
if y!=-1 and z !=-1 :
  print("email:",c)
else:
  print("nhap lai email")
  
  
  












    
  

