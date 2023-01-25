import hashlib

def sha1(input_str):
    sha1 = hashlib.sha1()
    sha1.update(input_str.encode())
    return sha1.hexdigest()

print(sha1(input("Enter a string: ")))