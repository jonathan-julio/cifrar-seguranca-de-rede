import unicodedata
import string
import sys
from utils import (carregarTexto, formarChave,removerBarra)

def tratarTexto(frase):
    frase = ''.join(ch for ch in unicodedata.normalize('NFKD', 
        frase) 
        if not unicodedata.combining(ch))
    frase = frase.upper()
    frase = list(frase)
    for x in range(len(frase)):
        if (((65 <= ord(frase[x]) <= 90)  is False ) 
            and (ord(frase[x]) != 32)):
            frase[x] = ""
    frase = "".join(frase)
    return frase

def cifrar(chave, frase):
    saida = list(frase)
    for x in range(len(frase)):
        if saida[x] == " ":
            pass
        else:
            if (ord(saida[x]) + int(list(chave)[x])) > 90:
                saida[x] = chr((ord(saida[x]) + 
                    int(list(chave)[x])) - 26 )
            else:
                saida[x] = chr(ord(saida[x]) + 
                    int(list(chave)[x]))
    saida = "".join(saida)
    return saida

def salvar(frase, arquivoSex):
    arquivo = open(arquivoSex, "w")
    arquivo.write(frase)
    print("Salvo.")

def __init__():
    data = removerBarra(sys.argv[1])    
    frase = tratarTexto(carregarTexto(sys.argv[2]))
    chave = formarChave(data,frase)
    saida = cifrar(chave, frase)
    salvar(saida, sys.argv[3])
__init__();

