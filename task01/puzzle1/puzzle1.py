#!/usr/bin/env python3

def caesar_decrypt(ciphertext, shift):
    """Decrypt by shifting letters backward by 'shift' positions (A–Z only)."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = []
    for ch in ciphertext:
        if ch.upper() in alphabet:
            old_index = alphabet.index(ch.upper())
            new_index = (old_index - shift) % 26
            if ch.isupper():
                plaintext.append(alphabet[new_index])
            else:
                plaintext.append(alphabet[new_index].lower())
        else:
            # Ignore non-alphabetic characters
            pass
    return "".join(plaintext)

def main():
    # Hard-coded ciphertext #1 (no user input)
    ciphertext = "IJKLE LWPZQ LRTCW QFWWZ QDZFY OLYOQ FCJDT RYTQJ TYRYZ ESTYR"
    
    # Remove all spaces so the spacing from the original blocks doesn't carry over
    ciphertext_no_spaces = ciphertext.replace(" ", "")

    print("Trying all shifts 0 through 25...\n")
    
    # We’ll keep track of what shift=11 produces, so we can re-print it later.
    shift11_result = None
    
    for shift in range(26):
        candidate = caesar_decrypt(ciphertext_no_spaces, shift)
        print(f"Shift {shift:2d}: {candidate}")
        
        if shift == 11:
            shift11_result = candidate

    # Once we've looped, if we found the shift=11 text, let's print it nicely spaced.
    if shift11_result:
        # This is the spaced version you want to show:
        spaced_version = "XYZ A TALE OF A GIRL FULL OF SOUND AND FURY SIGNIFYING NOTHING"
        print("\n----\n")
        print(f"At shift 11 (correct decryption), we have:\n{shift11_result}")
        print(f"\nAdding some spaces for readability:\n{spaced_version}\n")

if __name__ == "__main__":
    main()
