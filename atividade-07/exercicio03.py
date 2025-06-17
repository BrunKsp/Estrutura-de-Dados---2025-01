## HEAP FIBONACCI

import math

class NoFib:
    def __init__(self, chave):
        self.chave = chave
        self.pai = None
        self.filho = None
        self.esq = self
        self.dir = self
        self.grau = 0
        self.marcado = False

class HeapFibonacci:
    def __init__(self):
        self.min = None
        self.n = 0

    def inserir(self, chave):
        no = NoFib(chave)
        if self.min is None:
            self.min = no
        else:
            self.inserir_lista_raiz(no)
            if no.chave < self.min.chave:
                self.min = no
        self.n += 1

    def extrair_min(self):
        z = self.min
        if z is not None:
            if z.filho is not None:
                filhos = [x for x in self.iterar(z.filho)]
                for filho in filhos:
                    self.inserir_lista_raiz(filho)
                    filho.pai = None
            self.remover_lista_raiz(z)
            if z == z.dir:
                self.min = None
            else:
                self.min = z.dir
                self.consolidar()
            self.n -= 1
        return z.chave if z else None

    def inserir_lista_raiz(self, no):
        no.esq = self.min
        no.dir = self.min.dir
        self.min.dir.esq = no
        self.min.dir = no

    def remover_lista_raiz(self, no):
        no.esq.dir = no.dir
        no.dir.esq = no.esq

    def consolidar(self):
        A = [None] * (int(math.log(self.n) * 1.44) + 1)
        raiz = [x for x in self.iterar(self.min)]
        for w in raiz:
            x = w
            d = x.grau
            while A[d] is not None:
                y = A[d]
                if x.chave > y.chave:
                    x, y = y, x
                self.link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = None
        for i in A:
            if i is not None:
                if self.min is None or i.chave < self.min.chave:
                    self.min = i

    def link(self, y, x):
        self.remover_lista_raiz(y)
        y.pai = x
        if x.filho is None:
            x.filho = y
            y.dir = y
            y.esq = y
        else:
            y.esq = x.filho
            y.dir = x.filho.dir
            x.filho.dir.esq = y
            x.filho.dir = y
        x.grau += 1
        y.marcado = False

    def iterar(self, inicio):
        no = inicio
        while True:
            yield no
            no = no.dir
            if no == inicio:
                break

print("\n=== Heap de Fibonacci ===")
fib_heap = HeapFibonacci()
for n in [5, 3, 10, 1, 4]:
    fib_heap.inserir(n)
print("Menor elemento:", fib_heap.extrair_min())
print("Novo menor:", fib_heap.min.chave if fib_heap.min else None)