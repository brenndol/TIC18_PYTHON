from DataFruta import *

def montarMenu(opcoes):
    opcoes_size = len(opcoes)

    for i in range(opcoes_size + 1):
        if i == opcoes_size:
            print('0. Sair do programa')
        else:
            print(f'{i + 1}. {opcoes[i]}')

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    opcoes = ['Incluir um nome na lista de nomes',
              'Incluir um salário na lista de salários',
              'Incluir uma data na lista de datas',
              'Incluir uma idade na lista de idades',
              'Percorrer as listas de nomes e salários',
              'Calcular o valor da folha com um reajuste de 10%',
              'Modificar o dia das datas anteriores a 2019']
    opcoes_size = len(opcoes)

    while True:
        montarMenu(opcoes)

        opcao_usuario = int(input('\nSua opção: '))

        if opcao_usuario == 0:  # Finalizar programa
            print('Fim do programa!')
            break
        elif opcao_usuario == 1:  # Incluir nome
            nomes.entradaDeDados()
        elif opcao_usuario == 2:  # Incluir salário
            salarios.entradaDeDados()
        elif opcao_usuario == 3:  # Incluir data
            datas.entradaDeDados()
        elif opcao_usuario == 4:  # Incluir idade
            idades.entradaDeDados()
        elif opcao_usuario == 5:  # Percorrer nomes e salários
            nomes.mostraDados()
        elif opcao_usuario == 6:  # Calcular reajuste
            pass
        elif opcao_usuario == 7:  # Modificar antes de 2019
            pass
        else:  # Opção inválida
            print(f'Insira um número entre 0 e {opcoes_size}')

        print()  # Simples quebra de linha após execução de módulo


if __name__ == "__main__":
    main()