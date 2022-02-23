%6.	Una secuencia exponencial real creciente 
%y decreciente. Utilice el parámetro de 
%crecimiento y decrecimiento con el valor X=6.

A=0.01;
x=6;
t=0:0.001:1;
expcre=A*exp(x*t);
expdec=A*exp(-x*t);

figure(1)
stem(t,expcre)
grid on
title('Exponencial creciente')
xlabel('tiempo (s)');
ylabel('amplitud');

figure(2)
stem(t,expdec)
grid on
title('Exponencial decreciente')
xlabel('tiempo (s)');
ylabel('amplitud');

