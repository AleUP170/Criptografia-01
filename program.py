import fileinput

# Funcion que crea al cuadro 
def crearCuadro(alph, key):
    cuadro = {}
    for i in range (0,5):
        for j in range (0,5):
            if len(key) > 0:
                cuadro[key[0]]="{}{}".format(i,j)
                alph = alph.replace(key[0],"")
                key = key[1:]
            else:
                cuadro[alph[0]]="{}{}".format(i,j)
                alph = alph[1:]
    return cuadro

# Convierte texto a números
def convTextClaro(cuadro, texto):
    textCif = ""
    for x in texto:
        textCif+=cuadro[x]
    return textCif

# Genera cadena de números tomando pares
def genPares(cifrado):
    nuevCif = ["",""]
    for x in range(0,len(cifrado)):
        if x%2 == 0:
            nuevCif[0]+=cifrado[x]
        else: 
            nuevCif[1]+=cifrado[x]
    return nuevCif[0]+nuevCif[1]

# Toma los pares y genera texto cifrado
def cifrarPares(cifrado, cuadro):
    textCif = ""
    x = 0
    lista_llaves = list(cuadro.keys())
    lista_val = list(cuadro.values())

    while x < len(cifrado):
        par = cifrado[x]+cifrado[x+1]
        textCif += lista_llaves[lista_val.index(par)]
        x+=2
    return textCif

# Para decifrar, genera pares dividiendo los números a la mitad
def paresDecif(decif):
    listPar = ["",""]
    split = int(len(decif)/2)
    parCif = ""
    listPar[0] = decif[:split]
    listPar[1] = decif[split:]
    for x in range (0, split):
        parCif += listPar[0][x] + listPar[1][x]
    return parCif

# Cifrado
def cifrar(texto, cuadro):
    cif = convTextClaro(cuadro, texto)
    cif = genPares(cif)
    cif = cifrarPares(cif, cuadro)
    return cif

# Decifrado
def decifrar(texto, cuadro):
    decif = convTextClaro(cuadro, texto)
    decif = paresDecif(decif)
    decif = cifrarPares(decif, cuadro)
    return decif

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# Obtener las llaves y texto plano, limpiando el input
key = "ENCRYPT"
mode = lines[0].replace("\n","")
text = lines[1].replace(" ","") 
text = text.replace("\n","")

# Algoritmo
cuadro = crearCuadro(alphabet, key)
#if mode == "ENCRYPT":
print(cifrar(text, cuadro))
#elif mode == "DECRYPT":
#print(decifrar(text, cuadro))
