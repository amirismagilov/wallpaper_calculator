def perimetr_calculation(wall_1, wall_2,wall_3, wall_4):
    result = wall_1 + wall_2 + wall_3 + wall_4
    return result

def number_of_columns_calculation(perimetr, wallpaper_column_width):
    result = (perimetr // wallpaper_column_width * 1.15)  # общее необходимое количество столбцов
    return result

def wallpaper_column_in_each_pack_calculation(wallpaper_pack_lenght, wall_height):
    result = wallpaper_pack_lenght // wall_height
    return result

def total_number_of_packs_calculation(number_of_columns, wallpaper_column_in_each_pack):
    result = number_of_columns // wallpaper_column_in_each_pack +1
    return result

