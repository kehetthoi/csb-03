'''
import math
bk=float(input("nhap ban kinh hinh tron: "))
cv=2 * math.pi * bk
dt=math.pi * (bk ** 2)
print("chu vi la: ",cv)
print("dien tich la: ",dt)
'''
'''
import math
canh = float(input("nhap do dai canh hinh vuong: "))
dc = canh * math.sqrt(2)
print("Độ dài đường chéo của hình vuông là:", dc)
'''
'''
a=input("nhap ten rieng: ")
b=input("nhap ten mien(gmail.com): ")
print("ten rieng la: "+a)
print("ten mien la: "+b)
print("email day du: "+a+"@"+b)
'''
'''
a=input("nhap thang:")
b=input("nhap ngay:")
c=input("nhap nam:")
print("ngay da nhap theo kieu MM/DD/YYYY:"+a+"/"+b+"/"+c)
print("ngay da nhap theo kieu DD/MM/YYYY:"+b+"/"+a+"/"+c)
'''
'''
stg=float(input("nhap so tien gui ngan hang:"))
lai=1.05
stg1=stg*lai
stg2=stg*(lai)**2
stg3=stg*(lai)**10
print("so tien gui la:",stg)
print("so tien lai sau 1 nam:",stg1)
print("so tien lai sau 2 nam:",stg2)
print("so tien lai sau 10 nam:",stg3)
'''
'''
from turtle import *
pen
pensize(1)
pencolor('black')
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
penup()
goto(-100,-100)
pendown()
setheading(360)
pensize(4)
pencolor('#de5246')
left(90)
forward(100)
right(135)
forward(70)
left(90)
forward(70)
right(135)
forward(100)
mainloop()
'''
from turtle import *
pen
pensize(10)
pencolor('#cf8f03')
setheading(150)
forward(100)  
left(60)      
forward(100)  
left(120)   
forward(100)  
left(60)      
forward(100)  
left(120) 
penup()
goto(40,0)
pendown()
pensize(10)
pencolor('#0b2c3c')  
setheading(150)
forward(100)  
left(60)      
forward(100)  
left(120)   
forward(100)  
left(60)      
forward(100)  
left(120) 
mainloop()




