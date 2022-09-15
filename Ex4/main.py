import matplotlib.pyplot as plt
import numpy as np
import math as m
import timeit as t

def euler_otimizado(x, n_max = 9):
  numerador = np.multiply(x,x)
  denominador = 1.0
  euler = np.add(1.0, numerador/denominador)

  for n in range(1, n_max):
    numerador = np.power(x, (1 * n + 1))
    denominador = m.factorial(1 * n + 1)
    euler = np.add(euler, numerador/denominador)
    
  return euler


x = np.linspace(-2*np.pi, 2*np.pi, 1000) 
y = euler_otimizado(x)
y2 = np.exp(x)

fig,(ax, ax1) = plt.subplots(2)
fig.set_size_inches(5, 3)
ax.plot(x, y, linewidth=2.0, label="Otimizado", color="blueviolet")
ax.plot(x, y2, linewidth=2.0, label="Numpy", color="aquamarine")
ax.legend()
ax.grid() 
fig.show()

sesseta_graus = np.pi/3
start = t.default_timer()
euler_otimizadox = euler_otimizado(sesseta_graus)
t_euler_otimizado = t.default_timer() - start

print("Euler 60o - numpy", np.exp(sesseta_graus))
print("Euler 60o - otimizado", euler_otimizadox)
print('Euler otimizado: ', t_euler_otimizado*1000, "milissegundos")

n_max = 20
points = 360
enes = np.arange(1,n_max+1)
medias = np.zeros(n_max)
error = np.zeros(n_max)
xa = np.linspace(0, 2*np.pi, points) 


def tempo(xa,n):
  start = t.default_timer()
  valor = euler_otimizado(xa,n)
  loss_function = pow(valor - np.exp(xa),2) 
  return t.default_timer() - start, loss_function


tempo_vector = np.vectorize(tempo)

for n in enes:
  calc, erro = tempo_vector(xa,n)
  medias[n-1] = np.mean(calc)*1000*1000
  error[n-1] = np.sum(erro)/points

fig.set_size_inches(5,3)
ax1.plot(enes, medias, linewidth=2.0, color="lime")
ax1.grid()
color = "lime"
ax1.set_ylabel('tempo em ns', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax1 = ax1.twinx()
color = "red"
ax1.set_ylabel('Erro', color=color) 
ax1.plot(enes, error, color=color)
ax1.tick_params(axis='y', labelcolor=color)