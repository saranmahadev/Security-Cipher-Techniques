def vigenere_cipher(text, key):
    text = text.upper()
    key = key.upper()
    encoded_text = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            char_code = ord(char) + shift
            if char.isupper():
                char_code = char_code - ord('A')
                char_code = char_code % 26
                char_code = char_code + ord('A')
            encoded_text += chr(char_code)
        else:
            encoded_text += char
    return encoded_text

def vigenere_decode(text, key):
    text = text.upper()
    key = key.upper()
    decoded_text = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            char_code = ord(char) - shift
            if char.isupper():
                char_code = char_code - ord('A')
                char_code = char_code % 26
                char_code = char_code + ord('A')
            decoded_text += chr(char_code)
        else:
            decoded_text += char
    return decoded_text

key = "VIGENERECIPHER"
msg = "SecurityLaboratory"
print("Simulating Vigenere Cipher\n------------------------")
print("Input Message : " + msg)
enc = vigenere_cipher(msg, key)
print("Encrypted Message : " + enc)
print("Decrypted Message : " + vigenere_decode(enc, key))
