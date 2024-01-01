%Para la función f(x) = sen(xy):

% Cálculo de las series de Taylor
clear all;
close all;

x = linspace(-3, 3, 61);
y = linspace(-3, 3, 61);

[xx, yy] = meshgrid(x, y);
z = sin(xx .* yy);
z1 = xx .* yy;
z2 = xx .* yy - (xx.^3).*(yy.^3)/6;
z3 = xx .* yy - (xx.^3).*(yy.^3)/6 + (xx.^5).*(yy.^5)/120;

% Creación de las gráficas
figure;
subplot(2,2,1); surf(xx, yy, z); title('Función original');
subplot(2,2,2); surf(xx, yy, z1); title('Serie de Taylor de orden 1');
subplot(2,2,3); surf(xx, yy, z2); title('Serie de Taylor de orden 2');
subplot(2,2,4); surf(xx, yy, z3); title('Serie de Taylor de orden 3');




