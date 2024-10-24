% Definimos el vector de coste
c = [0.8 0.6];

% Definimos la matriz de coeficientes (restricciones)
A = [0.6 0.2; 0.1 0.5; 1 1];

% Definimos el vector de restricciones
b = [30 26 100];

% Definimos los límites inferiores de las variables
lb = [0 0];

% Definimos los límites superiores de las variables (no existe para x4)
ub = [];

% Definimos el tipo de restricción y de variable
%S =; L >=; U<=;
ctype = "LLS";
% C= continua I= discreta B= binario
vartype = "CC";

% Definimos el sentido de la optimización: s=1 para minimización y s=-1 para maximización
s = 1;

% Parámetros de computación (opcional)
param.msglev = 3;
param.itlim = 10;

% Ejecutamos el comando glpk
[xmax, fmax] = glpk(c, A, b, lb, ub, ctype, vartype, s, param);

%Mostramos el resultado final
disp(xmax)
disp(fmax)

