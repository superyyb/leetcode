# age=input("请问你几岁啦？")
# age=int()
# i=False
# if age<3:
#     print("Ticket is free.")
#     i=True
# elif age<12:
#     print("The fee is 10 dollar.")
#     i=True
# else:
#     print("The fee is 15 dollar.")
#     i = True
# if i==False:
#     continue


# age=int(input("请问你几岁啦？"))
# while True:
#     found=False
#     if age<3:
#         print("Ticket is free.")
#     elif age<12:
#         print("The fee is 10 dollars.")
#     else:
#         print("The fee is 15 dollars.")
#     found=True
#     break
#     if found==False:
#         print("请重新输入")

while True:
    age=input("请问你几岁啦？")
    if age=="quit":
        break
    else:
        age=int(age)
        if age<3:
            print("Ticket is free.")
        elif age<12:
            print("The fee is 10 dollars.")
        else:
            print("The fee is 15 dollars.")

