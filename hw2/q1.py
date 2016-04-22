from matplotlib.pylab import *
from numpy import *

n=30
A = zeros([n,n])


for i in range(0,7):
    for j in range(0,7):
        if(i!=j):
            A[i,j]=1

for i in range(7,14):
    for j in range(7,14):
        if(i!=j):
            A[i,j]=1
        
for i in range(14,22):
    for j in range(14,22):
        if(i!=j):
            A[i,j]=1

for i in range(22,30):
    for j in range(22,30):
        if(i!=j):
            A[i,j]=1

A[0,7]=1
A[7,0]=1

A[17,24]=1
A[24,17]=1


A[3,17]=1
A[17,3]=1
A[4,18]=1
A[18,4]=1

A[10,24]=1
A[24,10]=1
A[9,26]=1
A[26,9]=1



#modified graph
A[15,23]=1
A[23,15]=1
A[16,24]=1
A[24,16]=1

A[3,12]=1
A[12,3]=1




D=zeros([n,n])
for i in range(0,n):
    D[i,i]=sum(A[i,:])

L=D-A

Lt=eye(n)-dot(dot(inv(D**(1./2)),A),inv(D**(1./2)))
w,v=eigh(Lt)
cuts=v[:,1]

cuts2=zeros(n)
for i in range(0,n):
    if (cuts[i]>0):
        cuts2[i]=1
    else:
        cuts2[i]=0



savetxt("AspectralII.csv", A, delimiter=",",fmt='%x')
savetxt("cspectralII.csv", cuts2, delimiter=",",fmt='%x')
