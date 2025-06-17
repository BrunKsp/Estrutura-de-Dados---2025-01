## HEAP MAXIMO

class MaxHeap:
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
        if index > 0 and self.heap[index] > self.heap[pai]:
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            self.subir(pai)

    def descer(self, index):
        filho_esq = 2 * index + 1
        filho_dir = 2 * index + 2
        maior = index

        if filho_esq < len(self.heap) and self.heap[filho_esq] > self.heap[maior]:
            maior = filho_esq
        if filho_dir < len(self.heap) and self.heap[filho_dir] > self.heap[maior]:
            maior = filho_dir
        if maior != index:
            self.heap[index], self.heap[maior] = self.heap[maior], self.heap[index]
            self.descer(maior)


print("=== Max Heap ===")
max_heap = MaxHeap()
for n in [5, 3, 10, 1, 4]:
    max_heap.inserir(n)
print("Heap:", max_heap.heap)
print("Remover:", max_heap.remover())
print("Heap após remover:", max_heap.heap)