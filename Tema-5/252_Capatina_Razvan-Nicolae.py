import numpy as np
import matplotlib.pyplot as plt


def boxMullerSin(u1, u2):
    return np.sqrt(-2.0 * np.log(u1)) * np.sin(2.0 * np.pi * u2)


def boxMullerCos(u1, u2):
    return np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)


nrTeste = 1_000_000
nrBins = 30
nrIntervale = 1_000_000
raza = 7.5

u1 = np.random.random(nrTeste)
u2 = np.random.random(nrTeste)

z1 = boxMullerSin(u1, u2)
z2 = boxMullerCos(u1, u2)

plt.hist(z1, bins=nrBins, density=True, color='y', edgecolor='black')
intervale = np.linspace(-raza, raza, nrIntervale)
densitate = (1.0 / np.sqrt(2.0 * np.pi)) * np.exp(-0.5 * (intervale ** 2.0))
plt.plot(intervale, densitate, 'm--')

plt.title('Box-Muller Sin')
plt.show()

plt.hist(z2, bins=nrBins, density=True, color='y', edgecolor='black')
intervale = np.linspace(-raza, raza, nrIntervale)
densitate = (1.0 / np.sqrt(2.0 * np.pi)) * np.exp(-0.5 * (intervale ** 2.0))
plt.plot(intervale, densitate, 'm--')

plt.title('Box-Muller Cos')
plt.show()

