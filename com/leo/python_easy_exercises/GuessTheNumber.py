import random


def guess(x):
    random_num = random.randint(1, 20)
    if random_num is x:
        print("Great")
    else:
        print("Maybe next time.The number was " + random_num.__str__())


guess(int(input()))

