# To show the amount of pixels different in both of the images 
from PIL import Image
def main():
  number_of_differences=0
  img1 = input("Enter image name of the first image to be compared : ")
  img2 = input("enter the name of the second image to be compared : ")
  Image1 = Image.open(img1,'r')
  Image2 = Image.open(img2,'r')
  width,height = Image1.size
  for i in range (0,width-1):
    for j in range (0,height-1):
      [r,g,b]=Image1.getpixel((i,j))
      [rq,gq,bq]=Image2.getpixel((i,j))
      if([r,g,b]!=[rq,gq,bq]):
        number_of_differences= number_of_differences+1
  print("The number of differences in the given images: ", number_of_differences)
  print("Total number of pixels: ",width*height)
  print("Percentage of change = ", (100*number_of_differences)/(width*height))

main()
        
