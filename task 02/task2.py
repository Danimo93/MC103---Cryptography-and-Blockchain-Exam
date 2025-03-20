#!/usr/bin/env python3

def xor_cipher(text, key):
    """
    XOR each character in 'text' with the integer 'key'.
    XOR-ing twice with the same key returns the original text.
    """
    output = []
    for ch in text:
        # XOR this character's code point with the key
        xored_code = ord(ch) ^ key
        # Convert back to a character
        output.append(chr(xored_code))
    return "".join(output)

def main():
    # Example ciphertext from your screenshot:
    ciphertext = "Wkf#rvj`h#aqltm#el{#ivnsp#lufq#wkf#obyz#gld#bmg#ab`h-"
    # Example single integer key:
    key = 3

    # Decrypt
    plaintext = xor_cipher(ciphertext, key)
    
    # Print results
    print("Ciphertext:", ciphertext)
    print("Key:", key)
    print("\nDecrypted plaintext:")
    print(plaintext)

    # If you also want to re-encrypt, do:
    encrypted_again = xor_cipher(plaintext, key)
    print("\nEncrypting the plaintext again with the same key:")
    print(encrypted_again)
    print("\n(Should match the original ciphertext)")


if __name__ == "__main__":
    main()
