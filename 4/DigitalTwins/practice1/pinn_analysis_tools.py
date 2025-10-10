"""
Herramientas de Análisis para Práctica de PINNs
Funciones auxiliares para facilitar los ejercicios
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ============= EXTRACCIÓN DE PERFILES =============

def extract_velocity_profiles(model, x_min=0.0, x_max=1.0, y_min=0.0, y_max=1.0, n_points=100):
    """
    Extrae perfiles de velocidad en líneas de corte vertical y horizontal
    
    Returns:
        dict con 'vertical' y 'horizontal', cada uno con 'coords', 'u', 'v'
    """
    # Perfil vertical (línea central x = 0.5)
    y_vert = np.linspace(y_min, y_max, n_points)
    x_vert = 0.5 * np.ones_like(y_vert)
    XY_vert = tf.cast(np.stack([x_vert, y_vert], axis=1), tf.float32)
    u_vert, v_vert, _ = model(XY_vert)
    
    # Perfil horizontal (línea central y = 0.5)
    x_horiz = np.linspace(x_min, x_max, n_points)
    y_horiz = 0.5 * np.ones_like(x_horiz)
    XY_horiz = tf.cast(np.stack([x_horiz, y_horiz], axis=1), tf.float32)
    u_horiz, v_horiz, _ = model(XY_horiz)
    
    return {
        'vertical': {
            'y': y_vert,
            'u': u_vert.numpy().flatten(),
            'v': v_vert.numpy().flatten()
        },
        'horizontal': {
            'x': x_horiz,
            'u': u_horiz.numpy().flatten(),
            'v': v_horiz.numpy().flatten()
        }
    }

# ============= COMPARACIÓN DE CASOS =============

def compare_reynolds_numbers(results_dict):
    """
    Compara resultados para diferentes números de Reynolds
    
    Args:
        results_dict: diccionario con {Re: {'profiles': ..., 'model': ...}}
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfica 1: Perfil U vertical
    ax1 = axes[0]
    for Re, data in results_dict.items():
        profiles = data['profiles']
        ax1.plot(profiles['vertical']['u'], profiles['vertical']['y'], 
                label=f'Re = {Re}', linewidth=2)
    ax1.set_xlabel('Velocidad U', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title('Perfil de Velocidad U en x=0.5', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfica 2: Perfil V horizontal
    ax2 = axes[1]
    for Re, data in results_dict.items():
        profiles = data['profiles']
        ax2.plot(profiles['horizontal']['x'], profiles['horizontal']['v'],
                label=f'Re = {Re}', linewidth=2)
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('Velocidad V', fontsize=12)
    ax2.set_title('Perfil de Velocidad V en y=0.5', fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('reynolds_comparison.png', dpi=300)
    print("Comparación guardada en 'reynolds_comparison.png'")
    plt.show()

# ============= DATOS DE REFERENCIA (Ghia et al. 1982) =============

def get_ghia_benchmark_data():
    """
    Datos de referencia de Ghia et al. (1982) para Re = 100
    """
    # Perfil U en x = 0.5 (línea vertical central)
    y_ghia = np.array([0.0000, 0.0547, 0.0625, 0.0703, 0.1016, 0.1719, 
                       0.2813, 0.4531, 0.5000, 0.6172, 0.7344, 0.8516, 
                       0.9531, 0.9609, 0.9688, 0.9766, 1.0000])
    
    u_ghia = np.array([0.00000, -0.03717, -0.04192, -0.04775, -0.06434, 
                       -0.10150, -0.15662, -0.21090, -0.20581, -0.13641,
                       0.00332, 0.23151, 0.68717, 0.73722, 0.78871, 
                       0.84123, 1.00000])
    
    # Perfil V en y = 0.5 (línea horizontal central)
    x_ghia = np.array([0.0000, 0.0625, 0.0703, 0.0781, 0.0938, 0.1563,
                       0.2266, 0.2344, 0.5000, 0.8047, 0.8594, 0.9063,
                       0.9453, 0.9531, 0.9609, 0.9688, 1.0000])
    
    v_ghia = np.array([0.00000, 0.09233, 0.10091, 0.10890, 0.12317,
                       0.16077, 0.17507, 0.17527, 0.05454, -0.24533,
                       -0.22445, -0.16914, -0.10313, -0.08864, -0.07391,
                       -0.05906, 0.00000])
    
    return {
        'vertical': {'y': y_ghia, 'u': u_ghia},
        'horizontal': {'x': x_ghia, 'v': v_ghia}
    }

def compare_with_benchmark(model):
    """
    Compara resultados del modelo con datos de referencia
    """
    # Obtener perfiles del modelo
    profiles = extract_velocity_profiles(model)
    
    # Obtener datos de referencia
    ghia_data = get_ghia_benchmark_data()
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Comparar U vertical
    ax1 = axes[0]
    ax1.plot(profiles['vertical']['u'], profiles['vertical']['y'], 
            'b-', linewidth=2, label='PINN')
    ax1.plot(ghia_data['vertical']['u'], ghia_data['vertical']['y'], 
            'ro', markersize=8, label='Ghia et al. (1982)')
    ax1.set_xlabel('Velocidad U', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title('Perfil U en x=0.5 (Re=100)', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Comparar V horizontal
    ax2 = axes[1]
    ax2.plot(profiles['horizontal']['x'], profiles['horizontal']['v'],
            'b-', linewidth=2, label='PINN')
    ax2.plot(ghia_data['horizontal']['x'], ghia_data['horizontal']['v'],
            'ro', markersize=8, label='Ghia et al. (1982)')
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('Velocidad V', fontsize=12)
    ax2.set_title('Perfil V en y=0.5 (Re=100)', fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('benchmark_comparison.png', dpi=300)
    print("Comparación con benchmark guardada en 'benchmark_comparison.png'")
    plt.show()
    
    # Calcular errores
    from scipy.interpolate import interp1d
    
    # Interpolar para comparar en los mismos puntos
    u_interp = interp1d(profiles['vertical']['y'], profiles['vertical']['u'])
    u_pinn_at_ghia = u_interp(ghia_data['vertical']['y'])
    error_u = np.mean(np.abs(u_pinn_at_ghia - ghia_data['vertical']['u']))
    
    v_interp = interp1d(profiles['horizontal']['x'], profiles['horizontal']['v'])
    v_pinn_at_ghia = v_interp(ghia_data['horizontal']['x'])
    error_v = np.mean(np.abs(v_pinn_at_ghia - ghia_data['horizontal']['v']))
    
    print(f"\nError medio absoluto:")
    print(f"  Perfil U: {error_u:.6f}")
    print(f"  Perfil V: {error_v:.6f}")
    
    return error_u, error_v

# ============= ANÁLISIS DE CONVERGENCIA =============

def plot_detailed_convergence(loss_history, save_name='convergence_analysis.png'):
    """
    Crea gráficas detalladas de convergencia
    """
    fig = plt.figure(figsize=(15, 5))
    gs = GridSpec(1, 3, figure=fig)
    
    epochs = np.arange(len(loss_history))
    
    # Gráfica 1: Pérdida completa (escala log)
    ax1 = fig.add_subplot(gs[0])
    ax1.semilogy(epochs, loss_history, linewidth=2, color='blue')
    ax1.set_xlabel('Época', fontsize=12)
    ax1.set_ylabel('Pérdida (escala log)', fontsize=12)
    ax1.set_title('Convergencia Global', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Gráfica 2: Últimas 5000 épocas (escala lineal)
    ax2 = fig.add_subplot(gs[1])
    start_idx = max(0, len(loss_history) - 5000)
    ax2.plot(epochs[start_idx:], loss_history[start_idx:], 
            linewidth=2, color='green')
    ax2.set_xlabel('Época', fontsize=12)
    ax2.set_ylabel('Pérdida', fontsize=12)
    ax2.set_title('Últimas 5000 Épocas', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Gráfica 3: Tasa de cambio
    ax3 = fig.add_subplot(gs[2])
    if len(loss_history) > 100:
        window = 100
        rate_of_change = np.abs(np.diff(loss_history, prepend=loss_history[0]))
        smoothed = np.convolve(rate_of_change, np.ones(window)/window, mode='valid')
        ax3.semilogy(smoothed, linewidth=2, color='red')
        ax3.set_xlabel('Época', fontsize=12)
        ax3.set_ylabel('Tasa de Cambio (log)', fontsize=12)
        ax3.set_title('Velocidad de Convergencia', fontweight='bold')
        ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_name, dpi=300)
    print(f"Análisis de convergencia guardado en '{save_name}'")
    plt.show()

# ============= VISUALIZACIÓN MEJORADA =============

def plot_enhanced_results(model, X_grid, Y_grid, u_pred, v_pred, p_pred,
                         save_name='enhanced_results.png'):
    """
    Crea visualizaciones mejoradas con más detalles
    """
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
    
    # 1. Líneas de corriente con magnitud de velocidad
    ax1 = fig.add_subplot(gs[0, :2])
    velocity_mag = np.sqrt(u_pred**2 + v_pred**2)
    strm = ax1.streamplot(X_grid, Y_grid, u_pred, v_pred, 
                         density=2, linewidth=1, color=velocity_mag,
                         cmap='viridis', arrowsize=1.5)
    plt.colorbar(strm.lines, ax=ax1, label='|V|')
    ax1.set_title('Campo de Velocidad con Magnitud', fontweight='bold', fontsize=14)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_aspect('equal')
    
    # 2. Contornos de velocidad U
    ax2 = fig.add_subplot(gs[0, 2])
    cf1 = ax2.contourf(X_grid, Y_grid, u_pred, levels=20, cmap='RdBu_r')
    ax2.contour(X_grid, Y_grid, u_pred, levels=10, colors='black', 
               linewidths=0.5, alpha=0.3)
    plt.colorbar(cf1, ax=ax2, label='u')
    ax2.set_title('Componente U', fontweight='bold')
    ax2.set_aspect('equal')
    
    # 3. Contornos de velocidad V
    ax3 = fig.add_subplot(gs[1, 0])
    cf2 = ax3.contourf(X_grid, Y_grid, v_pred, levels=20, cmap='RdBu_r')
    ax3.contour(X_grid, Y_grid, v_pred, levels=10, colors='black',
               linewidths=0.5, alpha=0.3)
    plt.colorbar(cf2, ax=ax3, label='v')
    ax3.set_title('Componente V', fontweight='bold')
    ax3.set_aspect('equal')
    
    # 4. Campo de presión
    ax4 = fig.add_subplot(gs[1, 1])
    cf3 = ax4.contourf(X_grid, Y_grid, p_pred, levels=20, cmap='coolwarm')
    plt.colorbar(cf3, ax=ax4, label='p')
    ax4.set_title('Presión', fontweight='bold')
    ax4.set_aspect('equal')
    
    # 5. Magnitud de vorticidad
    ax5 = fig.add_subplot(gs[1, 2])
    # Calcular vorticidad: ω = ∂v/∂x - ∂u/∂y
    dy = (Y_grid[1,0] - Y_grid[0,0])
    dx = (X_grid[0,1] - X_grid[0,0])
    du_dy = np.gradient(u_pred, dy, axis=0)
    dv_dx = np.gradient(v_pred, dx, axis=1)
    vorticity = dv_dx - du_dy
    cf4 = ax5.contourf(X_grid, Y_grid, vorticity, levels=20, cmap='PuOr')
    plt.colorbar(cf4, ax=ax5, label='ω')
    ax5.set_title('Vorticidad', fontweight='bold')
    ax5.set_aspect('equal')
    
    # 6. Perfiles de velocidad
    ax6 = fig.add_subplot(gs[2, :])
    profiles = extract_velocity_profiles(model)
    ax6.plot(profiles['vertical']['u'], profiles['vertical']['y'],
            'b-', linewidth=2, label='U en x=0.5')
    ax6.plot(profiles['horizontal']['v'], profiles['horizontal']['x'],
            'r-', linewidth=2, label='V en y=0.5')
    ax6.set_xlabel('Velocidad', fontsize=12)
    ax6.set_ylabel('Posición', fontsize=12)
    ax6.set_title('Perfiles de Velocidad en Líneas Centrales', fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    plt.savefig(save_name, dpi=300, bbox_inches='tight')
    print(f"Resultados mejorados guardados en '{save_name}'")
    plt.show()

# ============= TABLA DE COMPARACIÓN =============

def create_comparison_table(experiments_data):
    """
    Crea una tabla de comparación de experimentos
    
    Args:
        experiments_data: lista de dicts con keys: 'name', 'loss', 'time', 'params'
    """
    print("\n" + "="*80)
    print("TABLA COMPARATIVA DE EXPERIMENTOS")
    print("="*80)
    print(f"{'Experimento':<25} {'Pérdida Final':>15} {'Tiempo (min)':>15} {'Parámetros':>20}")
    print("-"*80)
    
    for exp in experiments_data:
        name = exp['name']
        loss = exp.get('loss', 'N/A')
        time = exp.get('time', 'N/A')
        params = exp.get('params', 'N/A')
        
        loss_str = f"{loss:.6f}" if isinstance(loss, float) else str(loss)
        time_str = f"{time:.2f}" if isinstance(time, float) else str(time)
        
        print(f"{name:<25} {loss_str:>15} {time_str:>15} {str(params):>20}")
    
    print("="*80 + "\n")

# ============= EJEMPLO DE USO =============

if __name__ == "__main__":
    print("Herramientas de análisis cargadas correctamente!")
    print("\nFunciones disponibles:")
    print("  - extract_velocity_profiles(model)")
    print("  - compare_reynolds_numbers(results_dict)")
    print("  - compare_with_benchmark(model)")
    print("  - plot_detailed_convergence(loss_history)")
    print("  - plot_enhanced_results(model, X_grid, Y_grid, u, v, p)")
    print("  - create_comparison_table(experiments_data)")
    print("  - get_ghia_benchmark_data()")