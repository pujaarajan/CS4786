from numpy import *
from matplotlib import *
import csv
from scipy import sparse
m=1829
n=146983197



A=sparse.bmat([[None,graph],[transpose(graph),None]])
A2=sparse.coo_matrix((m,m))
D=sparse.coo_matrix((m,m))
D.row=zeros(m+n).astype(int32)
D.col=zeros(m+n).astype(int32)
D.data=zeros(m+n).astype(int32)
sum1=graph.sum(1)
sum2=graph.sum(0)
for i in range(0,m):
    D.row[i]=i
    D.col[i]=i
    D.data[i]=sum1[i,0]

#for i in range(0,n):
#    D.row[i+m]=i+m
#    D.col[i+m]=i+m
#    D.data[i+m]=sum2[0,i]


L2=D-A2
#
#Lh=sparse.eye(m+n).tocsc()-sparse.linalg.inv(D.sqrt())*A*sparse.linalg.inv(D.sqrt())
#
#w,v=sparse.linalg.eigsh(L)
#
#v[0:1828,1]



