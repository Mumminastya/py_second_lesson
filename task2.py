def run_task2():
    string_user = input("Введите список элементов через пробел: ")
    list_user = string_user.split()
    list_user_index = 0
    print(list_user)
    while list_user_index < len(list_user):
        if list_user_index == len(list_user) - 1:
            break
        x = list_user[list_user_index]
        y = list_user[list_user_index + 1]
        list_user[list_user_index] = y
        list_user[list_user_index + 1] = x
        list_user_index = list_user_index + 2
    print(list_user)

