from numpy import *
from matplotlib import *
import csv
from scipy import sparse

m=1829


def importd(stri,n):
    X_dat=genfromtxt(stri,delimiter=',')
    X_c=sparse.coo_matrix((m,n))
    X_c.data=X_dat[:,2].astype(float64)
    X_c.row=X_dat[:,0].astype(int32)
    X_c.col=X_dat[:,1].astype(int32)
    return X_c


soc=genfromtxt('social_and_evolution.csv',delimiter=',')
graph = importd('graph.csv',146983197)
des=importd('description.csv',8000)
#des=dec_c.todense()
#cov=dot(transpose(X-mean(X,0)),X-mean(X,0))
#c,v=linalg.eigh(cov)
#
#ans=v[:,5]*transpose(X-mean(X))
#ll=[12,
#1419,
#865,
#146,
#1653,
#1176
#]
#ans[array(ll)]
