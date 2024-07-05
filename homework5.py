# def showMN(list1):
#     dobutok  = 1
#     for i in list1:
#         dobutok *= i
#     print(dobutok)
# showMN([1,2,3,4,5,6])


# def dobutok(list1):
#     for i in list1:
#         a =  min(list1)
#     print(a)
# dobutok([5,2,3,4,5,6])

# def essyNum(list1):
#     count = 0
#     for i in list1:
#         if i%1==0:
#             if i%i==0:
#                 count+=1
#     print(count)
# essyNum([0.25, 5, 7 ,9 , 6.5])

# def removeNum(list1):
#     remove_count = 0
#     a = int(input("ВВеди число яке треба видалити: "))
#     if a not in list1: 
#         print("error")
#     if a in list1:
#         for i in list1:
#             list1.remove(a)
#             remove_count+=1
#         print(remove_count)

# removeNum([1,1,1,2,1,2,1,2,2,])

# def listToList(list1, list2):
#     list3 = list()
#     list3 = [list1 + list2]
#     print(list3)
# listToList([1,2,3,4,5,6,7,7], [8,7,6,5,4,3,2,1,1])

# def rang(list1, rang):
#     list2 = list()
#     for i in list1:
#         list2.append(i**rang)
#     print(list2)
# rang([1,2,3,4,5,6,7,8], 3)