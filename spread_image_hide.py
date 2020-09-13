import cv2
from PIL import Image
import array
import numpy as np
from numpy import *
from random import gauss
from random import seed

g = input("Enter string : ")
leng=len(g)
i=0
a=list();
for i in range(leng):
   a.append(0)  #initializing
j=0
for i in g:
    a[j]=ord(i)
    j+=1   
print(a)  #ascii values
bi= [ [ 0 for i in range(8) ] for j in range(leng) ]
j=0
i=7
while(j<leng):
    while(i>-1):
        bi[j][i]=a[j]%2
        a[j]=(a[j]-bi[j][i])//2
        i-=1
    j+=1
    i=7
print(bi)#binary
i=0
j=0
while(j<leng):
   while(i<8):
      if bi[j][i]==0:
         bi[j][i]=-1
      i+=1
   j+=1   
   i=0
i=0
j=0
print(bi)#this is where 0s are converted to -1s


#image
grap = cv2.imread("red.png")
#grep = grap.load()
l=len(grap)
cv2.imshow("red",grap)
b= [ [ 0 for i in range(8) ] for j in range(leng) ]
while(j<leng):
    while(i<8):
       b[j][i]=grap[j,i,2]
       i+=1
    j+=1
    i=0
print(b) #pixel values
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
print(Bi)   
#binary of pixel values;not displayed

key = input("Enter the key1 : ")
lenge=len(key)
o=list();
for i in range(lenge):
   o.append(0)  #initializing
j=0
for i in key:
    o[j]=int(i)
    j+=1   
j=0
i=0
print(o)#key 1 displayed
while(j<leng):
   for l in o:
      if i>7:
          i=0
      if j>0:
         Bi[l+(8*j)][7]=bi[j][i]
      else:
         Bi[l][7]=bi[j][i]
      i+=1
   j+=1
   i=0
print("lsb changed")
print(Bi)
u=0
v=0
#lsb changed


seed(1)
# create white noise series;not displayed here

series1r= [gauss(0.0, 1.0) for i in range(leng*64)]
series=reshape(series1r,(leng*8,8))
mini=series.min()
z=series-mini
maxi=z.max()
q=maxi/2**7
audio=fix(z/q)
signal1=audio/audio.max()

signal= [ [ 0 for i in range(8) ] for j in range(leng*8) ]
key2=input("enter the second key:")
lengt=len(key2)
q=list();
for i in range(lengt):
   q.append(0)
w=0   
for v in key2:
   q[w]=int(v)
   w+=1   
w=0
v=0
print(q)#key2

j=0
i=0
l=0
while(j<leng*8):
   for l in q:
      if i>7:
         i=0
      else:
         signal[j][i]=signal1[j][l]
      i+=1
      l+=1
   l=q[0]   
   j+=1
   i=0
print("noice signal")

#Noise generated;not displayed

s= [ [ 0 for i in range(8) ] for j in range(leng*8) ]
while(u<leng*8):
   while(v<8):
         s[u][v]=Bi[u][v]*signal[u][v]
         v+=1  
   u+=1   
   v=0  #embedded signal(product of message signal and noise)
u=0
v=0
print("embeddeed signal")
print(s)
t= [ [ 0 for i in range(8) ] for j in range(leng*8) ]
key3=input("enter the third key:")
length=len(key3)
p=list();
for i in range(length):
   p.append(0)
w=0   
for v in key3:
   p[w]=int(v)
   w+=1   
w=0
v=0
print(p)#key3

j=0
i=0
l=0
while(j<leng*8):
   for l in p:
      if i>7:
         i=0
      else:
         t[j][i]=s[j][l]
      i+=1
      l+=1
   l=p[0]   
   j+=1
   i=0
print("interleaving done")
print(t)#interleaving done

ta= [ [ 0 for i in range(8) ] for k in range(leng*8) ]
k=0
i=0
while(k<leng*8):
   for i in range(8):
      ta[k][i]=(t[k][i])*(2**8)
      i+=1   
   k+=1
   i=0
print("decimal=")
print(ta)#converting i values back to decimal value

print("grap original")

#[print(grap[i,j,2]) for i in range(leng) for j in range(8)]        
for i in range(leng*8):
    for j in range(8):
        grap[i,j,2]=ta[i][j]                    
#[print(grap[i,j,2]) for i in range(leng*8) for j in range(8)]

cv2.imwrite("newred1.png", grap)



        

       
