import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

# Creamos gráficos de funciones
x1 = np.linspace(-0.5, 2.5, 200)
y1 = np.cos(x1)

fig, axs = plt.subplots(2, 2, figsize=(15,10))

ax1 = axs[0,0]
ax1.plot(x1, y1, c='b', lw='5')
ax1.set_ylabel('Y', fontsize=10)
ax1.set_xlabel('X', fontsize=10)
ax1.axhline(y=0., c='black', lw='2')

ax1.axvline(x=0., ymin=-1, ymax=1, c='r')
ax1.text(-0.11, 0.05, 'a', c='r', fontsize=20)
ax1.axvline(x=2., ymin=-1, ymax=1, c='r')
ax1.text(2, 0.05, 'b', c='r', fontsize=20)
ax1.axvline(x=1., ymin=-1, ymax=1, c='g', ls='--')
ax1.text(1, 0.05, '$x_1$', c='g', fontsize=20)

ax2 = axs[0,1]
ax2.plot(x1, y1, c='b', lw='5')
ax2.set_ylabel('Y', fontsize=10)
ax2.set_xlabel('X', fontsize=10)
ax2.axhline(y=0., c='black', lw='2')

ax2.axvline(x=1., ymin=-1, ymax=1, c='r')
ax2.text(0.89, 0.05, 'a', c='r', fontsize=20)
ax2.axvline(x=2., ymin=-1, ymax=1, c='r')
ax2.text(2, 0.05, 'b', c='r', fontsize=20)
ax2.axvline(x=1.5, ymin=-1, ymax=1, c='g', ls='--')
ax2.text(1.5, 0.05, '$x_2$', c='g', fontsize=20)

ax3 = axs[1,0]
ax3.plot(x1, y1, c='b', lw='5')
ax3.set_ylabel('Y', fontsize=10)
ax3.set_xlabel('X', fontsize=10)
ax3.axhline(y=0., c='black', lw='2')

ax3.axvline(x=1.5, ymin=-1, ymax=1, c='r')
ax3.text(1.39, 0.05, 'a', c='r', fontsize=20)
ax3.axvline(x=2., ymin=-1, ymax=1, c='r')
ax3.text(2, 0.05, 'b', c='r', fontsize=20)
ax3.axvline(x=1.75, ymin=-1, ymax=1, c='g', ls='--')
ax3.text(1.75, 0.05, '$x_3$', c='g', fontsize=20)

ax4 = axs[1,1]
ax4.plot(x1, y1, c='b', lw='5')
ax4.set_ylabel('Y', fontsize=10)
ax4.set_xlabel('X', fontsize=10)
ax4.axhline(y=0., c='black', lw='2')

ax4.axvline(x=1.5, ymin=-1, ymax=1, c='r')
ax4.text(1.39, 0.05, 'a', c='r', fontsize=20)
ax4.axvline(x=1.75, ymin=-1, ymax=1, c='r')
ax4.text(1.75, 0.05, 'b', c='r', fontsize=20)
ax4.axvline(x=1.625, ymin=-1, ymax=1, c='g', ls='--')
ax4.text(1.625, 0.25, '$x_4$', c='g', fontsize=20)

plt.show()