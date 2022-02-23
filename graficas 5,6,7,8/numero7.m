%7.	Dos secuencias sinusoidales: 
%una cosenoidal y una senoidal de 
%frecuencia 10*X Hz 
% X=6 f=10*6=60 Hz.

t=0:0.1:10;
f=60;
x=6;
seno=1*sin(2*f*t).*exp(x/10*t);
coseno=1*cos(2*f*t).*exp(x/10*t);

figure(1)
stem(t,seno)
title('Señal senoidal amortiguada creciente')
xlabel ('60 Hz', 'FontName', 'Times', 'Fontsize', 14);
set (gca, 'xtick', [0], 'XTickLabel', {''});

figure(2)
stem(t,coseno);
title('Señal cosenoidal amortiguada creciente')
xlabel ('60 Hz', 'FontName', 'Times', 'Fontsize', 14);
set (gca, 'xtick', [0], 'XTickLabel', {''});