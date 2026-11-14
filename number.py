import random

guess = random.randint(1,100)
attempt = 0
cnt = 0

print("Загадано число от 1 до 100")

while attempt != guess:
    attempt = int(input("Ваша попытка: "))
    cnt += 1

    if cnt > 10:
        print("Вы проиграли")
        break

    if attempt < guess:
        print("Больше!!!")
    elif attempt > guess:
        print("Меньше!")
    else:
        print(f"Угадано за {cnt} попытки/ок!!")