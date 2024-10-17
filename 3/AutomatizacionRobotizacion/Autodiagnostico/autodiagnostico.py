from tkinter import *
from tkinter import filedialog, messagebox

# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x600+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Autodiagnóstico - Madurez Digital')

# color de fondo de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=2, relief=RIDGE, bg='burlywood')
panel_superior.pack(side=TOP, fill=X, pady=10)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Autodiagnóstico - Madurez Digital', fg='azure4',
                        font=('Dosis', 48, 'bold'), bg='burlywood', pady=10)
etiqueta_titulo.pack()

# panel principal
panel_principal = Frame(aplicacion, bd=2, relief=RIDGE, bg='burlywood')
panel_principal.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)

# preguntas del cuestionario con ponderaciones
preguntas = [
    ("¿Cuál es el enfoque de tu negocio hacia la innovación tecnológica?", [
        ("No se considera la innovación tecnológica como prioridad", 1),
        ("Se exploran tendencias tecnológicas, pero no se han aplicado", 2),
        ("Se implementan innovaciones de manera gradual", 3),
        ("La innovación tecnológica es parte fundamental del negocio", 4)
    ]),
    ("¿Cómo gestionas la integración de nuevas tecnologías en tu negocio?", [
        ("No se han implementado nuevas tecnologías", 1),
        ("Se han realizado pruebas piloto con tecnologías nuevas", 2),
        ("Algunas tecnologías están completamente integradas", 3),
        ("La tecnología está completamente integrada y optimizada en todos los procesos", 4)
    ]),
    ("¿Qué tan ágil es tu negocio para adaptarse a cambios tecnológicos?", [
        ("No hay flexibilidad para adoptar cambios tecnológicos", 1),
        ("Existe alguna flexibilidad para adaptarse a nuevas tecnologías", 2),
        ("Se han implementado procesos para adaptar cambios tecnológicos rápidamente", 3),
        ("La organización es completamente ágil y se adapta continuamente", 4)
    ]),
    ("¿Cómo utilizas la analítica de datos en tu negocio?", [
        ("No se utilizan datos", 1),
        ("Se recogen datos básicos pero no se analizan", 2),
        ("Se analizan datos para mejorar algunas decisiones", 3),
        ("Los datos se utilizan de manera integral para decisiones estratégicas", 4)
    ]),
    ("¿Qué tecnologías emergentes has considerado implementar?", [
        ("Ninguna", 1),
        ("Inteligencia Artificial (IA)", 2),
        ("Internet de las Cosas (IoT)", 3),
        ("Blockchain", 4),
        ("Realidad Aumentada/Virtual", 5),
        ("Big Data", 6)
    ]),
    ("¿Cómo gestionas el conocimiento en tu negocio?", [
        ("No hay sistemas para gestionar el conocimiento", 1),
        ("El conocimiento se gestiona de forma informal", 2),
        ("Existen sistemas para capturar, compartir y almacenar el conocimiento", 3),
        ("Hay una gestión integral del conocimiento con herramientas digitales", 4)
    ]),
    ("¿Qué métodos de interacción digital están disponibles para tus clientes?", [
        ("Ninguno", 1),
        ("Correo electrónico", 2),
        ("Chat en vivo", 3),
        ("Chatbots automatizados", 4),
        ("Redes sociales con atención activa", 5)
    ]),
    ("¿Realizas seguimiento de la satisfacción de tus clientes de manera digital?", [
        ("No", 1),
        ("A través de encuestas manuales", 2),
        ("Se recopilan datos de clientes mediante herramientas digitales", 3),
        ("Se emplean sistemas avanzados de satisfacción de clientes", 4)
    ]),
    ("¿Utilizas inteligencia artificial o aprendizaje automático en tu negocio?", [
        ("No", 1),
        ("Se está evaluando", 2),
        ("Se utiliza en algunos procesos", 3),
        ("Es una parte integral del negocio", 4)
    ]),
    ("¿Qué tan automatizados están los flujos de trabajo internos?", [
        ("No están automatizados", 1),
        ("Algunos procesos están automatizados", 2),
        ("La mayoría de los flujos de trabajo están automatizados", 3),
        ("Los flujos de trabajo están completamente automatizados y optimizados", 4)
    ]),
    ("¿Qué nivel de integración tienen los diferentes sistemas digitales en tu empresa (ERP, CRM, etc.)?", [
        ("No hay integración", 1),
        ("Hay sistemas separados sin integración", 2),
        ("Los sistemas están integrados parcialmente", 3),
        ("Todos los sistemas están completamente integrados", 4)
    ]),
    ("¿Qué nivel de personalización ofreces a tus clientes a través de herramientas digitales?", [
        ("No ofrezco personalización", 1),
        ("Personalización básica (por ejemplo, segmentación)", 2),
        ("Ofrezco productos/servicios personalizados a través de datos de clientes", 3),
        ("Ofrezco experiencias personalizadas y automatizadas basadas en IA", 4)
    ]),
    ("¿Cómo se mide el retorno de inversión (ROI) de tus iniciativas digitales?", [
        ("No se mide", 1),
        ("Medición limitada a indicadores básicos", 2),
        ("Se mide mediante KPIs digitales", 3),
        ("Se realiza un análisis exhaustivo y continuo del ROI de las iniciativas digitales", 4)
    ]),
    ("¿Cuál es la capacidad de tu negocio para escalar sus operaciones mediante herramientas digitales?", [
        ("No hay capacidad para escalar", 1),
        ("Hay limitaciones significativas", 2),
        ("Se puede escalar en algunos aspectos del negocio", 3),
        ("El negocio es altamente escalable gracias a la digitalización", 4)
    ]),
    ("¿Qué herramientas utilizas para la planificación estratégica digital?", [
        ("No hay herramientas", 1),
        ("Herramientas básicas como hojas de cálculo", 2),
        ("Software de planificación empresarial (Ej. Balanced Scorecard)", 3),
        ("Software especializado en planificación y estrategia digital", 4)
    ]),
    ("¿Qué nivel de digitalización existe en tus procesos de cadena de suministro?", [
        ("No están digitalizados", 1),
        ("Algunos procesos están digitalizados", 2),
        ("La mayoría de los procesos están digitalizados", 3),
        ("La cadena de suministro está completamente digitalizada y automatizada", 4)
    ]),
    ("¿Cómo realizas el seguimiento de la innovación tecnológica en tu sector?", [
        ("No realizo seguimiento", 1),
        ("Recurro a fuentes informales", 2),
        ("Realizo investigaciones periódicas", 3),
        ("Tengo un equipo dedicado a identificar innovaciones tecnológicas", 4)
    ]),
    ("¿Utilizas soluciones de Big Data para analizar información de tu negocio?", [
        ("No", 1),
        ("Planeo hacerlo", 2),
        ("Uso Big Data para análisis ocasional", 3),
        ("Uso Big Data de forma continua en la toma de decisiones", 4)
    ]),
    ("¿Cómo gestionas los recursos tecnológicos en tu empresa?", [
        ("No hay gestión", 1),
        ("Los recursos tecnológicos se gestionan de forma básica", 2),
        ("Hay una gestión planificada de los recursos tecnológicos", 3),
        ("Los recursos tecnológicos se gestionan de forma óptima con planificación continua", 4)
    ]),
    ("¿En qué nivel consideras que tu empresa se encuentra respecto a la competencia en términos de digitalización?", [
        ("Muy por detrás", 1),
        ("Ligeramente por detrás", 2),
        ("Al mismo nivel", 3),
        ("Por delante de la competencia", 4)
    ])
]

