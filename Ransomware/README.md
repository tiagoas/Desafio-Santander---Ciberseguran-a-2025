# Ransomware


![Imagem](https://assets.dio.me/L5Lo3zVlkpexxdlQdkC_YhBGbW6rdOIClcpKFWpS5RE/f:webp/h:77/q:80/w:77/L2xhYl9wcm9qZWN0cy9iYWRnZXMvOTc3ZDNkNmEtYzMzYi00YjEwLWE1NTUtODM0YzdkYWE2MjkwLnBuZw)


### 🧠 Funcionamento do Ransomware

1. **Infecção inicial:** O ransomware entra no sistema por phishing, anexos maliciosos, downloads infectados ou exploração de vulnerabilidades.
2. **Execução e propagação:** O malware se instala, desativa defesas e se espalha pela rede.
3. **Criptografia:** Arquivos são criptografados, tornando-se inacessíveis.
4. **Exigência de resgate:** Uma mensagem exige pagamento (geralmente em criptomoedas) para liberar os dados.
5. **Extorsão dupla:** Além da criptografia, os dados podem ser roubados e ameaçados de divulgação.

---

### 🚨 Riscos Associados

- **Perda de dados críticos**
- **Prejuízo financeiro** com resgates e paralisação de operações
- **Danos à reputação** por vazamento de informações
- **Multas legais** por violação de dados (ex.: LGPD)

---

### 🛡️ Como se Proteger

- **Backups regulares e offline**
- **Atualizações constantes** de sistemas e softwares
- **Antivírus e EDR** com proteção em tempo real
- **Autenticação multifator (MFA)**
- **Treinamento de usuários

## 📁 Estrutura do Código utilizado

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


