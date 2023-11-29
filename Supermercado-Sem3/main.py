
from produto import Produto

def cadastrar_produto(produtos):
    codigo = input("Digite o codigo do produto: ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preco do produto: "))

    produto = Produto(codigo, nome, preco)
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def excluir_produto(produtos):
    codigo = input("Digite o codigo do produto a ser excluido: ")
    for produto in produtos:
        if produto.codigo == codigo:
            produtos.remove(produto)
            print("Produto excluido com sucesso!")
            return
        print("Produto nao encontrado.")

def listar_produtos(produtos):
    for produto in produtos:
        print(produtos)

def consultar_precos(produtos):
    codigo = input("Digite o codigo do produto para consultar o preco: ")
    for produto in produtos:
        if produto.codigo == codigo:
            print(f"O preço do produto {produto.nome} é R${produto.preco: .2f}")
            return
        print("Produto nao encontrado.")


def menu():
    produtos =[]

    while True:
        print("\n====== MENU ======")
        print("1. Inserir novo produto")
        print("2. Excluir produto")
        print("3. Listar produtos")
        print("4. Consultar preco de um produto")
        print("0. Sair")

        opcao = input("Digite a opcao desejada: ")

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2:":
            excluir_produto(produtos)
        elif opcao == "3":
            listar_produtos(produtos)
        elif opcao == "4":
            consultar_precos(produtos)
        elif opcao == "0":
            print("Saindo do programa. Ate mais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    menu()


