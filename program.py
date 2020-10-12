import fileinput

# Funcion que crea al cuadro 
def crearCuadro(alph, key):
    cuadro = {}
    for i in range (0,len(key)):
        cuadro[key[i]] = i
        alph.replace(key[i],"")
    for i in range (0,26-len(key)):
        cuadro[alph[i]] = i    
    return cuadro

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Obtener las llaves y texto plano, limpiando el input
key = lines[0].replace("\n","")
text = lines[1].replace(" ","") 
text = text.replace("\n","")

print(crearCuadro(alphabet, key))
print(key, text)