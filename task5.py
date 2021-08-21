def run_task5():
    rating_list = [9, 7, 5, 3, 1]
    while 1 == 1:
        new_elem_insert_index = 0
        new_elem = int(input("Введите новый элемент рейтинга: "))
        if new_elem in rating_list:
            new_elem_insert_index = rating_list.index(new_elem)
        else:
            while new_elem_insert_index < len(rating_list):
                x = rating_list[new_elem_insert_index]
                if x < new_elem:
                    break
                new_elem_insert_index = new_elem_insert_index + 1
        rating_list.insert(new_elem_insert_index, new_elem)
        print(rating_list)










