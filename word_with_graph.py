def draw_graph(secret_word, revealed, tried_letters):
    print()
    print("┌" + "─" * 46 + "┐")

    # Строка с буквами (открытые — буква, закрытые — *)
    top = "  "
    for i, letter in enumerate(secret_word):
        top += (letter.upper() if i in revealed else "*") + "   "
    print("│ " + top.ljust(44) + " │")

    # Соединительные линии
    mid = "  "
    for _ in range(len(secret_word) - 1):
        mid += "─── "
    mid += "   "
    print("│ " + mid.ljust(44) + " │")

    # Номера позиций
    bot = "  "
    for i in range(len(secret_word)):
        bot += f"{i+1:<3} "
    print("│ " + bot.ljust(44) + " │")

    print("├" + "─" * 46 + "┤")

    status = f"Названо букв: {', '.join(sorted(tried_letters)) or '—'}"
    print("│ " + status.ljust(44) + " │")
    print("└" + "─" * 46 + "┘")


#  ИГРА: ЧЕЛОВЕК ЗАГАДЫВАЕТ СЛОВО  — КОМПЬЮТЕР ОТГАДЫВАЕТ

WORDS = ["компьютер", "программист", "алгоритм", "питон",
         "клавиатура", "монитор", "процессор", "интернет",
         "информатика", "робот"]


def play_reverse():
    print("=" * 50)
    print("   ИГРА: ВЫ ЗАГАДЫВАЕТЕ СЛОВО — КОМПЬЮТЕР ОТГАДЫВАЕТ")
    print("=" * 50)

    # Человек загадывает слово (из списка, чтобы компьютер мог отгадать)
    while True:
        secret = input("Загадайте слово (из списка ниже) и нажмите Enter:\n"
                       + ", ".join(WORDS) + "\n> ").strip().lower()
        if secret in WORDS:
            break
        print("Такого слова нет в списке. Попробуйте снова.\n")

    candidates = WORDS.copy()
    revealed = set()          # индексы открытых позиций
    tried_letters = set()     # названные буквы (и верные, и нет)
    wrong_letters = set()     # неверные буквы
    max_attempts = 6
    attempts = 0

    print(f"\nКомпьютер будет отгадывать слово из {len(secret)} букв.")
    print(f"У него {max_attempts} попыток на ошибку.\n")

    while attempts < max_attempts:
        # Показываем граф
        draw_graph(secret, revealed, tried_letters)

        # Проверка победы
        if len(revealed) == len(secret):
            print("\nКомпьютер отгадал слово:", secret.upper())
            return

        # Выбор буквы компьютером:
        # считаем частоту букв в пуле кандидатов на ещё закрытых позициях
        freq = {}
        for word in candidates:
            for i, letter in enumerate(word):
                if i not in revealed and letter not in tried_letters:
                    freq[letter] = freq.get(letter, 0) + 1

        if not freq:
            print("\nКомпьютер не смог найти подходящую букву. Слово:", secret.upper())
            return

        # Берём самую частую букву
        guess = max(freq, key=freq.get)
        tried_letters.add(guess)

        print(f"\nКомпьютер предлагает букву: «{guess}»")

        # Человек отвечает, есть ли буква в слове
        while True:
            answer = input("Есть ли эта буква в слове? (д/н): ").strip().lower()
            if answer in ("д", "да", "y", "yes"):
                has_letter = True
                break
            elif answer in ("н", "нет", "n", "no"):
                has_letter = False
                break
            else:
                print("Введите «д» или «н».")

        if has_letter:
            # Открываем все позиции с этой буквой
            for i, letter in enumerate(secret):
                if letter == guess:
                    revealed.add(i)
            print(f"Буква «{guess}» открыта!")
        else:
            wrong_letters.add(guess)
            attempts += 1
            print(f"Буквы «{guess}» нет. Осталось попыток: {max_attempts - attempts}")

        # Отсеиваем кандидатов, не подходящих под ответ
        new_candidates = []
        for word in candidates:
            # Должен совпадать по уже открытым позициям
            if any(word[i] != secret[i] for i in revealed):
                continue
            # Буква guess должна быть/не быть в слове
            if has_letter and guess not in word:
                continue
            if not has_letter and guess in word:
                continue
            # Названные неверные буквы не должны встречаться
            if any(letter in word for letter in wrong_letters):
                continue
            new_candidates.append(word)
        candidates = new_candidates

    # Проигрыш компьютера
    draw_graph(secret, revealed, tried_letters)
    print("\nКомпьютер проиграл! Загаданное слово:", secret.upper())

play_reverse()