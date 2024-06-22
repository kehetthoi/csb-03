# f=open("name.txt","r")
# print(f.read())
# # f = open("tenhs.txt","w")
# # f.write("VDH,lop CSB-03,MINDX")
# # f=open("tenhs.txt","r")
# # print(f.readlines())
# import os
# os.remove("name.txt")
# if os.path.exists("name.txt"):
#     print("file ton tai")
# else:
#     print("file ngu")

# # with open("name.txt","r") as f:
    
import os
from os import path
a = 'class/tuan11/'+str(input('Input a file name: '))+'.txt'
if path.exists(a):
    # b = open(a,'r')
    with open(a,'r') as f:
        print(f.read())
else:
    print('k co')
