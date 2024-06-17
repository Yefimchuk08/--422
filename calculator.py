from tkinter import*
import math

# root = Tk()
# root.title = "Calculator"
# root.geometry = "600x600"
# root.background = "#ffffff"

login = str("admin")
login = input("Enter your login: ")

if (login == "admin"):
    print("Okey. You did it")
else:
    print("Invalid login.")


password = input("Enter a password: ")

if len(password) > 8:
   if any(c.isalpha() for c in password):
       print("Valid password.")
   else:
       print("Invalid password. Must contain letters.")
else:
   print("Invalid password. Must be longer than 8 characters.")

a = float(input("Введи перше число"))
b = float(input("Введи друге число"))


print("1 - додавання")
print("2 - віднімання")
print("3 - множення")
print("4 - ділення")
print("5 - ділення націло")
print("6 - залишок від ділення")
print("7 - підняття до степення")

number = int(input("Enter one number and you can calculate: "))

if(number == 1):
    print("Your answer: ", a+b)

if(number == 2):
    print("Your answer: ", a-b)

if(number == 3):
    print("Your answer: ", a*b)

if(number == 4):
    print("Your answer: ", a/b)

if(number == 5):
    print("Your answer: ", a//b)

if(number == 6):
    print("Your answer: ", a%b)

if(number == 7):
    c = int(input("Введи до якого степення треба підняти число: "))
    d = int(input("Введи яке саме число треба підняти до степення 1 чи 2 :"))
    if (d == 1):
        print("Your answer: ", a**c)
    if (d == 2):
        print("Your answer: ", b**c)
    else:
        print("Error!!!!!!!!!")

if(number > 7):
    print("Error")