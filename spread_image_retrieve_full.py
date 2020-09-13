import cv2
from PIL import Image
import array
import numpy as np
from numpy import *
from random import gauss
from random import seed

grap = cv2.imread("newred1.png")
row=len(grap)
print("grap modified")
ta= [ [ 0 for i in range(8) ] for j in range(row) ]
i=0
j=0
while(j<row):
    while(i<8):
       ta[j][i]=grap[j,i,2]
       i+=1
    j+=1
    i=0
#print(ta) #pixel values

        
#retrieving begins
tb= [ [ 0 for i in range(8) ] for k in range(row) ]
k=0
i=0
while(k<row):
   for i in range(8):
       if i==0:
           ta[k][i]=-1*(256-ta[k][i])
       tb[k][i]=(ta[k][i])/(2**8)
       i+=1   
   k+=1
   i=0
print("decimal=")
#print(tb)#converting i values back to decimal value

sr= [ [ 0 for i in range(8) ] for j in range(row) ]
key3=input("enter key3:")
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
while(j<row):
   for l in p:
      if i>7:
         i=0
      else:
         sr[j][i]=tb[j][l]
      i+=1
      l+=1
   l=p[0]   
   j+=1
   i=0
print("interleaving retrieved")
#print(sr)#interleaving done
o=0
p=0
#lsb changed


seed(1)
# create white noise series;not displayed here
series1r= [gauss(0.0, 1.0) for i in range(row*8)]
seriesr=reshape(series1r,(row,8))
minir=seriesr.min()
zr=seriesr-minir
maxir=zr.max()
qr=maxir/2**7
audior=fix(zr/qr)
signal1r=audior/audior.max()
  
signalr= [ [ 0 for i in range(8) ] for j in range(row) ]
key2=input("enter the second key:")
lengt=len(key2)
qr=list();
for i in range(lengt):
   qr.append(0)
w=0   
for p in key2:
   qr[w]=int(p)
   w+=1   
w=0
p=0
print(qr)#key2

j=0
i=0
l=0
while(j<row):
   for l in qr:
      if i>7:
         i=0
      else:
         signalr[j][i]=(signal1r[j][l])
      i+=1
      l+=1
   l=qr[0]   
   j+=1
   i=0
print("noice signal")
print(signalr)

#Noise generated;not displayed

Bir= [ [ 0 for i in range(8) ] for j in range(row) ]
while(o<row):
   while(p<8):
       try:
           Bir[o][p]=((sr[o][p]/signalr[o][p]))
       except:
           Bir[0][p]=0
       p+=1  
   o+=1   
   p=0  #embedded signal(product of message signal and noise)
o=0
p=0
print("embeddeed signal")
#print(Bir)


key = input("Enter key1 : ")
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
bir= [ [ 0 for i in range(8) ] for j in range(row//8) ]
print(o)#key 1 displayed
while(j<row//8):
   for l in o:
      if i>7:
          i=0
      if j>0:
         bir[j][i]=Bir[l+(8*j)][7]
      else:
         bir[j][i]=Bir[l][7]
      i+=1
   j+=1
   i=0
print("lsb changed")
#print(bir)


i=0
j=0
while(j<row//8):
   while(i<8):
      if bir[j][i]==-1.0:
         bir[j][i]=0
      else:
         bir[j][i]=1
      i+=1
   j+=1   
   i=0
i=0
j=0
#print(bir)#converting -1s to 0s

var=[0 for i in range(row//8)]
i=7
j=0
while(j<row/8):
   sommy=0
   while(i>-1):
      sommy+=bir[j][i]*(2**(7-i))
      i-=1
   var[j]=sommy
   j+=1   
   i=7
i=0
j=0
#print(var)#decimal values

for i in range(row//8):
    if var[i]==92:
        break
    else:
       print(chr(var[i]))
