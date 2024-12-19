class Node:
    def __init__(self, name, price, category, quantity):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.left = None
        self.right = None

class Stock:

    def __init__(self):
        self.root = None

    # Inserção recursiva
    def insert(self, nome, preco, categoria, quantidade):
        def _insert(node, product):
            
            # if self.search(product.name) :
            #     print("Produto já existente")
            #     return

            if not node:
                # Caso estiver vazio
                return product

            # Ordenação com base no nome
            if product.name < node.name:
                node.left = _insert(node.left, product)
            elif product.name > node.name:
                node.right = _insert(node.right, product)
            
            return node


        newProduct = Node(nome, preco, categoria, quantidade)
        self.root = _insert(self.root, newProduct)

    def search(self, name):
        def _search(node, name):
            # Caso achar ou não achar o nó
            # retorna none ou o próprio nó
            if not node or node.name == name:
                return node
            
            if name < node.name:
                return _search(node.left, name)
            
            return _search(node.right, name)

        return _search(self.root, name)

    def remove(self, name):
        def _lower(node):
            while node.left:
                node = node.left

            return node

        def _remove(node, name):
            if not node:
                # Caso não achar o nodo na arvore.
                return None
            
            if name < node.name:
                # Nodo esquerdo for menor que o nodo atual
                node.left = _remove(node.left, name)

            elif name > node.name:
                # Nodo direito for menor que o nodo atual
                node.right = _remove(node.right, name)
                
            else:
                # Caso nodo encontrado
                if not node.left:
                    # Verifica se tem filhos a direita
                    return node.right
                
                if not node.right:
                    # Verifica se tem filhos a esquerda
                    return node.left
                
                # Caso tiver filhos dos dois lados
                # Procura o menor filho a direita para ocupar o nodo atual
                change = _lower(node.right)
                node.name, node.price, node.category, node.quantity = (
                    change.name,
                    change.price,
                    change.category,
                    change.quantity,
                )
                node.right = _remove(node.right, change.name)

            return node

        self.root = _remove(self.root, name)

    def totalValue(self):
        def _value(node):
            if not node:
                # Caso não possuir nenhum nodo
                return 0
            
            # Calculos solicitados na questão
            total = node.price * node.quantity
            total += _value(node.left)
            total += _value(node.right)

            return total

        return _value(self.root)

    def showStock(self):
        def _show(node):

            if not node:
                return
            
            _show(node.left)
            print(
                f"Nome: {node.name}, Preço: {node.price}, Categoria: {node.category}, Quantidade: {node.quantity}"
            )

            _show(node.right)

        _show(self.root)

def menu():
    stock = Stock()
    
    while True:
        print("\n=== SGE - Sistema de Gerenciamento de Estoque ===")
        print("1. Inserir produto")
        print("2. Buscar produto")
        print("3. Remover produto")
        print("4. Mostrar estoque")
        print("5. Valor total em estoque")
        print("0. Sair")

        option = input("Escolha uma opção: ")

        match(option):
            case 1:
                name = input("Digite o nome do produto: ")
                price = float(input("Digite o preço do produto: "))
                category = input("Digite a categoria do produto: ")
                quantity = int(input("Digite a quantidade do produto: "))
                stock.insert(name, price, category, quantity)
                print("Produto inserido com sucesso!")
        
            case 2:
                name = input("Digite o nome do produto que deseja buscar: ")
                product = stock.search(name)
                if product:
                    print(
                        f"Produto encontrado: Nome: {product.name}, Preço: {product.price}, Categoria: {product.category}, Quantidade: {product.quantity}"
                    )
                else:
                    print("Produto não encontrado!")
        
            case 3:
                name = input("Digite o nome do produto que deseja remover: ")
                stock.remove(name)
                print("Produto removido com sucesso, caso existisse no estoque!")
        
            case 4:
                print("\nProdutos em estoque:")
                stock.showStock()
        
            case 5:
                total = stock.totalValue()
                print(f"Valor total em estoque: R$ {total:.2f}")
        
            case 0:
                break
        
            case _:
                print("Opção inválida! Tente novamente.")

menu()