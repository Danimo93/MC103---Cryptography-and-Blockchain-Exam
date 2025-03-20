#!/usr/bin/env python3

def extended_caesar_decrypt_maketrans(ciphertext, shift, alphabet):
    """Use maketrans/translate to shift characters in 'alphabet' backward by 'shift'."""
    rotated_alphabet = alphabet[-shift:] + alphabet[:-shift]
    translation_table = str.maketrans(alphabet, rotated_alphabet)
    return ciphertext.translate(translation_table)

def main():
    # 62-character custom alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    # Ciphertext
    ciphertext = (
        "ZA z9 TcVmVi A5 3zE kyz4x9 r SzA sF vE6r4uz4x R26yrsvA "
        "r4u ruuz4x 4B3sv89"
    )

    correct_shift = None
    correct_plaintext = None
    
    # Try shifts 0 through 61
    for shift in range(len(alphabet)):
        candidate = extended_caesar_decrypt_maketrans(ciphertext, shift, alphabet)
        print(f"Shift {shift:2d}: {candidate}")
        if candidate.startswith("It is CLEVER to mix"):
            correct_shift = shift
            correct_plaintext = candidate
            break

    print("\n----\n")
    if correct_shift is not None:
        print(f"Found correct shift = {correct_shift}")
        print(f"Decrypted message:\n{correct_plaintext}\n")
    else:
        print("No matching plaintext found.")

if __name__ == "__main__":
    main()
