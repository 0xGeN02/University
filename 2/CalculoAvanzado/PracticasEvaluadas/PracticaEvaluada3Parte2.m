%%Para la función g(x) = exp(3x+2y):
clear all;
close all;

x = [-2:0.1:2];
y = [-2:0.1:2];
[xx,yy] = meshgrid(x,y);
z = exp(3.*xx + 2.*yy);
z1= 1 + 3.*xx + 2.*yy;
z2= 1 + 3.*xx + 2.*yy + (9.*xx.^2)/2 + 6.*xx.*yy + 2.*yy.^2;
z3 = 1 + 3.*xx + 2.*yy + (9.*xx.^2)/2 + 6.*xx.*yy + 2.*yy.^2 + (27.*xx.^3)/6 + (18.*xx.^2).*yy + (12.*xx).*(yy.^2) + (8.*(yy.^3))/6;

% Creación de las gráficas
figure;
subplot(2,2,1); surf(xx, yy, z); title('Función original');
subplot(2,2,2); surf(xx, yy, z1); title('Serie de Taylor de orden 1');
subplot(2,2,3); surf(xx, yy, z2); title('Serie de Taylor de orden 2');
subplot(2,2,4); surf(xx, yy, z3); title('Serie de Taylor de orden 3');
