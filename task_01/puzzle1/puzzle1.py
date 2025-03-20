#!/usr/bin/env python3

def caesar_decrypt(ciphertext, shift):
    """Decrypt by shifting letters backward by 'shift' positions (A–Z only)."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = []
    for ch in ciphertext:
        if ch.upper() in alphabet:
            old_index = alphabet.index(ch.upper())
            new_index = (old_index - shift) % 26
            # Preserve case
            plaintext.append(alphabet[new_index] if ch.isupper()
                             else alphabet[new_index].lower())
        else:
            # Ignore non-alphabetic characters
            pass
    return "".join(plaintext)

def main():
    # Ciphertext #1
    ciphertext = "IJKLE LWPZQ LRTCW QFWWZ QDZFY OLYOQ FCJDT RYTQJ TYRYZ ESTYR"
    
    # Remove spaces so old spacing doesn't carry over
    ciphertext_no_spaces = ciphertext.replace(" ", "")

    print("Trying all shifts from 0 to 25...\n")
    correct_decryption = None
    
    for shift in range(26):
        candidate = caesar_decrypt(ciphertext_no_spaces, shift)
        print(f"Shift {shift:2d}: {candidate}")
        
        # If we already know the correct shift is 11, we can capture it:
        if shift == 11:
            correct_decryption = candidate

    # Print the known correct answer:
    if correct_decryption:
        print("\n----\n")
        print(f"CORRECT SHIFT = 11\nDECRYPTION: {correct_decryption}")
        print("----")

if __name__ == "__main__":
    main()
