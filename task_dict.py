from utils import true_false,answer_for_user,dictionary

words = {}
answer = {}
count = 0
lvl = ['easy','medium','hard']
user_name = input('Введите свое имя ')
user_level = input("Введите уровень сложности:\nEasy,Medium,Hard:\n ").strip().lower()
if user_level not in lvl:
    print('По умолчанию выбран уровень easy')
    words = dictionary()[0]["questions"][0]['easy']
else:
    if user_level == 'easy':
        words = dictionary()[0]["questions"][0][user_level]
    elif user_level == 'medium':
        words = dictionary()[0]["questions"][1][user_level]
    elif user_level == 'hard':
        words = dictionary()[0]["questions"][2][user_level]


true_false(answer_for_user(words),user_name,user_level)
