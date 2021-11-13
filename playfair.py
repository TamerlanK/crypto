def createTable():
    alphabet = 'abcdefghijklmnopqrstuvxyz'
    table = []
    temp = []
    for i in alphabet:
        temp.append(i)
        if len(temp) == 5:
            table.append(temp)
            temp = []
    return table

def modifyText(text):
    if len(text) % 2 != 0:
        text += 'x'
    textList = list(text)
    for i in range(len(textList)):
        if i + 1 < len(textList):
            if i % 2 == 0 and textList[i] == textList[i+1]:
                textList.insert(i+1, 'x')
    return textList

def getLetterLocations(modifiedText, table):
    text_lst = list(modifiedText)
    temp = []
    locs = []
    for i in text_lst:
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

table = createTable()
option = int(input("""1.Shifrelemek : 
2.Deshifrelemek : """))
if option == 1:
    text = input("Shifrelenecek metn : ")
    modifiedText = modifyText(text)
    locationsBefore = getLetterLocations(modifiedText, table)
    locationsGroupped = groupLetterLocations(locationsBefore)
    locationsSwapped = swapForEncryption(locationsGroupped)
    cipher = locationsToLetters(locationsSwapped, table)
    print(cipher)
elif option == 2:
    cipher = input("Deshifrelenecek metn : ")
    locationsBefore = getLetterLocations(cipher, table)
    locationsGroupped = groupLetterLocations(locationsBefore)
    locationsSwapped = swapForDecryption(locationsGroupped)
    plaintext = locationsToLetters(locationsSwapped, table)
    print(plaintext)






