% Definimos el vector de coste
c = [15 20 5 25 22 17 30 4];

% Definimos la matriz de coeficientes (restricciones)
A = [51 60 40 62 63 50 70 10];

% Definimos el vector de restricciones
b = transpose([250]);

% Definimos los límites inferiores de las variables
lb = [0 0 0 0 0 0 0 0];

% Definimos los límites superiores de las variables (no existe para x4)
ub = [0 0 0 1 1 1 1 0];

% Definimos el tipo de restricción y de variable
%S =; L >=; U<=;
ctype = "U";
% C= continua I= discreta B= binario
vartype = "CCCCCCCC";

% Definimos el sentido de la optimización: s=1 para minimización y s=-1 para maximización
s = -1;

% Parámetros de computación (opcional)
param.msglev = 3;
param.itlim = 10;

% Ejecutamos el comando glpk
[xmax, fmax] = glpk(c, A, b, lb, ub, ctype, vartype, s, param);

%Mostramos el resultado final
disp(xmax)
disp(fmax)
