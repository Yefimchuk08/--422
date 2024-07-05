# text = input("Введи деяикй текст: ")
# count = {}

# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# print(count)

# dict1 = {
#     1 : 5,
#     2 : 7, 
#     3 : 10,
#     4 : "abc",
#     5: 18,
# }
# dict2 = {
#     3 : 7,
#     5 : 10,
#     7 : "abc",
#     4 : "abc"
# }
# list1 = list()
# dict3 = dict()
# for key, value in dict1.items():
#     if key not in dict2:
#         continue
#     if key in dict2:
#         list1.append(value)
# print(list1)

# dict1 = {
#     1 : 5,
#     2 : 7, 
#     3 : 10,
#     4 : "abc",
#     5: 18,
# }
# dict2 = {
#     3 : 7,
#     5 : 10,
#     7 : "abc",
#     4 : "abc"
# }

# dict3 = dict()
# for key, value in dict1.items():
#     if key in dict2:
#         continue
#     if key not in dict2:
#         dict3[value] = key
# print(dict3)


# dict1 = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
# dict2 = dict(sorted(dict1.items()))


# print( dict2)
# riadok = "Привіт я хочу вчити пайтон"
# dict1 = {
#     1: "Привіт",
#     2: "бути",
#     3: "хочу",
#     4: "я",
#     5: "буду",
#     6: "abc",
# }
# list1 = []

# for key, value in dict1.items():
#     if value in riadok:
#         list1.append(key)

# print(list1)

# dict1 = dict()
# list1 = [tuple([1, "a"]), tuple([2, "b"]), tuple([3, "c"])]
# for i in list1:
#     dict1.update(list1)
# print(dict1) 


# tuple_list = [(1, 'a'), (2, 'b'), (1, 'c')]

# result_dict = {}
# for key, value in tuple_list:
#     if key not in result_dict:
#         result_dict[key] = []
#     result_dict[key].append(value)

# print(result_dict)

# dict1 = {'a': [1, 2], 'b': [3, 4]}
# dict2 = {'a': [5], 'b': [6, 7]}

# result_dict = {}

# for key in dict1.keys() and dict2.keys():
#     result_dict[key] = dict1.get(key, []) + dict2.get(key, [])

# print(result_dict)



# list1 = list()
# dict1 = {
#     1: 3,
#     2: 6, 
#     3: 15,
#     4: 10,
#     5: 2,
#     6: 45,
#     7: 1,
#     8: 5
# }
# for key, value in dict1.items():
#     list1.append(value)
#     a = max(list1)
#     b = min(list1)
# print(a)
# print(b)

# list1 =list()
# dict1 = {
#     "a":{
#         "x":1,
#         "y":2
#     },
#     "b": {
#         "x":3,
#         "y":4
#     }
# }
# for key, value in dict1["a"].items():
#     list1.append(value)
# for key, value in dict1["b"].items():
#     list1.append(value)
# print(sum(list1))