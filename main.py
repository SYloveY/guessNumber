import random

top_of_range = input('Введите число: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('В следующий раз, вводите число больше 0!')
        quit()
else:
    print('В следующий раз, вводите число!')
    quit()

random_number = random.randint(0, top_of_range)
attempts = 0

while True:
    attempts += 1
    user_number = input('Попробуйте угадать число: ')
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print('В следующий раз, вводите число!')
        continue

    if user_number == random_number:
        print('Вы угадали!')
        break
    elif user_number > random_number:
        print('Ваше число больше')
    else:
        print('Ваше число меньше')

print('Вы угадали с', attempts, 'попытки!')