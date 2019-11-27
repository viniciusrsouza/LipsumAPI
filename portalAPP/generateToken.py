import random
import string
from .models import TokenAuth

def get_token():
    tk = ''
    while True:
        tk = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))
        token_auth = TokenAuth(token=tk)
        try:
            token_auth.save()
            break
        except:
            pass
    return tk

