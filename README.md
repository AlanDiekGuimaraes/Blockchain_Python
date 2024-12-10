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

## 🛠️ Tecnologias Utilizadas
- Python: Linguagem de programação utilizada.
- JSON: Para exportação e leitura dos dados.