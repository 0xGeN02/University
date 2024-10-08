% Define objective function coefficients
c = [25 45];

% Define constraint matrix
A = [
  5 8;  % Material constraint
  2 4;  % Machine time constraint
  1 0;  % First supplier limit (y1 <= 150)
  0 1   % Second supplier limit (y2 <= 100)
];

% Define constraint right-hand side
b = [
  110;  % Machine time limit
  150;  % First supplier limit
  100   % Second supplier limit
];

lb = zeros(4, 1);
ub = ones(4, 1);

% Definimos el tipo de restricción
ctype = "SS"; % Ambas restricciones son de tipo <=

% Definimos el tipo de variable
vartype = "IIII"; % Variables enteras

% Definimos el sentido de la optimización: -1 para maximización
s = -1;

% Parámetros de computación (opcional)
param.msglev = 1;
param.itlim = 10000;

% Ejecutamos el comando glpk
[xmax, fmax] = glpk(c, A, b, lb, ub, ctype, vartype, s, param);

% Mostramos el resultado final
disp('Cantidad de productos A y B a producir para maximizar beneficios:')
disp(xmax)
disp('Beneficio máximo:')
disp(fmax)
