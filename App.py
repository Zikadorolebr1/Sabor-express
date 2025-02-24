import os

restaurantes = []
produtos = []


def exibir_nome_do_programa():
    print("""""
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
    print("2. Listar restaurante\n")
    print("3. Ativar restaurante\n")
    print("4. Desativar restaurante\n")
    print("5. Sair\n")


def Encerrando_programa():
    os.system('cls')
    print("Encerrando programa\n")


def opção_invalida():
    print("Opção inválida!\n")
    input("Digite uma tecla para voltar ao menu principal:")
    main()


def cadastrar_novo_restaurante():
    os.system('cls')
    print("Cadastre novos restaurantes\n")
    nome_do_restaurante = input("Nome do restaurante que deseja cadastrar-lo: ")
    if nome_do_restaurante in restaurantes:
        print("Este restaurante já foi cadastrado!\n")
    else:
        restaurantes.append(nome_do_restaurante)
        print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()


def listar_restaurante():
    os.system('cls')
    print("Liste o restaurante\n")
    listar_restaurante = input("Listar restaurante: ")
    if listar_restaurante in restaurantes:
        print("Este restaurante já está listado.")
    else:
        restaurantes.append(listar_restaurante)
        print(f"O restaurante {listar_restaurante} foi listado com sucesso!\n")

    produto_cadastrado = input("Cadastre o produto do restaurante listado: ")
    if produto_cadastrado in produtos:
        print("Este produto já está cadastrado.")
    else:
        produtos.append(produto_cadastrado)
        print(f"O produto {produto_cadastrado} foi cadastrado com sucesso!\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()


def ativar_restaurante():
    os.system('cls')
    print("Ativa Restaurante\n")
    ativar_restaurante = input("Insira o nome do seguinte restaurante para ser ativado: ")
    if ativar_restaurante in restaurantes:
        print("Este restaurante já está em atividade.")
    else:
        restaurantes.append(ativar_restaurante)
        print(f"Este {ativar_restaurante} foi ativado com sucesso! ")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()


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
            print*("Opção de restaurante inválida!\n")
    except ValueError:
        print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()


def escolher_opções():
    try:
        opção_escolhida = int(input("Escolha uma opção: "))
        # opção_escolhida = input("opção_escolhida")

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurante()
        elif opção_escolhida == 3:
            ativar_restaurante()
        elif opção_escolhida == 4:
            desativar_restaurante()
        elif opção_escolhida == 5:
            Encerrando_programa()
        else:
            Encerrando_programa()
    except ValueError:
        opção_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_programa()
    escolher_opções()


if __name__ == '__main__':
    main()
