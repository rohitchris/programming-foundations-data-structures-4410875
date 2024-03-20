def find_second_smallest(my_list):

    set(my_list)
    my_list.sort()

    return f"the second smallest item is {my_list[1]}"



print(find_second_smallest([5, 8, 3, 2, 6, 2, 3, 4, 5]))
