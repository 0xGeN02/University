
#Para 1 termino
x= -4:0.01:4;
fs=zeros(size(x));
for k=1:1000
  fs=fs+2/k*(-1)^(k+1)*(sin(x*k));
end;
fs;
plot(x,fs)


#Para 5 termminos
x= -4:0.01:4;
fs=zeros(size(x));
for k=1:5
  fs=fs+2/k*(-1)^(k+1)*(sin(x*k));
end;
fs;
plot(x,fs)


#Para 20 termminos
x= -4:0.01:4;
fs=zeros(size(x));
for k=1:20
  fs=fs+2/k*(-1)^(k+1)*(sin(x*k));
end;
fs;
plot(x,fs)


#Para 100 termminos
x= -4:0.01:4;
fs=zeros(size(x));
for k=1:100
  fs=fs+2/k*(-1)^(k+1)*(sin(x*k));
end;
fs;
plot(x,fs)


#Para 1000 termminos
x= -4:0.01:4;
fs=zeros(size(x));
for k=1:1000
  fs=fs+2/k*(-1)^(k+1)*(sin(x*k));
end;
fs;
plot(x,fs)
