% Definición de la función de costo (reemplaza esto con tu propia función)
w=0;
function cost = my_cost_function(w)
    % Calcula el valor de la función de costo para los parámetros w
    % Aquí debes implementar tu propia función de costo
    % Por ejemplo, si es una función cuadrática:
        cost = (w(1) - 2)^2 + (w(2) + 3)^2 + (w(3) - 1)^2 + (w(4) + 4)^2 + (w(5) - 5)^2;
end

% Inicialización de los parámetros
w = zeros(5, 1); % Valores iniciales (puedes elegir otros valores)

% Hiperparámetros
learning_rate = 0.01;
max_iterations = 1;
tolerance = 0.15;

% Bucle de descenso de gradiente
for iter = 1:max_iterations
    gradient = zeros(5, 1);
    for i = 1:5
        % Calcula el gradiente parcial para cada parámetro
        epsilon = zeros(5, 1);
        epsilon(i) = 1e-6;
        gradient(i) = (my_cost_function(w + epsilon) - my_cost_function(w - epsilon)) / (2 * epsilon(i));
    end

    % Actualiza los parámetros
    w = w - learning_rate * gradient;

    % Verifica la convergencia
    if norm(gradient) < tolerance
        break;
    end
end

% El resultado final
fprintf('Parámetros óptimos:\n');
disp(w);
fprintf('Valor mínimo de la función de costo:\n');
disp(my_cost_function(w));
