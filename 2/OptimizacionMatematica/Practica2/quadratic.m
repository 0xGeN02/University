% Definimos la función objetivo
function f = obj_function(x)
  f = x(1)^2 + x(2)^2;
endfunction

% Definimos las restricciones
A = [1 2];
b = 15;
lb = [1 1];
ub = [10 10];

% Optimización
[xmin, fmin, info, lambda] = qp(x0, @obj_function, [], A, b, lb, ub);

% Mostramos los resultados
disp('Los valores de x1 y x2 que minimizan la función son:');
disp(xmin);
disp('El valor mínimo de la función es:');
disp(fmin);

