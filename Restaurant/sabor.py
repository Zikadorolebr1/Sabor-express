from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
# Código importado utilizando o from e o import

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_refrigerante = Bebida('Pepsi', 'R$7,00', 'Grande')
prato_macarrao = Prato('Macarronada', 'R$15,00', 'A melhor macarronada do Brasa!')

restaurante_praca.adicionar_no_cardapio(bebida_refrigerante)
restaurante_praca.adicionar_no_cardapio(prato_macarrao)
# restaurante_japones = Restaurante('Japanzil', 'Japonesa')
# restaurante_mexicano = Restaurante('MexicanZil', 'Mexicana')


def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
