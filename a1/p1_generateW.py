import numpy
import numpy.matlib
import matplotlib.pyplot
import random
import matplotlib.cm as cm

Xbad = numpy.matrix(numpy.loadtxt("q1/Xbad.csv", delimiter=","))
# now X is the data matrix and each row of X corresponds to one data point
MuGood = numpy.matrix(numpy.loadtxt("q1/Mu.csv", delimiter=","))
# Mu is the mean vector of all the smilie faces (in vector format)
WGood = numpy.matrix(numpy.loadtxt("q1/W.csv", delimiter=","))
Y1Good = numpy.matrix(numpy.loadtxt("q1/Y1.csv", delimiter=","))
#already good ones Y1, W, and Mu

Sigma = (numpy.transpose(Xbad-numpy.average(Xbad,0)))*((Xbad-numpy.average(Xbad,0)))
lambdaA,wA=numpy.linalg.eig(Sigma)
ind=numpy.argsort(lambdaA)[::-1]
Wbad = wA[:,ind[0:20]]
