A = int(input("Enter an integer: "))
sum = 0
for i in range(1, A + 1):
    if i % 2 == 0:
        sum += i
print("Sum of even numbers between 1 and", A, "is:", sum)