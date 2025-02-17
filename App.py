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
    print("4. Sair\n")


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
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()


def listar_novo_restaurante():
    os.system('cls')
    print("Liste o restaurante\n")
    listar_restaurante = input("Listar restaurante: ")
    restaurantes.append(listar_restaurante)
    print(f"O restaurante {listar_restaurante} foi listado com sucesso!")
    input("Digite uma tecla para voltar ao menu principal: ")
    produto_cadastrado = input("Cadastre o produto do restaurante listado: ")
    if produto_cadastrado in produtos:
        print("Este produto já está cadastrado.)
    else:
        produtos.append(produto_cadastrado)
     print(f"O {produto_cadastrado} foi cadastrado com sucesso!\n")   


def escolher_opções():
    try:
        opção_escolhida = int(input("Escolha uma opção: "))
        # opção_escolhida = input("opção_escolhida")

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurante()
        elif opção_escolhida == 3:
            print("Ativar restaurante:")
        elif opção_escolhida == 4:
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
