import hashlib


def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


filename = input("Enter the file path: ")

file_hash = calculate_sha256(filename)

if file_hash:
    print("SHA-256:", file_hash)
else:
    print("File not found.")
