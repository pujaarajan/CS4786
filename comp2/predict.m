sol=zeros(900,2);
for i=101:1000
    ind=find(isnan(dat(i,:)));
    if(ind>1)
        subs=dat(i,1:ind-1);
        likelystates = hmmviterbi(subs, ESTTR, ESTEMIT);
        [num,ind2]=max(ESTTR(likelystates(size(likelystates,2)),:));
        [num,ind3]=max(ESTEMIT(ind2,:));
        %[num,ind3]=max(ESTTR(likelystates(size(likelystates,2)),:)*ESTEMIT);
    else
        [num,ind3]=max(ESTEMIT(1,:));
    end
    dat2(i,ind)=ind3;
    sol(i-100,1)=i;
    sol(i-100,2)=ind3;
end

csvwrite('sub.csv',sol)