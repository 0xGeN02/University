"""
Práctica 7: Aprendizaje automático
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Tuple, Union

import numpy as np
import yaml

N_FILAS = 3
N_COLS = 3

"""
Esqueleto: completar las partes marcadas con TODO.
"""


class JugadorTresEnRaya(ABC):
    """
    Clase abstracta que define un jugador genérico de tres en raya.
    """
    def __init__(self, nombre: str) -> None:
        """
        Inicializa un jugador con un nombre.

        :param nombre: Nombre del jugador.
        """
        self.name = nombre

        self._estados_juego_actual = (
            []
        )  # Conjunto de estados visitados en la partida en curso

        self._experiencia_estado_valor = ()  # Experiencia pasada del agente: estado -> valor

    @abstractmethod  # Las clases hijas deben implementar este método
    def decide_accion(
        self, posiciones: List[Tuple[int, int]], tablero: np.ndarray, token: int
    ) -> Tuple[int, int]:
        """
        Dado un tablero y un token, decide la próxima acción a realizar.

        :param posiciones: Lista de posiciones libres en el tablero.
        :param tablero: Estado actual del tablero.
        :param token: Token del jugador actual.
        :return: Tupla con las coordenadas de la acción a realizar.
        """

    def reset(self):
        """
        Resetea el jugador para una nueva partida.
        """
        self._estados_juego_actual = (
            []
        )  # Resetea la lista de estados visitados en la partida en curso

    def guarda_politica(self, path_artefacto: Path):
        """
        Guarda la política del jugador en un fichero YAML.

        :param path_artefacto: Ruta donde se guardará el fichero YAML.
        """
        with open(path_artefacto, "w", encoding='utf-8') as f:
            yaml.dump(self._experiencia_estado_valor, f, Dumper=yaml.Dumper)

    def carga_politica(self, path_artefacto: Path):
        """
        Carga la política de un fichero YAML.

        :param path_artefacto: Ruta del fichero Pickle a YAML.
        """
        with open(path_artefacto, "rb") as f:
            self._experiencia_estado_valor = yaml.load(f, Loader=yaml.FullLoader)

class JugadorTresEnRayaMaq(JugadorTresEnRaya):
    """
    Clase que define un jugador máquina de tres en raya.
    """
    def __init__(
        self,
        nombre,
        tasa_exploracion: float = 0.3,
        tasa_aprendizaje: float = 0.2,
        descuento_gamma: float = 0.9,
    ):
        """
        Inicializa un jugador máquina.

        :param nombre: Nombre del jugador.
        :param tasa_exploracion: Ratio de exploración para los jugadores máquina.
            Por defecto, 0.3. Indica la probabilidad de que el jugador
            elija una acción aleatoria en lugar de la mejor acción posible.
            No tiene efecto en los jugadores humanos.
        :param tasa_aprendizaje: Tasa de aprendizaje para el jugador.
        :param descuento_gamma: Factor de descuento gamma para el jugador.
        """
        super().__init__(nombre)

        self._tasa_exploracion = tasa_exploracion

        self._tasa_aprendizaje = tasa_aprendizaje
        self._descuento_gamma = descuento_gamma
        self._experiencia_estado_valor = (
            {}
        )  # Experiencia pasada del agente: estado -> valor. Histórico de todas las partidas jugadas

    def decide_accion(
        self, posiciones: List[Tuple[int, int]], tablero: np.ndarray, token: int
    ) -> Tuple[int, int]:
        if (
            np.random.uniform(0, 1) <= self._tasa_exploracion
        ): #Actua aleatoriamente en base a la tasa de exploracion dada
            return posiciones[np.random.choice(len(posiciones))]

        #Si no, elige la accion con el mayor valor (recompensa) de la tabla,
        # para el jugador actual
        valor_max = -np.inf #Inicializa el valor maximo como infinito negativo
        mejor_accion = None #Inicializa la mejor accion como nula
        #Explora todas las posibles acciones
        for p in posiciones:
            siguiente_tablero = tablero.copy()
            siguiente_tablero[p] = token #Simula la jugada

            #Invoca el metodo semiprimativo de JuegoTresEnRaya para serializar el estado
            siguiente_tablero_hash = JuegoTresEnRaya.serializa_estado(
                siguiente_tablero, N_FILAS, N_COLS
            )

            #Obten el valor de la tabla de valores, o 0 si no se había visitado nunca
            valor = self._experiencia_estado_valor.get(siguiente_tablero_hash) or 0

            #Comprueba si el valor actual es mayor que el maximo.
            # O sea, si es la mejor jugada posible
            if valor >= valor_max:
                valor_max = valor
                mejor_accion = p

        return mejor_accion

    def guarda_estado(self, s):
        """
        Guarda el estado actual del jugador en la lista de estados visitados de la partida.

        :param estado: Hash del estado actual del tablero.
        """
        self._estados_juego_actual.append(s)

    def retropropaga_recompensa(self, recompensa_final: float) -> None:
        """
        Retropropaga la recompensa final de la partida a la serie de estados visitados por el jugador,
        para aprender de la partida.

        :param recompensa: Recompensa final de la partida.
        """
        recompensa = recompensa_final #La recomensa del ultimo estado será la recompensa final

        #Recorre la lista de estados de la partida en orden inverso,
        # porque la recompensa se va afectando en funcion de la cercania al final
        for s in reversed (self._estados_juego_actual):
            #Asignamos como valor del estado si este no habia sido visto nunca antes por el agente
            # a lo largo de su experiencia
            if s not in self._experiencia_estado_valor:
                self._experiencia_estado_valor[s] = 0

            #Actualiza el valor asociado para el estado actual en base al valor conocido de antemano por el mismo,
            # recompensa residual gamma y la tasa de aprendizaje
            self._experiencia_estado_valor[s] += self._tasa_aprendizaje * (
                self._descuento_gamma * recompensa - self._experiencia_estado_valor[s]
                )

            #Actualiza la recompensa para los estados sucesivos
            self._experiencia_estado_valor[s] += recompensa


class JugadorTresEnRayaHum(JugadorTresEnRaya):
    """
    Clase que define un jugador humano de tres en raya.
    """
    def decide_accion(
        self, posiciones: List[Tuple[int, int]], tablero: np.ndarray, token: int
    ) -> Tuple[int, int]:
        print(f"Posiciones libres: {posiciones}")
        while True:
            try:
                x, y = (
                    input(
                        "Introduzca la posición (fila, columna) donde desea jugar: "
                    )
                    .strip()
                    .split(",")
                )
                x = int(x)
                y = int(y)
                if (x, y) in posiciones:
                    return x, y
                raise ValueError("Posición no válida.")
            except(ValueError, TypeError):
                print("Entrada no válida. Inténtelo de nuevo...")
                continue


class JuegoTresEnRaya:
    """
    Clase que define el juego de tres en raya.
    """
    def __init__(
        self, jugador1: JugadorTresEnRayaMaq, jugador2: JugadorTresEnRaya
    ) -> None:
        """
        Inicializa el juego con dos jugadores. 
        El jugador 1 siempre será una máquina, y el jugador 2 puede ser
        una máquina o un humano.
        """
        self._jugador1 = jugador1
        self._jugador2 = jugador2

        self._n_filas = N_FILAS
        self._n_cols = N_COLS
        self._tablero = np.zeros((self._n_filas, self._n_cols))

        self._fin = False
        self._estado = None
        self._siguiente_jugador = (
            1  # Empieza el jugador 1, luego se cambia a -1, jugador 2
        )

    @staticmethod
    def _serializa_estado(tablero: np.ndarray, n_filas: int, n_cols: int) -> str:
        """
        Calcula una representación en string del tablero actual,
        para poder ser guardado en un diccionario.

        :return: String con la representación del tablero.
        """
        return str(tablero.reshape(n_cols * n_filas))

    @classmethod
    def serializa_estado(cls, tablero: np.ndarray, n_filas: int, n_cols: int) -> str:
        """
        Método de clase que invoca al método privado _serializa_estado.

        :return: String con la representación del tablero.
        """
        return cls._serializa_estado(tablero, n_filas, n_cols)

    def __calcula_ganador(self) -> Union[int, None]:
        """
        Comprueba si hay un ganador en el tablero actual.
        """
        ganador = None

        # Check rows and columns
        for i in range(self._n_filas):
            if np.all(self._tablero[i, :] == self._tablero[i, 0]) and self._tablero[i, 0] != 0:
                ganador = self._tablero[i, 0]
                break
            if np.all(self._tablero[:, i] == self._tablero[0, i]) and self._tablero[0, i] != 0:
                ganador = self._tablero[0, i]
                break

        # Check diagonals
        if ganador is None:
            if np.all(self._tablero.diagonal() == self._tablero[0, 0]) and self._tablero[0, 0] != 0:
                ganador = self._tablero[0, 0]
            elif np.all(np.fliplr(self._tablero).diagonal() == self._tablero[0, -1]) and self._tablero[0, -1] != 0:
                ganador = self._tablero[0, -1]

        return ganador

    @staticmethod
    def _calcular_ganador(tablero: np.ndarray) -> Union[int, None]:
        """
        Método estático que invoca a __calcula_ganador.
        """
        return JuegoTresEnRaya.__calcula_ganador(tablero)

    def __get_posiciones_libres(self) -> List[Tuple[int, int]]:
        """
        Devuelve una lista con las posiciones libres en el tablero.
        """
        positions = []
        for i in range(self._n_filas):
            for j in range(self._n_cols):
                if self._tablero[i, j] == 0:
                    positions.append((i, j))
        return positions

    def __actualiza_estado(self, position: Tuple[int, int]) -> None:
        """
        Actualiza el estado del tablero tras una jugada.

        :param position: Tupla con las coordenadas de la jugada.
        """
        self._tablero[position] = self._siguiente_jugador
        self._siguiente_jugador = (
            -1 if self._siguiente_jugador == 1 else 1
        )  # Cambia de jugador
        self._estado = self._serializa_estado(
            self._tablero, self._n_filas, self._n_cols
        )

    def __recompensa(self):
        """
        Calcula la recompensa para los jugadores al final de la partida.
        """
        resultado = self.__calcula_ganador()

        #Retropropaga la recompensa
        if resultado == 1:
            self._jugador1.retropropaga_recompensa(1)

            if isinstance(self._jugador2, JugadorTresEnRayaMaq):
                self._jugador2.retropropaga_recompensa(0)

        elif resultado == -1:
            self._jugador1.retropropaga_recompensa(0)

            if isinstance(self._jugador2, JugadorTresEnRayaMaq):
                self._jugador2.retropropaga_recompensa(1)

        else: #Empate
            self._jugador1.retropropaga_recompensa(0.3)
            #Penalizamos el empate para que el agente tianda a evitarlo

            if isinstance(self._jugador2, JugadorTresEnRayaMaq):
                self._jugador2.retropropaga_recompensa(0.5)

    def __reset(self):
        """
        Resetea el tablero y el estado del juego.
        """
        self._tablero = np.zeros((self._n_filas, self._n_cols))
        self._estado = None
        self._fin = False
        self._siguiente_jugador = 1

    def fit(self, rondas: int = 100) -> None:
        """
        Alias para el método juega_maq_maq.

        :param rondas: Número de partidas a jugar.
        """
        for i in range(rondas):
            if i % 10 == 0:
                print(f"Partida {i}")
            self.jugar()

    def jugar(self) -> None:
        """
        Inicia una serie de partidas entre los dos jugadores máquinas.

        :param rondas: Número de partidas a jugar.
        """
        # Se comprueba si el jugador 2 es una máquina o un humano para determinar la verbosidad
        verbosidad = isinstance(self._jugador2, JugadorTresEnRayaHum)

        while not self._fin:
            posiciones = self.__get_posiciones_libres()

            #juega el jugador 1 (siempre maquina)
            accion_j1 = self._jugador1.decide_accion(posiciones, self._tablero, 1)
            self.__actualiza_estado(accion_j1)
            self.print_tablero(verbosidad)
            self._jugador1.guarda_estado(self._estado)

            #Comprueba si hay ganador
            victoria = self.__calcula_ganador()
            if victoria is not None:
                if victoria == 1:
                    self.__print_verbosidad(f'¡Ha ganado el jugador {self._jugador1.name}!', verbosidad)
                elif victoria == -1:
                    self.__print_verbosidad(f'¡Ha ganado el jugador {self._jugador2.name}!', verbosidad)
                else:
                    self.__print_verbosidad('¡Empate!', verbosidad)

                self.print_tablero(verbosidad)
                self.__recompensa()
                self._jugador1.reset()
                self._jugador2.reset()
                self.__reset()
                break

            posiciones = self.__get_posiciones_libres()

            if not posiciones:
                self.__print_verbosidad('¡Empate!', verbosidad)
                self.print_tablero(verbosidad)
                self.__recompensa()
                self._jugador1.reset()
                self._jugador2.reset()
                self.__reset()
                break

            #juega el jugador 2
            accion_j2 = self._jugador2.decide_accion(posiciones, self._tablero, -1)
            self.__actualiza_estado(accion_j2)
            self.print_tablero(verbosidad)
            #guradar estado solo si es maquina
            if isinstance(self._jugador2, JugadorTresEnRayaMaq):
                self._jugador2.guarda_estado(self._estado)

            #Comprueba si hay ganador
            victoria = self.__calcula_ganador()
            if victoria is not None:
                if victoria == 1:
                    self.__print_verbosidad(f'¡Ha ganado el jugador {self._jugador1.name}!', verbosidad)
                elif victoria == -1:
                    self.__print_verbosidad(f'¡Ha ganado el jugador {self._jugador2.name}!', verbosidad)
                else:
                    self.__print_verbosidad('¡Empate!', verbosidad)

                self.print_tablero(verbosidad)
                self.__recompensa()
                self._jugador1.reset()
                self._jugador2.reset()
                self.__reset()
                break

    def print_tablero(self, verboso: bool = True) -> None:
        """
        Imprime el tablero actual por pantalla.

        :param verboso: Booleano que indica si se imprimirá el tablero o no.
        """
        token = None
        if verboso:
            for i in range(0, self._n_filas):
                print("-------------")
                salida = "| "
                for j in range(0, self._n_cols):
                    if self._tablero[i, j] == 1:
                        token = "x"
                    if self._tablero[i, j] == -1:
                        token = "o"
                    if self._tablero[i, j] == 0:
                        token = " "
                    salida += token + " | "
                print(salida)
            print("-------------")

    def __print_verbosidad(self, msg: str, verboso: bool) -> None:
        """
        Imprime un mensaje si la verbosidad está activada.

        :param msg: Mensaje a imprimir.
        :param verboso: Booleano que indica si la verbosidad está activada.
        """
        if verboso:
            print(msg)
