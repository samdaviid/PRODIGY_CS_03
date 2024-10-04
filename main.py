import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")


    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[@$!%*?&#]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character (@$!%*?&#).")

    if strength_score == 5:
        strength = "Strong"
    elif 3 <= strength_score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")
