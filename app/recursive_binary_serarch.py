def binary_search_recursive(target: int, target_list: list) -> bool:
    """Uses a recursive function to search for target in target_list"""
    if len(target_list) < 1:
        return False

    sorted_list = sorted(target_list)
    index = int(len(sorted_list) / 2)
    middle_pivot = sorted_list[index]


    if middle_pivot == target:
        #print(f"target: {target} found")
        return True
    elif middle_pivot > target:
        items_lower = [i for i in sorted_list if i < middle_pivot]
        return binary_search_recursive(target=target, target_list=items_lower)

    elif middle_pivot < target:
        items_upper = [i for i in sorted_list if i > middle_pivot]
        return binary_search_recursive(target=target, target_list=items_upper)







list1 = [1, 2, 3, 4, 5, 6, 7, 9, 10]
result = binary_search_recursive(target=10, target_list= list1)
print(result)
