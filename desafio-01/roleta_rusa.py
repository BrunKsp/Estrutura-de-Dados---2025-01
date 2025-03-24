import random


class ListaDE:
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None


def InserirElemento(lista, valor):
    novo = ListaDE(valor)
    
    if lista is None:
        novo.prox = novo
        novo.ant = novo
        return novo
    
    ultimo = lista.ant

    novo.prox = lista
    novo.ant = ultimo
    ultimo.prox = novo
    lista.ant = novo

    return lista 


def ExibirElementos(lista):
    if not lista:
        print("Lista vazia.")
        return

    atual = lista
    while True:
        print(atual.info, end=' ')
        atual = atual.prox
        if atual == lista:
            break
    print()


def BuscarElemento(lista, valor):
    if not lista:
        print("Lista vazia.")
        return

    atual = lista
    while True:
        if atual.info == valor:
            print("Elemento encontrado:", atual.info)
            return
        atual = atual.prox
        if atual == lista:
            break
    print("Elemento não encontrado!")


def RemoverElemento(lista, valor):
    if valor.prox == valor:
        return None, None  

    valor.ant.prox = valor.prox
    valor.prox.ant = valor.ant

    if valor == lista:
        return valor.prox, valor.prox
    else:
        return lista, valor.prox

def JogarRoletaRussa(lista):
    if not lista:
        print("Lista vazia.")
        return

    atual = lista
    rodada = 1

    while atual.prox != atual:
        passos = random.randint(1, 10)
        for i in range(passos):
            atual = atual.prox

        print(f"🔫 Jogador {atual.info} eliminado!")
        lista, atual = RemoverElemento(lista, atual)
        rodada += 1

    print(f"\n🏆 Sobrevivente: {atual.info}")

def main():
    primeiro_elemento = None

    print("🔫🎯 Roleta Russa !\n")
    while True:
        nome = input("Digite o nome de um jogador (ou 0 para iniciar o jogo): ")
        if nome == "0":
            break
        primeiro_elemento = InserirElemento(primeiro_elemento, nome)

    print("\n⚔️ Jogadores Corajosos:")
    ExibirElementos(primeiro_elemento)

    print("\n🎲 ATÉ O ULTIMO HOMEM...\n")
    JogarRoletaRussa(primeiro_elemento)


if __name__ == "__main__":
    main()
