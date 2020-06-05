t,g,r,rr=map(int,input().split())
day=1
p=0
pn=0
while(t>=0 and t<7000000000):
   n=t*(g/100)
   ni=int(n)
   rec=r*(rr/100)
   r=r+int(rec)
   
   t1=t+ni-r
   #print(t1)
   if t1>t:
      p=day
      pn=t1
   t=t1
   print(t)
   day+=1
print(day, p , pn)			
