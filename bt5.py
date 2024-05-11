# 1.Cả lists và tuples là các kiểu dữ liệu chuỗi có thể lưu trữ một bộ sưu tập các item(mục).
#   Mỗi item được lưu trữ trong một list  hoặc một tuple có thể thuộc bất kỳ loại dữ liệu nào.
# employee=['jane',22,'Engineer']
# employee[1]=23
# print(employee)
# 3.B 
# 4.B 
# 5.C

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("mang bth:", arr)
# cong2 = [x + 2 for x in arr]
# print("cong 2       :", cong2)
# nhan2 = [x * 2 for x in arr]
# print("mang gap 2:", nhan2)
# chuyen = arr[2:] + arr[:2] 
# print("Shift 2      :", chuyen)

# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l', 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
# a = arr[::-1]
# b = ''.join(a)
# print(b)

# num = int(input("nhap 1 so nguyen duong: "))
# a = [1, 1]
# for i in range(2, num):
#     a.append(a[-1] + a[-2])
# print(f"day can tim {num} so dau tien: {a}")

# a=int(input("nhap so luong mon an:"))
# menu=[]
# gia=[]
# for i in range(a):
#     mon=input(f"mon{i+1}:")
#     giamon=float(input(f"gia cua mon{i+1}:"))
#     menu.append((mon,giamon))
#     gia.append(giamon)

# giatrungbinh=sum(gia)/a
# print("gia trung binh cac mon la:",giatrungbinh)
# giatren=[b for b in menu if b[1]>giatrungbinh]
# print("cac mon co gia cao hon gia trung binh:",*giatren)

a=input("viet cau gi do:").split()
b=len(a)
print("so tu`:",b)




    






