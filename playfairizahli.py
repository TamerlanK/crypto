# Isteye gore istifadeciden alinan acar soze gore cedvel qurmaq
def createTableByKeyword(tableKey):
    alphabet = 'abcdefghijklmnopqrstuvxyz'
    table = []
    temp = []
    #Istifadechini daxil etdiyi sozu herfler tekrarlanmamaq shertile bir liste yigmaq
    for i in tableKey:
        if i not in table:
            table.append(i)
    #Elifbadan istifadechinin daxil etdiyi sozde olmayan herfleri sira ile hemin liste elave etmek
    for i in alphabet:
        if i not in table:
            table.append(i)
    #Son alinmish listi 5-5 qruplashdirmaq
    tableFull = []
    for i in table:
        temp.append(i)
        if len(temp) == 5:
            tableFull.append(temp)
            temp = []
    return tableFull

#Playfair ucun default cedvel yaratmaq
def createTable():
    # elifbada w herfi yoxdur
    alphabet = 'abcdefghijklmnopqrstuvxyz' #Cedvel bu stringe gore yaradilir
    table = []
    temp = []
    #Elifbadaki herfler muveqqeti bir temp listine elave olunur ve uzunlugu 5 olduqda 'table' listine elave olunur
    #ve temp listi her defe sifirlanir
    #Sonda ise [5][5] olcusunde 'table' ikiolculu listi, arrayi yaranir
    for i in alphabet:
        temp.append(i)
        if len(temp) == 5:
            table.append(temp)
            temp = []
    return table

#Istifadeciden alinan sozu kodlasdirmaya hazir hala getirmek
def modifyText(text):
    #Eger soz 2-2 tam bolunmurse sona 'x' elave etmek
    if len(text) % 2 != 0:
        text += 'x'
    #Burada ise soz 2-2 bolunende eger bir cutluye 2 eyni herf dushurse aralarina 'x' elave edilir

    #Istifadeciden alinan metn string tipinde olduguna gore ve pythonda stringler immutable yeni deyishmez oldugu ucun
    #o liste cevirilmelidir ki araya herf elave ede bilek
    textList = list(text)
    #Listin uzunlugu boyunca dovr edilir
    for i in range(len(textList)):
        #Sozun uzunlugunu ashmamaq ucun i + 1 < len(textList) sherti yoxlanir
        if i + 1 < len(textList):
            #Soz 2-2 bolunduke eger herfler bir cutluk icinde olarsa aralarina 'x' herfi elave edilir
            #ve her cutluyun bashladigi indexler cut olur meselen 'ta-me-rl-an' t indexi 0, m indexi 2 ve s
            #buna gore indexin cut ededden bashladigi ve bashlanan indexdeki ededleri sonraki ededin eyni olmasi yoxlanilir
            #Eger hal dogrudursa insert metodu ile i + 1 - ci yeni iki qosha herfin arasina 'x' elave olunur
            if i % 2 == 0 and textList[i] == textList[i+1]:
                textList.insert(i+1, 'x')
    return textList
#Kodlashdirmaga hazir sozdeki herflerin 'table' cedvelindeki indexlerini almaq
def getLetterLocations(modifiedText, table):
    temp = []
    locs = []
    #Sozdeki herfler uzerinde loop edilir
    for i in modifiedText:
        #Burada ise cedvel ikiolculu list(array) olduguna gore iki defe for loopu qurulur
        for j in range(len(table)): # j cedvelin 5 elementini
            for k in range(len(table[0])): # k ise her element icindeki 5 herfi gosterir
                #Eger cedvelin her hansi elementi i'ye yeni sozdeki herfe beraberdise hemin indexleri muveqqeti bir
                #temp listine yig
                if table[j][k] == i:
                    temp.append(j)
                    temp.append(k)
                    #Eger temp uzunlugu 2 olduqda yeni herfin [j][k] indexleri alindiqda hemin indexleri locs listine
                    #elave et ve tempi sifirla
                    if len(temp) == 2:
                        locs.append(temp)
                        temp = []
    #En sonda ise 2 olculu, uzunlugu modified olunmush sozun uzunluguna beraber list(array)
    #alinir ve bu defe her herfin yerine onlarin cedveldeki indexlerini gosteren locs listi yaranir
    return locs

#Burada ise sozu 2-2 kodlashdiracayiq deye locationlar listi bir daha 2-2 qruplashdirilir vee 3 olculu list yaranir
#Biraz cetin geldi he :D
def groupLetterLocations(locs):
    locs_groupped = []
    temp = []
    #Burda cox shey yoxdu hemenki tema
    for i in locs:
        temp.append(i)
        if len(temp) == 2:
            locs_groupped.append(temp)
            temp = []
    return locs_groupped

#       0    1    2    3    4
#  0 [['a', 'b', 'c', 'd', 'e'],
#  1 ['f', 'g', 'h', 'i', 'j'],
#  2 ['k', 'l', 'm', 'n', 'o'],
#  3 ['p', 'q', 'r', 's', 't'],
#  4 ['u', 'v', 'x', 'y', 'z']]

