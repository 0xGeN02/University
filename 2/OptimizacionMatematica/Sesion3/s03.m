%Préambulo
c = [4; -2; 7; -1]; %Vector de coste
A = [1, 0, 5, 0; 1, 1, -1, 0; 1, -5, 0, 0; 0, 1, 1, -1]; %Matriz de coeficientes
b = [10; 1; 0; 2]; %Vector de restricciones
lb = zeros(4, 1); %Cota inferior de las variables
ub = []; %Cota superior de las variables
ctype = "<="; %Tipo de restricciones
vartype = "C"; %Tipo de variables de decisión
s = "max"; %Sentido de la optimización (maximización)

%Parámetros de computación
param.msglev = 3;
param.itlim = 10;

%Optimización
[xmin, fmin] = glpk(c, A, b, lb, ub, ctype, vartype, s, param);

%Mostrar resultados
disp("Solución óptima (x1, x2, x3, x4):");
disp(xmin);
disp("Valor máximo de la función objetivo:");
disp(fmin);
