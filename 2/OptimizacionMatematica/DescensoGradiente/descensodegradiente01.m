% Definimos la funcion objetivo
x=0;
function y = f(x)
    y = 0.5*(x(1)^2 + 3*x(2)^2);
endfunction

% Definimos el gradiente de la funcion objetivo
function yp = fp(x)
    yp(1) = x(1);
    yp(2) = 3*x(2);
endfunction

more on
%Definimos el punto inicial
x0(1) = 3;
x0(2) = 1;

i = 1;
%Definimos las iteraciones
while (norm(fp(x0)) > 1.e-6)
    S = -fp(x0);
    ss = 0.01;
    x1 = x0 + ss*S;

    while (ss > 1.e-12)
        while (f(x0) - f(x1)) > 0
            x0 = x1;
            x1 = x0 + ss*S;
            ss = 0.5*ss;
        endwhile
        x0 = x1;
        i = i + 1;
    endwhile
endwhile

disp("Numero de iteraciones:"), disp(i)
disp("Solucion:"), disp(x0)
disp("Valor de la funcion objetivo:"), disp(f(x0))
disp("Norma del gradiente:"), disp(norm(fp(x0)))