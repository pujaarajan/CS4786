sol=zeros(900,2);
for i=101:1000
    ind=find(isnan(dat(i,:)));
    if(ind>1)
        subs=dat(i,1:ind-1);
        likelystates = hmmviterbi(subs, ESTTR, ESTEMIT);

        PSTATES = hmmdecode(subs,ESTTR,ESTEMIT);
        Plast=PSTATES(:,ind-1);
        Pcurr=zeros(states,1);
        for ii=1:states
            for jj=1:states
                Pcurr(ii)=Pcurr(ii)+Plast(jj)*ESTTR(jj,ii);
            end
        end
        Pem=zeros(emissions,1);
        for ii=1:states
            for jj=1:emissions
                Pem(jj)=Pem(jj)+Plast(ii)*ESTEMIT(ii,jj);
            end
        end        
        [num,ind2]=max(Pem);
        
        %[num,ind2]=max(ESTEMIT(likelystates(size(likelystates,2)),:));
        

    else
        [num,ind2]=max(ESTEMIT(1,:));
    end
    sol(i-100,1)=i;
    sol(i-100,2)=ind2;
end

corr=0;
for i=101:1000
    ind=find(isnan(dat(i,:)));
    if(ind>1)
        subs=dat(i,ind-1)==sol(i-100,2);
    end
    corr=corr+subs;
end
corr

sol=zeros(900,2);
for i=101:1000
    ind=find(isnan(dat(i,:)));
    if(ind>1)
        subs=dat(i,1:ind-1);
        likelystates = hmmviterbi(subs, ESTTR, ESTEMIT);
        [num,ind2]=max(ESTTR(likelystates(size(likelystates,2)),:));
        [num,ind3]=max(ESTTR(ind2,:));
        [num,ind4]=max(ESTEMIT(ind3,:));
    elseif(ind<1000)
        [num,ind4]=max(ESTEMIT(1,:));
    end
    sol(i-100,1)=i;
    sol(i-100,2)=ind4;
end

corr=0;
for i=101:1000
    ind=find(isnan(dat(i,:)));
    if(ind<100)
        subs=dat(i,ind+1)==sol(i-100,2);
    end
    corr=corr+subs;
end
corr
