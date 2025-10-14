import json

    # Criando a classe Produto
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    # Criando a classe Carrinho
class Cart:
    def __init__(self):
        self.items = {}  # Dicionário para armazenar os itens do carrinho

    def add_to_cart(self, product, quantity=1):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def list_cart(self):
        if not self.items:
            print("Seu carrinho está vazio.")
        else:
            for item in self.items.values():
                product = item['product']
                print(f"{product.name} (x{item['quantity']}) - ${product.price * item['quantity']}")

    def save_cart(self):
        cart_data = {
            'items': [{'product_id': item['product'].product_id, 'quantity': item['quantity']} for item in self.items.values()]
        }
        with open('cart.json', 'w') as f:
            json.dump(cart_data, f)

    def load_cart(self, products):
        try:
            with open('cart.json', 'r') as f:
                cart_data = json.load(f)
                for item in cart_data['items']:
                    product = next((p for p in products if p.product_id == item['product_id']), None)
                    if product:
                        self.add_to_cart(product, item['quantity'])
        except FileNotFoundError:
            print("Carrinho não encontrado!")

    # Função para carregar produtos de um arquivo
def load_products_from_file():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            return [Product(p['product_id'], p['name'], p['price']) for p in data]
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado!")
        return []

    # Função para salvar produtos em um arquivo
def save_products_to_file(products):
    data = [{'product_id': p.product_id, 'name': p.name, 'price': p.price} for p in products]
    with open('products.json', 'w') as f:
        json.dump(data, f)

    # Função para listar os produtos
def list_products(products):
    print("Produtos disponíveis:")
    for product in products:
        print(f"ID: {product.product_id}, Nome: {product.name}, Preço: ${product.price}")

    # Criando alguns produtos
prod1 = Product(1, "Laptop", 899.99)
prod2 = Product(2, "Smartphone", 679.99)
prod3 = Product(3, "Bola de Praia", 29.59)
prod4 = Product(4, "Shampoo pra Cachorro Anti-Pulga", 56.89)

    # Colocando os produtos em uma lista
products = [prod1, prod2, prod3, prod4]

    # Exibindo os produtos
list_products(products)

    # Criando o carrinho e adicionando alguns produtos (pra testar)
cart = Cart()
cart.add_to_cart(prod1, 1)
cart.add_to_cart(prod2, 2)

    # Mostrando os itens no carrinho e o total
cart.list_cart()
print(f"Total: ${cart.calculate_total():.2f}")

    # Salvando os produtos e o carrinho
save_products_to_file(products)
cart.save_cart()

    # Carregando os dados mais uma vez
loaded_products = load_products_from_file()
cart.load_cart(loaded_products)

    # Exibindo o carrinho com produtos
print("\nItens no Carrinho:")
cart.list_cart()
print(f"Total: ${cart.calculate_total():.2f}")