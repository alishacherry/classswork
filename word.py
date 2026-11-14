import random


def play_game():
    words = ["компьютер", "программист", "алгоритм", "питон", "клавиатура"]
    secret_word = random.choice(words)

    guessed_letters = set()   # отгаданные буквы
    wrong_letters = set()     # неверные буквы
    max_attempts = 6
    attempts = 0

    print("=" * 40)
    print("   ИГРА «ОТГАДАЙ СЛОВО»")
    print("=" * 40)
    print(f"Компьютер загадал слово из {len(secret_word)} букв.")
    print(f"У вас {max_attempts} попыток на ошибку.\n")

    while attempts < max_attempts:
        # Показываем слово: отгаданные буквы открыты, остальные — *
        display = " ".join(
            letter if letter in guessed_letters else "*"
            for letter in secret_word
        )
        print(f"Слово: {display}")
        print(f"Ошибки ({attempts}/{max_attempts}): {', '.join(sorted(wrong_letters)) or '—'}")

        # Победа?
        if all(letter in guessed_letters for letter in secret_word):
            print("\nПоздравляем! Вы отгадали слово:", secret_word.upper())
            break

        guess = input("Введите букву: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву (русскую).\n")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("Эту букву вы уже называли.\n")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Буква «{guess}» есть в слове!\n")
        else:
            wrong_letters.add(guess)
            attempts += 1
            print(f"Буквы «{guess}» нет. Осталось попыток: {max_attempts - attempts}\n")

    else:
        print("\nВы проиграли! Загаданное слово:", secret_word.upper())


play_game()