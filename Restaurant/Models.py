class Restaurante:
    restaurantes = []

    def __init__(this, nome, categoria, capacidade='0', nota_avaliacao='0.0', ativo=False):

        this.nome = nome   # Str ou string
        this.categoria = categoria  # Str
        this.capacidade = capacidade
        this.nota_avaliacao = nota_avaliacao
        this.ativo = ativo
        Restaurante.restaurantes.append(this)
        # Restaurante primeiro maiusculo porque chama a classe e logo depois restaurantes no plural para a lista

    def __str__(this):
        return (f' {this.nome} | {this.categoria} | {this.capaciade} | {this.nota_avaliacao}')

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.nota_avaliacao} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet', '30', '6.7')
restaurante_japones = Restaurante('Japastel', 'Japonesa', '20', '10.0')

restaurantes = [restaurante_praca,
                restaurante_japones]

Restaurante.listar_restaurantes()

# Dir é uma função para retornar um valor da lista de atributos pra um this especifico
# Vars é uma função que retorna o atribuito __dict__ de um this
