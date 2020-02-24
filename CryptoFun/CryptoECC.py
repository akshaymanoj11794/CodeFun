from Crypto.PublicKey import ECC
key=ECC.generate(curve='P-256')
key.public_key()
