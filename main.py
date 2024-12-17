from modelos.enemies import Inimigo
import os
import random

# Itens

bau = [{'nome': 'Espada', 'dano': 50}, 
       {'nome': 'Arco', 'dano': 60}, 
       {'nome': 'Adaga Suprema', 'dano': 100}]
personagem = []
inimigos_derrotados = []

# Lista de Inimigos

inimigo_1 = Inimigo('Gorila de Pedra', 35, 'Espada')
inimigo_2 = Inimigo('Mago Sombrio', 70, 'Adaga Suprema')
inimigo_3 = Inimigo('Dragão de Fogo', 100, 'Adaga Suprema')
inimigo_4 = Inimigo('Assassino Sombrio', 60, 'Arco')
inimigo_5 = Inimigo('Lobisomem Selvagem', 50, 'Espada')

# Função para criar seu personagem

def main():
    os.system('cls')
    nome_mc = False
    if not nome_mc:
        nome_mc = str(input('DIGITE O NOME DO SEU PERSONAGEM: '))
        menu()
    else:
        menu()

# Menu

def menu():
    os.system('cls')
    print('𝖒𝖊𝖓𝖚 \n')
    print('1. Explore o mapa e abra báus. \n')
    print('2. Veja os monstros da caverna. \n')
    print('3. Escolha um monstro para derrotar. \n')
    print('4. Para ver os seus itens. \n')
    print('5. Para ver os inimigos já derrotados. \n')
    escolha = input('Escolha uma ação: ')
    try:
        escolha = int(escolha)
        if escolha == 1:
            abrir_baus()
        elif escolha == 2:
            mostrar_inimigos()
        elif escolha == 3:
            batalhar()
        elif escolha == 4:
            itens()
        elif escolha == 5:
            derrotados()
        else:
            menu()
    except:
        menu()

# Abrir Báus

def abrir_baus():
    os.system('cls')
    input('Digite algo para abrir o Báu: ')
    escolha_bau = random.choice(bau)
    print(f'Você ganhou um(a) {escolha_bau['nome']}, parabéns! ')
    personagem.append(escolha_bau['nome'])
    input('Digite algo para voltar ao menu ')
    menu()

# Mostrar Inimigos

def mostrar_inimigos():
    os.system('cls')
    Inimigo.listar_inimigos()
    input('Digite algo para voltar ao menu ')
    menu()

# Derrotar Inimigos

def batalhar():
    os.system('cls')  # Limpar a tela
    Inimigo.listar_inimigos()  # Listar inimigos disponíveis
    escolha = str(input('Digite o nome do inimigo que deseja enfrentar: '))  # Escolher inimigo

    # Verificar se o inimigo escolhido existe
    inimigo_escolhido = None
    for i in Inimigo.inimigos:
        if escolha == i.nome: 
            inimigo_escolhido = i
            break

    if inimigo_escolhido is None:
        print("Inimigo não encontrado. Tente novamente.")
        return  # Encerra a função se o inimigo não for encontrado

    os.system('cls')  # Limpar a tela novamente
    print(f'INIMIGO {inimigo_escolhido.nome} SELECIONADO \n')
    
    # Mostrar armas disponíveis
    for k in personagem:
        print(f'. {k}')
    
    arma = str(input('Digite a arma que deseja utilizar: '))  # Escolher arma

    # Verificar se a arma escolhida é válida
    if arma not in personagem:
        print("Arma inválida. Tente novamente.")
        return  # Encerra a função se a arma não for válida
    
    # Verificar se a arma é a fraqueza do inimigo
    if arma == inimigo_escolhido.fraqueza:
        print('VOCÊ GANHOU A BATALHA!')
        inimigos_derrotados.append(inimigo_escolhido.nome)
    else:
        print('VOCÊ PERDEU A BATALHA!')

    input('Pressione Enter para voltar ao menu...')  # Espera o jogador pressionar Enter
    menu()  # Chama a função menu (não definida no código original)

# Verificar Itens

def itens():
    os.system('cls')
    for i in personagem:
        print(f'. {i}')
    input('Digite algo para voltar ao menu ')
    menu()

# Mostrar Derrotados

def derrotados():
    os.system('cls')
    for i in inimigos_derrotados:
        print(f'. {i}')
    input('Digite algo para voltar ao menu ')
    menu()

if __name__ == '__main__':
    main()