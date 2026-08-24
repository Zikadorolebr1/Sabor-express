import PySimpleGUI as sg

restaurantes = []
produtos = []

# Função para exibir nome do programa
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
            nome_do_restaurante = sg.popup_get_text("Digite o nome do restaurante:")  # Corrigido para capturar o nome do restaurante
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
            ponto_referencia = values["Ponto_referencia"]
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
            nome_produto = values["Novo_produto"]
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
            categoria = values["Categoria"]
            if categoria in ["Entradas", "Bebidas", "Pratos principais"]:
                sg.popup(f"Produto registrado na categoria {categoria} com sucesso!")
            else:
                sg.popup("Categoria inválida.")

    window.close()

def desativar_restaurante():
    layout = [
        [sg.Text("Restaurantes ativos: ")]
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Restaurantes Ativos", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        elif event == "Confirmar":
            ativos = values["Ativos"]
            if ativos in restaurantes:
                sg.popup[f"Restaurante desativado {restaurantes} com sucesso!"]
            else:
                sg.popup["Opção inválida!"]

            desativar_restaurante()

    window.close()

# Função principal que inicializa o programa
def main():
    exibir_nome_do_programa()  # Exibe a popup com o nome do sistema
    cadastrar_novo_restaurante()  # Chama a função para cadastrar um novo restaurante
    desativar_restaurante()



if __name__ == "__main__":
    main()  # Chama a função principal quando o programa inicia
