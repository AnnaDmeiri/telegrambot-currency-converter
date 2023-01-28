array = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Введите пожалуйста число!")
    except Exception:
        print("Неверный диапазон!")


print(binary_search(array, element, 0,  len(array)))