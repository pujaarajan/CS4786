from numpy import *
from matplotlib import *
import csv
from scipy import sparse

K=20
Y=zeros([m,K])
for j in range(0,K):
    for i in range(0,size(graph.row)):
        random.seed([graph.row[i],graph.col[i],j])
        Y[graph.row[i],j]=Y[graph.row[i],j]+sign(random.random()-.5)*graph.data[i]
    
Y/sqrt(K)
