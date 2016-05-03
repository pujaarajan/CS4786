from numpy import *
from matplotlib import *
import csv
from scipy import sparse

m=1829

def scun(A,d):
    D=eye(size(A,0))
    D2=sum(A,0)
    for i in range(0,size(A,0)):
        D[i,i]=D2[i]
    L=D-A
    w,v=linalg.eigh(L)
    return v[:,0:d]

def scn(A,d):
    D=eye(size(A,0))
    D2=sum(A,0)
    for i in range(0,size(A,0)):
        D[i,i]=sqrt(D2[i])**-1
    Lh=eye(size(A,0))-dot(dot(D,A),D)

    w,v=linalg.eigh(Lh)
    return v[:,0:d]

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
    XA_c=matrix(XA-average(XA,0))
    XB_c=matrix(XB-average(XB,0))
    sig11=transpose(XA_c)*XA_c
    sig12=transpose(XA_c)*XB_c
    sig22=transpose(XB_c)*XB_c
    sig21=transpose(XB_c)*XA_c
    lambdaA,wA=linalg.eigh(linalg.inv(sig11)*sig12*linalg.inv(sig22)*sig21)
    ind=argsort(lambdaA)[::-1]
    return XA_c*matrix(wA[:,ind[0:d]])

