import sys

def seekExtensionFile(fileName):
    dot=fileName.rfind(".")
    extensionSeek=list(range(dot,len(fileName)))
    extension = ''
    for i in extensionSeek:
        extension= extension + fileName[i]
    return extension

def seekWordsFile(file, words):
    count = 0
    for line in file:
        line = line.strip()
        if not line.startswith(words):
            continue
        count = count + 1
        print(line)
    return count


while True:
    print('\nAnalizador de Archivos\n')
    fileName = input('Asegurare de que el archivo a trabajar tenga extensión .txt\npara SALIR, escribe SALIR en Mayúsculas\nIngresa el nombre del archivo que deseas trabajar: ')

    extension=seekExtensionFile(fileName)

    if fileName == 'SALIR':
        print('TRABAJO TERMINADO, GRACIAS!!!\n')
        break
    elif extension != '.txt':
        print('La Extensión del archivo es:',extension,'\nrecuerda que solo trabajamos con archivos: ".txt"\n')
        continue
    try:
        file=open(fileName, 'r')
    except ValueError:
        print('Nombre o Tipo de Archivo incorrecto!!!\n')
        #sys.exit()
    except FileNotFoundError:
        print('El Archivo solicitado no existe en esta Ruta!!!\n')

    words=input('Ingresa las palabras que deseas buscar en el Archivo: ')

    wordsFind=seekWordsFile(file, words)
    if wordsFind < 0:
        print('las palabras buscadas: ',words,' no se encuentran en el Archivo',fileName,'\n')
    else:
        print('Las palabras:',words,' se encuentran',wordsFind,' veces en el Archivo:',fileName,'\n')

    fileName=input('Pulsa enter para Continuar o escribe SALIR para Terminar: ')
    if fileName == 'SALIR':
        print('TRABAJO TERMINADO, GRACIAS!!!\n')
        break
