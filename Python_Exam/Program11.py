"""11. Password Strength Checker
- Develop a program to check the strength of a password:
- Criteria: At least 8 characters, includes uppercase, lowercase, digits, and special
characters."""

def password_checker_for_eightcharectors_include_upper_lower_digits_special(n):
    if len(n)>=8:
        if(any(c.islower() for c in n) and any(c.isupper() for c in n) and any(c.isdigit() for c in n) and any(c in"!@#$%^&*()_+-={}:<>?/" for c in n)):
            return True
        else:
            return False
s=input('Enter the Password')
if password_checker_for_eightcharectors_include_upper_lower_digits_special(s):
    print(f"{s} is a valid password")
else:
    print(f"{s} is not a valid password")