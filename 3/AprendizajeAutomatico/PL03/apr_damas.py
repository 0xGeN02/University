from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Tuple, Union
import numpy as np
import yaml

N_FILAS = 8
N_COLS = 8

class JugadorDamas(ABC):
    def __init__(self, nombre: str) -> None:
        self.name = nombre
        self._estados_juego_actual = []
        self._experiencia_estado_valor = {}

    @abstractmethod
    def decide_accion(self, posiciones: List[Tuple[int, int]], tablero: np.ndarray, token: int) -> Tuple[int, int, int, int]:
        pass

    def reset(self):
        self._estados_juego_actual = []

    def guarda_politica(self, path_artefacto: Path):
        with open(path_artefacto, "w", encoding='utf-8') as f:
            yaml.dump(self._experiencia_estado_valor, f, Dumper=yaml.Dumper)

    def carga_politica(self, path_artefacto: Path):
        with open(path_artefacto, "rb") as f:
            self._experiencia_estado_valor = yaml.load(f, Loader=yaml.FullLoader)

class JugadorDamasMaq(JugadorDamas):
    def __init__(self, nombre, tasa_exploracion: float = 0.3, tasa_aprendizaje: float = 0.2, descuento_gamma: float = 0.9):
        super().__init__(nombre)
        self._tasa_exploracion = tasa_exploracion
        self._tasa_aprendizaje = tasa_aprendizaje
        self._descuento_gamma = descuento_gamma

    def decide_accion(self, posiciones: List[Tuple[int, int]], tablero: np.ndarray, token: int) -> Tuple[int, int, int, int]:
        movimientos_validos = []
        for origen in posiciones:
            if tablero[origen] == token:  # Revisar solo las piezas del jugador actual
                for dx in [-1, 1]:
                    for dy in [-1, 1]:
                        destino_simple = (origen[0] + dx, origen[1] + dy)
                        destino_salto = (origen[0] + 2*dx, origen[1] + 2*dy)
                        
                        # Movimiento simple
                        if JuegoDamas.es_movimiento_valido(tablero, origen, destino_simple, token):
                            movimientos_validos.append((*origen, *destino_simple))
                        
                        # Movimiento de captura
                        if JuegoDamas.es_movimiento_valido(tablero, origen, destino_salto, token):
                            movimientos_validos.append((*origen, *destino_salto))

        print(f"Movimientos válidos para {self.name}: {movimientos_validos}")
        if not movimientos_validos:
            return None  # No hay movimientos disponibles

        if np.random.uniform(0, 1) <= self._tasa_exploracion:
            return movimientos_validos[np.random.choice(len(movimientos_validos))]

        # Selección de mejor acción basada en política
        valor_max = -np.inf
        mejor_accion = None
        for movimiento in movimientos_validos:
            origen, destino = (movimiento[0], movimiento[1]), (movimiento[2], movimiento[3])
            siguiente_tablero = tablero.copy()
            JuegoDamas.mover_pieza(siguiente_tablero, origen, destino)
            siguiente_tablero_hash = JuegoDamas.serializa_estado(siguiente_tablero, N_FILAS, N_COLS)
            valor = self._experiencia_estado_valor.get(siguiente_tablero_hash, 0)
            if valor > valor_max:
                valor_max = valor
                mejor_accion = movimiento

        return mejor_accion

    def guarda_estado(self, s):
        self._estados_juego_actual.append(s)

    def retropropaga_recompensa(self, recompensa_final: float) -> None:
        recompensa = recompensa_final
        for s in reversed(self._estados_juego_actual):
            if s not in self._experiencia_estado_valor:
                self._experiencia_estado_valor[s] = 0
            self._experiencia_estado_valor[s] += self._tasa_aprendizaje * (
                self._descuento_gamma * recompensa - self._experiencia_estado_valor[s]
            )
            recompensa = self._experiencia_estado_valor[s]

