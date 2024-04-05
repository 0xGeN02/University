 %Definimos la funcion que queremos minimizar
 x=0;
 fcn = @(x) (x(1)+10*x(2)).^2+5*(x(3)-x(4)).^2+(x(2)-2*x(3)).^4+10*(x(1)-x(4)).^4;
 %Determimanos el punto inicial
 x0 = [3; -1; 0; 1];
 %Ejecutamos la busqueda del minimo
 [xmin, fval] = fminsearch (fcn, x0)
