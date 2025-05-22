def bubble_sort_swaps(arr):
    a = arr[:]
    swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps

def insertion_sort_swaps(arr):
    a = arr[:]
    swaps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            swaps += 1
        a[j + 1] = key
    return swaps

def compare_swaps_bubble_insertion_sort(arr):
    if len(arr) <= 1:
        return "insertion"
    bubble_swaps = bubble_sort_swaps(arr)
    insertion_swaps = insertion_sort_swaps(arr)
    return "bubble" if bubble_swaps < insertion_swaps else "insertion"

