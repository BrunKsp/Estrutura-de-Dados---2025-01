## HEAP MINIMO

class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        self.heap.append(valor)
        self.subir(len(self.heap) - 1)

    def remover(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.descer(0)
        return raiz

    def subir(self, index):
        pai = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[pai]:
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            self.subir(pai)

    def descer(self, index):
        filho_esq = 2 * index + 1
        filho_dir = 2 * index + 2
        menor = index

        if filho_esq < len(self.heap) and self.heap[filho_esq] < self.heap[menor]:
            menor = filho_esq
        if filho_dir < len(self.heap) and self.heap[filho_dir] < self.heap[menor]:
            menor = filho_dir
        if menor != index:
            self.heap[index], self.heap[menor] = self.heap[menor], self.heap[index]
            self.descer(menor)


print("\n=== Min Heap ===")
min_heap = MinHeap()
for n in [5, 3, 10, 1, 4]:
    min_heap.inserir(n)
print("Heap:", min_heap.heap)
print("Remover:", min_heap.remover())
print("Heap após remover:", min_heap.heap)