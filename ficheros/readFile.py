texto = open('mbox-short.txt', 'r')

archivo=0

"""
for linea in texto:
    linea=linea.strip()
    if linea == '':
        continue
    else:
        archivo = archivo + 1
    print(archivo)
"""

count = 0
for line in texto:
    line = line.strip()
    if not line.startswith("From:"):
        continue
    count = count + 1
    print(line)

print ('\nTotal correos encontrados:',count)
