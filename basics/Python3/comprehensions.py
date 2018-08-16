seq = range(0,10)
# un comprehension inseamna o expresie urmata de cel putin un for apoi iar if, for etc
print([x**2 for x in seq if x > 5])
# x nu mai exista
# print(x)

# calc the transposed
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# the long way
transposed=[]
row_len=len(matrix[0])
for column_nr in range(0,row_len):
    transposed.append([])
    for row in matrix:
        transposed[column_nr].append(row[column_nr])

print(transposed)
# the compressed way
# forul cel mai din urma e de fapt primul din secventa de mai sus; [] reprezinta o delimitare de lista
transp = [[row[i] for row in matrix] for i in range(4) ]
print(transp)


