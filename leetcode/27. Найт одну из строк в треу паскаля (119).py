def getRow(rowIndex):
#комбинаторика -=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=
    # row = [1]
    #
    # for k in range(rowIndex):
    #     row.append(row[-1] * (rowIndex - k) // (k + 1))
    #
    # return row
#второй способ -=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=
    res = [1]

    for i in range(rowIndex):
        next_row = [0] * (len(res) + 1)
        for j in range(len(res)):
            next_row[j] += res[j]
            next_row[j + 1] += res[j]
        res = next_row

    return res

