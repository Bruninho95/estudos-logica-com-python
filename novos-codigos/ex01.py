 
# Lista de compras inicial (vazia)
lista_de_compras = []

def exibir_lista():
    """Função para exibir todos os itens na lista de compras"""
    if not lista_de_compras:
        print("A lista de compras está vazia.")
    else:
        print("Lista de Compras:")
        for item in lista_de_compras:
            print(f"- {item}")

def adicionar_item(item):
    """Função para adicionar um item à lista de compras"""
    lista_de_compras.append(item)
    print(f"'{item}' foi adicionado à lista de compras.")

def remover_item(item):
    """Função para remover um item da lista de compras"""
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"'{item}' foi removido da lista de compras.")
    else:
        print(f"'{item}' não está na lista de compras.")

def menu():
    """Função para exibir o menu de opções"""
    print("\nMenu:")
    print("1. Exibir lista de compras")
    print("2. Adicionar item")
    print("3. Remover item")
    print("4. Sair")

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_lista()
    elif opcao == "2":
        item = input("Digite o nome do item a ser adicionado: ")
        adicionar_item(item)
    elif opcao == "3":
        item = input("Digite o nome do item a ser removido: ")
        remover_item(item)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
