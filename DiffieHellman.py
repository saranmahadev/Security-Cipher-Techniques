p = 23
g = 5
x = 4
y = 3

alice_sends = (g ** x) % p
bob_computes = (alice_sends ** y) % p
bob_sends = (g ** y) % p
alice_computes = (bob_sends ** x) % p
shared_secret = (g ** (x * y)) % p

print("Simulation of Diffie-Hellman key exchange algorithm\n")
print("Alice Sends: ", alice_sends)
print("Bob Computes: ", bob_computes)
print("Bob Sends: ", bob_sends)
print("Alice Computes: ", alice_computes)
print("Shared Secret: ", shared_secret)

if alice_computes == bob_computes and alice_computes == shared_secret:
    print("Success: Shared Secrets Matches! ", shared_secret)
else:
    print("Error: Shared Secrets does not Match")
