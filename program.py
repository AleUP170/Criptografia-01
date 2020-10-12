import fileinput

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

#Obtener las llaves y texto plano
key = lines[1]
text = lines[2].replace(" ","") 

print(key, text)