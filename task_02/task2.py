#!/usr/bin/env python3

def xor_cipher(text, key):
    """XOR each character in 'text' with the integer 'key'."""
    output = []
    for ch in text:
        xored_code = ord(ch) ^ key
        output.append(chr(xored_code))
    return "".join(output)

def main():
    ciphertext = "Wkf#rvj`h#aqltm#el{#ivnsp#lufq#wkf#obyz#gld#bmg#ab`h-"
    key = 3
    
    plaintext = xor_cipher(ciphertext, key)
    print("Ciphertext:", ciphertext)
    print("Key:", key)
    print("\nDecrypted plaintext:")
    print(plaintext)
    
    encrypted_again = xor_cipher(plaintext, key)
    print("\nEncrypting the plaintext again with the same key:")
    print(encrypted_again)
    print("\n(Should match the original ciphertext)")

if __name__ == "__main__":
    main()
