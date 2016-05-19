states=2;
emissions=5;
TRGUESS=zeros(states);
EMITGUESS=zeros(states,emissions);
for i=1:states
    for j=1:states
        TRGUESS(i,j)=rand();
    end
    TRGUESS(i,:)=TRGUESS(i,:)/sum(TRGUESS(i,:));
end
for i=1:states
    for j=1:emissions
        EMITGUESS(i,j)=rand();
    end
    EMITGUESS(i,:)=EMITGUESS(i,:)/sum(EMITGUESS(i,:));
end

[ESTTR,ESTEMIT] = hmmtrain(dat1,TRGUESS,EMITGUESS);

for i=101:1000
    ind=find(isnan(dat(i,:)));
    if(ind>1)
        subs=dat(i,1:ind-1);
        likelystates = hmmviterbi(subs, ESTTR, ESTEMIT);
    end
end