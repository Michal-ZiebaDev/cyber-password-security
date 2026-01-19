```python
from password_tool import password_score, password_rating

def analyze_file(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        passwords = [line.strip() for line in file.readlines() if line.strip()]

    weak = 0
    medium = 0
    strong = 0

    for pwd in passwords:
        score = password_score(pwd)
        rating = password_rating(score)

        if rating == "Weak":
            weak += 1
        elif rating == "Medium":
            medium += 1
        else:
            strong += 1

        print(f"{pwd}: {rating} ({score}/6)")

    print("\n=== Summary ===")
    print(f"Weak: {weak}")
    print(f"Medium: {medium}")
    print(f"Strong: {strong}")

def main():
    analyze_file("passwords.txt")

if __name__ == "__main__":
    main()
