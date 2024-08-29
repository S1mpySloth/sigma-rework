def lowest_highest_num(array):
    # empty list
    min_max = []
    # sorts list from lowest to highest value
    sorted_array = sorted(array)
    # assigns lowest and highest value to variables
    lowest_num = sorted_array[0]
    highest_num = sorted_array[-1]
    # extendss empty
    min_max.extend([lowest_num, highest_num])

    return min_max


array = [2, 4, 1, 0, 2, -1]  # change values in list as necessary
result = lowest_highest_num(array)
print(result)
