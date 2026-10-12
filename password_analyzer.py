
import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123",
}

COMMON_WORDS = (
    "password",
    "admin",
    "welcome",
    "qwerty",
    "letmein",
    "iloveyou",
)

SEQUENCES = (
    "0123456789",
    "abcdefghijklmnopqrstuvwxyz",
)


def detect_patterns(password):
    """Detect common and predictable password patterns."""
    findings = []
    normalized = password.lower()

    # Check known common passwords
    if normalized in COMMON_PASSWORDS:
        findings.append("Common password detected.")

    # Check common words in combinations such as Password123!
    if any(word in normalized for word in COMMON_WORDS):
        findings.append("Predictable word or password combination detected.")

    # Check for four or more identical consecutive characters
    if any(
        password[i] == password[i + 1] == password[i + 2] == password[i + 3]
        for i in range(len(password) - 3)
    ):
        findings.append("Repeated-character pattern detected.")

    # Check for four-character ascending or descending sequences
    for sequence in SEQUENCES:
        if any(
            sequence[i:i + 4] in normalized
            or sequence[i:i + 4][::-1] in normalized
            for i in range(len(sequence) - 3)
        ):
            findings.append("Sequential-character pattern detected.")
            break

    return findings



def analyze_password(password):
    score = 0
    recommendations = []

    # 1. Evaluate password length
    if len(password) >= 16:
        score += 40
    elif len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        recommendations.append(
            "Use a longer password, ideally 16 or more characters."
        )

    # 2. Evaluate character diversity
    if any(char.islower() for char in password):
        score += 10
    else:
        recommendations.append("Consider including lowercase letters.")

    if any(char.isupper() for char in password):
        score += 10
    else:
        recommendations.append("Consider including uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 10
    else:
        recommendations.append("Consider including numbers.")

    if any(char in string.punctuation for char in password):
        score += 10
    else:
        recommendations.append("Consider including special characters.")

    # 3. Detect predictable patterns
    patterns = detect_patterns(password)

    if "Common password detected." in patterns:
        score -= 50
        recommendations.append(
            "Avoid commonly used passwords."
        )

    if "Predictable word or password combination detected." in patterns:
        score -= 25
        recommendations.append(
            "Avoid common words and predictable combinations."
        )

    if "Repeated-character pattern detected." in patterns:
        score -= 20
        recommendations.append(
            "Avoid long runs of repeated characters."
        )

    if "Sequential-character pattern detected." in patterns:
        score -= 20
        recommendations.append(
            "Avoid predictable letter or number sequences."
        )

    # 4. Keep score within the permitted range
    score = max(0, min(score, 100))

    # 5. Classify strength
    if password.lower() in COMMON_PASSWORDS or len(password) == 0:
        strength = "Weak"
    elif patterns:
        strength = "Medium" if score >= 40 else "Weak"
    elif score >= 70:
        strength = "Strong"
    elif score >= 40:
        strength = "Medium"
    else:
        strength = "Weak"

    # 6. Provide a fallback recommendation
    if not recommendations:
        recommendations.append(
            "No listed issues detected. This does not guarantee security."
        )

    return {
        "score": score,
        "strength": strength,
        "patterns": patterns,
        "recommendations": recommendations,
    }

if __name__ == "__main__":
    password = input("Enter a sample password to analyze: ")
    result = analyze_password(password)

    print("\n--- Password Security Report ---")
    print(f"Score: {result['score']}/100")
    print(f"Strength: {result['strength']}")

    print("\nPattern Detection:")
    if result["patterns"]:
        for pattern in result["patterns"]:
            print(f"- {pattern}")
    else:
        print("- No listed predictable patterns detected.")

    print("\nSecurity Recommendations:")
    for recommendation in result["recommendations"]:
        print(f"- {recommendation}")
