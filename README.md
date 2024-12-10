# Blockchain para Validação de Dados de Exames

Este projeto implementa uma blockchain em Python para armazenar e validar dados de exames médicos, como níveis de glicose, utilizando um contrato inteligente (SmartContract). O projeto também exporta os blocos para um arquivo JSON e exibe os dados de forma organizada no terminal.

---

## 📝 Funcionalidades

- **Criação de Blockchain**:
  - Cada bloco contém: índice, timestamp, dados do exame, hash anterior, hash atual e nonce.
  - Garante segurança e imutabilidade dos dados.

- **Validação de Exames**:
  - Contrato inteligente verifica a validade dos dados (ex.: níveis de glicose entre 70 e 200).
  - Retorna mensagens de sucesso ou erro, dependendo da entrada.

- **Exportação e Visualização**:
  - Exporta a blockchain para um arquivo JSON (`blockchain.json`).
  - Exibe o conteúdo do arquivo no terminal de forma clara e separada por delimitadores visuais.

---

## 📂 Estrutura do Projeto

- **`blockchain.py`**: Código principal contendo a implementação da blockchain e do contrato inteligente.
- **`blockchain.json`**: Arquivo gerado automaticamente com os dados dos blocos.
- **`README.md`**: Documentação do projeto.

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.7 ou superior.
- Biblioteca padrão `json` do Python.

### Passos

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/AlanDiekGuimaraes/Blockchain_Python.git

2. **Execulte o arquivo:**
    python blockchain.py

3. **Verifique a saída:**
    O arquivo blockchain.json será gerado com os dados da blockchain.
    Os dados também serão exibidos no terminal de forma legível.

---

## 📘 Exemplo de Saída
No terminal, os dados de cada bloco serão exibidos com separadores visuais, por exemplo:

- ====================================================================================================
-        Índice: 1
-     Timestamp: 1733852828.300565
-         Dados: {'glicose': 70.0}
- Hash Anterior: 22843f1829c6cb109068ae05037f2c82dfb09e184004bed18a5359b5b465d4d2
-    Hash Atual: 00903abfa310a33265bb81094742cb4150ca16f8db38d50e9e1b72643aba3f1a
-         Nonce: 324
- ====================================================================================================

---

## 🛠️ Tecnologias Utilizadas
- Python: Linguagem de programação utilizada.
- JSON: Para exportação e leitura dos dados.