def cook_book():
    with open('блюда.txt') as file:
        cook_books = {}
        for line in file:
            dish_name = line.strip()
            dishes_count = int(file.readline())
            dishes = []
            for _ in range(dishes_count):
                dish = file.readline().strip()
                ingredient_name, quantity, measure = dish.split(' | ')
                dishes.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': quantity,
                     'measure': measure}
                    )
            cook_books[dish_name] = dishes
            file.readline()
        return cook_books


def get_shop_list_by_dishes(disheses, person_count):
    final = {}
    if isinstance(disheses, list):
        for el_dish in disheses:
            if el_dish in cook_book():
                for value in cook_book()[el_dish]:
                    if value['ingredient_name'] in final:
                        for i, k in final.items():
                            if value['ingredient_name'] == i:
                                k['quantity'] += (int(value['quantity']) * person_count)
                    else:
                        final.update({value['ingredient_name']: {'measure': value['measure'], 'quantity': (
                                            int(value['quantity']) * person_count)}})
            else:
                print(f'Блюда "{el_dish}" нет в списке')
    else:
        return print('Меня научили работать толлько со списком!')
    return print(final)


order = ['Буритос', 'Фахитос']

get_shop_list_by_dishes(order, 1)
