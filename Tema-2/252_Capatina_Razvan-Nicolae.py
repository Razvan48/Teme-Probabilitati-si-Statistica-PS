import numpy as np
import matplotlib.pyplot as plt

################################### Exercitiul 1, c)

# Exemplificare a)

# Copilul mare stim ca este fata, ramane doar sa simulam faptul ca cel mic poate fi baiat sau fata.
nrTeste = 10_000_000
valori = np.random.random(nrTeste)
valori = valori > 0.5
print("Probabilitate ex. 1, a): ", np.sum(valori) / nrTeste)
print("Probabilitate teoretica ex. 1, a): ", 1/2)

# Exemplificare b)

# Stim ca exista macar o fata, avem 3 cazuri:

# Cazul 1: ambii copii fete
# Cazul 2: copilul mare baiat, copilul mic fata
# Cazul 3: copilul mic baiat, copilul mare fata

nrTeste = 10_000_000
valori = np.random.random(nrTeste)
valori = valori < 1/3
print("Probabilitate ex. 1, b): ", np.sum(valori) / nrTeste)
print("Probabilitate teoretica ex. 1, b): ", 1/3)

############################################ Exercitiul 2

def factorial(x):
    sol = 1
    for i in range(1, x + 1):
        sol *= i
    return sol

def combinari(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)

nrTeste = 10_000_000

n = 12
k = 5

# Idee:
# Voi genera nrTeste numere in intervalul inchis [0; 2^n - 1] si ma voi uita numai la cei mai nesemnificativi
# n bits din reprezentarea lor binara.
# Voi filtra array-ul obtinut folosind o functie ce va numara cati bits de 1 are fiecare element
# si va pastra numai elementele cu exact k bits de 1.
# Ma folosesc si de Two's Complement Architecture pentru a optimiza functia de filtrare.

def nrBits(x):
    x = int(x)
    sol = 0
    while x:
        x &= (x - 1) # Two's Complement Architecture
        sol += 1
    return sol == k

limitaInferioara = 0
limitaSuperioara = 2**n - 1

# import time
# timpStart = time.time()

valori = np.random.random(nrTeste) # valori in [0; 1]
valori = valori * limitaInferioara + (1 - valori) * limitaSuperioara # interpolez liniar
# valori = [nrBits(int(x)) for x in valori] # 6.14 secunde
valori = np.vectorize(nrBits)(valori) # 5.27 secunde

print("Probabilitate ex. 2: ", np.sum(valori) / nrTeste)
print("Probabilitate teoretica ex. 2: ", combinari(n, k) / (2 ** n))

# print("Durata timp ex. 2: ", time.time() - timpStart)

################################################ Exercitiul 3

plt.title("Exercitiul 3")
plt.xlabel("Axa OX")
plt.ylabel("Axa OY")

axe = plt.gca()
axe.cla()

n = 1_000_000
a = 0.0 # Parametrii a si b pot fi schimbati. Ne asteptam ca in fiecare caz limita sa convearga la b - a. (b >= a)
b = 0.05

sir = np.random.uniform(0, 1, size=n)
valoriInInterval = (a <= sir) & (sir <= b)

plt.plot([1, n], [b - a] * 2, color='r', linewidth=2) # Desenam cu rosu dreapta de ecuatie y = constant = b - a.

sumaPartValoriInInterval = np.cumsum(valoriInInterval)
xValori = np.linspace(1, n, num=n)
yValori = sumaPartValoriInInterval / xValori

plt.plot(xValori, yValori, color='b', linewidth=2)

plt.show()





