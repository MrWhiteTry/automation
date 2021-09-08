def printTable(data):
    colWidths = [0] * len(data)
    t = 0
    for i in data:  # идём во вложенные спсики
        for j in i:  # В них перебираем список по словам
            if len(j) > colWidths[t]:  # если длина слова больше максимальной
                colWidths[t] = len(j)  # перезаписываем
        t += 1
    # print(colWidths)
    ind_1 = 0
    while ind_1 < 4:
        ind_2 = 0
        emptyList = ''
        while ind_2 < 3:
            emptyList = emptyList + ' ' + str(data[ind_2][ind_1].rjust(colWidths[ind_2]))
            ind_2 += 1
        print(emptyList)
        ind_1 += 1


tableDate = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alise', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableDate)
