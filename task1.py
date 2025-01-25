import random
import timeit

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Порівняння алгоритмів
def compare_algorithms():
    sizes = [100, 1000, 5000, 10000]  # Розміри масивів
    results = {}

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        random_array = [random.randint(1, 10000) for _ in range(size)]
        results[size] = {}

        # Копії масиву для різних алгоритмів
        array_for_insertion = random_array[:]
        array_for_merge = random_array[:]
        array_for_sorted = random_array[:]

        # Вимір часу для сортування вставками
        time_insertion = timeit.timeit(lambda: insertion_sort(array_for_insertion), number=1)
        print(f"Сортування вставками: {time_insertion:.6f} секунд")
        results[size]["insertion_sort"] = time_insertion

        # Вимір часу для сортування злиттям
        time_merge = timeit.timeit(lambda: merge_sort(array_for_merge), number=1)
        print(f"Сортування злиттям: {time_merge:.6f} секунд")
        results[size]["merge_sort"] = time_merge

        # Вимір часу для Timsort
        time_sorted = timeit.timeit(lambda: sorted(array_for_sorted), number=1)
        print(f"Timsort (вбудоване): {time_sorted:.6f} секунд")
        results[size]["timsort"] = time_sorted

    return results

# Головна функція
if __name__ == "__main__":
    results = compare_algorithms()

    # Висновки
    print("\nВисновки:")
    for size, times in results.items():
        print(f"\nРозмір масиву: {size}")
        print(f"Сортування вставками: {times['insertion_sort']:.6f} секунд")
        print(f"Сортування злиттям: {times['merge_sort']:.6f} секунд")
        print(f"Timsort (вбудоване): {times['timsort']:.6f} секунд")