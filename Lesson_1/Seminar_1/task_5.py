# zv = "*"
# prob = " "
#
# hite = int(input("Enter num: "))
# shir = hite - 1
#
# col_zv = 1
#
# while hite > 0:
#     for i in range(shir):
#         print(prob,end="")
#
#     for i in range(col_zv):
#         print(zv,end="")
#
#     shir -=1
#     col_zv +=2
#     hite -=1
#     print()


num_stars = int(input("enter num stars: "))

for i in range(num_stars):
    print(" " * (num_stars -i -1)+ "*" * (2*i + 1))