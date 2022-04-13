sec = int(input("Напишите, пожалуйста, количество секунд, которые Вы бе хотели преобразовать в часы и минуты: "))
hour = int((sec // 3600))
min = int((sec // 60))


print(hour, "часы", min, "минуты", sec % 60, "секунды")

//
hour = sec // 3600
min = sec // 60 - hour * 60
seconds = sec % 60
print(f"{hour:02}:{min:02}:{seconds:02}")