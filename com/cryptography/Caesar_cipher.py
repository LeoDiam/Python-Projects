import io


def caesar_cipher(plaintext, shift):
    ciphertext = [chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                  for c in plaintext]
    return ''.join(ciphertext)


ciphertext = caesar_cipher('MELENEODYSSEA', 5)
print(ciphertext)
print('Decryption:', caesar_cipher(ciphertext,-5))
