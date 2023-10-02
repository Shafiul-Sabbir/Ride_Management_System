import hashlib

data = "a".encode()  # Bytes-like object to be hashed
# data = data.encode()
# Create an MD5 hash object
md5_hash = hashlib.md5(data)
md5_digest = md5_hash.hexdigest()

# Create a SHA-256 hash object
sha256_hash = hashlib.sha256(data)
sha256_digest = sha256_hash.hexdigest()

print(f"MD5 Digest: {md5_digest}")
print(f"SHA-256 Digest: {sha256_digest}")
