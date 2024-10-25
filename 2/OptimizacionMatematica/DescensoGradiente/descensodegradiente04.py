# Función de costo
def cost_function(x, y):
    return 0.5 * (x**2 + 3*y**2)

# Parámetros iniciales
x = 3
y = 1
alpha = 0.01  # Tasa de aprendizaje
num_iteraciones = 1000

# Descenso del gradiente
for iter in range(num_iteraciones):
    # Calculamos las derivadas parciales
    grad_x = x
    grad_y = 3 * y
    
    # Actualizamos los valores de x e y
    x -= alpha * grad_x
    y -= alpha * grad_y
    
    # Calculamos la función de costo en cada iteración
    J = cost_function(x, y)
    
    # Mostramos la función de costo
    print(f"Iteración {iter+1}: J = {J:.4f}, x = {x:.4f}, y = {y:.4f}")

print("Resultado final:")
print(f"x = {x:.4f}, y = {y:.4f}")
