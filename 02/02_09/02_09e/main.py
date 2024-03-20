def find_second_smallest(my_list):
    if len(my_list)<2:
        return f"your list only has 1 value {my_list}"

    smallest = float('inf')
    ssmallest = float('inf')

    for i, num in enumerate(my_list):
        if num<smallest:
            # DEBUG
            # print(f"@idx{i} LOOP1=>num={num} and smallest={smallest} and ssmallest={ssmallest}")
            ssmallest = smallest
            smallest = num
        elif num<ssmallest and num!=smallest:
            # DEBUG
            # print(f"@idx{i} LOOP2=>num={num} and smallest={smallest} and ssmallest={ssmallest}")
            ssmallest = num

    return f"the second smallest item is {ssmallest}"

# print(find_second_smallest([5]))
# print(find_second_smallest([5, 8, 3, 2, 6]))
# print(find_second_smallest([5, 8, 3, 2, 6, 5, 8, 3, 2, 6]))
print(find_second_smallest([5, 8, 3, 2, 6, 2, 1, 2, 1, 3, 4, 1, 2, 3]))
