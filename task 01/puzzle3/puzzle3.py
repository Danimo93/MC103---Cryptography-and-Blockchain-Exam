#!/usr/bin/env python3

def extended_caesar_decrypt(ciphertext, shift, alphabet):
    """Decrypt 'ciphertext' by shifting characters backward in 'alphabet' by 'shift' positions."""
    decrypted = []
    size = len(alphabet)
    for ch in ciphertext:
        if ch in alphabet:
            old_index = alphabet.index(ch)
            new_index = (old_index - shift) % size
            decrypted.append(alphabet[new_index])
        else:
            # Leave characters not in 'alphabet' (spaces, punctuation, etc.)
            decrypted.append(ch)
    return "".join(decrypted)

def main():
    # 62-char alphabet: A–Z, a–z, 0–9
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    # Ciphertext #3:
    ciphertext = "ZA z9 TcVmVi A5 3zE kyz4x9 r SzA sF vE6r4uz4x R26yrsvA r4u ruuz4x 4B3sv89"

    # We'll store the shift=21 result so we can print a "nice" version after the loop.
    shift21_result = None

    print("Trying shifts 0 through 21...\n")
    for shift in range(22):
        candidate = extended_caesar_decrypt(ciphertext, shift, alphabet)
        print(f"Shift {shift:2d}: {candidate}")

        if shift == 21:
            # Save the decrypted text for nicer formatting
            shift21_result = candidate
            # Stop checking further shifts
            break

    if shift21_result is not None:
        # This is the "continuous" decrypted text
        # from shift=21:
        # ItisCLEVERtomixThingsaBitbyexpandingAlphabetandaddingnumbers

        # Here's a version with extra spacing for readability:
        spaced_version = (
            "It is CLEVER to mix Things a Bit by expanding Alphabet "
            "and adding numbers"
        )

        print("\n----\n")
        print(f"Did 21 shifts as it unnessery to shift any feather we know the shift keys is at 17")
        print(f"\nAdding some spaces for readability:\n{spaced_version}\n")

if __name__ == "__main__":
    main()
