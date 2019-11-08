import random
import string

def get_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))

