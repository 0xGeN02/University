% Definimos la funcion que queremos minimizar
fcn = @(x) ((x(1) - 5)^2 + (x(2) - 8)^4 + 3*x(1)*x(2));

% Determinamos el punto inicial
x0 = [0; 0];

% Opciones para fminsearch
options = optimset('Display', 'iter', 'MaxIter', 1000);

% Ejecutamos la búsqueda del mínimo
[xmin, fval, exitflag, output] = fminsearch(fcn, x0, options);

% Mostramos los resultados
disp('Punto mínimo:')
disp(['x = ', num2str(xmin(1))]);
disp(['y = ', num2str(xmin(2))]);
disp(['Valor mínimo de la función: ', num2str(fval)]);

% Verificamos la convergencia
if exitflag == 1
  disp('La optimización convergió exitosamente.');
else
  disp('La optimización no convergió.');
end

% Mostramos información adicional
disp('Iteraciones: ', output.iterations);
disp('Valor de la función en el punto inicial: ', output.fval);

% Ejemplo de evaluación en el punto mínimo
f_minimo = fcn(xmin);
disp(['Valor de la función en el punto mínimo: ', num2str(f_minimo)]);

