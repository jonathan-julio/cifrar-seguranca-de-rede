import sys

def removerBarra(data):
    data = data.replace("/","")
    return data

def formarChave(data, frase):
    saida = list()
    y = 0
    for x in list(frase):
        if x == " ":
            saida.append(x)
        else:
            if y >= len(data):
                y = 0
            x = data[y]
            saida.append(x)
            y = y + 1
    saida = "".join(saida)
    return saida

def carregarTexto(nomeArquivo):
    saida = ""
    try:
        arquivo = open(nomeArquivo, "r")
        for linha in arquivo:
            saida = str(saida) + str(linha) 
        arquivo.close()
        return saida
    except Exception as e:
        print("Exception: ", e)
        sys.exit()
