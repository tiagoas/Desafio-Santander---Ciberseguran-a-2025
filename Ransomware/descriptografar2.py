from cryptography.fernet import Fernet
import os


# 1. Carregar a chave
def carregar_chave():
    """ Acessa o arquivo 'chave.key' e obtem o texto com a chave """
    return open("chave.key", "rb").read()

# 2 Descriptografar arquivo
def descriptografar_arquivo(arquivo, chave):
    """ Acessa o arquivo, desincripta os dados e reescreve o texto desincriptografado. """
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

# 3. Encontrar arquivos
def encontrar_arquivos(diretorio, ):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista


def main():
    
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    
    print("Arquivos restaurados com sucesso")
    
    # Sugestão de exercício:
    # Ao invés de printar a mensagem acima, criar um arquivo com essa mensagem.

if __name__ == "__main__":
    main()
