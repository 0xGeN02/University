%Definimos la funcion que queremos minimizar
 x=0;
 fcn = @(x) 100*(x(1)^2 - x(2))^2 + (1 - x(1))^2;
 %Determimanos el punto inicial
 x0 = [-2;-2];
 %Ejecutamos la busqueda del minimo
 [xmin, fval] = fminsearch (fcn, x0)
