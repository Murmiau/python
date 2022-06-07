import itertools
#1
count = 0
for n in itertools.product("7328",repeat=3):
    print(''.join(n))
    count = count + 1
print("Всего вариантов с данными числами:", count)
print()

#2 Комбинации
count = 0
for n in itertools.combinations("5892",2):
    print(''.join(str(x) for x in n))
    count = count + 1
print("Всего комбинаций:", count)
print()

#3 Перестановки
count = 0
for n in itertools.permutations("6281",3):
    print(''.join(str(x) for x in n))
    count = count + 1
print("Всего перестановок:", count)
print()
