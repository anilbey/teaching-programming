# Problem: Check if a String is a Palindrome
s = input("Enter a string: ")

length = len(s)
is_palindrome = True
i = 0

while i < length // 2:
    if s[i] != s[length - i - 1]:
        is_palindrome = False
        break
    i += 1

print(is_palindrome)
