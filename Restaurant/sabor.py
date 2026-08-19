from models.restaurante import Restaurante
# Código importado utilizando o from e o import

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_japones = Restaurante('Japanzil', 'Japonesa')
# restaurante_mexicano = Restaurante('MexicanZil', 'Mexicana')

restaurante_praca.receber_avaliacao('Murillo', '10')
restaurante_praca.receber_avaliacao('Ana', '8.7')


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
