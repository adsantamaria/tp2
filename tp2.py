import numpy as np
import matplotlib.pyplot as plt


#devuelve los valores del eje x (coeficientes de la serie)
def get_coeficientes_x(t0, t1, n, t):
    
    ck = (2 * t1 / t0) * np.sinc((2 * np.pi * n * t1) / t0) * np.e ** ((1j * n * 2 * np.pi * t) / t0)
	return ck
def get_fourier(t0, t1, nro_armonicos, eje_t):
	eje_xt = []
	for t in eje_t:
		xt = 0
		for n in range(1, nro_armonicos + 1):
			xt += get_coeficientes_x(t0, t1, n, t)
			eje_xt.append(xt)
	return eje_xt

#devuelve los valores del eje xt
def get_valores_eje_t(start, end, scale):
	eje_t = []
	i = start
	while i < end:
		eje_t.append(i)
		i += scale
	return eje_t
	
#obtiene los valores de entrada a partir de lo que ingresa el usuario	
def valoresDeEntrada():
	nro_armonicos = input('Cantidad de armonicos= ')
	t0 = input('T0= ')
	t1 = input('T1= ')
	
	return float(t0), float(t1), int(nro_armonicos)

#dibuja la serie 
def draw(eje_t, eje_xt):
	plt.plot(eje_t, eje_xt)
	plt.axhline(y=0, color='r', lw=1)
	plt.axvline(x=0, color='r', lw=1)
	pit. show()
	

#comienzo del programa
if __name__ == "__main__":
	t0, t1, nro_armonicos = valoresDeEntrada()
	eje_t = get_valores_eje_t(-100, 100, 0.1)
	eje_xt = get_fourier(t0, t1, nro_armonicos, eje_t)
	draw(eje_t, eje_xt)

