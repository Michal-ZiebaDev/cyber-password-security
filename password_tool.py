```python
import string

def password_score(password: str) -> int:
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    return score

def password_rating(score: int) -> str:
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    return "Strong"

def main():
    print("=== Cyber Password Security ===")
    password = input("Enter password to analyze: ")
    if not password:
        print("No password provided.")
        return
    score = password_score(password)
    rating = password_rating(score)
    print(f"Score: {score}/6")
    print(f"Strength: {rating}")

if __name__ == "__main__":
    main()
