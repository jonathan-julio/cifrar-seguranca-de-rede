import sys
from utils import (carregarTexto, formarChave,removerBarra)

def decifrar(chave, frase):
    saida = list(frase)
    for x in range(len(frase)):
        if saida[x] == " ":
            pass
        else:
            if (ord(saida[x]) - int(list(chave)[x])) < 65:
                saida[x] = chr((ord(saida[x]) - 
                    int(list(chave)[x])) + 26 )
            else:
                saida[x] = chr(ord(saida[x]) - 
                    int(list(chave)[x]))
    saida = "".join(saida)
    return saida

def __init__():
    data = removerBarra(sys.argv[1])
    frase = carregarTexto(sys.argv[2])
    chave = formarChave(data,frase)
    saida = decifrar(chave, frase)
    print(saida)
__init__();
