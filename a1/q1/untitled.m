Xbad=importdata('q1/Xbad.csv');
Mu=importdata('q1/mu.csv');
W=importdata('q1/W.csv');
Y1=importdata('q1/Y1.csv');

Y = (Xbad-repmat(mean(Xbad),[28,1]))*W;

for t=1:length(Y1)
    if (sign(Y1(t))~=sign(Y(1,t)))
        Y(t,:)=-Y(t,:);
    end
end
Xhat = Y1*transpose(W) + repmat(Mu,[1,1]);
Ximage = zeros(105,105,28);
Ximage2 = zeros(105,105,28);
for t=1:1
    for n=1:105
        for m=1:105
            Ximage(n,m,t)=Xhat(t,(m-1)*105+n);
            Ximage2(n,m,t)=Xbad(t,(m-1)*105+n);
        end
    end
end


    imshow(Ximage(:,:,1))