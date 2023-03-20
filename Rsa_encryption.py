import rsa
# generate public and private keys with rsa.newkeys method,this method accepts key length(atleast 16) as its parameter
publicKey, privateKey = rsa.newkeys(2048)
with open("Public_key.pem",'wb') as f:
    f.write(publicKey.save_pkcs1("PEM"))
with open("Private_key.pem",'wb') as f:
    f.write(privateKey.save_pkcs1("PEM"))
# this is the string that we will be encrypting
file = open("message.txt","r")
mess = file.read()
file.close()
# rsa.encrypt method is used to encrypt string with public key string should be encode to byte string before encryption
encMessage = rsa.encrypt(mess.encode(),publicKey)
print("original string: ", mess)
print("encrypted string: ", encMessage)
file = open("rsa_encrypted.txt","wb")
file.write(encMessage)
file.close()