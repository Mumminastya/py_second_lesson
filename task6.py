def run_task6():
    result = tuple()
    while 1 == 1:
        prod_num = (input("Введите номер товара: "))
        prod_name = (input("Введите название товара: "))
        prod_price = (input("Введите цену товара: "))
        result = result + (prod_num, {'название': prod_name, 'цена': prod_price})
        quest = input("Хотите ещё? (Д/Н): ")
        if quest == "Н":
            break
    print(result)










