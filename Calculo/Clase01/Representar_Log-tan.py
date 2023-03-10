import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

# Creamos gráficos de funciones

x1 = np.linspace(0.1, 1, 200)
y1 = np.log(np.tan(x1))

plt.plot(x1,y1,'r', label= 'f')
plt.plot(x1,0*y1)
plt.legend()

plt.show()