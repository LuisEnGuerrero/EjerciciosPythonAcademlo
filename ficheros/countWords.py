from io import open


def countWords(fileText):
    try:
        fileOpen = open(fileText, 'r')
    except:
        print("ERROR!!! El nombre de Archivo ingresado no es correcto o no existe!!!")

    allMaxWords = {}
    tenMaxWords = {}
    #sizeWords = []
    fileWords = fileOpen.read()
    fileOpen.close()
    maxWords = fileWords
    maxWords.strip()
    maxWords.expandtabs(tabsize = 1)
    maxWords = maxWords.split()
    words = set(maxWords)
    if len(words) > 10:
        for word in words:
            #sizeWords.append(fileWords.count(word))
            allMaxWords[word]=fileWords.count(word)
        size = list(allMaxWords.values())
        size.sort()
        #rangeMax = size[-1]
        #rangeMin = size[-10]
        for clave in allMaxWords:
            if allMaxWords[clave] >= size[-10]:
                tenMaxWords[clave] = allMaxWords[clave]

    else:
        tenMaxWords = list(words)

    #print('maxWords:', maxWords)
    #print('words:', words)
    #print('sizeWords:', sizeWords)
    #print('tenMaxWords:', tenMaxWords)
    #print('size:', size)
    #print('range:', rangeMin, ' - ', rangeMax)
    return tenMaxWords

file = input("Ingrese el nombre del Archivo .txt a Analizar: ")
tenWords = countWords(file)
print("Las diez palabras más repetidas en el documento son: \n", tenWords)
