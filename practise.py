# #Q Multiplication of table
a=int(input("Enter a number"))
for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")



# Q Generate prime number from 1 to 50

for num in range(2, 51):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")

# # Q.write a program to find largest upon three numbers using nested loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b and a>c :
    print(f"{a} is greater number:")
elif b>a and b>c:
    print(f"{b} is greater number:")
else:
    print(f"{c} is greater number:")

# #Q if number is divisible by 3 and 5
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 3 == 0:
    print("The number is divisible by both 5 and 3.")
else:
    print("The number is not divisible by both 5 and 3.")



# #Q. first n natural number by using while loop 


n = int(input("Enter the value of n: "))
i = 1
print(f"First {n} natural numbers:")
while i <= n:
    print(i, end=" ")
    i += 1

# #Q.use break statement



for num in range(2, 51):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
