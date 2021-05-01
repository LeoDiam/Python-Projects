def ord0(c):
    return ord(c) - ord('A')


def otpad_encrypt(plaintext, randomtext):
    encrypted = [chr((ord0(c) + ord0(r)) % 26 + ord('A'))
                 for c, r in zip(plaintext, randomtext)]
    return ''.join(encrypted)


plaintext = "IFYOUREALLYWANTTO"
randomtext = "RDUUWJEMCJJXZDOWJ"

ciphertext = otpad_encrypt(plaintext, randomtext)
print(ciphertext)


def otpad_decrypt(ciphertext, randomtext):
    decrypted = [chr((ord0(c) - ord0(r)) % 26 + ord('A'))
                 for c, r in zip(ciphertext, randomtext)]
    return ''.join(decrypted)


plaintext = otpad_decrypt(ciphertext, randomtext)
print(plaintext)