# índice de la pregunta actual
indice_pregunta = 0

# variable para almacenar las respuestas
respuestas = []

# variable para la respuesta actual
var_respuesta = StringVar()

# función para mostrar la pregunta actual
def mostrar_pregunta():
    global indice_pregunta
    pregunta, opciones = preguntas[indice_pregunta]
    etiqueta_pregunta.config(text=pregunta)
    for i, (opcion, valor) in enumerate(opciones):
        if i < len(radiobuttons):
            radiobuttons[i].config(text=opcion, value=valor)
            radiobuttons[i].pack(anchor=W, padx=20, pady=2)
        else:
            rb = Radiobutton(panel_principal, text=opcion, variable=var_respuesta, value=valor, font=('Dosis', 18), bg='burlywood', fg='azure4')
            rb.pack(anchor=W, padx=20, pady=2)
            radiobuttons.append(rb)
    for i in range(len(opciones), len(radiobuttons)):
        radiobuttons[i].pack_forget()
    var_respuesta.set(None)

# función para manejar el botón "Siguiente"
def siguiente_pregunta():
    global indice_pregunta
    respuesta = var_respuesta.get()
    if respuesta:
        respuestas.append(int(respuesta))
        indice_pregunta += 1
        if indice_pregunta < len(preguntas):
            mostrar_pregunta()
        else:
            mostrar_resultado()
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una opción antes de continuar.")

# función para mostrar el resultado final
def mostrar_resultado():
    puntuacion_total = sum(respuestas)
    if puntuacion_total <= 40:
        valoracion = "Baja madurez digital"
    elif puntuacion_total <= 60:
        valoracion = "Madurez digital media"
    else:
        valoracion = "Alta madurez digital"
    
    messagebox.showinfo("Resultado", f"Tu puntuación total es: {puntuacion_total}\nValoración: {valoracion}")
    aplicacion.quit()

# etiqueta para la pregunta
etiqueta_pregunta = Label(panel_principal, text="", font=('Dosis', 18, 'bold'), bg='burlywood', fg='azure4')
etiqueta_pregunta.pack(pady=20)

# radiobuttons para las opciones
radiobuttons = []

# mostrar la primera pregunta
mostrar_pregunta()

# botón "Siguiente"
boton_siguiente = Button(panel_principal, text="Siguiente", font=('Dosis', 14, 'bold'), bg='azure4', fg='white', command=siguiente_pregunta)
boton_siguiente.pack(pady=20, side=BOTTOM)

# evitar que la pantalla se cierre
aplicacion.mainloop()
