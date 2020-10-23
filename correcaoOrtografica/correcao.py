import nltk

def principal(texto):
    lista = tratamento(texto) 
    listaPalavras = geradorPalavras(lista) 
    palavra_certa = max(listaPalavras,key=probabilidade)  

def tratamento(texto):
    listaPalavras=[]
    tokens = nltk.tokenize.word_tokenize(texto)
    for token in tokens:
        if token.isalpha():
            listaPalavras.append(token.lower())
    return listaPalavras

def geradorPalavras(palavras):
    possibilidades = []
    for palavra in palavras:
        fatias = []
        for i in range(len(palavra)):
            fatias.append((palavra[:i],palavra[i:]))
        possibilidades.append(inserirLetra(fatias))
    return possibilidades


def inserirLetra(palavras):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in palavras:
        for letra in letras:
            novas_palavras.append(E + letra + D)
        return novas_palavras

def corretor(palavras):
