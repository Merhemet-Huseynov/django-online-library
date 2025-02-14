import random

__all__ = ["generate_verification_code"]


def generate_verification_code() -> str:
    code = str(random.randint(100000, 999999))
    return code