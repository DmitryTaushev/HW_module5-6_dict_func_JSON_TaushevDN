def true_false(answer,user_name,user_level):
    import json

    with open('questions.json', encoding='utf-8') as file:
        json_data = file.read()
        python_data = json.loads(json_data)

    count_true = 0
    user_data_list = []
    true_list = []
    false_list = []
    true_dict = {}
    false_dict = {}
    result_dict = {}
    level_dict = {}
    for keys in answer:
        if answer[keys] == 'True':
            count_true += 1
            true_list.append(keys)
        else:
            false_list.append(keys)
    if len(true_list) > 0:
        print('Правильно отвечены слова:')
        for i in true_list:
            print(i)
    if len(false_list) > 0:
        print('Неправильно отвечены слова:')
        for i in false_list:
            print(i)
    print(f'Ваш уровень - {python_data[1]['levels'][str(count_true)]}')
    user_data_lvl_1 = f'Уровень {user_name}'
    user_data_lvl_2 = python_data[1]['levels'][str(count_true)]
    user_data_list.append(user_name)
    level_dict['Выбранный уровень'] = user_level
    true_dict['Правильно отвечены слова'] = true_list
    false_dict['Неправильно отвечены слова'] = false_list
    result_dict[user_data_lvl_1] = user_data_lvl_2
    user_data_list.append(level_dict)
    user_data_list.append(true_dict)
    user_data_list.append(false_dict)
    user_data_list.append(result_dict)
    json_data_list = json.dumps(user_data_list, ensure_ascii=False, indent=2)

    with open(f'{user_name}.json', 'w',encoding = 'utf-8') as file:
        file.write(json_data_list)

def answer_for_user(words):
    answer = {}
    count = 0
    for i in range(len(words)):
        user_answer = input(
            f"{list(words.keys())[count]}, {len(words[list(words.keys())[count]])} букв, начинается на {words[list(words.keys())[count]][0]}...").strip().lower()
        if user_answer == words[list(words.keys())[count]]:
            print(f'Верно {list(words.keys())[count]} - это {words[list(words.keys())[count]]}')
            answer[list(words.keys())[count]] = 'True'
        else:
            print(f'Неверно. {list(words.keys())[count]} — это {words[list(words.keys())[count]]}.')
            answer[list(words.keys())[count]] = 'False'
        count += 1

    return answer

def dictionary():
    import json

    with open('questions.json', encoding='utf-8') as file:
        json_data = file.read()
        dict = json.loads(json_data)

    return dict


