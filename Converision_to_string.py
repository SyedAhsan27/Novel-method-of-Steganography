# Defining BinarytoDecimal() function
def BinaryToDecimal(binary):
 binary1 = binary
 decimal, i, n = 0, 0, 0
 while(binary != 0):
  dec = int(binary) % 10
  decimal = decimal + dec * pow(2, i)
  binary = int(binary)//10
  i += 1
 return (decimal)

file = open("RSA_encrypte.txt","r")
bin_data=file.read()
file.close()

# initializing a empty string for
# storing the string data
str_data =''

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 8):
 # slicing the bin_data from index range [0, 8] and storing it in temp_data
 temp_data = bin_data[i:i + 8]
 # passing temp_data in BinarytoDecimal() function
 # to get decimal value of corresponding temp_data
 decimal_data = BinaryToDecimal(temp_data)
 # in str_data
 str_data = str_data + chr(decimal_data)

# printing the result
file = open("String.txt","w")
file.write(str_data)
file.close()

import base64
with open("String.txt", "rb") as File:
 str2= (File.read())
textdata = base64.b64decode(str2)
filename = 'Decrypted_message.txt'
with open(filename, 'wb') as f:
 f.write(textdata)
print("decrypted string: ", textdata)
