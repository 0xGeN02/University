% Función de costo
function f = cost_function(x, y)
 f = 2*x.^2 + 2*x - x.^2 - 2*y.^2;
end

% Parámetros
x = 0;
y = 0;

% Tasa de aprendizaje
alpha = 0.01;
num_iteraciones = 1000;

% Descenso del gradiente
for iter = 1:num_iteraciones
 % Calcula el gradiente
 grad_x = 4*x + 2;
 grad_y = -4*y;

 % Actualiza los valores de x e y
 x = x - alpha * grad_x;
 y = y - alpha * grad_y;

 % Calcula la función de costo en cada iteración
 f = cost_function(x, y);

 % Muestra la función de costo
 fprintf('Iteración %d: f = %.4f, x = %.4f, y = %.4f\n', iter, f, x, y);
end

% Muestra el resultado final
fprintf('Resultado final: f = %.4f, x = %.4f, y = %.4f\n', f, x, y);

