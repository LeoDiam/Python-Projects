import io


def caesar_cipher(plaintext, shift):
    ciphertext = [chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                  for c in plaintext]
    return ''.join(ciphertext)


ciphertext = caesar_cipher('IAMSEATEDINANOFFICE', 5)
print(ciphertext)
