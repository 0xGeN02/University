# Arquitectura ISA-95 / Pirámide Purdue

## Línea Textil Inteligente - (Textiles del Noroeste S.A.)

---

## 🟪 NIVEL 4 - ERP TEXTIL

### Gestión Empresarial y Planificación

**Funciones principales:**

- Planificación semanal de pedidos
- Gestión de inventario y materias primas
- Trazabilidad completa del producto (desde prenda final hasta lote de tejido y operario)
- Integración con datos del MES

**Comunicación:**

- SQL / APIs REST hacia MES

**Flujo de información:**

- ⬇️ Envía: Órdenes de producción, planificación
- ⬆️ Recibe: Resultados de ejecución, KPIs consolidados

---

## ↕️ COMUNICACIÓN BIDIRECCIONAL

**Descendente:** Órdenes y planificación  
**Ascendente:** Resultados y datos de ejecución

---

## 🔵 NIVEL 3 - MES TEXTIL + GRAFANA

### Sistema de Ejecución de Manufactura y Visualización

**KPIs en Tiempo Real:**

- **OEE** (Overall Equipment Effectiveness)
- **Throughput** (piezas/hora)
- **Defect Ratio** (%)
- **Disponibilidad de Línea**
- **MTBF** (Mean Time Between Failures)

**Bases de Datos:**

- **InfluxDB:** Almacenamiento de series temporales
  - Temperaturas
  - Velocidades
  - Tiempos de ciclo
  - Piezas procesadas
- **PostgreSQL:** Almacenamiento estructurado
  - Órdenes de producción
  - Lotes
  - Defectos
  - Operadores
  - Trazabilidad

**Visualización (Grafana):**

- Dashboards con códigos de color
- Gráficos de tendencia por estación
- Análisis de eficiencia y cuellos de botella
- Identificación de operarios y paradas

**Elementos opcionales:**

- Gemelo Digital 3D/VR (Unity, Three.js, Babylon.js)
- Visualización en tiempo real del estado de la planta

**Comunicación:**

- ⬇️ Hacia Node-RED: Comandos y configuraciones
- ⬆️ Desde Node-RED: Datos de proceso en formato JSON

---

## ↕️ COMUNICACIÓN BIDIRECCIONAL II

**Descendente:** Comandos y configuraciones  
**Ascendente:** Datos de proceso y eventos

---

## 🟢 NIVEL 2 - GATEWAY IoT NODE-RED (SCADA LIGERO)

### Supervisión, Control y Adquisición de Datos

**Funciones principales:**

- **Concentrador de datos IoT** (Nivel 2 ISA-95)
- Recepción de datos desde múltiples protocolos
- Validación y transformación a formato común JSON
- Mini-SCADA para monitorización de estados
- Pasarela entre capa OT (Operational Technology) y capa IT (Information Technology)

**Protocolos de entrada:**

- **MQTT** (desde E3 - Inspección)
- **Modbus TCP** (desde E1 - Corte y E4 - Empaquetado)
- **OPC UA** (desde E2 - Costura)

**Monitorización visual de estados:**

- 🟢 **Verde:** Máquina operativa
- 🟡 **Amarillo:** En mantenimiento
- 🔴 **Rojo:** Avería o parada

**Generación de alertas:**

- Alerta cuando una estación se detiene más de 1 minuto
- Alerta cuando la tasa de defectos supera un umbral
- Propagación de alarmas hacia bases de datos

**Comunicación:**

- ⬇️ Hacia Estaciones: Comandos de control
- ⬆️ Desde Estaciones: Datos de sensores y estados
- ➡️ Hacia Bases de Datos: Datos procesados (InfluxDB y PostgreSQL)

---

## ↕️ COMUNICACIÓN BIDIRECCIONAL III

**Descendente:** Control y comandos  
**Ascendente:** Datos de sensores y actuadores

---

## 🟠 NIVEL 0-1 - CAMPO

### Sensores, Actuadores y Controladores Locales (PLCs)

### 📍 E1: ESTACIÓN DE CORTE AUTOMÁTICO

**Controlador:**

- PLC Siemens

**Sensores:**

- Sensor de vibración (cabezal de corte)
- Sensor de temperatura (cabezal de corte)
- Sensor óptico (validación posicionamiento de tela)

**Función:**

- Corte de tejidos según patrones enviados por MES
- Control de motores

**Protocolo:** Modbus TCP → Node-RED

---

### 📍 E2: ESTACIÓN DE COSTURA INTELIGENTE

**Equipamiento:**

- Múltiples máquinas de coser robotizadas

**Sensores:**

- Sensores de presión
- Sensores ópticos de hilo

**Datos reportados en tiempo real:**

- Piezas cosidas
- Tiempo de ciclo
- Rotura de hilo

**Protocolo:** OPC UA → Node-RED

- Expone variables estructuradas del proceso

---

### 📍 E3: ESTACIÓN DE INSPECCIÓN DE CALIDAD

**Equipamiento:**

- Cámaras de visión artificial
- Algoritmos de IA

**Función:**

- Detección de defectos en costuras
- Detección de manchas en el tejido

**Datos enviados:**

- Resultados de inspección
- Defectos identificados
- Marcado de lotes defectuosos

