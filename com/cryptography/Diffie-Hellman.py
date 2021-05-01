g = 2
p = 13

for x in range(1, 13):
    print(pow(g, x), pow(g, x, p))

import random

a = random.getrandbits(256)
print(a)

alice_to_bob = pow(g, a, p)
print(alice_to_bob)
b = random.getrandbits(256)
print('b =', b)

bob_to_alice = pow(g, b, p)
print(bob_to_alice)

shared_secret_alice = pow(bob_to_alice, a, p)
print(shared_secret_alice)


shared_secret_bob = pow(alice_to_bob, b, p)
print(shared_secret_bob)
