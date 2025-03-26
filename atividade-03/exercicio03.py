# . Em uma arena circular, cavaleiros se enfrentam em uma batalha épica. Cada cavaleiro é representado por um nó na lista simplesmente encadeada circular.

# Regras do Jogo
# Cada cavaleiro começa com uma quantidade de HP (vida) gerada aleatoriamente entre 50 e 100.
# Cada cavaleiro ataca o próximo jogador da lista, causando uma quantidade de dano gerada aleatoriamente entre 5 e 10.
# Quando o HP de um cavaleiro chega a zero ou menos, ele é eliminado da lista.
# O jogo termina quando restar apenas um cavaleiro na arena, que será declarado o campeão.

import random


class Jogador:
    def __init__(self, info):
        self.info = info
        self.hp = random.randint(50,100)
        self.prox = None
        

def insert_node(lista, info):
    new_element = Jogador(info)

    if lista == None:
        new_element.prox = new_element
        return new_element

    atual = lista

    while atual.prox != lista:
        atual = atual.prox

    atual.prox = new_element
    new_element.prox = lista

    return new_element


def show_elements(lista):
    atual = lista
    count = 0 
    while True:
        print("Jogador:", atual.info, "Sua Vida:", atual.hp)
        atual = atual.prox
        count+=1
        if atual == lista:
            return count
        
        
def remove_element(lista, value):
    if lista is None:
        return None

    if lista.prox == lista and lista.info == value:
        print("💀 Último jogador removido, a arena está vazia!")
        return None

    atual = lista
    anterior = None

    while True:
        if atual.info == value:
            print(f"💀 {atual.info} foi eliminado!")
            if anterior:
                anterior.prox = atual.prox
            if atual == lista:
                lista = atual.prox
            return lista

        anterior = atual
        atual = atual.prox

        if atual == lista:
            print("Jogador não encontrado!")
            break

    return lista



def iniciar_batalha(lista):
   
    while lista and lista.prox != lista:
        atacante = lista
        defensor = atacante.prox

        dano = random.randint(5, 10)
        defensor.hp -= dano

        print(f"\n⚔️ {atacante.info} atacou {defensor.info} causando {dano} de dano!")

        if defensor.hp <= 0:
            lista = remove_element(lista, defensor.info)

        lista = lista.prox  

    print(f"\n🏆 {lista.info} é o Campeão da arena!\n")
        
        

def main():
    jogadores = None 

    while True:
        try:
            valor = input("Digite um jogador (0 para sair): ")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue

        if valor == "0":
            break 
        
        jogadores= insert_node(jogadores, valor)

    show_elements(jogadores)
    iniciar_batalha(jogadores)
    # remover = int(input("Insira um valor para remover da lista:"))

    # if (buscarValor(primeiro_elemento, remover) is None): 
    #         return print("Valor inexistente não pode ser removido!")

    # primeiro_elemento = retira_n(primeiro_elemento,remover)
    # lista_imprime_recursivo(primeiro_elemento )


if __name__ == "__main__":
    main()