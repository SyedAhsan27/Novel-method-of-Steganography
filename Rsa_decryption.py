import rsa
# this is the string that we will be encrypting
file = open("rsa_encrypted.txt","rb")
message = file.read()
file.close()
# the encrypted message can be decrypted with ras.decrypt method and private key
# decrypt method returns encoded byte string, use decode method to convert it to string
# public key cannot be used for decryption
with open("Private_key.pem",'rb') as f:
    p = rsa.PrivateKey.load_pkcs1(f.read())
print(p)
decMessage = rsa.decrypt(message, p)
print("decrypted message: ", decMessage)
file = open("Rsa_decrypted.txt","w")
print('Decryption Done')