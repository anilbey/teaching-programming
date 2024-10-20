# Problem: Is Prime?
num = int(input("Enter a number: "))
i = 2
result = True
while i < num:
    if num % i == 0:
        result = False
        break
    i += 1
print(result)
