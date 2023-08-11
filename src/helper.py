import string
import random


def generate_text(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def generate_email():
    return generate_text(7) + "@gmail.com"
