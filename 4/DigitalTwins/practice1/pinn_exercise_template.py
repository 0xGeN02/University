"""
PLANTILLA PARA EJERCICIOS - PINN CAVIDAD CON TAPA
Ejemplo: Ejercicio 1 - Efecto del Número de Reynolds

Nombre del estudiante: ___________________
Fecha: ___________________
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time

# Importar herramientas de análisis
from pinn_analysis_tools import (
    extract_velocity_profiles,
    compare_with_benchmark,
    plot_detailed_convergence,
    plot_enhanced_results,
    create_comparison_table
)

# =============== EJERCICIO 1: EFECTO DEL NÚMERO DE REYNOLDS ===============

# Lista de casos a simular
reynolds_cases = {
    10: {'nu': 0.1, 'color': 'blue'},
    100: {'nu': 0.01, 'color': 'green'},
    1000: {'nu': 0.001, 'color': 'red'}
}

# Parámetros del dominio
x_min, x_max = 0.0, 1.0
y_min, y_max = 0.0, 1.0
U_lid = 1.0

# Parámetros de entrenamiento (puedes ajustarlos)
N_f = 10000
N_b = 2000
epochs = 10000  # Reducido para pruebas rápidas
learning_rate = 1e-3

# =============== CLASE DEL MODELO PINN ===============

class PINN(tf.keras.Model):
    def __init__(self, num_hidden_layers=8, num_neurons=20):
        super(PINN, self).__init__()
        self.hidden_layers = []
        
        for _ in range(num_hidden_layers):
            layer = tf.keras.layers.Dense(
                num_neurons,
                activation='tanh',
                kernel_initializer='glorot_normal'
            )
            self.hidden_layers.append(layer)
        
        self.u_output = tf.keras.layers.Dense(1, activation=None)
        self.v_output = tf.keras.layers.Dense(1, activation=None)
        self.p_output = tf.keras.layers.Dense(1, activation=None)
    
    def call(self, inputs):
        x, y = inputs[:, 0:1], inputs[:, 1:2]
        X = tf.concat([x, y], axis=1)
        
        for layer in self.hidden_layers:
            X = layer(X)
        
        u = self.u_output(X)
        v = self.v_output(X)
        p = self.p_output(X)
        
        return u, v, p

# =============== FUNCIÓN DE PÉRDIDA ===============

def loss_fn(model, X_f, X_b, u_b, v_b, nu):
    X_f = tf.Variable(X_f, trainable=False, dtype=tf.float32)
    
    with tf.GradientTape(persistent=True) as tape:
        tape.watch(X_f)
        u, v, p = model(X_f)
        u = tf.squeeze(u)
        v = tf.squeeze(v)
        p = tf.squeeze(p)
    
    u_x = tape.gradient(u, X_f)[:, 0]
    u_y = tape.gradient(u, X_f)[:, 1]
    v_x = tape.gradient(v, X_f)[:, 0]
    v_y = tape.gradient(v, X_f)[:, 1]
    p_x = tape.gradient(p, X_f)[:, 0]
    p_y = tape.gradient(p, X_f)[:, 1]
    
    continuity = u_x + v_y
    
    with tf.GradientTape(persistent=True) as tape2:
        tape2.watch(X_f)
        with tf.GradientTape(persistent=True) as tape3:
            tape3.watch(X_f)
            u_temp, v_temp, _ = model(X_f)
            u_temp = tf.squeeze(u_temp)
            v_temp = tf.squeeze(v_temp)
        
        u_x_temp = tape3.gradient(u_temp, X_f)[:, 0]
        u_y_temp = tape3.gradient(u_temp, X_f)[:, 1]
        v_x_temp = tape3.gradient(v_temp, X_f)[:, 0]
        v_y_temp = tape3.gradient(v_temp, X_f)[:, 1]
    
    u_xx = tape2.gradient(u_x_temp, X_f)[:, 0]
    u_yy = tape2.gradient(u_y_temp, X_f)[:, 1]
    v_xx = tape2.gradient(v_x_temp, X_f)[:, 0]
    v_yy = tape2.gradient(v_y_temp, X_f)[:, 1]
    
    momentum_u = u * u_x + v * u_y + p_x - nu * (u_xx + u_yy)
    momentum_v = u * v_x + v * v_y + p_y - nu * (v_xx + v_yy)
    
    f_pde = tf.reduce_mean(tf.square(continuity)) + \
            tf.reduce_mean(tf.square(momentum_u)) + \
            tf.reduce_mean(tf.square(momentum_v))
    
    u_pred_b, v_pred_b, _ = model(X_b)
    bc_loss = tf.reduce_mean(tf.square(u_pred_b - u_b)) + \
              tf.reduce_mean(tf.square(v_pred_b - v_b))
    
    total_loss = f_pde + bc_loss
    
    del tape, tape2, tape3
    return total_loss

# =============== GENERAR PUNTOS DE COLOCACIÓN Y FRONTERA ===============

def generate_training_points():
    """Genera puntos de colocación y frontera"""
    # Puntos de colocación
    x_f = tf.random.uniform((N_f, 1), x_min, x_max, dtype=tf.float32)
    y_f = tf.random.uniform((N_f, 1), y_min, y_max, dtype=tf.float32)
    X_f = tf.concat([x_f, y_f], axis=1)
    
    # Puntos de frontera
    x_left = x_min * tf.ones((N_b // 4, 1), dtype=tf.float32)
    y_left = tf.random.uniform((N_b // 4, 1), y_min, y_max, dtype=tf.float32)
    
    x_right = x_max * tf.ones((N_b // 4, 1), dtype=tf.float32)
    y_right = tf.random.uniform((N_b // 4, 1), y_min, y_max, dtype=tf.float32)
    
    x_bottom = tf.random.uniform((N_b // 4, 1), x_min, x_max, dtype=tf.float32)
    y_bottom = y_min * tf.ones((N_b // 4, 1), dtype=tf.float32)
    
    x_top = tf.random.uniform((N_b // 4, 1), x_min, x_max, dtype=tf.float32)
    y_top = y_max * tf.ones((N_b // 4, 1), dtype=tf.float32)
    
    X_b = tf.concat([
        tf.concat([x_left, y_left], axis=1),
        tf.concat([x_right, y_right], axis=1),
        tf.concat([x_bottom, y_bottom], axis=1),
        tf.concat([x_top, y_top], axis=1)
    ], axis=0)
    
    # Condiciones de frontera
    u_top = U_lid * tf.ones((N_b // 4, 1), dtype=tf.float32)
    v_top = tf.zeros((N_b // 4, 1), dtype=tf.float32)
    u_side = tf.zeros((3 * N_b // 4, 1), dtype=tf.float32)
    v_side = tf.zeros((3 * N_b // 4, 1), dtype=tf.float32)
    
    u_b = tf.concat([u_side, u_top], axis=0)
    v_b = tf.concat([v_side, v_top], axis=0)
    
    return X_f, X_b, u_b, v_b

# =============== FUNCIÓN DE ENTRENAMIENTO ===============

def train_model(nu, Re, X_f, X_b, u_b, v_b):
    """Entrena el modelo para un número de Reynolds dado"""
    print(f"\n{'='*60}")
    print(f"ENTRENANDO PARA Re = {Re} (nu = {nu})")
    print(f"{'='*60}")
    
    model = PINN()
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    
    def train_step():
        with tf.GradientTape() as tape:
            loss_value = loss_fn(model, X_f, X_b, u_b, v_b, nu)
        grads = tape.gradient(loss_value, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
        return loss_value
    
    loss_history = []
    start_time = time.time()
    
    for epoch in range(epochs):
        loss_value = train_step()
        loss_history.append(loss_value.numpy())
        
        if epoch % 500 == 0:
            print(f"Época {epoch:5d}, Pérdida: {loss_value.numpy():.6f}")
    
    training_time = (time.time() - start_time) / 60
    print(f"\nTiempo de entrenamiento: {training_time:.2f} minutos")
    print(f"Pérdida final: {loss_history[-1]:.6f}")
    
    return model, loss_history, training_time

# =============== SCRIPT PRINCIPAL ===============

if __name__ == "__main__":
    print("="*60)
    print("EJERCICIO 1: EFECTO DEL NÚMERO DE REYNOLDS")
    print("="*60)
    
    # Generar puntos de entrenamiento (comunes para todos los casos)
    print("\nGenerando puntos de colocación y frontera...")
    X_f, X_b, u_b, v_b = generate_training_points()
    
    # Almacenar resultados
    results = {}
    experiments_data = []
    
    # Entrenar para cada número de Reynolds
    for Re, params in reynolds_cases.items():
        nu = params['nu']
        
        # Entrenar modelo
        model, loss_history, training_time = train_model(nu, Re, X_f, X_b, u_b, v_b)
        
        # Extraer perfiles
        profiles = extract_velocity_profiles(model)
        
        # Guardar resultados
        results[Re] = {
            'model': model,
            'loss_history': loss_history,
            'profiles': profiles,
            'nu': nu
        }
        
        experiments_data.append({
            'name': f'Re = {Re}',
            'loss': loss_history[-1],
            'time': training_time,
            'params': f'nu = {nu}'
        })
        
        # Guardar modelo
        model.save_weights(f'model_Re{Re}.weights.h5')
        print(f"✓ Modelo guardado: model_Re{Re}.weights.h5")
    
    # =============== ANÁLISIS Y VISUALIZACIÓN ===============
    
    print("\n" + "="*60)
    print("GENERANDO ANÁLISIS COMPARATIVOS")
    print("="*60)
    
    # 1. Tabla comparativa
    create_comparison_table(experiments_data)
    
    # 2. Comparar perfiles de velocidad
    from pinn_analysis_tools import compare_reynolds_numbers
    compare_reynolds_numbers(results)
    
    # 3. Gráficas de convergencia
    plt.figure(figsize=(12, 4))
    for Re, data in results.items():
        plt.plot(data['loss_history'], 
                label=f'Re = {Re}',
                color=reynolds_cases[Re]['color'],
                linewidth=2)
    plt.xlabel('Época', fontsize=12)
    plt.ylabel('Pérdida', fontsize=12)
    plt.title('Convergencia para Diferentes Números de Reynolds', fontweight='bold')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('exercise1_convergence.png', dpi=300)
    print("✓ Convergencia guardada: exercise1_convergence.png")
    plt.show()
    
    # 4. Visualizaciones detalladas para cada caso
    for Re, data in results.items():
        print(f"\nGenerando visualización para Re = {Re}...")
        
        # Crear malla
        nx, ny = 50, 50
        x_plot = tf.linspace(x_min, x_max, nx)
        y_plot = tf.linspace(y_min, y_max, ny)
        X_grid, Y_grid = tf.meshgrid(x_plot, y_plot)
        X_flat = tf.reshape(X_grid, [-1])
        Y_flat = tf.reshape(Y_grid, [-1])
        XY = tf.stack([X_flat, Y_flat], axis=1)
        
        # Predecir
        u_pred, v_pred, p_pred = data['model'](XY)
        u_pred = tf.reshape(u_pred, (ny, nx)).numpy()
        v_pred = tf.reshape(v_pred, (ny, nx)).numpy()
        p_pred = tf.reshape(p_pred, (ny, nx)).numpy()
        
        # Visualización mejorada
        plot_enhanced_results(
            data['model'], 
            X_grid.numpy(), 
            Y_grid.numpy(), 
            u_pred, v_pred, p_pred,
            save_name=f'exercise1_Re{Re}_detailed.png'
        )
    
    print("\n" + "="*60)
    print("¡EJERCICIO COMPLETADO!")
    print("="*60)
    
    # =============== PREGUNTAS PARA EL INFORME ===============
    
    print("\n📝 PREGUNTAS PARA RESPONDER EN EL INFORME:")
    print("-" * 60)
    print("1. ¿Cómo cambia la posición del centro del vórtice con Re?")
    print("2. ¿Se observan vórtices secundarios en algún caso?")
    print("3. ¿Qué caso converge más rápido? ¿Por qué?")
    print("4. Compare los perfiles de velocidad: ¿qué tendencias observa?")
    print("5. ¿Es consistente el campo de presión con el flujo observado?")
    print("-" * 60)
    
    # Guardar datos para análisis posterior
    np.savez('exercise1_results.npz',
             Re_values=list(results.keys()),
             final_losses=[data['loss_history'][-1] for data in results.values()],
             training_times=[exp['time'] for exp in experiments_data])
    
    print("\n✓ Datos guardados en: exercise1_results.npz")
    print("\nArchivos generados:")
    print("  - exercise1_convergence.png")
    print("  - exercise1_Re*_detailed.png (para cada Re)")
    print("  - reynolds_comparison.png")
    print("  - model_Re*.weights.h5 (modelos entrenados)")
    print("  - exercise1_results.npz (datos numéricos)")