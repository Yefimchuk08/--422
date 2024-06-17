# i = int(input("Введи перше число: "))
# j = int(input("Введи друге число: "))
# for h in range(i,j,1):
#     print(h)

# q = int(input("Введи перше число: "))
# w = int(input("Введи друге число: "))
# for e in range(q,w,1):
#     if(e%2==0):
#         continue
#     print(e)

# r = int(input("Введи перше число: "))
# t = int(input("Введи друге число: "))
# for y in range(r,t,1):
#     if(y%2!=0):
#         continue
#     print(y)

# u = int(input("Введи перше число: "))
# o = int(input("Введи друге число: "))
# if(u>o):
#     for p in range(u,o,1):
#         print(p)
# if(o>u):
#     for a in range(o,u,1):
#         print(a)

# s = int(input("Введи перше число: "))
# d = int(input("Введи друге число: "))
# if (s>d):
#     for f in range(d,s,1):
#         if(f%2==0):
#             continue
#         print(f)
# else:
#     for g in range(d,s,1):
#         if(g%2==0):
#             continue
#         print(g)




#  2  завдання

# sum = 0
# ar = 0

# k = int(input("Введи перше число: "))
# l = int(input("Введи друге число: "))
# for z in range(k,l+1,1):
#     sum += z 
#     ar += 1
# if ar > 0:
#     print(sum)
#     print(sum/ar)


# factorial = 1
# num = int(input("Введи число: "))
# for v in range(1,num+1,1):
#     factorial *= v
#     print(factorial)

# number = 0
# wigth = int(input("Введи довжину лінії: "))
# for wi in range(1, wigth, 1):
#     number += 1
# if (number > 0):
#     print("*"*(number+1))

# sumbol = str(input("Введи символ: "))
# number1 = 0
# wigth1 = int(input("Введи довжину лінії: "))
# for wi in range(1, wigth1, 1):
#     number1 += 1
# if (number1 > 0):
#     print( sumbol*(number1+1))


# 3 завдання


# tabl = int(input("Введи число: "))
# for m in range(1, 11,1):
#     print(f"{m}*{tabl}={tabl*m}")



print("Для початку роботи натиснть - 1")
print("Для закнчення роботи натиснть  - 0")
start = int(input(": "))
while start == 1:

    print("MENU")
    print("1 - Євро")
    print("2 - Доллар")
    print("3 - Фунт")
    num = int(input(": "))
    num = float(input("Введи суму: "))
    if num == 1:


