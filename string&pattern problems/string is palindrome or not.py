def is_palindrome(s):
    # Remove spaces and make lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

text = input("Enter String: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
