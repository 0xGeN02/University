# Programa Genera Carta
# Realizado por Equipo (5)
# 1  Miguel Abelairas    (Responsable quien sube el fichero)
# 2  Mario Baños     Participa : SI
# 3  Hugo Cabero     Participa : SI
# 4  Monica De Paula    Participa : SI
# 5  Manuel Delagado     Participa : SI
# Fecha: 12/11/2022
# Bibliotecas
import random
# Declaraciones

# Inicio
print("Programa generador de cartas al azar")
random.seed
Generador_aleatorio_1 = random.randint(1,12)
Generador_aleatorio_2 = random.randint(21,24)
if Generador_aleatorio_1 == 1:
    print("As ",end=" ")
elif Generador_aleatorio_1 == 10:
    print("Sota ",end=" ")
elif Generador_aleatorio_1 == 11:
    print("Caballo ",end=" ")
elif Generador_aleatorio_1 == 12:
    print("Rey ",end=" ")
else:
    print(Generador_aleatorio_1)

if Generador_aleatorio_2 == 21:
    print(" de Oros")
elif Generador_aleatorio_2 == 22:
    print("de Espadas")
elif Generador_aleatorio_2 == 23:
    print("de Bastos")
else:
    print("de Copas")
# Fin