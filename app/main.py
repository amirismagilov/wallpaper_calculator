from app.lib import *
room_form_question = input('Комната прямоугольной формы (Да/ Нет): ')
if room_form_question == 'да' or room_form_question == 'Да':
    wall_1 = wall_2 = int(input('Введите ширину комнаты в см: '))
    wall_3 = wall_4 =  int(input('Введите длинну комнаты в см: '))
    perimetr = perimetr_calculation(wall_1_input, wall_2_input, wall_3_input, wall_4_input)
    print('Периметр комнаты равен ', perimetr)

elif room_form_question == 'нет' or room_form_question == 'Нет' :
    wall_1 = int(input('Введите длинну стены 1 в см: '))
    wall_2 = int(input('Введите длинну стены 2 в см: '))
    wall_3 = int(input('Введите длинну стены 3 в см: '))
    wall_4 = int(input('Введите длинну стены 4 в см: '))
    perimetr = perimetr_calculation(wall_1, wall_2, wall_3, wall_4)
    print('Периметр комнаты равен ', perimetr)
else:
    print ('Введено не корректное значение. Введите да или нет')
# wall_1 = 100
# wall_2 = 200
# wall_3 = 300
# wall_4 = 400
# perimentr = perimetr_calculation(wall_4, wall_3, wall_2, wall_1)
# print(perimentr)

wallpaper_column_width = int(input('Введите ширину рулона в см: '))
number_of_columns = number_of_columns_calculation(perimetr, wallpaper_column_width)

wall_height = int(input('Введите высоту стен в см: '))
wallpaper_pack_lenght = int((input('Введите длинну рулона в см: ')))
wallpaper_column_in_each_pack = wallpaper_column_in_each_pack_calculation(wallpaper_pack_lenght, wall_height) #количество столбцов в одном рулоне

total_number_of_packs = total_number_of_packs_calculation(number_of_columns, wallpaper_column_in_each_pack) #количество рулонов
print("Нужное количество рулонов с запасом - ", total_number_of_packs)


