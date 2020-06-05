import cv2
from PIL import Image
import array
import numpy as np
from numpy import *


word = input("Enter string : ") #entering the string
leng=len(word) #obtaining length of string
i=0
a=list();#creating a list
for i in range(leng):
   a.append(0)  #initializing
j=0
for i in word:
    a[j]=ord(i) #ord function used to obtain ascii value of string
    j+=1
print("ascii values of text are:")
print(a)  #ascii values
bi= [ [ 0 for i in range(8) ] for j in range(leng) ]  #creating  a matrix of size leng X 8
j=0
i=7
while(j<leng):
    while(i>-1):
        bi[j][i]=a[j]%2
        a[j]=(a[j]-bi[j][i])//2  #comments in python are created using hashtags
        i-=1  #this segment is for converting the ascii value of letters into binary
    j+=1
    i=7
print("binary of ascii values")
print(bi)#binary
i=0
j=0

#image
imag = cv2.imread("earth.jpg")
cv2.imshow("earth whwn it began",imag)
grap=cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)#converting the image to grayscale
cv2.imshow("earth after hiding",grap)#displaying the image
b= [ [ 0 for i in range(8) ] for j in range(leng) ]
while(j<leng):
    while(i<8):
       b[j][i]=grap[j,i]
       i+=1
    j+=1
    i=0
print("the original pixel values are:")
print(b)#pixel values of image selected
Bi= [ [ 0 for i in range(8) ] for j in range(leng*8) ]
j=0
i=7
k=0
while(j<leng):
   while(k<8):
       while(i>-1):
          if j>0:
              Bi[k+(8*j)][i]=b[j][k]%2
              b[j][k]=(b[j][k]-  Bi[k+(8*j)][i])//2
          else:
              Bi[k][i]=b[j][k]%2
              b[j][k]=(b[j][k]-  Bi[k][i])//2
          i-=1
       k+=1
       i=7
   j+=1
   k=0
#binary of pixel values

i=0
j=0
while(j<leng):
   while(i<8):
      if j>0:
         Bi[i+(8*j)][7]=bi[j][i]
      else:
         Bi[i][7]=bi[j][i]
      i+=1
   j+=1
   i=0
print("the pixel values after hiding are")

#lsb replacement performed.
add=0
i=0
k=-1
temp = [ [ 0 for i in range(leng*8) ] for j in range(1) ]
while(i<leng*8):
   j=7
   add=0
   while(j>-1):
      add=add+(Bi[i][j]*(2**(7-j)))
      j-=1
   temp[0][i]=add
   i+=1

d=reshape(temp,(leng,8))
print(d)# modified pixel values are converted converted back to decimal
i=0
j=0
while(i<leng):
   while(j<8):      
         grap.itemset((i,j),d[i][j])#modified pic
         j+=1
   i+=1
   j=0


 
