import hashlib

text = input("Enter text to hash: ")

sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("SHA-256:", sha256_hash)
