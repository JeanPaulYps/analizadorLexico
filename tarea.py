import re
from copy import copy

### Hay que corregir los binarios y hexadecimales
categoriasTokens = {
    "comentarios": r"\(\*(.|\s)*\*\)|\/\/\/.*",
    "numeros": r"0b[0-1]+|0[0-7]+|0x([0-9]|[a-f]|[A-F])+|(?!0)\d{1,}|0",
    "palabrasReservadas": r"_if|_while|_main"
}
categoriasNumeros ={
    "decimal": r"(?!0)\d{1,}|0(\s|$)",
    "binario": r"0b[0-1]+",
    "octal": r"0[0-7]+",
    "hexadecimal": r"0x([0-9]|[a-f]|[A-F])+"
}

def clasificarTokens(tokensEncontrados):
    Tokens = []
    for token in tokensEncontrados:
        cadena = token.group()
        if (esComentario(cadena)):
            Tokens.append( ("comentario", cadena))
        elif (esNumero(cadena)):
            if (esDecimal(cadena)):
                Tokens.append(("decimal", cadena))
            elif (esBinario(cadena)):
                Tokens.append(("binario", cadena))
            elif (esOctal(cadena)):
                Tokens.append(("octal", cadena))
            elif (esHexadecimal(cadena)):
                Tokens.append(("hexadecimal", cadena))
        elif (esPalabraReservada(cadena)):
            Tokens.append(("reservada", cadena))
        else:
            Tokens.append(("simbolo", cadena))
    return Tokens

def esComentario (cadena):
    return re.match(categoriasTokens["comentarios"],cadena)

def esNumero (cadena):
    return re.match(categoriasTokens["numeros"],cadena)

def esPalabraReservada (cadena):
    return re.match(categoriasTokens["palabrasReservadas"],cadena)

def esBinario (cadena):
    return re.match(categoriasNumeros["binario"], cadena)

def esOctal (cadena):
    return re.match(categoriasNumeros["octal"], cadena)

def esHexadecimal (cadena):
    return re.match(categoriasNumeros["hexadecimal"], cadena)

def esDecimal (cadena):
    return re.match(categoriasNumeros["decimal"], cadena)

regexTokens = r"\(\*(.|\s)*\*\)|\/\/\/.*|0b[0-1]+|0[0-7]+|0x([0-9]|[a-f]|[A-F])+|(?!0)\d{1,}|0|_if|_while|_main|[A-z]{1}(\d|\w)*"
print("Bienvenido")
f = open("entrada.txt",'r')
entrada = f.read()
tokensEncontrados = re.finditer(regexTokens,entrada)
Tokens = clasificarTokens(tokensEncontrados)

Tabla = """\
+---------------------------------------------+
| Tipo                 |                 Valor|
|---------------------------------------------|
{}
+---------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<20} | {:>20} |".format(*fila)
 for fila in Tokens)))
print (Tabla)
#for tipo, valor in Tokens:
#  print("{:<20} {:<20}".format(tipo,valor))

"""for i in re.finditer(tokens,entrada):
    print(i)
    print(i.group())"""


