#На заводе «Кофейный» открывается новое кафе.

ingredient = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}

def choose_coffee(preferences):
    res = []
    for i in preferences:
        if ingredient[i][0] <= ingredients[0] and ingredient[i][1] <= ingredients[1] and ingredient[i][2] <= ingredients[2]:
            ingredients[0] -= ingredient[i][0]
            ingredients[1] -= ingredient[i][1]
            ingredients[2] -= ingredient[i][2]
            res.append(i)
    if len(res) == len(preferences): return res
    else: return ['К сожалению, не можем предложить Вам напиток']

#ингридиенты
ingredients = []
ingredients.append(int(input('Сколько у нас порций кофейныз зерен: '))) 
ingredients.append(int(input('Сколько у нас порций молока: ')))
ingredients.append(int(input('Сколько у нас порций взбитых сливок: ')))
print('')

#меню
print('Меню:','1. Эспрессо.','2. Капучино.','3. Маккиато','4. Кофе по-венски.','5. Латте Маккиато.', '6. Кон Панна','', sep='\n')

#заказ
order = []
a = input('Введите номера заказа из меню:').split()
for i in a:
    if i=='1': order.append('Эспрессо')
    elif i=='2': order.append('Капучино')
    elif i=='3': order.append('Маккиато')
    elif i=='4': order.append('Кофе по-венски')
    elif i=='5': order.append('Латте Маккиато')
    elif i=='6': order.append('Кон Панна')
print('')   

#исполнение
print('Ответ: ')
print(*choose_coffee(order),sep=', ')