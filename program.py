import fileinput

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

#Obtener las llaves y texto plano, limpiando el input
key = lines[0].replace("\n","")
text = lines[1].replace(" ","") 
text = text.replace("\n","") 

print(key, text)