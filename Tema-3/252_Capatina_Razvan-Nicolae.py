import numpy as np

nrTeste = 10_000
n = 32
nrBiti = 4

def filtrare(x):
    x = int(x)

    # ((1 << nrBiti) - 1) este o masca de biti de forma 111...11 de nrBiti ori. Aceasta masca o shiftam in toate pozitiile
    # posibile ale numarului si vedem daca numarul x are macar intr-un loc nrBiti consecutivi de 1.
    for i in range(0, n - nrBiti + 1):
        if (x & (((1 << nrBiti) - 1) << i)) == (((1 << nrBiti) - 1) << i):
            return True
    return False


valori = np.random.random(nrTeste) * (1 << n) # generez nrTeste numere in intervalul [0, 2^n] (numere cu n bits)
valori = np.vectorize(filtrare)(valori)

print("Probabilitate practica: ", np.sum(valori) / nrTeste)

# Formula: A(n) = 1/2 * A(n - 1) + 1/4 * A(n - 2) + 1/8 * A(n - 3) + 1/16 * A(n - 4) + 1/16

solutie = 0

if n == 4:
    solutie = 1/16
elif n > 4:
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 1/16
    indexCrt = 4
    while indexCrt + 1 <= n:
        auxiliar = 1/2 * a4 + 1/4 * a3 + 1/8 * a2 + 1/16 * a1 + 1/16
        a1 = a2
        a2 = a3
        a3 = a4
        a4 = auxiliar

        indexCrt += 1

    solutie = a4

print("Probabilitate teoretica: ", solutie)

