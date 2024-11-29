import json

# Nome do arquivo onde os produtos serão salvos
ARQUIVO_DADOS = "produtos.json"

# Tenta carregar os produtos do arquivo JSON
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir

# Salva os dados no arquivo JSON
def salvar_dados():
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump(promocoes, arquivo, indent=4)

# Lista para armazenar os produtos em promoção
promocoes = carregar_dados()

# Função para exibir o menu
def exibir_menu():
    print("\n=== Sistema de Controle de Promoções ===")
    print("1. Adicionar produto em promoção")
    print("2. Listar produtos em promoção")
    print("3. Remover produto da promoção")
    print("4. Gerar relatório")
    print("5. Sair")
    return input("Escolha uma opção: ")

# Função para adicionar produtos
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    desconto = input("Digite o percentual de desconto (%): ")
    preco_original = float(input("Digite o preço original do produto (R$): "))
    preco_promocional = preco_original * (1 - float(desconto) / 100)
    produto = {
        "nome": nome,
        "desconto": desconto,
        "preco_original": preco_original,
        "preco_promocional": preco_promocional
    }
    promocoes.append(produto)
    salvar_dados()
    print(f"Produto '{nome}' adicionado com sucesso!")

# Função para listar produtos
def listar_produtos():
    if not promocoes:
        print("Nenhum produto em promoção.")
        return
    print("\n=== Produtos em Promoção ===")
    for idx, produto in enumerate(promocoes, 1):
        print(f"{idx}. {produto['nome']} - {produto['desconto']}% OFF")
        print(f"   Preço Original: R$ {produto['preco_original']:.2f}")
        print(f"   Preço Promocional: R$ {produto['preco_promocional']:.2f}")

# Função para remover produtos
def remover_produto():
    listar_produtos()
    if not promocoes:
        return
    idx = int(input("\nDigite o número do produto para remover: ")) - 1
    if 0 <= idx < len(promocoes):
        produto = promocoes.pop(idx)
        salvar_dados()
        print(f"Produto '{produto['nome']}' removido com sucesso!")
    else:
        print("Número inválido.")

# Função para gerar relatório
def gerar_relatorio():
    if not promocoes:
        print("Nenhum produto em promoção para gerar relatório.")
        return
    total_produtos = len(promocoes)
    economia_total = sum(p['preco_original'] - p['preco_promocional'] for p in promocoes)
    print("\n=== Relatório de Promoções ===")
    print(f"Total de produtos em promoção: {total_produtos}")
    print(f"Economia potencial para os clientes: R$ {economia_total:.2f}")
    print("Produtos mais atrativos:")
    for produto in sorted(promocoes, key=lambda p: float(p['desconto']), reverse=True)[:3]:
        print(f"  - {produto['nome']} ({produto['desconto']}% OFF)")

# Programa principal
while True:
    opcao = exibir_menu()
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        remover_produto()
    elif opcao == "4":
        gerar_relatorio()
    elif opcao == "5":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
