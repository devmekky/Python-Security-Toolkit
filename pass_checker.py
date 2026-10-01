import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("[-] Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("[-] Add uppercase letters.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("[-] Add lowercase letters.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("[-] Add numbers (0-9).")

    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("[-] Add special characters (e.g., @$!%*?&).")

    # Evaluate score
    print("-" * 50)
    print(f"Password Strength Score: {score}/5")
    if score == 5:
        print("[+] Strong Password! Excellent security.")
    elif score >= 3:
        print("[*] Moderate Password. Consider making it stronger.")
    else:
        print("[-] Weak Password. Please fix the following issues:")
        for tip in feedback:
            print(tip)
    print("-" * 50)

if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    check_password_strength(pwd)