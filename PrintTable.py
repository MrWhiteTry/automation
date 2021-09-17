def printTable(data):
    # 1st we need to search max width in every column and add it in the list
    colWidths = [0] * len(data)
    t = 0
    for i in data:  # идём во вложенные спсики
        for j in i:  # В них перебираем список по словам
            if len(j) > colWidths[t]:  # если длина слова больше максимальной
                colWidths[t] = len(j)  # перезаписываем
        t += 1
    # print(colWidths)
    # 2nd we need to print our table and align it
    ind_1 = 0  #TODO придумать способ как привязать счётчик к длинне списка, если он не будет известен зараенее
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
