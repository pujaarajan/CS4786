avgerr=zeros(100,1);

for i=1:100
    [PSTATES,logpseq]=hmmdecode(dat1(i,:),TRGUESS,EMITGUESS);
    avgerr(i)=logpseq;
end
