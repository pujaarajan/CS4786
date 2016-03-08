onecolmu = numpy.mean(Xbad,0) #IS THIS RIGHT

allcolmu = numpy.matlib.repmat(onecolmu,28,1) #IS THIS RIGHT

YBad = (Xbad-allcolmu)*Wbad
Y1Bad = YBad[0]
for j in range(0,20):
    if(numpy.sign(Y1Good[0,j])!=numpy.sign(Y1Bad[0,j])):
        YBad[:,j]=-YBad[:,j]
Xhat = YBad*numpy.transpose(WGood) + MuGood
Ximage2 = numpy.empty((105,105,28))
for t in range(0,28):
    for n in range(0,105):
        for m in range(0, 105):
            #Ihat(n,m,t) = Xhat(t,(m-1)*105+ n)
            Ximage2[n,m,t] = Xhat[t,m*105+n-1]
matplotlib.pyplot.imshow(Ximage2[:,:,8],cmap=cm.Greys_r)
