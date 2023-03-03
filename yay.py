import hashlib

password = "" #change this
salt = "" #change this

salted_password = salt + password

encoded_password = salted_password.encode()

hash_object = hashlib.sha256() #change the crypting format example: hashlib.md5() hashlib.md4()

hash_object.update(encoded_password)

hashed_password = hash_object.hexdigest()

print("Salted password:", salted_password)
print("Hashed password:", hashed_password)
