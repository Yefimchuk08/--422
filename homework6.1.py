# ЗАВДАННЯ 1, 2

# a = input("Введи своє ім'я: ")
# b = int(input("Введи свій вік: "))
# def Hi():
#     global a
#     global b
#     if b > 0 or b < 130:
#         print(f"Привіт {a}! Твій вік - {b}. ")
#     else:
#         raise Exception
# Hi()



# def format_greeting(name, age):
#     if age <= 0 or age >= 130:
#         raise ValueError("Вік має бути в діапазоні від 0 до 130 років.")
    
#     return f"Привіт, {name}! Твій вік — {age}"


# try:
#     name = input("Введіть ваше ім'я: ")
#     age = int(input("Введіть ваш вік: "))
#     greeting = format_greeting(name, age)
#     print(greeting)
    
# except ValueError:
#     print(f"Помилка")

# ЗАВДАННЯ 3, 4

# def plus( ):
#     c = int(input("Введи скіьки чисел має бути в списку: "))
#     count = 0
#     list1 = list()
#     while count < c:
#         a = int(input("Введи число яке ти хочеш додати до списку: "))
#         count += 1
#         list1.append(a)
#     for i in list1:
#         if i <= 0:
#             raise Exception
#         else:
#             b = sum(list1)
#     print(b)
# plus()


# def plus(c, count):
#     list1 = list()
#     while count < c:
#         a = int(input("Введи число яке ти хочеш додати до списку: "))
#         count += 1
#         list1.append(a)
#     for i in list1:
#         if i <= 0:
#             raise ZeroDivisionError("Число менше за 0")
#     return sum(list1)
# try:
#     c = int(input("Введи скіьки чисел має бути в списку: "))
#     end = plus(c, 0)
#     print(end)
# except ZeroDivisionError:
#     print("Exception")