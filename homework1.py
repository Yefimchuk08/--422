# sum_even = 0
# count_even = 0

# sum_odd = 0
# count_odd = 0

# sum_multiples_nine = 0
# count_multiples_nine = 0


# first_number = int(input("Введи перше число: "))
# second_number = int(input("Введи друге число: "))
# for i in range(first_number, second_number+1,1):
#     if(i%2!=0):
#         continue
#     sum_even += i
#     count_even += 1
#     print(f"Сума парних чисел: {sum_even}")
#     if(count_even > 0):
#         print(f"Середнє арифметичне парних числе: {sum_even/count_even}")
# for v in range(first_number,second_number+1,1):
#     if(v%2==0):
#         continue
#     sum_odd += v
#     count_odd +=1
#     print(f"Сума непарних чисел: {sum_odd}")
#     if(count_odd > 0):
#         print(f"Середнє арифметичне непарних чисел: {sum_odd/count_odd}")
# for a in range(first_number, second_number+1,1):
#     if(a%9!=0):
#         continue
#     sum_multiples_nine += a
#     count_multiples_nine += 1
#     print(f"Сума кратних чисел 9 в вказаному діапазоні: {sum_multiples_nine}")
#     if (count_multiples_nine > 0):
#         print(f"Середнє арифметичне чисел кратних 9 у вказаному діапазоні: {sum_multiples_nine/count_multiples_nine}")



        
# wight_line = int(input("Введи довжину лінії: "))
# sumbol = input("Введи символ яким буде позначатись лінія: ")

# for n in range(wight_line+1):
#     print(sumbol)


# while True:

#     num = float(input("Введи число: "))
#     if (num == 7):
#         print("Good bye!")
#         break
#     elif(num > 0):
#         print("Number is positive")
#     elif (num < 0):
#         print("Number is negative")

#     else:
#         print("Number is equal to zero")






# min_num = None
# max_num = None
# total_sum = 0

# while True:

#     numer = int(input("Введи число: "))
#     if numer == 7:
#         print("Good bye!")
#         break
#     total_sum += numer
#     if max_num is None or numer > max_num:
#         max_num = numer

#     if min_num is None or numer < min_num:
#         min_num = numer
#     print(f"Сума: {total_sum}, мінімальне число: {min_num}, максимальне число: {max_num}")
    
    
# start_num = int(input("Введи стартове число: "))
# finish_num = int(input("Введи фінішне число: "))

# for k in range(start_num, finish_num+1, 1):
#     if (k%7!=0):
#         continue
#     print(k)





# count_five = 0
# start = int(input("Введи стартове число діапазону: "))
# finish = int(input("Введи фінішне число діапазону: "))
# for a1 in range(start,finish+1):
#     print(a1)
# if(finish>start):
#     for i1 in range(finish, start-1, -1):
#         print(i1)
# for l in range(start, finish+1):
#     if(l%7!=0):
#         continue
#     print(l)
# for o in range(start, finish+1):
#     if(o%5==0):
#         count_five += 1
# print(count_five)

start1 = int(input("Введи стартове число діапазону: "))
finish1 = int(input("Введи фінішне число діапазону: "))

for i in range(start1, finish1,1):
    if(i%3==0):
        if(i%5==0):
            print("Fizz Buzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")

    else:
        print(i)