#Playfairde eger herfler eyni setir ve yaxudda sutunda deyildilerse duzbucaq yaradilirdi ve sagdaki herf sola, soldaki
#herf ise saga kecirdi. Yeni meselen 'ta-me-rl-an' sozunu kodlashirdanda evvelce 'ta' cutluyu goturulur
#t herfinin indexi cedvelde [3][4], a herfininki ise [0][0] dir.
#Kodlashdirmaq ucun 't' nin yerine 'p', 'a' nin yerine ise 'e' yazmaq lazimdir
#Yeni indexi [3][4] olan 't' herfi indexi [3][0] olan 'p' ile, indexi [0][0] olan 'a' herfi ise indexi
#[0][4] olan 'e' herfi ile evez olunur. Diqqet yetirsek gorerikki indexlerin birinci indexleri deyishmeyib, ikinci
#indexleri ise yer deyishdirib
#[[3][4],[0][0]] -> [[3][0],[0][4]]
# Bu proses eger herfler eyni sutun ve yaxudda setirde olmadiqda aparilir
#Eger herfler eyni setirde olarsa onlarin indexleri yalniz +1 saga surushdurulur [x][y] -> [x][y+1]
#Eger herfler eyni sutunda olarsa onlarin sutun nomreleri +1 ashagi surushdurulur [x][y] -> [x+1][y]

#Kodlashdirmaq ucun funksiya
def swapForEncryption(locs_gr):
    #Uc olculu list uzre loop edilir burada i sadece cutlukler uzre dovr etmek ucundur
    #2ci ve 3cu indexler ise sira ile cutlukdeki 1ci ve ya 2ci herfi(indeksle 0 1), 3cu indeks ise herfin cedveleki
    #koordinatlarini gosterir(yeni 0 olduqda [x][y] x indexini, 1 olduqda ise y indexini gosterir.
    for i in range(len(locs_gr)):
        # Eger iki herfin setir ve sutun indexleri ferqlidirse onlari diaqonal uzre yerlerini deyishmek
        if locs_gr[i][0][0] != locs_gr[i][1][0] and locs_gr[i][0][1] != locs_gr[i][1][1]:
            #Burda ise [0][1] yeni cutlukdeki ilk herfin ikinci indexi
            # [1][1] ile yeni ikinci herfin ikinci indexi ile deyishdirilir
            #Basha dushmedinse 105-ci line yeniden oxu
            locs_gr[i][0][1], locs_gr[i][1][1] = locs_gr[i][1][1], locs_gr[i][0][1]
        # Eger herfler eyni setirdedirse 1 saga surushdurmek
        # Herflerin eyni setirde olmasi demek onlarin birinci indexlerinin eyni olmasi demekdir
        # Meselen her ikisi de [0][1]  [0][3] kimi yerleshib
        # Bu zaman herflerin birinci index qalir, ikinci indexi +1 artilir ki herf saga surushsun
        elif locs_gr[i][0][0] == locs_gr[i][1][0]:
            locs_gr[i][0][1] = (locs_gr[i][0][1] + 1) % 5 # mod 5 ise index 5-i kechmesin deye alinir
            locs_gr[i][1][1] = (locs_gr[i][1][1] + 1) % 5
        # Eger herfler eyni sutundadirsa 1 ashagi surushdurmek
        # Herflerin bu defe eyni sutunda olmasi ikinci indexlerini eyni olmasi demekdir.
        # Bu zaman ise ikicni index qalir ve birinci index +1 artirilir ki, herf ashagi surushsun
        elif locs_gr[i][0][1] == locs_gr[i][1][1]:
            locs_gr[i][0][0] = (locs_gr[i][0][0] + 1) % 5
            locs_gr[i][1][0] = (locs_gr[i][1][0] + 1) % 5
    # Burda chashmiyim deye bashqa deyishene atamisham onemli deyil
    locs_swapped = locs_gr
    return locs_swapped

#Burda da swapForEncryption funksiyasinin eynisi sadece +1 artimaq yerine -1 azaldilib
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

#Burda da artiq yeni indexleri tapdiqdan sonra cedveldeki herflerle evez etmek lazimdir
def locationsToLetters(locs_swapped, table):
    cipher = ''
    #locs_swapped listi yene 3 olculu olaraq qaldigi ucun 2 defe loop edirik ve son indexi yeni herflerin indexini ozumuz
    # yaziriq cunki forla eliyende error verir bruh
    for i in range(len(locs_swapped)):
        for j in range(len(locs_swapped[0])):
            #locs_swapped[i][j][0] herfin 1-ci indexini gosterir ona gore table[][]-da birinciye yazilir
            #locs_swapped[i][j][1] de herfin 2-ci indexini gosterir ona gore table[][]-da ikinciye yazilir
            #ve cipher stringine elave olunurlar
            cipher += table[locs_swapped[i][j][0]][locs_swapped[i][j][1]]
    return cipher

#Daha sonrasi asandi
table = createTable()
customTable = input('Cedvel ucun achar soz daxil edilsin? (yes/no) ?\n')
if customTable == 'yes':
    keyword = input('Achar sozu daxil edin : ')
    table = createTableByKeyword(keyword)
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






