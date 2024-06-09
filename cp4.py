#phan1
#bai1
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

#phan2
#bai1
# shop={
# "HP":20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop["TOSHIBA"]=10
# print(shop)

#bai2
# shop={
# "HP":20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop["TOSHIBA"]=10
# a=input("nhap ten hang may:")
# b=int(input("nhap so luong cua may:"))
# shop[a]=b
# print(shop)

#bai3
# shop={
# "HP":20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop["DELL"] += 10
# shop["MACBOOK"] -= 10
# print(shop)

#bai4
# shop={
# "HP":20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop=sum(shop.values())
# print(shop)

#phan3
#bai1
# shop={
# "HP":600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }

#bai2
# shop={
# "HP":600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }

# print("gia cua may asus la:",shop["ASUS"])

#bai3
# shop={
# "HP":600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }
# a=input("nhap hang ban muon xem :")
# if a in shop:
#     print(f"gia cua {a} la:",shop[a])
# else:
#     print("hang khong ton tai")

#phan4
#bai1
# shop={
# "HP":600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }
# a=shop["ASUS"]*5
# print("gia cua 5 chiec asus la:",a)

#bai2
# shop={
# "HP":600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }
# a=input("nhap hang may ban mua mua:")
# b=int(input("nhap so luong:"))
# if a in shop:
#     print(f"gia cua {b} may {a} la:",b*shop[a])
# else:
#     print("hang khong ton tai")

#bai3
# shop={
# "HP":600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }
# shop2={
# "HP":20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# a=input("nhap hang may ban mua mua:")
# b=int(input("nhap so luong:"))
# if a in shop:
#     print(f"gia cua {b} may {a} la:",b*shop[a])
#     shop2[a]-=b
#     print(shop2)
# else:
#     print("hang khong ton tai")

#phan5
#bai1
# shop = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }

# shop2 = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }
# total_money = sum(shop[brand] * shop2[brand] for brand in shop)
# print("Tổng số tiền của toàn bộ hàng tồn kho:", total_money)
#bai2
# shop = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }

# shop2 = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }
# total_values = {brand: shop[brand] * shop2[brand] for brand in shop}
# print("Total value of available brands:")
# for brand, total_value in total_values.items():
#     print(f"- {brand}: {total_value}")

#phan6
#bai1
# char={
#  "Name": "Light",
#  "Age": 17,
#  "Strength": 8,
#  "Defense": 10,
#  "HP": 100,
#  "Backpack": "Shield, Bread Loaf",
#  "Gold": 100,
#  "Level": 2
# }

#bai2
# char={
#  "Name": "Light",
#  "Age": 17,
#  "Strength": 8,
#  "Defense": 10,
#  "HP": 100,
#  "Backpack": "Shield, Bread Loaf",
#  "Gold": 100,
#  "Level": 2
# }
# char["GOld"]+=50
#print(char)

#bai3
# char = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2
# }

# char["Backpack"].append("FlintStone")

# print(char)

#phan7
#bai1
# # char = {
# #     "Name": "Light",
# #     "Age": 17,
# #     "Strength": 8,
# #     "Defense": 10,
# #     "HP": 100,
# #     "Backpack": ["Shield", "Bread Loaf"],
# #     "Gold": 100,
# #     "Level": 2
# # }
# # skill = {
# #     "Skill 1": {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
# #     "Skill 2": {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
# #     "Skill 3": {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
# }

#bai2
# char = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2
# }
# skill = {
#     "Skill 1": {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
#     "Skill 2": {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
#     "Skill 3": {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
# }
# for skill_key, skill_info in skill.items():
#     print(f"{skill_key}: {skill_info['Name']}")

#phan8
#bai1
import random

# Character and skill data
char = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}

skill = {
    "Skill 1": {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    },
    "Skill 2": {
        "Name": "Quick Attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5
    },
    "Skill 3": {
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2
    }
}

# Display skills
print("Available skills:")
for skill_key, skill_info in skill.items():
    print(f"{skill_key}: {skill_info['Name']}")

# Choose skill
skill_choice = input("Choose skill by number: ")
chosen_skill_key = f"Skill {skill_choice}"

if chosen_skill_key in skill:
    chosen_skill = skill[chosen_skill_key]
    print(f"You chose {chosen_skill['Name']}.")
    
    # Check level
    if char["Level"] >= chosen_skill["Minimum level"]:
        # Determine if the skill hits
        if random.random() < chosen_skill["Hit rate"]:
            print(f"Damage: {chosen_skill['Damage']}")
        else:
            print("Missed.")
    else:
        print(f"Cannot deploy. Required level {chosen_skill['Minimum level']}.")
else:
    print("Invalid skill choice.")

  



