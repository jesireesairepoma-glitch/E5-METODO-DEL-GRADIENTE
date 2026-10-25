# Método del Gradiente - Ejercicio 5
import numpy as np

def F(X):
    x, y = X
    return 2*x**2 + 3*y**2 + 4*x - 5

def dF(X):
    x, y = X
    df = np.zeros(2)
    df[0] = 4*x + 4
    df[1] = 6*y
    return df

# Punto inicial y parámetros
X = np.array([0.0, 0.0])
alfa = 0.1
iteraciones = 100
lim_inf = np.array([-3.0, -3.0])
lim_sup = np.array([3.0, 3.0])

for i in range(iteraciones):
    grad = dF(X)
    X_nuevo = X - alfa * grad
    
    # Restricción circular: x^2 + y^2 <= 16
    if X_nuevo[0]**2 + X_nuevo[1]**2 > 16:
        X_nuevo = X_nuevo * (4.0 / np.sqrt(X_nuevo[0]**2 + X_nuevo[1]**2))
        
    X = np.clip(X_nuevo, lim_inf, lim_sup)

print("--- RESULTADOS MÉTODO DEL GRADIENTE ---")
print(f"Valor mínimo: {F(X):.6f}")
print(f"x = {X[0]:.6f}")
print(f"y = {X[1]:.6f}")