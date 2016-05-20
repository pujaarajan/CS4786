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
for i=1:5
    EMITGUESS(1,i)=sum(dat(:,1)==i)/1000;
end
for i=1:states
    for j=1:emissions
        EMITGUESS(i,j)=rand();
    end
    EMITGUESS(i,:)=EMITGUESS(i,:)/sum(EMITGUESS(i,:));
end



[ESTTR,ESTEMIT] = hmmtrain(dat3,TRGUESS,EMITGUESS,'maxiterations',100);

for i=1:5
    ESTEMIT(1,i)=sum(dat(:,1)==i)/1000;
end