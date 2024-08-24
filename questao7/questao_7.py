estoque = "aaa"

def verificar(palavra):
    global estoque
    estoque_temporario = estoque
    for letra in estoque_temporario:
        if letra in palavra:
            estoque = estoque_temporario.replace(letra, "", 1)
        else:
            print(False) 
            return
    if not estoque_temporario:
        print(True)
    else:
        print(False)
entrada = input("Digite o código do medicamento: ")
verificar(palavra=entrada)