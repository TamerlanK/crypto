alphabet = " abcdefghijklmnopqrstuvwxyz"
n = 3
key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
text = 'tamerlan'
# arrayde catismayan herfleri tamamlamaq
while len(text) % n != 0:
    text += 'x'
# herfleri sira nomresi ile yazmaq
text_alphabet_order = []
for i in text:
    text_alphabet_order.append(alphabet.find(i))
#print(text_alphabet_order)
#sira nomrelerini n-n qruplasdirmaq
text_alphabet_order_grouped = []
temp = []
for i in text_alphabet_order:
    temp.append(i)
    if len(temp) == n:
        text_alphabet_order_grouped.append(temp)
        temp = []
#print(text_alphabet_order_grouped)
#hill alqoritmi
#key = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
#text_alphabet_order_grouped = [[20, 1, 13],
#                               [5, 18, 12],
#                               [1, 14, 24]]
hilled_nums = []
tmp = 0
for k in range(len(text_alphabet_order_grouped)):
    for i in range(n):
        for j in range(n):
            tmp += text_alphabet_order_grouped[k][j] * key[j][i]
        hilled_nums.append(tmp % 26)
        tmp = 0
#print(hilled_nums)
#ededleri herfe cevirmek
hilled = ""
for i in hilled_nums:
    hilled += alphabet[i]
print(hilled)