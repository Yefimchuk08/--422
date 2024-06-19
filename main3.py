count_five = 0
a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))
for i in range(a,b+1,1):
    print(i)
if (a<b):
    for a in range(b,a,-1):
        print(a)
for s in range(a,b+1,1):
    if(s%7!=0):
        continue
    print(s)
for d in range(a,b+1,1):
    if (d%5==0):
        count_five += 1
        print(count_five)
