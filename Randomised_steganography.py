from PIL import Image
import random


# Encode data into image
def encode(img):
 image = Image.open(img, 'r')
 copy_of_image = image.copy()
 width, height = copy_of_image.size
 cols=[]
 rows=[]

 while(len(cols)!=64):
    x = random.randint(1,width-1)
    if(x not in cols):
        cols.append(x)

 while(len(rows)!=43):
    x = random.randint(1,height-1)
    if(x not in rows):
        rows.append(x)
 cols.sort()
 rows.sort()
 for i in cols:
    [r,g,b]=copy_of_image.getpixel((i, 0))
    if(b<255):
        b=b+1
    else:
        b=b-1
    copy_of_image.putpixel((i,0),(r,g,b))

 
 for i in rows:
    [r,g,b]=copy_of_image.getpixel((0, i))
    if(b<255):
        b=b+1
    else:
        b=b-1
    copy_of_image.putpixel((0,i),(r,g,b))
 
 file = open("Binary.txt","r")
 data = file.read()
 file.close()
 data = str(data)
 if (len(data) == 0):
  raise ValueError('Data is empty')

 c=0
 for i in range(0,height-1):
    for j in range(0,width-1):
        if(i in rows and j in cols):
            [r,g,b]=copy_of_image.getpixel((j,i))
            if(data[c]=="1"):
                if(b!=255):
                    b=b+1
                else:
                    b=b-1
                copy_of_image.putpixel((j,i),(r,g,b))    
            c=c+1
        else:
                if(i!=0 and j!=0):
                  q=random.randint(0,2)
                else:
                  q=random.randint(0,1)
                [r,g,b]=copy_of_image.getpixel((j,i))
                if(q==0):
                    copy_of_image.putpixel((j,i),(r+random.randrange(-1,2,2),g,b))
                elif(q==1):
                    copy_of_image.putpixel((j,i),(r,g+random.randrange(-1,2,2),b))
                elif(q==2):
                    copy_of_image.putpixel((j,i),(r,g,b+random.randrange(-1,2,2)))
 

 new_img_name = input("Enter the name of new encrypted image(with extension) : ")
 copy_of_image.save(new_img_name, str(new_img_name.split(".")[1].upper()))

# Decode the data in the image
def decode(original_image):
 img = input("Enter the name of the image to be decrypted(with extension) : ")
 image = Image.open(img, 'r')

 original = Image.open(original_image,'r')

 data = ""

 width, height = original.size

 rows=[]
 cols=[]

 for i in range(0,width):
    [r,g,b]=image.getpixel((i,0))
    [r1,g1,b1]=original.getpixel((i,0))
    if(b-b1==1 or b1-b==1):
        cols.append(i)
 
 for i in range(0,height):
    [r,g,b]=image.getpixel((0,i))
    [r1,g1,b1]=original.getpixel((0,i))
    if(b-b1==1 or b1-b==1):
        rows.append(i)

 for i in rows:
    for j in cols:
        [r,g,b]=image.getpixel((j,i))
        [r1,g1,b1]=original.getpixel((j,i))
        if(b-b1==1 or b1-b==1):
            data+="1"
        else:
            data+="0"
 return data 

# Main Function
def main():
 file = open("Binary.txt","r")
 bin_data = file.read()
 file.close()
 img = input("Enter image name of the image to be encrypted(with extension) : ")
 encode(img)
 print("Encryption completed")
 dec_data = decode(img)


 print(dec_data == bin_data)
 file = open("RSA_encrypte.txt","w")
 file.write(dec_data)
 file.close()
 
 print("Image decrpyted")
 print("Binary string from decrypted image: ", dec_data)



# Calling main function
main()