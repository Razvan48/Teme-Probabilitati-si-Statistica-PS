import numpy as np
import matplotlib.pyplot as plt


def random_shuffle_manual(lista):
    for i in range(len(lista) - 1, -1, -1):
        poz = int(np.random.random() * (i - 1))
        aux = lista[poz]
        lista[poz] = lista[i]
        lista[i] = aux
    return lista


def factorial(N):
    sol = 1
    for i in range(1, N + 1):
        sol *= i
    return sol


def combinari(N, K):
    return factorial(N) / factorial(K) / factorial(N - K)


#Poisson (exercitiul 3)

nPoisson = 100_000 #ar trebui sa tinda la infinit

n = 20
lam = 1

#Poisson Practic

def poissonPractic(lam):
    valori = (np.random.random(nPoisson) < (lam / nPoisson))
    return np.sum(valori)


nrTeste = 10_000
listaCastiguri = np.array([poissonPractic(lam) for i in range(nrTeste)])
bins = np.linspace(-0.5, -0.5 + np.max(listaCastiguri) + 1, np.max(listaCastiguri) + 1)
plt.hist(listaCastiguri, bins, ec='black', density=True)
plt.xlabel('Numar de evenimente rare')
plt.ylabel('Probabilitate')
plt.title('Histograma Poisson Practic')
plt.show()

#Poisson Teoretic

def poissonTeoretic(lam, k):
    return (np.e ** (-lam)) * (lam**k) / factorial(k)


listaProbabilitati = np.array([poissonTeoretic(lam, k) for k in range(0, np.max(listaCastiguri) + 1)])
bins = np.linspace(-0.5, -0.5 + np.max(listaCastiguri) + 1, np.max(listaCastiguri) + 1)
plt.bar(range(np.max(listaCastiguri) + 1), listaProbabilitati, ec='black', width=1.0)
plt.xlabel('Numar de evenimente rare')
plt.ylabel('Probabilitate')
plt.title('Histograma Poisson Teoretic')
plt.show()

#Binomial (exercitiul 3, punctul b, comparatie)

n = 20
lam = 1

#Binomial Practic

def binomialPractic(n, lam):
    valori = (np.random.random(n) < (lam / n))
    return np.sum(valori)


listaCastiguri = np.array([binomialPractic(n, lam) for i in range(nrTeste)])
bins = np.linspace(-0.5, -0.5 + n + 1, n + 1)
plt.hist(listaCastiguri, bins, ec='black', density=True)
plt.xlabel('Numar de evenimente')
plt.ylabel('Probabilitate')
plt.title('Histograma Binomial Practic')
plt.show()

#Binomial Teoretic

def binomialTeoretic(n, lam, k):
    return combinari(n, k) * ((lam / n) ** k) * ((1 - lam / n) ** (n - k))


listaProbabilitati = np.array([binomialTeoretic(n, lam, k) for k in range(0, n + 1)])
bins = np.linspace(-0.5, -0.5 + n + 1, n + 1)
plt.bar(range(n + 1), listaProbabilitati, ec='black', width=1.0)
plt.xlabel('Numar de evenimente')
plt.ylabel('Probabilitate')
plt.title('Histograma Binomial Teoretic')
plt.show()

#Hypergeometrica (exercitiul 4)

N = 50
K = 25
n = 13

#Hypergeometrica Practica

def hyperGeomPractica(N, K, n):
    castigatoare = np.array([True] * K + [False] * (N - K))
    #np.random.shuffle(castigatoare)
    random_shuffle_manual(castigatoare)
    alese = np.array([True] * n + [False] * (N - n))
    np.random.shuffle(alese)
    return np.sum(castigatoare & alese)


nrTeste = 10_000
listaCastiguri = np.array([hyperGeomPractica(N, K, n) for i in range(nrTeste)])
bins = np.linspace(-0.5, -0.5 + min(n, K) + 1, min(n, K) + 2)
plt.hist(listaCastiguri, bins, ec='black', density=True)
plt.xlabel('Numar de numere castigatoare alese')
plt.ylabel('Probabilitate')
plt.title('Histograma Hypergeometrica Practica')
plt.show()

#Hypergeometrica Teoretica

def hyperGeomTeoretica(N, K, n, k):
    return combinari(K, k) * combinari(N - K, n - k) / combinari(N, n)


listaProbabilitati = np.array([hyperGeomTeoretica(N, K, n, k) for k in range(min(n, K) + 1)])
bins = np.linspace(-0.5, -0.5 + min(n, K) + 1, min(n, K) + 2)
plt.bar(range(min(n, K) + 1), listaProbabilitati, ec='black', width=1.0)
plt.xlabel('Numar de numere castigatoare alese')
plt.ylabel('Probabilitate')
plt.title('Histograma Hypergeometrica Teoretica')
plt.show()


