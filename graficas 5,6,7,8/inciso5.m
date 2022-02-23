%5.	Dos secuencias sinusoidales: 
%una cosenoidal y una senoidal 
%de frecuencia 10*X Hz, X=6 f=60Hz

f=60;
p=1/f;
a=1;
t=linspace(0,p,1000);
seno=a*sin(2*pi*f*t);
coseno=a*cos(2*pi*f*t);
 
figure(1)
stem(t,seno)
grid on
title('Señal senoidal')
xlabel('tiempo (s)');
ylabel('amplitud');

figure(2)
stem(t,coseno)
grid on
title('Señal cosenoidal')
xlabel('tiempo (s)');
ylabel('amplitud');


 


 


