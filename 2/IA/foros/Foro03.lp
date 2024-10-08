% casas.lp

casa(1..5).

tipo(persona, (britanico; sueco; danes; aleman; noruego)).
tipo(color, (rojo; azul; verde; amarillo; blanco)).
tipo(bebida, (te; cafe; leche; cerveza; agua)).
tipo(tabaco, (pall; dunhill; blends; prince; bluem)).
tipo(mascota, (pez; pajaro; gato; perro; caballo)).

% Restricción valores diferentes para un tipo en una casa
1 { en(C, T, V) : casa(C) } 1 :- tipo(T, V).
:- en(C, T, V1), en(C, T, V2), V1 != V2.

% El britanico vive en la casa roja.
:- en(C, persona, britanico), not en(C, color, rojo).

% El sueco tiene perros como mascotas.
:- en(C, persona, sueco), not en(C, mascota, perro).

% El danes bebe te.
:- en(C, persona, danes), not en(C, bebida, te).

% La casa verde esta inmediatamente a la izquierda de la casa blanca.
:- en(C, color, verde), not en(C+1, color, blanco).

% El dueno de la casa verde bebe cafe.
:- en(C, color, verde), not en(C, bebida, cafe).

% El que fuma Pall Mall cria pajaros.
:- en(C, tabaco, pall), not en(C, mascota, pajaro).

% El dueno de la casa amarilla fuma Dunhill.
:- en(C, color, amarillo), not en(C, tabaco, dunhill).

% El que vive en la casa central bebe leche.
:- not en(3, bebida, leche).

% El noruego vive en la primera casa.
:- not en(1, persona, noruego).

% El que fuma Blends es vecino del que tiene gatos.
:- en(C, tabaco, blends), not en(C-1, mascota, gato), not en(C+1, mascota, gato).

% El que tiene caballos vive al lado del que fuma Dunhill.
:- en(C, mascota, caballo), not en(C-1, tabaco, dunhill), not en(C+1, tabaco, dunhill).

% El que fuma Bluemasters bebe cerveza.
:- en(C, tabaco, bluem), not en(C, bebida, cerveza).

% El aleman fuma Prince.
:- en(C, persona, aleman), not en(C, tabaco, prince).

% El noruego vive al lado de la casa azul.
:- en(C, persona, noruego), not en(C+1, color, azul), not en(C-1, color, azul).

% El que fuma Blends vive al lado del que bebe agua.
:- en(C, tabaco, blends), not en(C+1, bebida, agua), not en(C-1, bebida, agua).

solucion(X) :- en(C, mascota, pez), en(C, persona, X).

#show solucion/1.