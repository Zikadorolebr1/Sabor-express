from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
# Código importado utilizando o from e o import

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_refrigerante = Bebida('Pepsi', 'R$7,00', 'Grande')
prato_macarrao = Prato('Macarronada', 'R$15,00', 'A melhor macarronada do Brasa!')
# restaurante_japones = Restaurante('Japanzil', 'Japonesa')
# restaurante_mexicano = Restaurante('MexicanZil', 'Mexicana')


def main():
    print(bebida_refrigerante)
    print(prato_macarrao)


if __name__ == '__main__':
    main()
