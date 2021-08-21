def run_task4():
    word = input("Введи несколько слов, раздённых пробелами: ")
    word_list = word.split()
    word_list_index = 1

    for word_list_elem in word_list:
        print(f'{word_list_index} - {word_list_elem [0:10]}')
        word_list_index = word_list_index + 1
