x = 0;

% Definimos la funcion objetivo
function y = f(x)
  y = (x(1) + 2*x(2) - 7)^2 + (2*x(1) + x(2) - 5)^2;
endfunction

% Definimos el gradiente de la funcion objetivo
function yp = fp(x)
  yp(1) = 2*(x(1) + 2*x(2) - 7) + 4*(2*x(1) + x(2) - 5);
  yp(2) = 4*(x(1) + 2*x(2) - 7) + 2*(2*x(1) + x(2) - 5);
endfunction

% Punto inicial, margen de error y tasa de aprendizaje inicial
x0 = [0; 0];
epsilon = 0.0001;
S0 = 0.01;

% Bucle principal
i = 1;
while norm(fp(x0)) > epsilon
  S = S0 / 2^i;
  d = -fp(x0);
  x1 = x0 + S * d;
  while f(x0) - f(x1) > 0
    x0 = x1;
    x1 = x0 + S * d;
    S = S / 2;
  end
  x0 = x1;
  i = i + 1;
end

% Mostrar resultados
disp("Número de iteraciones:"), disp(i)
disp("Solución:"), disp(x0)
disp("Valor de la función objetivo:"), disp(f(x0))
disp("Norma del gradiente:"), disp(norm(fp(x0)))

