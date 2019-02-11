def perimetr_calculation(wall_1, wall_2,wall_3, wall_4):
    """
    >>> perimetr_calculation(120, 200,300, 130)
    750
    """
    result = wall_1 + wall_2 + wall_3 + wall_4
    return result

def number_of_columns_calculation(perimetr, wallpaper_column_width):
    """
    >>> number_of_columns_calculation(750, 25)
    34
    """
    result = round((perimetr // wallpaper_column_width * 1.15))  # общее необходимое количество столбцов
    return result

def wallpaper_column_in_each_pack_calculation(wallpaper_pack_lenght, wall_height):
    """
    >>> wallpaper_column_in_each_pack_calculation(200, 21)
    9
    """
    result = wallpaper_pack_lenght // wall_height
    return result

def total_number_of_packs_calculation(number_of_columns, wallpaper_column_in_each_pack):
    """
    >>> total_number_of_packs_calculation(35, 8)
    5
    """
    result = number_of_columns // wallpaper_column_in_each_pack +1
    return result

