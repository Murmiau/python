wor1a = input("Введите, пожалуйста, название товара: ")
wor1b = int(input("Введите, пожалуйста, цену товара: "))
wor1c = int(input("Введите, пожалуйста, количество товара: "))
wor2a = input("Введите, пожалуйста, название товара: ")
wor2b = int(input("Введите, пожалуйста, цену товара: "))
wor2c = int(input("Введите, пожалуйста, количество товара: "))
wor3a = input("Введите, пожалуйста, название товара: ")
wor3b = int(input("Введите, пожалуйста, цену товара: "))
wor3c = int(input("Введите, пожалуйста, количество товара: "))

my_dict1 = {"название": wor1a, "цена": wor1b, "количество": wor1c, "ед": "шт."}
my_dict2 = {"название": wor2a, "цена": wor2b, "количество": wor2c, "ед": "шт."}
my_dict3 = {"название": wor3a, "цена": wor3b, "количество": wor3c, "ед": "шт."}

tup = tuple = ({"название": wor1a, "цена": wor1b, "количество": wor1c, "ед": "шт."},
         {"название": wor2a, "цена": wor2b, "количество": wor2c, "ед": "шт."},
         {"название": wor3a, "цена": wor3b, "количество": wor3c, "ед": "шт."})

print(enumerate(tup))