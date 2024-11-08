# PLE02: Gimnasio - Partición del conjunto de datos e implementación de los modelos

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

### Descripción de los Archivos

- **PLE02_1_EDA_Pre.ipynb**: Notebook que contiene el análisis exploratorio de datos (EDA) y la preprocesamiento de los datos.
- **ple02_transform.csv**: Archivo CSV con los datos limpios y preprocesados.
- **PLE02_2_Modelos.ipynb**: Notebook que contiene la implementación y evaluación de los modelos de aprendizaje automático.
- **ple02_gimnasio.csv**: Archivo CSV con los datos originales del gimnasio.
- **rf_transform.pkl**: Modelo de Random Forest entrenado y guardado.
- **rl_transform.pkl**: Modelo de Regresión Lineal entrenado y guardado.
- **svr_transform.pkl**: Modelo de Support Vector Regression (SVR) entrenado y guardado.
- **X_test.csv**: Conjunto de características de prueba.
- **X_train.csv**: Conjunto de características de entrenamiento.
- **y_test.csv**: Conjunto de etiquetas de prueba.
- **y_train.csv**: Conjunto de etiquetas de entrenamiento.

## Canalización de Datos

La canalización de datos sigue los siguientes pasos:

1. **Análisis Exploratorio de Datos (EDA) y Preprocesamiento (PLE02_1_EDA_Pre.ipynb)**:
   - Ejecutar el notebook `PLE02_1_EDA_Pre.ipynb` para realizar el análisis exploratorio de datos y preprocesar los datos.
   - Guardar los datos limpios en `ple02transform.csv`.

2. **Partición del Conjunto de Datos (PLE02_2_Modelos.ipynb)**:
   - Dividir los datos en conjuntos de entrenamiento y prueba.
   - Guardar las particiones en `X_train.csv`, `X_test.csv`, `y_train.csv` y `y_test.csv`.

3. **Entrenamiento y Evaluación de Modelos (PLE02_2_Modelos.ipynb)**:
   - Ejecutar el notebook `PLE02_2_Modelos.ipynb` para entrenar y evaluar los modelos de aprendizaje automático.
   - Guardar los modelos entrenados en `rf_transform.pkl`, `rl_transform.pkl` y `svr_transform.pkl`.
