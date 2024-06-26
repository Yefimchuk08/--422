# riadok = input("Введіть рядок: ")
# string = riadok.replace(" ", "").lower()


# is_palindrome = string == string[::-1]

# if is_palindrome:
#     print("Введений рядок є паліндромом.")
# else:
#     print("Введений рядок не є паліндромом.")



# def replace_reserved_words(text, reserved_words):
#     words = text.split()
#     for i in range(len(words)):
#         if words[i].lower() in reserved_words:
#             words[i] = words[i].upper()
#     return ' '.join(words)
# text = input("Введіть текст: ")
# reserved_words_input = input("Введіть зарезервовані слова через кому: ")
# reserved_words = {word.strip().lower() for word in reserved_words_input.split(',')}
# result = replace_reserved_words(text, reserved_words)
# print("Змінений текст: ", result)




# sentenses = 0
# text = input("Введи деякий декст для того щоб я порахував кількість речень в ньому: ")
# for i in text:
#     if(i == "." ):
#         sentenses += 1
#     elif(i == "!"):
#         sentenses += 1
#     elif(i == "?"):
#         sentenses += 1
# print(sentenses) 

# a = int(input("Введи перше число: "))
# b = int(input("Введи друге число: "))
# c = input("Введи операцію: ")
# if (c == "+"):
#     print(a+b)
# elif(c == "-"):
#     print(a-b)
# elif(c == "*"):
#     print(a*b)
# elif(c == "/"):
#     print(a/b)
# else:
#     print("Error")