% torres.lp
% clingo -c n=4 torres.lp
% 
% Define el tamaño del tablero y el número de torres. Por defecto, 10
#const n=10.

% Define el dominio del tablero por filas y columnas
fila(1..n).
columna(1..n).
% de 1 a n

% Define un predicado a colocar en una posición determinada a la vez. Cardinalidad 1-1
1 { torre(X, Y) : fila(X) } 1 :- columna(Y).

% Resitricciones para evitar que una torre se ataque con otra 
% Restricción horizontal
:-torre(X, Y1), torre(X, Y2), Y1 != Y2.

% Restricción vertical
:-torre(X1, Y), torre(X2, Y), X1 != X2.

#show torre/2.
