import re


COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "football", "1234567", "letmein",
    "iloveyou", "admin", "welcome", "monkey", "login"
}


def check_password_strength(pwd: str) -> dict:
    """
    Vérifie la robustesse d'un mot de passe selon plusieurs critères :
      - longueur minimale (>= 12)
      - présence d'au moins une majuscule, une minuscule, un chiffre, un symbole
      - le mot de passe n'est pas trop commun (pas dans COMMON_PASSWORDS)

    Retourne un dict contenant :
      - "password" : le mot de passe testé
      - "score"    : entier de 0 à 6
      - "details"  : dict des booléens pour chaque critère
      - "verdict"  : chaîne ("Très fort", "Fort", "Moyen" ou "Faible")
    """
    details = {
        "length_ok": False,
        "has_upper": False,
        "has_lower": False,
        "has_digit": False,
        "has_symbol": False,
        "not_common": False,
    }


    if len(pwd) >= 12:
        details["length_ok"] = True


    if re.search(r"[A-Z]", pwd):
        details["has_upper"] = True
    if re.search(r"[a-z]", pwd):
        details["has_lower"] = True
    if re.search(r"[0-9]", pwd):
        details["has_digit"] = True
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-\[\]\\\/`~'+=;]", pwd):
        details["has_symbol"] = True

    if pwd.lower() not in COMMON_PASSWORDS:
        details["not_common"] = True


    score = sum(details.values())


    if score == 6:
        verdict = "Très fort"
    elif 4 <= score < 6:
        verdict = "Fort"
    elif 2 <= score < 4:
        verdict = "Moyen"
    else:
        verdict = "Faible"

    return {
        "password": pwd,
        "score": score,
        "details": details,
        "verdict": verdict
    }


if __name__ == "__main__":
 
    mots_de_test = [
        "password123",
        "Azerty!2025",
        "CorrectHorseBatteryStaple!",
        "P@55w0rd",
        "Tr0ub4dor&3",
        "MonMotDePasseTropSimple",
        "S3curit3_Passw0rd2025!"
    ]

    for m in mots_de_test:
        result = check_password_strength(m)
        print(f"Mot de passe testé : {m!r}")
        print(f"  - Score     : {result['score']} / 6")
        print(f"  - Détails   :")
        for critere, ok in result["details"].items():
            statut = "✓" if ok else "✗"
            print(f"      {critere:12s} : {statut}")
        print(f"  → Verdict   : {result['verdict']}\n")
