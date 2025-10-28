
![Logo](https://assets.dio.me/C_w739DMTY1XPvnkcaSY7doWFM9I5MREIuft-gfwJDY/f:webp/h:120/q:80/L3RyYWNrcy83MGI2Y2EwOC0xZDdlLTQxNTctYmI0OC05NmMxMTY0ZmQ3ZTcucG5n)


![Evidência](https://github.com/tiagoas/Desafio-Santander---Ciberseguran-a-2025/blob/main/Keylogger/Dados%20Capturados.png)


# 🛑 Ransomware Simulado em Python

Este projeto demonstra o funcionamento básico de um **ransomware** — um tipo de software malicioso que criptografa arquivos e exige pagamento para restaurá-los. **⚠️ Este código é apenas para fins educacionais e de pesquisa. Não deve ser usado em ambientes reais ou para fins maliciosos.**

---

## ⚙️ Funcionalidades

- Geração de chave de criptografia com `Fernet` (biblioteca `cryptography`)
- Criptografia de arquivos em uma pasta específica
- Criação de mensagem de resgate
- Exclusão de arquivos sensíveis do processo (como o próprio script e a chave)

---

## 📁 Estrutura do Código

### 1. `gerar_chave()`
Gera uma chave de criptografia e salva em `chave.key`.

### 2. `carregar_chave()`
Carrega a chave salva para uso na criptografia.

### 3. `criptografar_arquivo(arquivo, chave)`
Criptografa o conteúdo de um arquivo usando a chave fornecida.

### 4. `encontrar_arquivos(diretorio)`
Percorre recursivamente o diretório especificado e retorna uma lista de arquivos a serem criptografados, ignorando o script e arquivos `.key`.

### 5. `criar_mensagem_resgate()`
Cria um arquivo `LEIA ISSO.txt` com instruções de pagamento e recuperação dos dados.

### 6. `main()`
Executa todas as etapas:
- Gera e carrega a chave
- Encontra os arquivos
- Criptografa os arquivos
- Cria a mensagem de resgate

---

## 🚀 Como Executar

1. Instale a biblioteca necessária:
   ```bash
   pip install cryptography


