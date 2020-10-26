import nltk
from correcaoOrtografica import correcao


frase = "olhm, stamos tentundo corigir as palabras"
#frase = "tldo"

def main():
    correcao.principal(frase)

if __name__ == "__main__":
    main()