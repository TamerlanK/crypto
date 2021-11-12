alphabet = 'abcdefghijklmnopqrstuvxyz'
# Elifbadaki herfleri 5-5 qruplasdirib table listine elave etmek
table = []
temp = []
for i in alphabet:
    temp.append(i)
    if len(temp) == 5:
        table.append(temp)
        temp = []
# [['a', 'b', 'c', 'd', 'e'], 0
# ['f', 'g', 'h', 'i', 'j'], 1
# ['k', 'l', 'm', 'n', 'o'], 2
# ['p', 'q', 'r', 's', 't'], 3
# ['u', 'v', 'x', 'y', 'z']] 4
text = input('Shifrelenecek sozu daxil edin : ')
# Eger uzunluq 2-ye tam bolunmurse sona 'x' elave etmek
if len(text) % 2 != 0:
    text += 'x'
# Eger sozde bir cutlukde iki eyni herf olarsa aralarina 'x' elave etmek
text_lst = list(text)
for i in range(len(text_lst)):
    if i + 1 <= len(text):
        if i % 2 == 0 and text_lst[i] == text_lst[i+1]:
            text_lst.insert(i+1,'x')
# Sozdeki herflerin cedveldeki indexlerini almaq
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
# Indexleri kodlashdirmaq ucun 2-2 qruplashdirmaq
locs_gr = []
for i in locs:
    temp.append(i)
    if len(temp) == 2:
        locs_gr.append(temp)
        temp = []
locs_gr_main = locs_gr
#playfair alqoritmi
for i in range(len(locs_gr)):
    #Eger iki herfin indexleri ferqlidirse onlari diaqonal uzre yerleni deyishmek
    if locs_gr[i][0][0] != locs_gr[i][1][0] and locs_gr[i][0][1] != locs_gr[i][1][1]:
        locs_gr[i][0][1], locs_gr[i][1][1] = locs_gr[i][1][1], locs_gr[i][0][1]
    #Eger herfler eyni setirdedirse 1 saga surushdurmek
    elif locs_gr[i][0][0] == locs_gr[i][1][0]:
        locs_gr[i][0][1] = (locs_gr[i][0][1] + 1) % 5
        locs_gr[i][1][1] = (locs_gr[i][1][1] + 1) % 5
    #Eger herfler eyni sutundadirsa 1 ashagi surushdurmek
    elif locs_gr[i][0][1] == locs_gr[i][1][1]:
        locs_gr[i][0][0] = (locs_gr[i][0][0] + 1) % 5
        locs_gr[i][1][0] = (locs_gr[i][1][0] + 1) % 5
locs_swapped = locs_gr
#Indexleri cedveldeki herflerle evez etmek
cipher = ''
for i in range(len(locs_gr)):
    for j in range(len(locs_gr[0])):
        cipher += table[locs_swapped[i][j][0]][locs_swapped[i][j][1]]
print(cipher)
