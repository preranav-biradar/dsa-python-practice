# Problem:  string is a palindrome or not
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))