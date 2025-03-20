# import hashlib, base58

# # 65-byte “pubkey” = 0x04 followed by 64 zeros
# pub = b"\x04" + b"\x00"*64

# # SHA-256
# sha = hashlib.sha256(pub).digest()

# # RIPEMD-160 of that
# rip = hashlib.new('ripemd160')
# rip.update(sha)
# keyhash = rip.digest()

# # Prepend version 0x00 and do double-SHA-256
# vh = b"\x00" + keyhash
# chk = hashlib.sha256(hashlib.sha256(vh).digest()).digest()[:4]

# # Base58Check-encode
# addr = base58.b58encode(vh + chk).decode()
# print(addr)




#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Demonstrate a "zero" uncompressed pubkey and its resulting P2PKH address

import hashlib
import base58

# For an uncompressed SEC pubkey:
# - 1 byte of 0x04 prefix
# - 32-byte X coordinate (all zeros)
# - 32-byte Y coordinate (all zeros)
# => 1 + 32 + 32 = 65 bytes in total => 130 hex characters
pubkey = '04' + ('00' * 64)  # That is 2 hex chars + 128 hex chars => 130 total => 65 bytes

compress_pubkey = False

def hash160(data_bytes):
    """Perform SHA-256 followed by RIPEMD-160."""
    sha = hashlib.sha256(data_bytes).digest()
    rip = hashlib.new('ripemd160')
    rip.update(sha)
    print("key_hash =       ", rip.hexdigest())
    return rip.hexdigest()

if compress_pubkey:
    # (Meaningless in a "zero" scenario, but left here for completeness.)
    last_byte = int(pubkey[-2:], 16)  # Get final byte in hex
    prefix = '02' if ((last_byte % 2) == 0) else '03'
    # Compressed: prefix + X coord
    pubkey_compressed = prefix + pubkey[2:66]
    pubkey_bytes = bytearray.fromhex(pubkey_compressed)
else:
    pubkey_bytes = bytearray.fromhex(pubkey)

# 1. Hash160 of pubkey
h160_str = hash160(pubkey_bytes)

# 2. Add version byte 0x00 in front (mainnet)
versioned_payload = '00' + h160_str

# 3. Double-SHA-256 => get checksum (first 4 bytes)
stage1 = hashlib.sha256(bytearray.fromhex(versioned_payload)).digest()
stage2 = hashlib.sha256(stage1).hexdigest()
checksum = stage2[:8]

print("checksum =       ", stage2)
print("key_hash + checksum = ", versioned_payload, checksum)

# 4. Base58Check-encode
final_bytes = bytearray.fromhex(versioned_payload + checksum)
btc_address = base58.b58encode(final_bytes).decode('utf-8')
print("bitcoin address =", btc_address)

