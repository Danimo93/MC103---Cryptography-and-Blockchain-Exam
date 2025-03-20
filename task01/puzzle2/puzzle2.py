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
            if ch.isupper():
                plaintext.append(alphabet[new_index])
            else:
                plaintext.append(alphabet[new_index].lower())
        else:
            # Ignore non-alpha chars
            pass
    return "".join(plaintext)

def main():
    # Hard-coded ciphertext #2 (no user input):
    ciphertext = "QBBJXUMEHBTYIQIJQWUQDTQBBJXUCUDQDTMECUDCUHUBOFBQOUHI"
    
    # Remove spaces, if any. (Here, there are none, so this is optional.)
    ciphertext_no_spaces = ciphertext.replace(" ", "")

    print("Trying all shifts 0 through 25...\n")

    # We'll store the result for shift=16 so we can show it nicely at the end.
    shift16_result = None

    for shift in range(26):
        candidate = caesar_decrypt(ciphertext_no_spaces, shift)
        print(f"Shift {shift:2d}: {candidate}")
        
        # Check if this is shift=16; store the result for nice formatting.
        if shift == 16:
            shift16_result = candidate

    # After printing all shifts, show the nicely spaced version of shift=16
    if shift16_result:
        # Nicely spaced version:
        spaced_version = (
            "ALL THE WORLD IS A STAGE AND ALL THE MEN AND WOMEN MERELY PLAYERS"
        )

        print("\n----\n")
        print(f"At shift 16 (correct decryption), we get:\n{shift16_result}")
        print(f"\nAdding some spaces for readability:\n{spaced_version}\n")

if __name__ == "__main__":
    main()
