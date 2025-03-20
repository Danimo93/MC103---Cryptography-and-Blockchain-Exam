#!/usr/bin/env python3
import hashlib

# We have four names:
names = ["Mariusz", "Sarah", "Fabian", "Daniel"]

# (a) SHA-1 target
target_sha1 = "3b472fb496e7185001072f414b34f91b252a982e"

# (b) MD5 target
target_md5 = "262031397020fd8df478ec13b4b096c5"

# --- (a) Which name hashes to the given SHA-1? ---
found_name_sha1 = None
print("=== (a) Checking SHA-1 ===")
for nm in names:
    sha1_hash = hashlib.sha1(nm.encode()).hexdigest()
    print(f"{nm} => SHA-1: {sha1_hash}")
    if sha1_hash == target_sha1:
        found_name_sha1 = nm

if found_name_sha1:
    print(f"\n** FOUND (a): '{found_name_sha1}' matches SHA-1: {target_sha1}")
else:
    print("\n** No match found for the given SHA-1.")

# --- (b) Which name hashes to the given MD5? ---
found_name_md5 = None
print("\n=== (b) Checking MD5 ===")
for nm in names:
    md5_hash = hashlib.md5(nm.encode()).hexdigest()
    print(f"{nm} => MD5: {md5_hash}")
    if md5_hash == target_md5:
        found_name_md5 = nm

if found_name_md5:
    print(f"\n** FOUND (b): '{found_name_md5}' matches MD5: {target_md5}")
else:
    print("\n** No match found for the given MD5.")

# --- (c) SHA-256 of "Mariusz" ---
print("\n=== (c) SHA-256('Mariusz') ===")
mariusz_sha256 = hashlib.sha256("Mariusz".encode()).hexdigest()
print(f"SHA-256('Mariusz') = {mariusz_sha256}")

# --- (d) RIPEMD-160 of "Fabian" ---
print("\n=== (d) RIPEMD-160('Fabian') ===")
try:
    ripemd160_hasher = hashlib.new('ripemd160')
    ripemd160_hasher.update("Fabian".encode())
    fabian_ripemd160 = ripemd160_hasher.hexdigest()
    print(f"RIPEMD-160('Fabian') = {fabian_ripemd160}")
except ValueError:
    print("RIPEMD-160 is not supported in this Python environment.")

# --- (e) Bit length of the given hash ---
given_hash = "408d890298c4963dfaac2e8b508552b9e1ee8048"
hex_len = len(given_hash)
bit_len = hex_len * 4

print("\n=== (e) Hash Length in Bits ===")
print(f"Hash given: {given_hash}")
print(f"Hex characters: {hex_len}")
print(f"Bit length: {bit_len}")
print("Why? Each hex digit = 4 bits, so 40 hex digits × 4 = 160 bits.")
print("SHA-1 and RIPEMD-160 both produce 160-bit hashes.\n")
