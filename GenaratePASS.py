import random
import string

def GenaratePASS():
    all_word = string.ascii_letters + string.digits + string.punctuation
    for i in range(10):
        password = []
        for j in range(12):
            word=random.choice(all_word)
            password.append(word)
        print(''.join(password))

GenaratePASS()
