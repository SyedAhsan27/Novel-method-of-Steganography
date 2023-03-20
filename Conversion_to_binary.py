import base64
#, encoding="unicode_escape"
with open("rsa_encrypted.txt", "rb") as File:
 str1= base64.b64encode(File.read())

filename = 'base64_encrypt.txt'
# we are considering a file to store the string.
with open(filename, 'wb') as f:
 f.write(str1)

file = open("base64_encrypt.txt","r")
text=file.read()
file.close()

# using join() + ord() + format() to convert into binary
bin_result = ''.join(format(ord(x), '08b') for x in text)

file = open("Binary.txt","w")
file.write(bin_result)
file.close()
print("binary string: ", bin_result)
print(len(bin_result))