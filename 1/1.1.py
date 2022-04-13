rating = [8, 6, 4, 4, 1]

while True:
    num = int(input("Введите, пожалуйста, целое положительное число, для завершения програмы напишите 0: "))
    if num > 0:
        for i in rating:
            if i > num:
                print(rating.insert(i, num))
            elif i == i + 1 > num:
                print(rating.insert(i + 1, num))
    elif num == 0:
        rating.pop(0)
        break
    else:
        print("Попробуйте еще раз")