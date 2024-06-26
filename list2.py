import random

# our_producks1 = frozenset()
# list1 = [123, 5, 'gh']
# tuple1 = tuple(list1)
# print(tuple1)
# list1.append('Hello')
# print(tuple1)
# # нічого не змнилось
# list2 = []
# tuple2 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in tuple2:
#     if i%2==0:
#         list2.append(i)
# tuple3 = tuple(list2)
# print(tuple3)

# tuple4 = tuple([ 1, 2, 3, 4, 5])
# print(tuple4.index(1), tuple4.index(2))

# print(tuple4.index(4), tuple4.index(5))
# list3 = [tuple4.index(3)]
# print(list3)

# # 2 
# list4 = [random.randint(1,20) for i in range(10)] 
# print(list4)
# list4.sort()
# tuple5 = tuple(list4)
# print(tuple5)



# one_list = [random.randint(1,20) for i in range(10)]
# print(one_list)
# one_set = set(one_list)
# two_list = [random.randint(1,20) for i in range(10)]
# print(two_list)
# two_set = set(two_list)
# print(one_set.isdisjoint(two_set))
# print(one_set.intersection(two_set))
# print(one_set.difference(two_set))
# print(one_set.symmetric_difference(two_set))

# tuple1 = tuple(random.randint(1,20) for i in range(10))
# print(tuple1)
# set1 = set(tuple1)
# tuple2 = tuple(random.randint(1,20) for i in range(10))
# print(tuple2)
# set2 = set(tuple2)
# list1 = (set1.intersection(set2))
# tuple3 = tuple(list1)
# print(tuple3)

# list1 = [random.randint(1,20) for i in range(10)]
# print(list1)
# list1.sort
# set1 = set(list1)
# set1.difference(set1)
# tuple1 = tuple(set1)
# print(tuple1)

# list1 = [[random.randint(1,20) for i in range(10)], [random.randint(1,20) for i in range(10)], [random.randint(1,20) for i in range(10)], [random.randint(1,20) for i in range(10)]]
# print(list1)
# one_set = set(list1[0])
# two_set = set(list1[1])
# three_set = set(list1[2])
# for_set = set(list1[3])
# print(one_set.intersection(two_set).intersection(three_set).intersection(for_set))

# list1 = [tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3)), tuple(random.randint(1,100) for i in range(3))]
# print(list1)
# one_set = set(list1)
# print(one_set)

# 3

# ar = 0
# sum = 0
# dob = 1
# count = 0
# tuple1 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 45, 53])
# for i in tuple1:
#     sum += i
#     dob *= i
#     count += 1
#     if count > 0:
#         ar = sum/count
#     else:
#         print("ERROR")
# print(sum)
# print(dob)
# print(ar)

# tuple1 = tuple([tuple(["ad"]), tuple([23]), tuple([3, 14]), tuple([True])])
# print(tuple1)


# count_1 = 0
# count_2 = 0
# count_3 = 0
# list1 = [random.randint(1,3) for i in range(10)]
# print(list1)
# one_set = set(list1)
# for i in one_set:
#     if i == 1:
#         count_1 += 1
#     if i == 2:
#         count_2 += 2
#     if i == 3:
#         count_3 += 3
# if count_1 > count_2:
#     if count_1 > count_3:
#         print(1)
# if count_2 > count_1:
#     if count_2 > count_3:
#         print(2)
# if count_3 > count_1:
#     if count_3 > count_2:
#         print(3)


list1 = [[2356, 45, 51], [10, 12, 76], [100, 200, 300], [400, 500, 600], [700, 800, 900]]


set1 = set(list1[0])
set2 = set(list1[1])
set3 = set(list1[2])
set4 = set(list1[3])
set5 = set(list1[4])


list2 = [set1, set2, set3, set4, set5]

tuple1 = tuple(list2)
print(tuple1)

