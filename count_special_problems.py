def count_special_problems(n, k, arr):
    special_count = 0
    page = 1

    for problems_in_chapter in arr:
        for problem_num in range(1, problems_in_chapter + 1):
            if problem_num == page:
                special_count += 1
            if problem_num % k == 0 or problem_num == problems_in_chapter:
                page += 1

    return special_count
