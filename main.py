import nltk
from correcaoOrtografica import correcao


frase = "Oiá, tldo bem? você podeia testar a formatação e correçao de texto d nlkt."


def main():
    correcao.principal(frase)


if __name__ == "__main__":
    main()