# thisdict={
#     "classname":"csb03",
#     "year":2024,
#     "student":10

# }
# print(thisdict["classname"])
# thisdict["Student"]=9
# print(thisdict["student"])
# thisdict["hsmoi"]="quynh anh"
# print(thisdict)
# thisdict.pop("hsmoi")
# thisdict.popitem()
# print(thisdict)

# for x in thisdict:
#     print(x)

# for y in thisdict:
#     print(thisdict[y])

# for a,b in thisdict.items():
#     print(a,b)

# newdict=thisdict.copy()
# print(newdict)

# myclass={
#     "student1":{
#         "name":"Tai",
#         "age":18
#    },
#    "student2":{
#        "name":"Lam",
#        "age":17
#    },
#     "student3":{
#        "name":"Huy",
#        "age":15
#    }
# }

# for i in myclass.values():
#     print(i["name"])
# for x,y in myclass.items():
#     print(y["name"])

# char={
# "Name": "Light",
# "Age": 17,
# "Strength": 8,
# "Defense": 10,
# "HP": 100,
# "Backpack": "Shield, Bread Loaf",
# "Gold": 100,
# "Level": 2
# }
# char["Gold"]=150
# char["Backpack"]=["Shield, Bread Loaf,Flintstone"]
# char["Pocket"]=["MonsterDex,Flashlight"]
# print(char)

# shop={
# "HP":20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# print(shop["MACBOOK"])
# hang=input("nhap hang may tinh:")
# if hang in shop:
#     print(f"so luong may tinh {hang} co trong shop la:{shop[hang]}")
# else:
#     print("hang khong ton tai")

# a="David"
# if a in hs:
#     print(hs["David"])
# else:
#     print("David ko co trong danh sach")
hs = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78}
}

sorted_students = sorted(hs.items(), key=lambda x: x[1]["score"], reverse=True)
print(sorted_students)

