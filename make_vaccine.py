from random import choice, shuffle

def drop_n(arr):  #Функция выброса \n
    for i in range(len(arr)):
        tmp = arr[i].split()
        tmp = tmp[0]
        arr[i] = str(tmp)
    return arr


snippets = drop_n(open('peptid_snippets.fasta', 'r+').readlines()[1::2])
epitopes = drop_n(open('epitopes.fasta', 'r+').readlines()[1::2])


num_of_aminoacids = ((len(epitopes) * 9) + (len(epitopes) * 5)) * 2 - 5 #Для лучшего уровня презентации мы решили продублировать эпитопы

RES = list()
for i in range(len(epitopes)): #Заполнение первой части пептида
    RES.append(epitopes[i])
    RES.append(choice(snippets))#Выбираем рандомную вставку.Это можно сделать, так как ни одна связка не перекрывает эпитопы

shuffle(epitopes)#чтобы пептид не получился зеркальным, делаем пермешку эпитопов

for i in range(len(epitopes)):
    RES.append(epitopes[i])
    RES.append(choice(snippets))
RES.pop()

RES  = ''.join(RES)
print(RES)

if len(RES) == num_of_aminoacids:
    print('Расчеты длины пептида оказались верными')
with open('answer.fasta', 'a') as f:
    f.write('>Препарат BLASTёров_из_Москвы\n')
    f.write(RES)
