from numpy import *
from matplotlib import *
import csv
from scipy import sparse

m=1829

def pca(A,d):
    meanA=(average(A,0))
    centA=A-meanA
    sigA=transpose(matrix(A))*matrix(A)
    lambdaA,wA=linalg.eigh(sigA)
    WA=zeros((size(A,1),d))
    for i in range(0,d):
        WA[:,i]=real(transpose(wA[:,i]))
    yA=matrix(A)*matrix(WA)
    return yA


def cca(XA,XB,d):
    XA_m=XA.mean(0)
    XA_c=XA-XA_m
    XB_m=XB.mean(0)
    XB_c=XB-XB_m
    sig11=transpose(XA_c).dot(XA_c)
    sig12=transpose(XA_c).dot(XB_c)
    sig22=transpose(XB_c).dot(XB_c)
    sig21=transpose(XB_c).dot(XA_c)
    sig=linalg.inv(sig11)*sig12*linalg.inv(sig22)*sig21
    lambdaA,wA=linalg.eig(sig)
    ind=argsort(lambdaA)[::-1]
    return XA_c*matrix(wA[:,ind[0:d]])
