%8.	Una secuencia exponencial compleja de longitud X. 
%Grafique su parte real e imaginaria en la misma 
%pantalla.

clear all % Elimina variables utilizadas en otras rutinas
x=3; % longitud 6 == -3<x<3
t = -x*10^(-3): 10^(-5): x*10^(-3) % Base de tiempos
am = 0.5; % Módulo de la amplitud compleja
fase = pi/4; % Fase de la amplitud compleja
A = am*exp(j*fase); % Amplitud compleja
sigma = 0.5*10^3; % Parte real del coeficiente del exponente
T = 10^(-3); % Periodo de la función
f = 1/T; % Frecuencia
w = 2*pi*f; % Frecuencia angular
s = sigma + j*w; % Coeficiente del exponente
y = A*exp(s*t); % Función
subplot (2, 1, 1); % Recuadro parte real
plot (t, real(y), 'b', 'LineWidth', 1); % Curva en azul de grosor 2
hold on
%plot (t, abs(y), 'r'); % Envolvente de la parte superior (en rojo)
%plot (t, -abs(y), 'r'); % Envolvente de la parte inferior (en rojo)
%xlabel ('-3 t 3', 'FontName', 'Times', 'Fontsize', 14); % Eje abscisas
ylabel ('Parte real', 'FontName', 'Times', 'Fontsize', 14); % Eje ordenadas
grid on; % Malla
axis ([-2*10^(-3), 2*10^(-3), -3, 3]); % Área de dibujo
set (gca, 'xtick', [0], 'XTickLabel', {'-3<t<3'}, 'FontName', 'Times', 'Fontsize', 12);
set (gca, 'ytick', [-0.5 0.5], 'YTickLabel', {' '; ' '}, 'FontName', 'Times', 'Fontsize', 12);
title ('Exponencial compleja') % Título
subplot (2, 1, 2); % Recuadro parte imaginaria
plot (t, imag(y), 'b', 'LineWidth', 1); % Curva en azul 
hold on
%plot (t, abs(y), 'r'); % Envolvente de la parte superior (en rojo)
%plot (t, -abs(y), 'r'); % Envolvente de la parte inferior (en rojo)
%xlabel ('-3 t 3', 'FontName', 'Times', 'Fontsize', 14); % Eje abscisas
ylabel ('Parte imaginaria', 'FontName', 'Times', 'Fontsize', 14); % Eje ordenadas
grid on; % Malla
axis ([-2*10^(-3), 2*10^(-3), -3, 3]); % Área de dibujo
set (gca, 'xtick', [0], 'XTickLabel', {'-3<t<3'}, 'FontName', 'Times', 'Fontsize', 12);
set (gca, 'ytick', [-0.5 0.5], 'YTickLabel', {' '; ' '}, 'FontName', 'Times', 'Fontsize', 12);

hold off
clear all;