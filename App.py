import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},     # Dicionario {} e colocamos o valor
                {'nome': 'Praça', 'categoria': 'A la carte', 'ativo': True},
                {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}]
produtos = []


def exibir_nome_do_programa():
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
""")


def exibir_programa():
    print("1. Cadastrar restaurante\n")
    print("2. Cadastrar produto\n")
    print("3. Ativar restaurante\n")
    print("4. Desativar restaurante\n")
    print("5. Sair\n")


def voltar_menu_principal():
    input("\nDigite uma tecla para retornar ao menu principal: ")
    main()


def opção_invalida():
    print("Opção inválida! Tente novamente.\n")
    voltar_menu_principal()


def exibir_subtitulo(texto):
    # Função para exibir o texto (titulo)
    os.system('cls')
    print(texto)
    print()


for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = restaurante['ativo']
    print(f'-{nome_restaurante} | {categoria} | {ativo}')  # Dicionario usado para classificar nome, categoria e ativos


def cadastrar_novo_restaurante():
    # função para cadastrar um restaurante
    os.system('cls')
    exibir_subtitulo("Cadastre novos restaurantes\n")
    nome_do_restaurante = input("Nome do restaurante que deseja cadastrar-lo: ")
    categoria = input(f"Cateogira do restaurante que deseja cadastral-lo {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append = [dados_do_restaurante]
    '''Sempre vai ser falso porque quando o restaurante será criado
    ele ainda deve ser ativado'''

    if nome_do_restaurante in restaurantes:
        print("Este restaurante já foi cadastrado!\n")
        input("Digite uma tecla para voltar ao menu principal: ")
        main()

    else:
        restaurantes.append(nome_do_restaurante)
        print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("Cadastre o tipo de restaurante(ex: fast food, restaurante à la carte, self service): ")
    input("Descrição sobre o restaurante (como é o estilo de cozinha): ")
    input("Ponto de referência (Opcional): ")

    voltar_menu_principal()


def cadastrar_novo_produto():
    os.system('cls')
    print("Cadastre novos produtos")
    produto_cadastrado = input("Cadastre o produto do restaurante: ")

    print('Escolha uma categoria para seu produto:')
    print('1. Entradas: ')
    print('2. Bebidas: ')
    print('3. Pratos principais: ')
    categoria = input('Digite o número da categoria: ')

    categoria = {
        '1:' 'Entradas',
        '2:' 'Bebidas',
        '3:' 'Pratos principais'
    }

    categoria_nome = categoria.get(categoria)
    if categoria_nome:
        if categoria_nome not in produtos:
            produtos[categoria_nome] = []
        produtos[categoria_nome].append(produto_cadastrado)
        print(f"O {produto_cadastrado} foi cadastrado na categoria ccategoria nome com sucesso!")
    else:
        print("Opção inválida!\n")

    voltar_menu_principal() 


def alterar_estado_restaurante():
    exibir_subtitulo("Alterar estado atual do restaurante")
    nome_restaurante = input("Digite o nome do restaurante: ")      
### A onde eu parei foi aqui 
    voltar_menu_principal()


def desativar_restaurante():
    os.system('cls')
    print("Desativar restaurante\n")

    if not restaurantes:
        print("Nenhum restaurante para desativar\n")
        input("Digite uma tecla para voltar ao menu principal: ")
    else:
        print("Restaurantes cadastrados:")
    for i, restaurante in enumerate(restaurantes, 1):
        print(f"{i}, {restaurante}")
    try:
        restaurantes_ativo = int(input("\nEscolha um restaurante para desativar: "))
        if 1 <= restaurantes_ativo <= len(restaurantes):
            restaurante_nome = restaurantes.pop(restaurantes_ativo - 1)
            print(f"O restaurante {restaurante_nome} foi desativado no sistema.")
        else:
            print("Opção de restaurante inválida!\n")
    except ValueError:
        print("Opção inválida\n")
    voltar_menu_principal()


def escolher_opções():
    try:
        opção_escolhida = int(input("Escolha uma opção: "))
        # opção_escolhida = input("opção_escolhida")

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            cadastrar_novo_produto()
        elif opção_escolhida == 3:
            alterar_estado_restaurante()
        elif opção_escolhida == 5:
            Encerrando_programa()
        else:
            Encerrando_programa()
    except ValueError:
        opção_invalida()


def Encerrando_programa():
    exibir_subtitulo("Finalizando programa")


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_programa()
    escolher_opções()


if __name__ == '__main__':
    main()
