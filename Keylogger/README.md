
<h1 align="center">Keylogger</h1>


![Logo](https://assets.dio.me/L5Lo3zVlkpexxdlQdkC_YhBGbW6rdOIClcpKFWpS5RE/f:webp/h:77/q:80/w:77/L2xhYl9wcm9qZWN0cy9iYWRnZXMvOTc3ZDNkNmEtYzMzYi00YjEwLWE1NTUtODM0YzdkYWE2MjkwLnBuZw)





## 💀 O que é um Keylogger

Um **keylogger** é uma ferramenta que registra tudo o que é digitado no teclado. Pode ser usado por atacantes para roubar senhas, dados bancários e outras informações confidenciais.

---

## ⚙️ Como funciona

- **Software:** Instalado como malware via phishing, anexos maliciosos ou sites inseguros.
- **Hardware:** Dispositivo físico conectado entre o teclado e o computador.
- **Objetivo:** Capturar tudo que é digitado e enviar para o atacante.

---

## 🚨 Riscos

- Roubo de identidade
- Fraudes financeiras
- Espionagem corporativa


![Evidência](https://github.com/tiagoas/Desafio-Santander---Ciberseguran-a-2025/blob/main/Keylogger/Dados%20Capturados.png)  
*Figura 1: Dados capturados por keylogger durante a realização do desafio*
*Foi usado o email da vítima e do atacante. A imagem vista é do email do atacante recebendo os dados de teclas.*


---

## 🛡️ Como se proteger

- Mantenha o sistema e programas atualizados
- Use antivírus e antimalware confiáveis
- Evite clicar em links ou abrir anexos suspeitos
- Ative autenticação multifator (MFA)
- Monitore processos e conexões de rede
- Use firewall e ferramentas de detecção (EDR, SIEM)

---

## 🔍 Como detectar um keylogger

- Lentidão incomum no sistema
- Atividades de rede suspeitas
- Programas desconhecidos iniciando com o sistema
- Arquivos ocultos ou logs em locais incomuns

- 


## 🧠 O Código em python

### 🔐 Primeiro Código – Envio por E-mail

- **Captura de teclas**: Registra letras, números e teclas especiais (espaço, enter, backspace).
- **Envio automático**: A cada 60 segundos, os dados são enviados por e-mail usando `smtplib`.
- **Execução contínua**: O `keyboard.Listener` mantém o monitoramento ativo.

### 🗂️ Segundo Código – Gravação em Arquivo

- **Captura de teclas**: Registra tudo o que é digitado, ignorando teclas como Shift, Ctrl e Alt.
- **Armazenamento local**: As informações são salvas diretamente no arquivo `log.txt`.
- **Formato legível**: Teclas especiais são convertidas para símbolos visuais (ex.: `[ESC]`, `\n`, `\t`).




