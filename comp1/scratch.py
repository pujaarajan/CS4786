#pp[ll,:]+=10000
#pp[:,ll]+=10000
#
#pp[12,1419  ]=10000
#pp[1419,12  ]=10000
#pp[1419,865 ]=10000
#pp[865,1419 ]=10000
#pp[865,12   ]=10000
#pp[12,865   ]=10000
#pp[146,1653 ]=10000
#pp[1653,146 ]=10000
#pp[1653,1176]=10000
#pp[1176,1653]=10000
#pp[1176,146 ]=10000
#pp[146,1176 ]=10000

import itertools
pp=(graph*transpose(graph)).toarray()

def connect(a):
    l=array(list(itertools.combinations(a,2)))
    for i in range(0,size(l,0)):
        if (pp[l[i,0],l[i,1]]<20000):
            pp[l[i,0],l[i,1]]=20000
            pp[l[i,1],l[i,0]]=20000
        #pp[l[i,0],l[i,1]]*=10000
        #pp[l[i,1],l[i,0]]*=10000

def disconnect1(a,b):
    l=list(itertools.product(a,b))
    for i in range(0,size(l,0)):
        pp[l[i][0],l[i][1]]=0
        pp[l[i][1],l[i][0]]=0
          


temp1=[i for i,v in enumerate(pp[ll[0],:]) if v>0]
temp1+=[i for i,v in enumerate(pp[ll[1],:]) if v>0]
temp1+=[i for i,v in enumerate(pp[ll[2],:]) if v>0]
temp1=ll[0:3]
connect(temp1)




temp2=[i for i,v in enumerate(pp[ll[3],:]) if v>0]
temp2+=[i for i,v in enumerate(pp[ll[4],:]) if v>0]
temp2+=[i for i,v in enumerate(pp[ll[5],:]) if v>0]
temp2=ll[3::]
connect(temp2)
disconnect1(temp1,temp2)

for i in range(0,1829):
    pp[i,i]=0


