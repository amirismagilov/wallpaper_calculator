room_form_question = input('Комната прямоугольной формы (Да/ Нет): ')
if room_form_question == 'да' or room_form_question == 'Да':
    rooms_width = int(input('Введите ширину комнаты в см: '))
    rooms_lengh =  int(input('Введите длинну комнаты в см: '))
    perimetr = 2*(rooms_lengh + rooms_width)
    print('Периметр комнаты равен ', perimetr, 'см')
elif room_form_question == 'нет' or room_form_question == 'Нет' :
    wall_1 = int(input('Введите длинну стены 1 в см: '))
    wall_2 = int(input('Введите длинну стены 2 в см: '))
    wall_3 = int(input('Введите длинну стены 3 в см: '))
    wall_4 = int(input('Введите длинну стены 4 в см: '))
    perimetr = wall_1 + wall_2 + wall_3 + wall_4
    print('Периметр комнаты равен ', perimetr, 'см')
else:
    print ('Введено не корректное значение. Введите да или нет')

wallpaper_column_width = int(input('Введите ширину рулона в см: '))
if wallpaper_column_width > perimetr:
    print('Введено не верное значение')
    break()

number_of_columns = (perimetr // wallpaper_column_width * 1.15) #общее необходимое количество столбцов

wall_height = int(input('Введите высоту стен в см: '))
wallpaper_pack_lenght = int((input('Введите длинну рулона в см: ')))
wallpaper_column_in_each_pack = wallpaper_pack_lenght // wall_height #количество столбцов в одном рулоне

total_number_of_packs = number_of_columns // wallpaper_column_in_each_pack + 1 #количество рулонов
print('Нужное количество рулонов с запасом - ', total_number_of_packs)