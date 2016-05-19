states=9;
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

[ESTTR,ESTEMIT] = hmmtrain(dat1,TRGUESS,EMITGUESS,'maxiterations',1000);

