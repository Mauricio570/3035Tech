def numVogaisPalavras(string):
    somador = 0
    for vogais in string:
        if vogais == "a" or vogais== "e" or vogais== "i" or vogais== "o" or vogais== "u" or vogais== "A" or vogais== "E" or vogais== "I" or vogais== "O" or vogais== "U":
            somador += 1
            print(vogais)
    return somador
def numVogais(lista):
    somador =0
    for palavra in lista:
        somador += numVogaisPalavras(palavra)
    return somador
    
palavras = "contador de vogais"
print(numVogais(palavras))