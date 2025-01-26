"""9. String Analysis Tool
- Write a program to analyze a string:
- Count vowels, consonants, digits, and special characters.
- Reverse the string and display the result."""


def analyze_string(s):

    s = s.lower()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    digits = '0123456789'

    count_vowels = 0
    count_consonants = 0
    count_digits = 0
    count_special_characters = 0

    for char in s:
        if char in vowels:
            count_vowels += 1
        elif char in consonants:
            count_consonants += 1
        elif char in digits:
            count_digits += 1
        else:
            count_special_characters += 1

    return count_vowels, count_consonants, count_digits, count_special_characters

def reverse_string(s):
    return s[::-1]

string = input("Enter the string for analysis and reversal: ")


vowels, consonants, digits, special_characters = analyze_string(string)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_characters}")

reversed_string = reverse_string(string)
print(f"Reversed String: {reversed_string}")
