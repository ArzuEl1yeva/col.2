def find_common_strings_with_least_index_sum(list1, list2):
    index_map = {s: i for i, s in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for j, s in enumerate(list2):
        if s in index_map:
            total_index = index_map[s] + j
            if total_index < min_sum:
                min_sum = total_index
                result = [s]
            elif total_index == min_sum:
                result.append(s)
    return result

