# Actividad Práctica: La Ruleta Francesa

## Computación Cuántica y Natural - Sesión 05

**Alumno:** Mateo Delgado  
**Profesor:** Yago González Rozas  
**Fecha:** 8 Octubre 2025

---

## 1. Objetivos de la Actividad

El objetivo de esta práctica es trabajar con múltiples qubits implementando un juego de ruleta francesa mediante circuitos cuánticos, demostrando los conceptos de:

- Superposición cuántica
- Medición y colapso del estado
- Independencia de circuitos cuánticos
- Manipulación de estados mediante compuertas

---

## 2. Respuestas a las Preguntas de la Práctica

### Pregunta 1: ¿Qué necesitas para representar 37 números?

**Respuesta:**

Se necesitan **6 qubits** para representar los 37 números de la ruleta francesa (0-36).

**Justificación:**

- Con n qubits podemos representar 2^n estados diferentes
- 5 qubits: 2^5 = 32 estados (insuficiente para 37 números)
- 6 qubits: 2^6 = 64 estados (suficiente para 37 números)

Por lo tanto, 6 qubits es el mínimo necesario, aunque genera estados adicionales (37-63) que deben ser descartados.

---

### Pregunta 2: ¿Qué debes hacer si el número resultante del croupier no está entre los 37?

**Respuesta:**

Se debe **repetir la medición del circuito cuántico** hasta obtener un número válido en el rango [0-36].

**Implementación:**

```python
while True:
    # Crear circuito, aplicar Hadamard, medir
    numero = convertir_bits_a_decimal(resultado)
    
    if numero <= 36:
        return numero  # Número válido
    # Si numero > 36, el bucle continúa
```

**Justificación:**
Esta técnica, conocida como "rejection sampling", mantiene la distribución uniforme de probabilidades para todos los números válidos (0-36), sin sesgar el resultado hacia ningún número específico.

---

### Pregunta 3: ¿Qué necesitas para representar las apuestas?

**Respuesta:**

Para representar todas las apuestas posibles se utiliza una **combinación de circuitos**:

1. **3 qubits principales** para determinar el tipo de apuesta:
   - 2^3 = 8 posibles combinaciones
   - Suficiente para los 4 tipos de apuesta (número, paridad, rango, color)

2. **6 qubits adicionales** cuando se apuesta a un número específico:
   - Necesario para generar números en el rango [0-36]
   - Solo se ejecuta este circuito si el tipo de apuesta lo requiere

**Mapeo de apuestas:**

```sh
Valor 0:     Número específico (requiere 6 qubits adicionales)
Valor 1-2:   Paridad (par/impar)
Valor 3-4:   Rango (manque 1-18 / passe 19-36)
Valor 5-7:   Color (rojo/negro)
```

---

### Pregunta 4: ¿Mismo algoritmo cuántico para mantener la independencia?

**Respuesta:**

Sí, todos los participantes (croupier, jugador 1, jugador 2) utilizan el **mismo algoritmo cuántico básico**, pero cada uno ejecuta su **propio circuito independiente**.

**Algoritmo común:**

1. Inicializar qubits en estado |0⟩
2. Aplicar compuerta Hadamard (H) a todos los qubits
3. Medir todos los qubits
4. Convertir resultado binario a decimal

**Independencia garantizada:**

- Cada participante tiene su propia instancia de `get_qc()`
- Los circuitos se ejecutan de forma aislada
- No hay entrelazamiento entre los qubits de diferentes participantes
- Las mediciones de un circuito no afectan a los demás

**Código:**

```python
# Croupier - circuito independiente
qc_croupier = get_qc('6q-qvm')
numero_croupier = generar_numero_croupier()

# Jugador 1 - circuito independiente
qc_jugador1 = get_qc('3q-qvm')
apuesta_j1 = generar_apuesta_jugador(1)

# Jugador 2 - circuito independiente
qc_jugador2 = get_qc('3q-qvm')
apuesta_j2 = generar_apuesta_jugador(2)
```

---

## 3. Análisis de la Implementación

### Parte 1: Ruleta Normal

**Características principales:**

- Circuitos cuánticos completamente independientes
- Distribución uniforme de probabilidades
- Sin interferencia entre participantes
- Simulación honesta del juego

**Resultados esperados:**

- Probabilidad teórica de ganar depende del tipo de apuesta:
  - Número específico: 1/37 ≈ 2.7%
  - Paridad/Color: 18/37 ≈ 48.6%
  - Rango (manque/passe): 18/37 ≈ 48.6%

### Parte 2: Ruleta con Trampas

**Mecanismo de trampa:**

1. El croupier espía a un jugador aleatorio
2. Verifica si su número inicial coincide con la apuesta espiada
3. Si hay coincidencia, aplica una compuerta X a un qubit aleatorio
4. Esto modifica el estado cuántico y cambia el número resultante

**Implementación de la trampa:**

```python
# Si hay coincidencia, voltear un qubit aleatorio
qubit_a_cambiar = random.randint(0, 5)
p += X(qubit_a_cambiar)  # Compuerta NOT cuántica
```

**Impacto:**

- La casa (croupier) tiene ventaja adicional
- Los jugadores pierden con mayor frecuencia
- El croupier acumula más monedas a lo largo del juego

---

## 4. Conceptos Cuánticos Aplicados

### Superposición

- Los qubits existen en superposición de estados |0⟩ y |1⟩
- La compuerta Hadamard crea esta superposición equiprobable
- Todos los números tienen la misma probabilidad antes de la medición

### Medición

- Colapsa el estado cuántico a un valor clásico definido
- Proceso irreversible
- Proporciona el resultado aleatorio del juego

### Compuertas Cuánticas

- **H (Hadamard):** Crea superposición uniforme
- **X (NOT):** Invierte el estado del qubit (usada en las trampas)
- **MEASURE:** Colapsa el estado y obtiene valor clásico

### Independencia Cuántica

- Circuitos separados aseguran que no hay correlación
- Fundamental para la equidad del juego (Parte 1)
- Permite manipulación selectiva (Parte 2)

---

## 5. Conclusiones

Esta práctica ha permitido:

1. **Comprender el uso de múltiples qubits** para representar información compleja (37 números, 4 tipos de apuestas)

2. **Aplicar conceptos cuánticos fundamentales** como superposición, medición y manipulación de estados

3. **Implementar circuitos independientes** que no se afectan mutuamente, crucial para aplicaciones distribuidas

4. **Explorar la manipulación de estados cuánticos** mediante la implementación de trampas que modifican selectivamente qubits

5. **Desarrollar código cuántico profesional** utilizando PyQuil y siguiendo buenas prácticas de programación

La diferencia entre ambas partes ilustra cómo la computación cuántica puede ser tanto una herramienta para generar aleatoriedad verdadera como un sistema susceptible de manipulación si se puede acceder y modificar el estado cuántico antes de la medición.

---

## 6. Archivos Entregados

1. `Roulette.py` - Parte 1 (sin trampas)
2. `RouletteScam.py` - Parte 2 (con trampas)
3. `Ruleta.md` - Este documento

---

Mateo Delgado  
Computación Cuántica y Natural
