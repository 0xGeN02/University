% Definimos la función objetivoç
x=0
function y = f(x)
    y = (x(1)+10*x(2)).^2 + 5*(x(3)-x(4)).^2+(x(2)-2*x(3)).^4+10*(x(1)-x(4)).^4;
endfunction

% Definimos el vector gradiente
function yp = fp(x)
    yp1 = 2*(x(1) + 10*x(2)) + 40*(x(1) - x(4))^3;
    yp2 = 20*(x(1) + 10*x(2)) + 4*(x(2) - 2*x(3))^3;
    yp3 = 10*(x(3) - x(4)) - 8*(x(2) - 2*x(3))^3;
    yp4 = -10*(x(3) - x(4)) - 40*(x(1) - x(4))^3;
    yp = [yp1; yp2; yp3; yp4];

endfunction

% Definimos la matriz Jacobiana
function J = fpp(x)
        J = [
        2 + 120*(x(1) - x(4))^2, 20, 0, -120*(x(1) - x(4))^2;
        20, 200 + 12*(x(2) - 2*x(3))^2, -24*(x(2) - 2*x(3))^2, 0;
        0, -24*(x(2) - 2*x(3))^2, 10 + 48*(x(2) - 2*x(3))^2, -10;
        -120*(x(1) - x(4))^2, 0, -10, 10 + 120*(x(1) - x(4))^2
    ];

endfunction

% Definimos el punto inicial
x0 = [3;-1;0;1];

% Definimos el margen de error
epsilon = 0.01;

% Definimos la iteración
i = 1;
JJ = inv(fpp(x0));

while norm(fp(x0)) > epsilon
    S = -JJ * fp(x0);

    % Tasa de aprendizaje inicial
    ss = 0.001;
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
