
def cocktail_sort(array: list[int]) -> None:
    n = len(array)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True


        start += 1


if __name__ == "__main__":
    import random

    # Create a list with random numbers
    my_list = [random.randint(0, 100) for _ in range(20)]
    print("Unsorted list:", my_list)
    cocktail_sort(my_list)
    print("Sorted list:", my_list)
