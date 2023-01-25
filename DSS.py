import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

msg = input("Enter some text: ")

private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
signature = private_key.sign(msg.encode(), hashes.SHA256())
signature_b64 = base64.b64encode(signature)

print("Digital signature for given text: " + signature_b64.decode())
