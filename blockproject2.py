import re

def check_password_strength(password: str) -> str:
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if criteria_met <= 2:
        return "Weak"
    elif criteria_met == 3 or criteria_met == 4:
        return "Good"
    else:
        return "Strong"

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")