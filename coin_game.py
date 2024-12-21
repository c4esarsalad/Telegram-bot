import random

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    
print(flip_coin())
print(gen_emodji())