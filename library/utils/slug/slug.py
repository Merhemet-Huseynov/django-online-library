import re

__all__ = ["convert_to_slug"]


AZERBAIJANI_TO_LATIN = {
    "ş": "s",
    "ə": "e", 
    "ı": "i", 
    "ç": "c", 
    "ğ": "g", 
    "ö": "o", 
    "ü": "u",
    "Ş": "S", 
    "Ə": "E", 
    "İ": "I", 
    "Ç": "C", 
    "Ğ": "G", 
    "Ö": "O", 
    "Ü": "U"
}

def convert_to_slug(text):
   
    for az_letter, lat_letter in AZERBAIJANI_TO_LATIN.items():
        text = text.replace(az_letter, lat_letter)

    text = text.lower()
    text = re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9-]", "-", text))

    return text.strip("-")
