% Definimos la función objetivo
x=0
function y = f(x)
    y = 100*(((x(1)).^2 - x(2)).^2) + (1 - x(1)).^2;
endfunction

% Definimos el vector gradiente
function yp = fp(x)
    yp1 = 400 * (x(1)).^3 - (400*x(1)*x(2)) - 2 + 2*x(1);
    yp2 = -200*(x(1)).^2 + 200 * x(2);
    yp = [yp1; yp2];
endfunction

% Definimos la matriz Jacobiana
function J = fpp(x)
    J = [(1200*(x(1)).^2-400*x(2)+2), -400*x(1); -400*x(1), 200];
endfunction

% Definimos el punto inicial
x0 = [-2; -2];

% Definimos el margen de error
epsilon = 0.01;

% Definimos la iteración
i = 1;
JJ = inv(fpp(x0));

while norm(fp(x0)) > epsilon
    S = -JJ * fp(x0);

    % Tasa de aprendizaje inicial
    ss = 0.01;
    x1 = x0 + ss * S;

    while ss > 1.e-6
        while f(x0) - f(x1) > 0
            x0 = x1;
            x1 = x0 + ss * S;
        endwhile
        x0 = x0 - ss * S;
        ss = 0.5 * ss;
    endwhile

    x0 = x1;
    i = i + 1;
endwhile

disp("Número de iteraciones:"), disp(i)
disp("Solución:"), disp(x0)
disp("Valor mínimo de la función:"), disp(f(x0))
disp("Norma del gradiente:"), disp(norm(fp(x0)))
