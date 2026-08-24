import os
import PySimpleGUI as sg


restaurantes = [{'nome': 'categoria' }]
produtos = []


def exibir_nome_do_programa():
    sg.popup(
        "Sistema do restaurante",
        "╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮\n"
        "┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯\n"
        "┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮\n"
        "╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫\n"
        "┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃\n"
        "╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯"
    )


# Função para cadastrar novo restaurante
def cadastrar_novo_restaurante():
    layout = [
        [sg.Text("Seja bem-vindo(a) Sabor Express", size=(25, 1), font=("Times New Roman", 16))],
        [sg.Button("Cadastrar restaurante"), sg.Button("Cadastrar produto"), sg.Button("Ativar restaurante"), sg.Button("Desativar restaurante"), sg.Button("Sair")]
    ]

    window = sg.Window("Sabor Express", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "Cadastrar restaurante":
            nome_do_restaurante = values["Cadastrar restaurante"]  # Ajustado a atribuição
            if nome_do_restaurante in restaurantes:
                sg.popup("Restaurante já cadastrado.")
            else:
                restaurantes.append(nome_do_restaurante)  # Adicionando o restaurante à lista
                sg.popup(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
            
            # Agora, exibe a janela para cadastrar o ponto de referência
            cadastrar_ponto_referencia()

    window.close()


# Função para cadastrar ponto de referência
def cadastrar_ponto_referencia():
    layout = [
        [sg.Text("Cadastre o tipo de restaurante (ex: fast food, restaurante à la carte, self service): ")],
        [sg.Text("Descrição sobre o restaurante (como é o estilo de cozinha): ")],
        [sg.Text("Ponto de referência (opcional): ")],
        [sg.InputText(key="Ponto_referencia")],
        [sg.Button("Ok"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Ponto de Referência", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        elif event == "Ok":
            ponto_referencia = values["Ponto_referencia"]  # Corrigido para obter a variável
            if ponto_referencia:
                sg.popup(f"Ponto de referência fornecido: {ponto_referencia}")
            else:
                sg.popup("Nenhum ponto de referência foi fornecido.")

    window.close()


# Função para cadastrar novo produto
def cadastrar_novo_produto():
    layout = [
        [sg.Text("Cadastre novo produto")],
        [sg.InputText(key="Novo_produto")],
        [sg.Button("Cancelar"), sg.Button("Confirmar")]
    ]
    
    window = sg.Window("Cadastrar Novo Produto", layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        elif event == "Confirmar":
            nome_produto = values["Novo_produto"]  # Corrigido a atribuição
            if nome_produto in produtos:
                sg.popup("Produto já cadastrado.")
            else:
                produtos.append(nome_produto)  # Adicionando o produto à lista
                sg.popup(f"Produto {nome_produto} cadastrado com sucesso!")

            # Agora, exibe a janela para escolher categoria do produto
            cadastrar_categoria_produto()

    window.close()


# Função para cadastrar categoria de produto
def cadastrar_categoria_produto():
    layout = [
        [sg.Text("Escolha uma categoria para seu produto: ")],
        [sg.Text("1. Entradas"), sg.Text("2. Bebidas"), sg.Text("3. Pratos principais")],
        [sg.InputText(key="Categoria")],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]
    
    window = sg.Window("Escolher Categoria de Produto", layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        elif event == "Confirmar":
            categoria = values["Categoria"]  # Corrigido a atribuição
            if categoria in ["Entradas", "Bebidas", "Pratos principais"]:
                sg.popup(f"Produto registrado na categoria {categoria} com sucesso!")
            else:
                sg.popup("Categoria inválida.")

    window.close()
# Chama a função para cadastrar o restaurante ao iniciar o programa
    cadastrar_novo_restaurante()


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
            print("Opção de restaurante inválida!\n")
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
            cadastrar_novo_produto()
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
