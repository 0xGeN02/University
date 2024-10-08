x=0
% Definimos la nueva función objetivo
function y = f(x)
    y = x(1) - x(2) + 2*x(1)^2 + 2*x(1)*x(2) + x(2)^2;
end

% Definimos el nuevo vector gradiente de la función
function yp = fp(x)
    yp1 = 1 + 4*x(1) + 2*x(2);
    yp2 = -1 + 2*x(1) + 2*x(2);
    yp = [yp1; yp2];
end

% Definimos la matriz Hessiana de la función
function J = fpp(x)
    J = [
        4, 2;
        2, 2
    ];
end

% Definimos el punto inicial
x0 = [0; 0];

% Definimos el margen de error
epsilon = 0.0001;

% Definimos la iteración
i = 1;
JJ = inv(fpp(x0)); % Calculamos la inversa de la matriz Hessiana una vez ya que es constante

while norm(fp(x0)) > epsilon
    S = -JJ * fp(x0); % Dirección de descenso

    % Tasa de aprendizaje óptima para este paso (se podría usar búsqueda de línea aquí)
    % Para simplificar, se asume una tasa constante
    ss = 1; % Se ajusta la tasa de aprendizaje a 1 dado que la Hessiana es constante y conocemos la forma exacta de la función
    x1 = x0 + ss * S;

    x0 = x1;
    i = i + 1;
end

disp("Número de iteraciones:"), disp(i)
disp("Solución:"), disp(x0)
disp("Valor mínimo de la función:"), disp(f(x0))
disp("Norma del gradiente:"), disp(norm(fp(x0)))

