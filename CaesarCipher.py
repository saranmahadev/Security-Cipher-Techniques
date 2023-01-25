def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        ch = message[i]
        if ch.isalpha():
            ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        encrypted_message += ch
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        ch = encrypted_message[i]
        if ch.isalpha():
            ch = chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        decrypted_message += ch
    return decrypted_message

message = input("Enter a message: ")
key = int(input("Enter a key: "))
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
