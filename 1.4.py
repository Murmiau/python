num = int(input("Введите целое положительное число: "))
num2 = num % 10
num = num // 10
while num > 0:
    if num % 10 > num2:
        num2 = num % 10
    num = num // 10
print("Наибольшая цифра:", num2)
