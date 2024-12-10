# Criação do Bloco e Blockchain.
import hashlib          # Importa a biblioteca que faz o calculo do hash.
import json             # Importa o arquivo que manipula arquivos json.
from operator import index
from time import time   # Importa a função time para obter o timestamp (data e hora).


# Criando uma SmartContract para validar os dados de exames.
class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain
    
    def validar_dados_exame(self, dados):
        # Verifica se os dados são válidos
        if 'glicose' not in dados or not isinstance(dados['glicose'], (int, float)):
            return False, "Dados de glicose inválidos ou ausentes."
        if dados['glicose'] < 70 or dados['glicose'] > 200:
            return False, "Valor de glicose fora do intervalo permitido (70 a 200)."
        return True, "Dados válidos."
    
        
class Bloco:
    def __init__(self, index, dados, hash_anterior=""):
        # Inicializar o bloco com os parâmetros fornecidos e os atributos necessários.
        self.index = index  	            # Indice do bloco de cadeia.
        self.timestamp = time()             # Registra o momento de criação do bloco. 
        self.dados = dados                  # Dados armazenados no bloco (Ex: transações).
        self.hash_anterior = hash_anterior  # Hash do bloco anterior na cadeia.
        self.nonce = 0                      # Valor usado na prova de trabalho para alterar o hash.
        self.hash_atual = self.gerar_hash() # Gerar o hash do bloco.
    
    def gerar_hash(self):
        # Função para gerar o hash SHA-256 do bloco.
        conteudo_bloco = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'dados': self.dados,
            'hash_anterior': self.hash_anterior,
            'nonce': self.nonce
        }, sort_keys=True).encode()         # Converte os dados do bloco em uma string JSON ordenada
        return hashlib.sha256(conteudo_bloco).hexdigest()  # Calcula o hash e retorna como uma string hexadecimal.
    
    def prova_de_trabalho(self, dificuldade):
        # Realiza a prova de trabalho ajustando o nonce até que o hash comece com 'dificuldade' zeros.
        while self.hash_atual[:dificuldade] != '0' * dificuldade:   #
            self.nonce += 1                                         # Incrementa o nonce para alterar o hash.
            self.hash_atual = self.gerar_hash()                     # Recalcula o hash com o novo nonce.
    
class Blockchain:
    def __init__(self, nome_arquivo='blockchain.json'):
        # Tenta carregar a cadeia de blocos de um arquivo JSON.
        self.nome_arquivo = nome_arquivo
        cadeia_carregada = carregar_cadeia_de_json(nome_arquivo)
        if cadeia_carregada:
            self.cadeia = cadeia_carregada
        else:
            # Se não houver dados carregados, inicia com o bloco Gênesis e defini a dificuldade da prova de trabalho.
            self.cadeia = [self.criar_bloco_genesis()]              # Lista que armazena os Blocos na cadeia.
        self.dificuldade = 2                                        # Define o numero de zeros necessários no hash da prova de trabalho.                                     
        
    def criar_bloco_genesis(self):
        # Cria um bloco inicial com dados fixos.
        return Bloco(0, "Bloco Gênesis", "0")                       # Cria o bloco genesis.
    
    def obter_ultimo_bloco(self):
        # Retorna o último bloco da cadeia.
        if len(self.cadeia) < 1:
            return None
        return self.cadeia[-1] 
        
    def adicionar_bloco(self, novo_bloco):
        # Adiciona um novo bloco a cadeia.
        novo_bloco.hash_anterior = self.obter_ultimo_bloco().hash_atual     # Define o hash do bloco anterior.
        novo_bloco.prova_de_trabalho(self.dificuldade)                      # Realiza a prova de trabalho para alterar o hash. 
        self.cadeia.append(novo_bloco)                                      # Adiciona o novo bloco à cadeia.
    
    def validar_cadeia(self):
        # Valida a integridade da cadeia de blocos.
        for i in range(1, len(self.cadeia)):
            bloco_atual = self.cadeia[i]
            bloco_anterior = self.cadeia[i-1]
            
            # Verifica se o hash do bloco atual é válido.
            if bloco_atual.hash_atual!= bloco_atual.gerar_hash():
                return False
            
            # Verifica se o hash do bloco anterior é válido.
            if bloco_atual.hash_anterior!= bloco_anterior.hash_atual:
                return False
        
        return True                                                         # Retorna verdadeiro se a cadeia for valida.
    
    def salvar_em_json(self, nome_arquivo='blockchain.json'):
        # Salva a cadeia de blocos em um arquivo JSON.
        with open(nome_arquivo, 'w') as arquivo:
            json.dump([bloco.__dict__ for bloco in self.cadeia], arquivo, indent=4)

