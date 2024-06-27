import random


list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

print("List 1:", list1)
print("List 2:", list2)


list3 = list1 + list2
print("Combined List:", list3)


list4 = []
for i in list1 + list2:
    if i not in list4:
        list4.append(i)
print("Combined Unique List:", list4)


list5 = []
for a in list1:
    if i in list2 and a not in list5:
        list5.append(i)
print("Common Elements List:", list5)


list6 = []
for i in list1:
    if i not in list2:
        list6.append(i)
for i in list2:
    if i not in list1:
        list6.append(i)
print("Unique Elements List:", list6)


min_max_list = [min(list1), max(list1), min(list2), max(list2)]
print("Min and Max Elements List:", min_max_list)
