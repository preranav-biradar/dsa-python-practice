# Problem:Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 25, 12, 22, 11]))

# Problem: Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    more = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)

print(quick_sort([10, 7, 8, 9, 1, 5]))