% reinas.lp
% clingo -c n=4 reinas.lp
% python pintar_reinas.py
% Define el tamaño del tablero y el número de reinas. Por defecto, 8
#const n=8.

% Define el dominio del tablero por filas y columnas
fila(1..n).
columna(1..n).
% de 1 a n

% Define un predicado a colocar en una posición determinada a la vez. Cardinalidad 1-1
1 { reina(X, Y) : fila(X) } 1 :- columna(Y).

% Resitricciones para evitar que una reina se ataque con otra 
% Restricción horizontal
:-reina(X, Y1), reina(X, Y2), Y1 != Y2.

% Restricción vertical
:-reina(X1, Y), reina(X2, Y), X1 != X2.

% Restricción diagonal
:-reina(X1, Y1), reina(X2, Y2), X1 != X2, Y1 != Y2, X1 + Y1 = X2 + Y2.
:-reina(X1, Y1), reina(X2, Y2), X1 != X2, Y1 != Y2, X1 - Y1 = X2 - Y2.

#show reina/2.