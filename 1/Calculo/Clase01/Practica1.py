import matplotlib as mp
import matplotlib.pyplot as plt
mp.__version__
import numpy as np

n=np.arrange(1.,15,1.)
plt.plot(n,2*n,'ro',n,(-1)**n,'bo',n,2+1/n,'go',n,0*n)
plt.show()