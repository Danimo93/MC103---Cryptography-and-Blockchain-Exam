import hashlib
import base58

# Uncompressed pubkey: 0x04 + 64 zero bytes for X & Y coordinates
pubkey = '04' + ('00' * 64)
compress_pubkey = False

def hash160(data_bytes):
    """SHA-256 -> RIPEMD-160."""
    sha = hashlib.sha256(data_bytes).digest()
    rip = hashlib.new('ripemd160')
    rip.update(sha)
    print("key_hash =", rip.hexdigest())
    return rip.hexdigest()

if compress_pubkey:
    # Compressed pubkey: prefix 0x02 or 0x03 + X coord
    last_byte = int(pubkey[-2:], 16)
    prefix = '02' if (last_byte % 2 == 0) else '03'
    pubkey_bytes = bytearray.fromhex(prefix + pubkey[2:66])
else:
    # Uncompressed pubkey: full 65 bytes
    pubkey_bytes = bytearray.fromhex(pubkey)

# 1) HASH160 of pubkey
h160_str = hash160(pubkey_bytes)

# 2) Prepend version byte 0x00 (mainnet)
versioned_payload = '00' + h160_str

# 3) Double SHA-256 => 4-byte checksum
stage1 = hashlib.sha256(bytearray.fromhex(versioned_payload)).digest()
stage2 = hashlib.sha256(stage1).hexdigest()
checksum = stage2[:8]

print("checksum =", stage2)
print("payload + checksum =", versioned_payload, checksum)

# 4) Base58Check encode
final_bytes = bytearray.fromhex(versioned_payload + checksum)
btc_address = base58.b58encode(final_bytes).decode('utf-8')

print("Bitcoin address =", btc_address)
