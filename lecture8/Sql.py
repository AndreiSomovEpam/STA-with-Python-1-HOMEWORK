from lecture8.TableData import TableData

presidents = TableData('example.sqlite', 'presidents')

print(len(presidents))

print(presidents["Yeltsin"])

print('Yeltsin' in presidents)

for president in presidents:
    print(president[0])
