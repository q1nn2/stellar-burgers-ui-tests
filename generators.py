import random
import string

from data import COHORT_NUMBER, EMAIL_DOMAIN


def generate_login():
    number = random.randint(100, 999)
    return f"anatoly_el_{COHORT_NUMBER}_{number}@{EMAIL_DOMAIN}"


def generate_password(length=8):
    """Генерирует пароль заданной длины."""
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))
