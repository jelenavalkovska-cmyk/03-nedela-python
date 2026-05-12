import re
from datetime import datetime


# 1. Pārbauda, vai teksts satur @ un .
def is_email(text):
    return "@" in text and "." in text

# 2. Pārbauda, vai sākas ar +371 un seko tieši 8 cipari
def is_telephone_number(text):
    # Izmantojam regulāro izteiksmi precizitātei
    # ^+371 - jāsākas ar +371
    # \d{8}$ - jābeidzas ar tieši 8 cipariem
    return bool(re.match(r'^\+371\d{8}$', text))

# 3. Pārbauda, vai skaitlis ir integer un robežās no 0 līdz 150
def is_valid_age(age):
    if isinstance(age, int):
        return 0 <= age <= 150
    return False

# 4. Pārbauda: vai parolei ir vismaz 8 simboli, satur burtus UN ciparus
def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    return has_letter and has_digit

# 5. Pārbauda datuma formātu yyyy-mm-dd
def is_valid_date(date_text):
    try:
        # Mēģina noparsēt tekstu atbilstoši formātam
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        # Ja formāts nav pareizs vai datums nav eksistējošs (piem. 31. februāris)
        return False

# --- Pārbaudes piemēri ---

if __name__ == "__main__":
    print(f"E-pasts: {is_email('janis@piemers.lv')}")
    print(f"Telefons: {is_telephone_number('+37120000000')}")
    print(f"Vecums: {is_valid_age(25)}")
    print(f"Parole: {is_strong_password('DroshaParole123')}")
    print(f"Datums: {is_valid_date('2023-12-31')}")