import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("fecha_mancha.dat")
year=datos[:,0]
manchas=datos[:,1]

plt.plot(year,manchas)
plt.savefig("fecha_mancha.pdf")
