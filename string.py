# Problem: Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("prerana")) 

# Problem: Check if two strings are anagrams
def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("listen", "silent")) 