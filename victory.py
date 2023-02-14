answer = None

while answer != 'Нет':
    correct_answers = 0

# Год рождения Пушкина 1799
    answer = input("Год рождения А.С. Пушкина")
    if answer == "1799":
        correct_answers += 1

# Год рождения Тургенева 1818
    answer = input("Год рождения И.С. Тургенева")
    if answer == "1818":
        correct_answers += 1

# Год рождения Лермонтова 1814
    answer = input("Год рождения М.Ю. Лермонтова")
    if answer == "1814":
        correct_answers += 1

# Год рождения Толстого 1828
    answer = input("Год рождения Л.Н. Толстого")
    if answer == "1828":
        correct_answers += 1

# Год рождения Есенина 1895
    answer = input("Год рождения С.А. Есенина")
    if answer == "1895":
        correct_answers += 1

    wrong_answers = 5 - correct_answers
    percent_correct_answers = (correct_answers * 100) / 5
    percent_wrong_answers = (wrong_answers * 100) / 5

# Выводим результаты: количество правильных ответов, количество ошибок,  процент правильных ответов, процент неправильных ответов
    print('Правильных ответов:', correct_answers)
    print('Неправильных ответов:', wrong_answers)
    print('Процент правильных ответов:', percent_correct_answers)
    print('Процент неправильных ответов:', percent_wrong_answers)

# Предлагаем пройти викторину повторно. Да - запускаем сначала. Нет - выходим
    answer = input('Хотите ещё пройти викторину? (Да/Нет)')
    if answer == 'Нет':
        break

print('Спасибо за прохождение нашей викторины')