def carregar_cadeia_de_json(nome_arquivo='blockchain.json'):
    try:
        # Tenta abrir e ler os dados do arquivo JSON.
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            # Reconstrói a cadeia de blocos a partir dos dados do JSON.
            cadeia = [Bloco(
                index=bloco['index'],
                dados=bloco['dados'],
                hash_anterior=bloco['hash_anterior']
            ) for bloco in dados]
            # Ajusta os hashes e nonces de cada bloco.
            for i, bloco in enumerate(cadeia):
                bloco.timestamp = dados[i]['timestamp']
                bloco.hash_atual = dados[i]['hash_atual']
                bloco.nonce = dados[i]['nonce']
            return cadeia
    except FileNotFoundError:
        # Retorna None se o arquivo não existir.
        print(f"Arquivo {nome_arquivo} não encontrado. Criando uma nova blockchain...")
        return None
    except json.JSONDecodeError:
        # Retorna None se o arquivo não for válido.
        print(f"Erro ao decodificar {nome_arquivo}. Criando uma nova blockchain...")
        return None    
    
# Função para coletar dados de exames médicos. 
def coletar_dados_exame():
    try:
        # Implementar a função para coletar dados de exames médicos.
        glicose = float(input('Digite o valor da glicose: '))
        return { 'glicose': glicose }                               # Retorna um dicionario com os dados coletados. 
    except ValueError:
        print("Erro: valor inválido. Digite um número válido.")
        return coletar_dados_exame()
    

# Instanciar a Blockchain.
blockchain = Blockchain(nome_arquivo='blockchain.json')
smart_contract = SmartContract(blockchain)

# Adicionar um Bloco.
while True:
   
    # Coletar os dados de exames do usuário. 
    dados_exame = coletar_dados_exame()

    # Validar os dados utilizando o SmartContract
    valido, mensagem = smart_contract.validar_dados_exame(dados_exame)
    if not valido:
        print(f"Erro: {mensagem}")
        continue  # Solicita novamente os dados caso sejam inválidos

    # Criar um novo bloco com os dados coletados.
    novo_bloco = Bloco(blockchain.obter_ultimo_bloco().index + 1, dados_exame)

    # Define o índice do novo bloco como índice do ultimo bloco + 
    # Associa os dados coletados ao bloco criado.

    # Adiciona o novo bloco a blockchain
    blockchain.adicionar_bloco(novo_bloco)

    # Verifica a integridade da blockchain após adição do bloco
    if blockchain.validar_cadeia():
        blockchain.salvar_em_json()
        print('Blockchain válida e salva com sucesso!')
    else:
        print('Blockchain inválida!')
    
    # Perguntar ao usuário se deseja continuar ou encerrar.
    continuar = input("Deseja adicionar mais blocos? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa...")
        break

# Exibir o conteúdo dpo arquivo JSON
def print_json_content(filename):
    #tenta abrir e processar o arquivo json
    separador = "=" * 100
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            #print(json.dumps(data, indent=4))
            for bloco in data:
                print(separador)
                print(f"       Índice: {bloco['index']}")
                print(f"    Timestamp: {bloco['timestamp']}")
                print(f"        Dados: {bloco['dados']}")
                print(f"Hash Anterior: {bloco['hash_anterior']}")
                print(f"   Hash Atual: {bloco['hash_atual']}")
                print(f"        Nonce: {bloco['nonce']}")
            print(separador)  
            

    except FileNotFoundError:
        print(f"Erro: Arquivo {filename} não encontrado")
    except json.JSONDecodeError:
        print(f"Erro: Arquivo {filename} não é um json valido")
print_json_content('blockchain.json')


