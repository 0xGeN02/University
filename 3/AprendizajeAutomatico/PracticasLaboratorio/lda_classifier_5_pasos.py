"""
Este módulo contiene la clase `LDAClassifier5Pasos`, implementada a partir de las piezas desarrolladas
en el notebook de la PL04 `pl04_lda_5_pasos.ipynb`. Revísese dicho notebook para más información.

Cópiese la clase en una celda del notebook o utilícese el comando mágico `%load` para cargar el código
a partir de este archivo. Indicación de celda mágica:

```python
%load ../src/lda_classifier_5_pasos.py  # Edítese la ruta si es necesario
```
"""

import numpy as np


class LDAClassifier5Pasos:
    """
    Implementación de un clasificador LDA basado en los 5 pasos descritos en las
    transparencias de la asignatura [Transparencias U2-S05].
    """

    def __init__(self, n_discriminantes):
        self.n_discriminantes = n_discriminantes

        # Atributos para guardar los resultados del entrenamiento. Se inicializan a `None`
        self.W = None
        self.centroides = None

        # Mensaje de error si no se ha entrenado el modelo
        self._msg_error_no_entrenado = (
            "No se ha entrenado el modelo. Úsese `fit` antes de proyectar los datos."
        )

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Ajusta el clasificador LDA a los datos de entrenamiento `X` e `y`.

        :param X: Datos de entrenamiento, características.
        :param y: Etiquetas de los datos de entrenamiento.
        """
        # Vector de medias de las clases
        mv = np.array([self.__calcular_vector_m(X, y, cl) for cl in np.unique(y)])

        # Matrices de dispersión intra e interclase
        s_intra = np.sum(
            [
                self.__calcular_matriz_dispersion_intra(X, y, cl, mv)
                for cl, mv in zip(np.unique(y), mv)
            ],
            axis=0,
        )
        s_inter = self.__calcular_matriz_dispersion_inter(X, y, mv)

        # Eigenvalores y eigenvectores
        eig_vals, eig_vecs = self.__calcular_matriz_eigen(s_intra, s_inter)

        # Seleccionar los discriminantes lineales: eigenvectores asociados a los mayores eigenvalores
        self.W = self.__seleccionar_discriminantes_lineales(
            eig_vals, eig_vecs, s_inter, self.n_discriminantes
        )  # Matriz de proyección. Se guarda como atributo de la clase para usar en `predict`

        # Proyección de los datos de entrenamiento
        X_proy = self.proyectar(X)

        # Cálculo de los centroides de las clases en el espacio de las características proyectadas
        self.centroides = np.array(
            [np.mean(X_proy[y == cl], axis=0) for cl in np.unique(y)]
        )  # Se guarda como atributo de la clase para usar en `predict`

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predice las etiquetas de las nuevas muestras de entrada `X`.

        :param X: Nuevas características de entrada.
        :return: Etiquetas inferidas para las muestras de entrada.
        """
        if self.W is None or self.centroides is None:
            raise ValueError(self._msg_error_no_entrenado)

        # Se proyectan los datos nuevos en el espacio de las características transformadas
        X_proy = self.proyectar(X)

        # Se infiere la clase midiendo la distancia euclídea a los centroides, asignando la clase más cercana
        y_pred = np.zeros(X_proy.shape[0])
        for i, x in enumerate(X_proy):
            y_pred[i] = (
                np.argmin(
                    [np.linalg.norm(x - centroide) for centroide in self.centroides]
                )
                + 1
            )

        return y_pred

    def proyectar(self, X):
        """
        Proyecta los datos `X` en el espacio de las características transformadas por `W`.

        Este método se expone públicamente, además de `fit` y `predict`, para permitir
        calcular proyecciones de datos en el subespacio de las características transformadas, lo
        que típicamente será útil para visualizaciones que ayuden a explicar el modelo.

        :param X: Datos a proyectar.
        """
        if self.W is None:
            raise ValueError(self._msg_error_no_entrenado)

        return X.dot(self.W)

    ###############################################################
    # Se incluyen las funciones desarrolladas en las celdas anteriores como métodos privados
    # de la clase. Se usan métodos estáticos por conveniencia, ya que no se necesita acceder
    # a los atributos de la clase, que se pasan como argumentos a los métodos

    @staticmethod
    def __calcular_vector_m(X, y, cl):
        m = np.mean(X[y == cl], axis=0)
        return m

    @staticmethod
    def __calcular_matriz_dispersion_intra(X, y, cl, mv):
        m_global = np.mean(X, axis=0).reshape(X.shape[1], 1)

        s_inter = np.zeros((X.shape[1], X.shape[1]))

        for row in X[y == cl]:
            row, mv = row.reshape(X.shape[1], 1), mv.reshape(X.shape[1], 1)
            s_inter += (row - mv).dot((row - mv).T)

        return s_inter

    @staticmethod
    def __calcular_matriz_dispersion_inter(X, y, mv):
        m_global = np.mean(X, axis=0).reshape(X.shape[1], 1)

        s_inter = np.zeros((X.shape[1], X.shape[1]))

        for cl, m in zip(np.unique(y), mv):
            m = m.reshape(X.shape[1], 1)
            s_inter += (m - m_global).dot((m - m_global).T)

        return s_inter

    @staticmethod
    def __calcular_matriz_eigen(s_intra, s_inter):
        eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(s_intra).dot(s_inter))

        for i in range(len(eig_vals)):
            eig_vec = eig_vecs[:, i].reshape(s_inter.shape[0], 1)
            eig_val = eig_vals[i]
            A = np.linalg.inv(s_intra).dot(s_inter)
            np.testing.assert_array_almost_equal(
                A.dot(eig_vec),
                eig_val * eig_vec,
                decimal=6,
                err_msg=f"Error en el vector propio {i}",
            )
        print(f"Eigenvectores y eigenvalores correctos.")

        return eig_vals, eig_vecs

    @staticmethod
    def __seleccionar_discriminantes_lineales(
        eig_vals, eig_vecs, s_inter, n_discriminantes
    ):
        eig_pares = [
            (np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))
        ]
        eig_pares = sorted(eig_pares, key=lambda k: k[0], reverse=True)

        eig_vals_sum = sum(eig_vals)
        print(f"La varianza explicada por cada discriminante lineal es:")
        for par_idx, par in enumerate(eig_pares):
            print(f"Par {par_idx}: `{(par[0]/eig_vals_sum).real:.2%}`")

        return np.hstack(
            [
                eig_pares[i][1].reshape(s_inter.shape[0], 1)
                for i in range(n_discriminantes)
            ]
        )  # Matriz de proyección, `W`
