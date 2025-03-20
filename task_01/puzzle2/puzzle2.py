#!/usr/bin/env python3

def caesar_decrypt(ciphertext, shift):
    """Decrypt by shifting letters backward by 'shift' positions (A–Z only)."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = []
    for ch in ciphertext:
        if ch.upper() in alphabet:
            old_index = alphabet.index(ch.upper())
            new_index = (old_index - shift) % 26
            # Preserve uppercase/lowercase
            new_char = alphabet[new_index] if ch.isupper() else alphabet[new_index].lower()
            plaintext.append(new_char)
    return "".join(plaintext)

def main():
    # Hard-coded ciphertext
    ciphertext = "QBBJXUMEHBTYIQIJQWUQDTQBBJXUCUDQDTMECUDCUHUBOFBQOUHI"
    
    # Remove any spaces (not strictly necessary, but just in case)
    ciphertext_no_spaces = ciphertext.replace(" ", "")

    print("Trying all shifts 0 through 25...\n")

    shift16_result = None

    for shift in range(26):
        candidate = caesar_decrypt(ciphertext_no_spaces, shift)
        print(f"Shift {shift:2d}: {candidate}")
        if shift == 16:
            shift16_result = candidate

    if shift16_result:
        print("\n----\n")
        print(f"At shift 16 (correct decryption), we get:\n{shift16_result}\n")

if __name__ == "__main__":
    main()
