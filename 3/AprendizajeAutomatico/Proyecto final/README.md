## Introducción del Proyecto

Este proyecto forma parte de la asignatura de Aprendizaje Automático y constituye una actividad integradora que representa el 25% de la calificación final del curso. Su objetivo es que los estudiantes apliquen de manera práctica y holística los conocimientos adquiridos durante la asignatura, enfrentándose a todas las fases de un proyecto real de aprendizaje automático. Desde el análisis inicial del conjunto de datos hasta la obtención de modelos predictivos y su presentación final, los estudiantes tendrán la oportunidad de trabajar en equipo, tomar decisiones fundamentadas y resolver problemas de forma autónoma.

El contexto del proyecto gira en torno a un centro educativo que busca mejorar la atención personalizada a sus estudiantes mediante el análisis de datos. Para ello, se han propuesto tres líneas de trabajo principales:

1. **Clusterización**: Identificar grupos de estudiantes con características similares para personalizar estrategias educativas.
2. **Clasificación**: Determinar qué estudiantes cumplen con los requisitos para obtener una beca según su rendimiento académico.
3. **Regresión**: Predecir la nota final de los estudiantes con base en la información disponible.

El conjunto de datos proporcionado está anonimizado y contiene información sobre características y desempeño académico de los estudiantes, además de datos recopilados a través de encuestas. Los equipos deben abordar los tres tipos de problemas aplicando técnicas de análisis exploratorio de datos (EDA), preprocesamiento, modelado y evaluación, demostrando una correcta implementación técnica y una capacidad de comunicación clara en la presentación de sus resultados.

## Requisitos

- Python 3.x
- Jupyter Notebook
- Librerías: pandas, numpy, seaborn, matplotlib, scikit-learn, scipy, DiCE, shap, joblib, plotly

## Descripción de archivos

- En primer lugar tenemos los archivos .csv que comienzan por DF seguido de un índice. Se corresponden con los dataframe utilizados en el proyecto. 
DF0.0_proy_escuela_dev es el dataframe original, dado por el profesor de la asignatura para poder llevar a cabo el proyecto. DF1.0_proy_escuela_eda_general es el dataframe del que parten todas las ramas del proyecto, porque se corresponde al df obtenido tras el un eda y preprocesamiento general, común tanto a regresión como a clasificación y clustering. Los demás csv se corresponden a ramas concretas del proyecto, indicadas en su nombre.

- Por otro lado tenemos los notebooks empleados, que siguen la misma lógica. Los que empiezan por N1 se corresponden con tareas de preprocesamiento y eda. El N1.0
es el correspondiente con el mencionado general, y a partir de este a los edas y preprocesamientos particulares de cada línea de trabajo. Los N2 se corresponden al bloque general de trabajo de cada área.

- Por último tenemos los archivos .pkl que comienzan por la letra P seguida de un índice. Esto indica que son persistencias necesarias para el correcto funcionamiento de la herramienta y para futuras modificaciones o extensiones. Hay que destacar que los P0 se corresponden a los escaladores entrenados de normalización y estandarización, pensados para ser utilizados con datos nuevos de entrada. Los P con índice numérico mayor a 0 se corresponden a ya modelos entrenados, ordenados por línea de trabajo y listos para ser utilizados donde se desee. 