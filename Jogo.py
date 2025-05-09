# PARTE 1

class Jogo: 
    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco

    def exibir(self):  # Exibe as perguntas para detalhar
        print("Coloque o título do jogo: ", self.titulo)
        print("Coloque o gênero do jogo: ", self.genero)
        print("Qual a classificação do jogo: ", self.classificacao_etaria)
        print("Qual o preço do jogo: ", self.preco)

# Exemplo de uso 
jogo1 = Jogo("The Last of Us", "Ação/Aventura", "18+", 249.99)
jogo1.exibir()

# PARTE 2 

class Jogador:
    def __init__(self, nickname, id_jogador, saldo_carteira):
        self.nickname = nickname
        self.id_jogador = id_jogador
        self.saldo_carteira = saldo_carteira
        self.biblioteca_de_jogos = []

    # Adiciona um jogo na biblioteca
    def adicionar_jogo(self, jogo):
        self.biblioteca_de_jogos.append(jogo)  

    def adicionar_saldo(self, valor):
        self.saldo_carteira += valor

    def exibir(self):  # Exibe as perguntas para detalhar
        print("O nickname: ", self.nickname)
        print("O seu ID: ", self.id_jogador)
        print("Seu saldo na carteira é: R$", self.saldo_carteira)
        print("Sua biblioteca de jogos possui: ", [jogo.titulo for jogo in self.biblioteca_de_jogos])

# Exemplo de uso 
jogador1 = Jogador("Fabio Matador de Onça", "345432", 100.00)
jogador1.exibir()

# Adicionar jogos
jogador1.adicionar_jogo("The Last of Us")
jogador1.adicionar_jogo("God of War")
jogador1.exibir()

# PARTE 3

class Catalogo: 
    def __init__(self):
        self.catalogo = []
        self.jogadores_cadastrados = []

    def adicionar_jogador(self, jogador):
        self.jogadores_cadastrados.append(jogador)

    def adicionar_jogo_catalogo(self, jogo):
        self.catalogo.append(jogo)
        
    def buscar_jogo_por_titulo(self, titulo_jogo):
        for jogo in self.catalogo:
            if jogo.titulo == titulo_jogo:
                return jogo
        return None
    
    def buscar_jogador_por_id(self, id_jogador_busca):
        for jogador in self.jogadores_cadastrados:
            if jogador.id_jogador == id_jogador_busca:
                return jogador
        return None
    
    def listar_jogos_catalogo(self):
        for jogo in self.catalogo:
            jogo.exibir()
            
    def realizar_compra(self, id_jogador_comprador, titulo_jogo_desejado):
        jogador_obj = self.buscar_jogador_por_id(id_jogador_comprador)
        jogo_obj = self.buscar_jogo_por_titulo(titulo_jogo_desejado)

        if jogador_obj is None:
            print("Jogador não existente")
            return

        if jogo_obj is None:
            print("Jogo não encontrado")
            return

        # Verificação se o jogador já tem o jogo
        if jogo_obj in jogador_obj.biblioteca_de_jogos:
            print("Você já possui este jogo na biblioteca.")
            return
        
        # Verificação se possui saldo suficiente e faz a compra
        if jogador_obj.debitar_saldo(jogo_obj.preco):
            jogador_obj.adicionar_jogo(jogo_obj)
            print("Compra realizada com sucesso!")
        else:
            print("Saldo insuficiente para realizar a compra.")

# Exemplo de uso
catalogo = Catalogo()
catalogo.adicionar_jogo_catalogo(jogo1)

# Realizando uma compra
catalogo.realizar_compra("345432", "The Last of Us")
jogador1.exibir()

# PARTE 4

# Criação da plataforma de jogos
class Plataforma:
    def __init__(self):
        self.catalogo = Catalogo()

    def adicionar_jogo(self, jogo):
        self.catalogo.adicionar_jogo_catalogo(jogo)

    def adicionar_jogador(self, jogador):
        self.catalogo