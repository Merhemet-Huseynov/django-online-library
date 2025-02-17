import random
import logging

__all__ = ["generate_verification_code"]

logger = logging.getLogger(__name__)


def generate_verification_code() -> str:
    code = str(random.randint(100000, 999999))
    logger.info(f"Generated verification code: {code}")
    return code