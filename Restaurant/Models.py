class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, capacidade='0', nota_avaliacao='0.0', ativo=False):

        self._nome = nome.title()   # Str ou string
        self._categoria = categoria.upper()  # Str
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self._ativo = False     # Quando se insere o underline ele se torna um atributo privado onde ninguém consegue mudar o valor dele
        Restaurante.restaurantes.append(self)
        # Restaurante primeiro maiusculo porque chama a classe e logo depois restaurantes no plural para a lista

    def __str__(self):
        return (f' {self._nome} | {self._categoria} | {self.capaciade} | {self.nota_avaliacao}')

    @classmethod  # permite que você chame o metodo de uma classe sem precisar instânciar a classe
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} |'
              f'{'Categoria'.ljust(25)} |'
              f'{'Nota do restaurante'.ljust(25)} |'
              f'{'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} |'
                  f'{restaurante._categoria.ljust(25)} |'
                  f'{restaurante.nota_avaliacao.ljust(25)} |'
                  f'{restaurante.ativo.ljust(25)}')

    @property  # is a built-in decorator that allows you to define methods in a class that can be accessed like regular attributes
    def ativo(self):
        return '✅​✅​' if self._ativo else '❌​❌​'

    def altenar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('Praça', 'Gourmet', '30', '6.7')
restaurante_praca.altenar_estado()
restaurante_japones = Restaurante('Japastel', 'Japonesa', '20', '10.0')

restaurantes = [restaurante_praca,
                restaurante_japones]

Restaurante.listar_restaurantes()

# Dir é uma função para retornar um valor da lista de atributos pra um self especifico
# Vars é uma função que retorna o atribuito __dict__ de um objeto
