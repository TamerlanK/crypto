def createTable(tableKey):
    alphabet = 'abcdefghijklmnopqrstuvxyz'
    table = []
    temp = []
    for i in tableKey:
        if i not in table:
            table.append(i)
    for i in alphabet:
        if i not in table:
            table.append(i)
    tableGrouped = []
    for i in table:
        temp.append(i)
        if len(temp) == 5:
            tableGrouped.append(temp)
            temp = []
    return tableGrouped

def modifyText(text):
    textList = list(text)
    for i in range(len(textList)):
        if len(textList) % 2 != 0:
            textList.append('x')
        if i + 1 <= len(textList):
            if i % 2 == 0 and textList[i] == textList[i + 1]:
                textList.insert(i + 1, 'x')
    textListString = "".join(textList)
    return textListString


def getLetterLocations(modifiedText, table):
    temp = []
    locs = []
    for i in modifiedText:
        for j in range(len(table)):
            for k in range(len(table[0])):
                if table[j][k] == i:
                    temp.append(j)
                    temp.append(k)
                    if len(temp) == 2:
                        locs.append(temp)
                        temp = []
    return locs


def groupLetterLocations(locs):
    locs_groupped = []
    temp = []
    for i in locs:
        temp.append(i)
        if len(temp) == 2:
            locs_groupped.append(temp)
            temp = []
    return locs_groupped


def swapForEncryption(locs_gr):
    for i in range(len(locs_gr)):
        if locs_gr[i][0][0] != locs_gr[i][1][0] and locs_gr[i][0][1] != locs_gr[i][1][1]:
            locs_gr[i][0][1], locs_gr[i][1][1] = locs_gr[i][1][1], locs_gr[i][0][1]
        elif locs_gr[i][0][0] == locs_gr[i][1][0]:
            locs_gr[i][0][1] = (locs_gr[i][0][1] + 1) % 5
            locs_gr[i][1][1] = (locs_gr[i][1][1] + 1) % 5
        elif locs_gr[i][0][1] == locs_gr[i][1][1]:
            locs_gr[i][0][0] = (locs_gr[i][0][0] + 1) % 5
            locs_gr[i][1][0] = (locs_gr[i][1][0] + 1) % 5
    locs_swapped = locs_gr
    return locs_swapped


def swapForDecryption(locs_gr):
    for i in range(len(locs_gr)):
        if locs_gr[i][0][0] != locs_gr[i][1][0] and locs_gr[i][0][1] != locs_gr[i][1][1]:
            locs_gr[i][0][1], locs_gr[i][1][1] = locs_gr[i][1][1], locs_gr[i][0][1]
        elif locs_gr[i][0][0] == locs_gr[i][1][0]:
            locs_gr[i][0][1] = (locs_gr[i][0][1] - 1) % 5
            locs_gr[i][1][1] = (locs_gr[i][1][1] - 1) % 5
        elif locs_gr[i][0][1] == locs_gr[i][1][1]:
            locs_gr[i][0][0] = (locs_gr[i][0][0] - 1) % 5
            locs_gr[i][1][0] = (locs_gr[i][1][0] - 1) % 5
    locs_swapped = locs_gr
    return locs_swapped


def locationsToLetters(locs_swapped, table):
    cipher = ''
    for i in range(len(locs_swapped)):
        for j in range(len(locs_swapped[0])):
            cipher += table[locs_swapped[i][j][0]][locs_swapped[i][j][1]]
    return cipher



def playfairEncryption(plaintext, table, uppercases):
    locationsBefore = getLetterLocations(plaintext, table)
    locationsGroupped = groupLetterLocations(locationsBefore)
    locationsSwapped = swapForEncryption(locationsGroupped)
    cipher = locationsToLetters(locationsSwapped, table)
    cipher = changeCases(cipher, uppercases)
    return cipher

def playfairDecrpytion(cipher, table, uppercases):
    locationsBefore = getLetterLocations(cipher, table)
    locationsGroupped = groupLetterLocations(locationsBefore)
    locationsSwapped = swapForDecryption(locationsGroupped)
    plaintext = locationsToLetters(locationsSwapped, table)
    plaintext = changeCases(plaintext, uppercases)
    return plaintext

def changeCases(cipher, uppercases):
    cipher = list(cipher)
    for i in uppercases:
        cipher[i] = cipher[i].upper()
    return "".join(cipher)

def getUpperCases(text):
    return [i for i in range(len(text)) if text[i].isupper()]

table = createTable('')
tableKeySelection = input('Cedvel ucun achar soz daxil edilsin?(yes/no) : ')
if tableKeySelection.lower() == 'yes':
    tableKey = input('Achar sozu daxil edin : ')
    table = createTable(tableKey)
option = int(input("""1.Shifrelemek : 
2.Deshifrelemek : \n"""))
if option == 1:
    text = input("Shifrelenecek metn : ")
    modifiedText = modifyText(text)
    cipher = playfairEncryption(modifiedText.lower(), table, getUpperCases(modifiedText))
    print(cipher)
elif option == 2:
    cipher = input("Deshifrelenecek metn : ")
    plaintext = playfairDecrpytion(cipher.lower(), table, getUpperCases(cipher))
    print(plaintext)
