import fileinput

# Funcion que crea al cuadro 
def crearCuadro(alph, key):
    cuadro = {}
    for i in range (0,5):
        for j in range (0,5):
            if i + j < len(key):
                cuadro[key[0]]="{}{}".format(i,j)
                alph = alph.replace(key[0],"")
                key = key[1:]
            else:
                cuadro[alph[0]]="{}{}".format(i,j)
                alph = alph[1:]
    return cuadro

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

#Obtener las llaves y texto plano, limpiando el input
key = lines[0].replace("\n","")
text = lines[1].replace(" ","") 
text = text.replace("\n","")

print(crearCuadro(alphabet, key))
print(key, text)