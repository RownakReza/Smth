import random
def cointoss():
    x = random.randint(0, 1)
    outcomes = ["Heads", "Tails"]
    return outcomes[x]

t1 = cointoss()
print(t1)