#!/usr/bin/env python3

def rail_fence_decrypt(ciphertext, rails):
    """
    Decrypts 'ciphertext' using a Rail Fence Cipher with the given number of 'rails'.
    Only letters are used (and made lowercase); spaces/punctuation are ignored.
    """
    # 1) Clean up the ciphertext: keep only A–Z letters, force lowercase
    text = "".join(ch for ch in ciphertext if ch.isalpha()).lower()
    length = len(text)

    # 2) Build the 'zig-zag' pattern (which row each character belongs to)
    pattern = []
    row = 0
    direction = 1  # +1 means "down" the rails, -1 means "up"
    for _ in range(length):
        pattern.append(row)
        row += direction
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

    # 3) Count how many letters go in each row
    row_counts = [0] * rails
    for r in pattern:
        row_counts[r] += 1

    # 4) Split the cleaned text across each row
    rows = []
    idx = 0
    for count in row_counts:
        rows.append(list(text[idx : idx + count]))
        idx += count

    # 5) Rebuild the plaintext by following the zig-zag pattern
    decrypted = []
    for r in pattern:
        decrypted.append(rows[r].pop(0))

    return "".join(decrypted)

def main():
    # Ciphertext #5, hard-coded:
    ciphertext = "Teu cgeno jmsvr hlz dghqi kref xup oete ayo"
    
    # We'll try rails from 2 up to, say, 10
    print("Trying rail counts from 2 to 10...\n")
    best_rails = None
    best_text = None

    for rails in range(2, 11):
        result = rail_fence_decrypt(ciphertext, rails)
        print(f"Rails={rails}: {result}")
        
        # If you KNOW rails=2 is correct, you can store it:
        if rails == 2:
            best_rails = 2
            best_text = result

    # Finally, if you want to highlight rails=2 at the end:
    if best_rails:
        print("\n----\n"
              f"** The best decryption (rails={best_rails}) is:\n{best_text}\n")

if __name__ == "__main__":
    main()
