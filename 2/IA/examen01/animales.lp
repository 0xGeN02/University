% Definición de animales
animal(leon).
animal(cebra).
animal(jirafa).
animal(antilope).
animal(tigre).
animal(bufalo).
animal(cocodrilo).

% Definición de hábitats
habitat(1..3).

% Clasificación de animales
carnivoro(leon).
carnivoro(tigre).
carnivoro(cocodrilo).
herbivoro(X) :- animal(X), not carnivoro(X).

% Animales solitarios
solitario(tigre).

% Restricciones de cohabitación debido a la depredación
depredador_presa(leon, cebra).
depredador_presa(leon, antilope).
depredador_presa(leon, bufalo).
depredador_presa(cocodrilo, cebra).
depredador_presa(cocodrilo, bufalo).
depredador_presa(tigre, bufalo).

% Asignación de animales a hábitats
1 { en_habitat(A,H) : habitat(H) } 1 :- animal(A).

% Restricción para separar carnívoros de herbívoros
:- en_habitat(A,H), en_habitat(B,H), carnivoro(A), herbivoro(B).

% Restricción para animales solitarios
:- en_habitat(A,H), en_habitat(B,H), A != B, solitario(A).

% Restricción para evitar depredadores con sus presas
:- en_habitat(A,H), en_habitat(B,H), depredador_presa(A,B).

% Visualización de resultados
#show en_habitat/2.