class JugadorDamasHum(JugadorDamas):
    def decide_accion(self, posiciones: List[Tuple[int, int]], tablero: np.ndarray, token: int) -> Tuple[int, int, int, int]:
        print(f"Posiciones libres: {posiciones}")
        while True:
            try:
                x1, y1, x2, y2 = input("Introduzca la posición de origen (fila, columna) y destino (fila, columna) donde desea jugar: ").strip().split(",")
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                if (x1, y1) in posiciones and JuegoDamas.es_movimiento_valido(tablero, (x1, y1), (x2, y2), token):
                    return x1, y1, x2, y2
                raise ValueError("Movimiento no válido.")
            except(ValueError, TypeError):
                print("Entrada no válida. Inténtelo de nuevo...")
                continue

    def guarda_estado(self, s):
        pass  # Do nothing for human player

class JuegoDamas:
    def __init__(self, jugador1: JugadorDamas, jugador2: JugadorDamas) -> None:
        self._jugador1 = jugador1
        self._jugador2 = jugador2
        self._n_filas = N_FILAS
        self._n_cols = N_COLS
        self._tablero = self.inicializar_tablero()
        self._fin = False
        self._estado = None
        self._siguiente_jugador = 1
        self.print_tablero()  # Print the initial board setup

    def inicializar_tablero(self) -> np.ndarray:
        tablero = np.zeros((self._n_filas, self._n_cols))
        # Place player 1 pieces (white) on the dark squares of the first three rows
        for i in range(3):
            for j in range(self._n_cols):
                if (i + j) % 2 == 1:
                    tablero[i, j] = 1
        # Place player 2 pieces (black) on the dark squares of the last three rows
        for i in range(5, 8):
            for j in range(self._n_cols):
                if (i + j) % 2 == 1:
                    tablero[i, j] = -1
        return tablero

    @staticmethod
    def _serializa_estado(tablero: np.ndarray, n_filas: int, n_cols: int) -> str:
        return str(tablero.reshape(n_cols * n_filas))

    @classmethod
    def serializa_estado(cls, tablero: np.ndarray, n_filas: int, n_cols: int) -> str:
        return cls._serializa_estado(tablero, n_filas, n_cols)

    def __calcula_ganador(self) -> Union[int, None]:
        piezas_jugador1 = np.sum(self._tablero == 1)
        piezas_jugador2 = np.sum(self._tablero == -1)

        if piezas_jugador1 == 0:
            return -1
        if piezas_jugador2 == 0:
            return 1

        if not self.__get_posiciones_libres():
            if self._siguiente_jugador == 1:
                return -1
            else:
                return 1

        return None

    @staticmethod
    def es_movimiento_valido(tablero: np.ndarray, origen: Tuple[int, int], destino: Tuple[int, int], jugador: int) -> bool:
        if not (0 <= destino[0] < tablero.shape[0] and 0 <= destino[1] < tablero.shape[1]):
            return False
        if tablero[destino] != 0:  # El destino debe estar vacío
            return False
        dx = destino[0] - origen[0]
        dy = destino[1] - origen[1]
        
        # Movimiento simple
        if abs(dx) == 1 and abs(dy) == 1 and jugador * dx > 0:  # Debe moverse en dirección correcta (hacia adelante)
            return True

        # Captura
        if abs(dx) == 2 and abs(dy) == 2:
            medio = ((origen[0] + destino[0]) // 2, (origen[1] + destino[1]) // 2)
            if tablero[medio] == -jugador:  # La casilla intermedia debe tener una pieza enemiga
                return True
        
        return False

    @staticmethod
    def mover_pieza(tablero: np.ndarray, origen: Tuple[int, int], destino: Tuple[int, int]) -> None:
        jugador = tablero[origen]
        tablero[origen] = 0
        tablero[destino] = jugador
        if abs(destino[0] - origen[0]) == 2:
            medio = ((origen[0] + destino[0]) // 2, (origen[1] + destino[1]) // 2)
            tablero[medio] = 0
        if destino[0] == 0 and jugador == 1:
            tablero[destino] = 2  # King for player 1
        if destino[0] == tablero.shape[0] - 1 and jugador == -1:
            tablero[destino] = -2  # King for player 2

    def __get_posiciones_libres(self) -> List[Tuple[int, int]]:
        positions = []
        for i in range(self._n_filas):
            for j in range(self._n_cols):
                if self._tablero[i, j] == self._siguiente_jugador:
                    positions.append((i, j))
        return positions

    def __actualiza_estado(self, origen: Tuple[int, int], destino: Tuple[int, int]) -> None:
        self.mover_pieza(self._tablero, origen, destino)
        self._siguiente_jugador = -self._siguiente_jugador
        self._estado = self._serializa_estado(self._tablero, self._n_filas, self._n_cols)

    def __recompensa(self):
        resultado = self.__calcula_ganador()
        if resultado == 1:
            self._jugador1.retropropaga_recompensa(1)
            if isinstance(self._jugador2, JugadorDamasMaq):
                self._jugador2.retropropaga_recompensa(0)
        elif resultado == -1:
            self._jugador1.retropropaga_recompensa(0)
            if isinstance(self._jugador2, JugadorDamasMaq):
                self._jugador2.retropropaga_recompensa(1)
        else:
            self._jugador1.retropropaga_recompensa(0.3)
            if isinstance(self._jugador2, JugadorDamasMaq):
                self._jugador2.retropropaga_recompensa(0.5)

    def __reset(self):
        self._tablero = self.inicializar_tablero()
        self._estado = None
        self._fin = False
        self._siguiente_jugador = 1

    def fit(self, rondas: int = 100) -> None:
        for i in range(rondas):
            if i % 10 == 0:
                print(f"Partida {i}")
            self.jugar()

    def jugar(self) -> None:
        verbosidad = isinstance(self._jugador2, JugadorDamasHum)
        while not self._fin:
            posiciones = self.__get_posiciones_libres()
            accion_j1 = self._jugador1.decide_accion(posiciones, self._tablero, 1)
            if accion_j1 is None:
                print(f"No valid moves for {self._jugador1.name}")
                self._fin = True
                break
            if accion_j1 is not None:
                self.__actualiza_estado((accion_j1[0], accion_j1[1]), (accion_j1[2], accion_j1[3]))
            else:
                print("Error: La acción de jugador 1 es None")
            self.print_tablero(verbosidad)
            self._jugador1.guarda_estado(self._estado)
            victoria = self.__calcula_ganador()
            if victoria is not None:
                self.__print_verbosidad(f'¡Ha ganado el jugador {self._jugador1.name}!', verbosidad)
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
            accion_j2 = self._jugador2.decide_accion(posiciones, self._tablero, -1)
            if accion_j2 is None:
                print(f"No valid moves for {self._jugador2.name}")
                self._fin = True
                break
            self.__actualiza_estado((accion_j2[0], accion_j2[1]), (accion_j2[2], accion_j2[3]))
            self.print_tablero(verbosidad)
            if isinstance(self._jugador2, JugadorDamasMaq):
                self._jugador2.guarda_estado(self._estado)
            victoria = self.__calcula_ganador()
            if victoria is not None:
                self.__print_verbosidad(f'¡Ha ganado el jugador {self._jugador2.name}!', verbosidad)
                self.print_tablero(verbosidad)
                self.__recompensa()
                self._jugador1.reset()
                self._jugador2.reset()
                self.__reset()
                break

    def print_tablero(self, verboso: bool = True) -> None:
        if verboso:
            for i in range(0, self._n_filas):
                print("-------------")
                salida = "| "
                for j in range(0, self._n_cols):
                    token = " "
                    if self._tablero[i, j] == 1:
                        token = "x"
                    elif self._tablero[i, j] == -1:
                        token = "o"
                    elif self._tablero[i, j] == 2:
                        token = "X"
                    elif self._tablero[i, j] == -2:
                        token = "O"
                    salida += token + " | "
                print(salida)
            print("-------------")

    def __print_verbosidad(self, msg: str, verboso: bool) -> None:
        if verboso:
            print(msg)