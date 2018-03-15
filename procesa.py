import numpy as np
datos = np.loadtxt("monthrg.dat")

dat = datos[np.where(datos[:,3]!=-99.0)]

an= dat[:,0]+ (dat[:,1]-1)/12.0
manchas= dat[:,3]

year= an[an >1900]

manchas1=manchas[an >1900]

info=np.array([year,manchas1])
info1=info.T

archivo = open("fecha_mancha.dat","w")
np.savetxt(archivo,info1)
