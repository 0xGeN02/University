% taxi.lp

taxi(taxi1).
pasajero(ana; bea; carlos; daniel).

1 { viaje(T, P) : pasajero(P) } 4 :- taxi(T).

#show viaje/2.