**Protocolo:** MQTT → Node-RED

- **Topic:** textile/inspection/defects
- **Broker:** Mosquitto

---

### 📍 E4: ESTACIÓN DE EMPAQUETADO

**Función:**

- Pesar prendas
- Etiquetar
- Sellar paquetes

**Sensores:**

- Sensores de peso
- Lectores de código QR

**Datos registrados automáticamente:**

- Peso del paquete
- Lote
- Operario
- Hora/timestamp

**Protocolo:** Modbus TCP → Node-RED

---

## 🔌 RESUMEN DE PROTOCOLOS DE COMUNICACIÓN

| Protocolo | Origen | Destino | Uso |
|-----------|--------|---------|-----|
| **MQTT** | E3 (Inspección) | Node-RED | Datos de defectos vía Broker Mosquitto |
| **Modbus TCP** | E1 (Corte) y E4 (Empaquetado) | Node-RED | Comunicación con PLCs industriales |
| **OPC UA** | E2 (Costura) | Node-RED | Variables estructuradas de proceso |
| **JSON/HTTP** | Node-RED | InfluxDB + PostgreSQL | Almacenamiento de datos |
| **SQL/REST** | MES | ERP | Integración nivel empresarial |

---

## 🔄 FLUJO BIDIRECCIONAL DE INFORMACIÓN

### ⬇️ DE ARRIBA A ABAJO (Planificación y Control)

```shell
ERP → MES → Node-RED → Estaciones (E1, E2, E3, E4)
```

**Contenido:**

- Órdenes de producción
- Patrones de corte
- Planificación de lotes
- Configuraciones de proceso

### ⬆️ DE ABAJO A ARRIBA (Ejecución y Resultados)

```shell
Sensores → Node-RED → MES/Bases de Datos → ERP
```

**Contenido:**

- Datos de sensores en tiempo real
- Estados de máquinas
- KPIs de producción
- Defectos y alarmas
- Trazabilidad completa

---

## 📊 BASES DE DATOS Y ALMACENAMIENTO

### InfluxDB (Series Temporales)

- Temperaturas de cabezales
- Velocidades de máquinas
- Tiempos de ciclo
- Piezas procesadas por hora
- Datos continuos para análisis de tendencias

### PostgreSQL (Datos Estructurados)

- Órdenes de producción
- Registros de lotes
- Defectos por estación
- Operadores asignados
- Trazabilidad de productos

---

## 🎯 TRAZABILIDAD COMPLETA

El sistema permite rastrear cada prenda desde:

- **Origen:** Lote de tejido específico
- **Proceso:** Qué estaciones la procesaron
- **Operarios:** Quién la manipuló en cada fase
- **Calidad:** Inspecciones y defectos detectados
- **Destino:** Paquete final con código QR

Esta trazabilidad se registra en PostgreSQL y está disponible en tiempo real desde el ERP.

---

## 🎮 GEMELO DIGITAL (Opcional)

**Tecnologías sugeridas:**

- Unity
- Three.js
- Babylon.js

**Visualización 3D de la planta:**

- Estaciones que cambian de color según estado
- Flujos animados de prendas en la línea
- Simulación de averías y su impacto
- Reorganización virtual del flujo de producción

---

## 📈 KPIs INDUSTRIALES CALCULADOS

### OEE (Overall Equipment Effectiveness)

```math
OEE = Disponibilidad × Rendimiento × Calidad
```

### Throughput

- Piezas producidas por hora
- Por estación y global

### Defect Ratio

```math
DefectRatio = (PiezasDefectuosas / TotalProducido) × 100
```

### Disponibilidad de Línea

```math
Disponibilidad = (TiempoOperativo / TiempoPlanificado) × 100
```

### MTBF (Mean Time Between Failures)

- Tiempo medio entre fallos por estación

---

## 🎓 OBJETIVOS DE APRENDIZAJE CUBIERTOS

✅ Trazabilidad completa desde el nivel de campo hasta ERP  
✅ Cálculo e interpretación de KPIs industriales (OEE, throughput, defect ratio)  
✅ Configuración de flujo IoT con protocolos mixtos (MQTT + Modbus + OPC UA)  
✅ Análisis de escenarios de fallo y su impacto en indicadores  
✅ Uso de gemelo digital para supervisión en tiempo real  
✅ Comprensión del modelo ISA-95 y pirámide Purdue aplicado a caso real

---

## 🏭 TECNOLOGÍAS IMPLICADAS

- **Node-RED:** Gateway IoT y SCADA ligero
- **Mosquitto:** MQTT broker para intercambio de datos
- **InfluxDB:** Almacenamiento de series temporales
- **PostgreSQL:** Almacenamiento estructurado
- **Grafana:** Dashboards de KPIs industriales
- **Python:** Simuladores de estaciones e incidencias
- **Unity/Three.js:** (Opcional) Planta virtual 3D

---

**Actividad Post-Clase - Sesión 06**  
**Asignatura:** Empresa Inteligente y Gemelos Digitales  
**Caso de Uso:** Línea Textil Inteligente con Trazabilidad y KPIs de Producción  
**Empresa:** Textiles del Noroeste S.A. - Ourense, Galicia
