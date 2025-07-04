# sum=0

# for i in range (101) :
#     sum += i
# print (sum)


# for i in range(100, 0, -1) :
#   print(i)

# number=int(input("Enter the number: "))

# for hello in range(11) :
#     print(hello*number)


for i in range (1, 101) :
    x=str(i)
    if i % 3 == 0: 
       x += " foo"

    if i % 5 == 0:
       x += " bar"

    if i % 10 == 0:
       x += " hello"

    print(x)