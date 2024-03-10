from typing import List, Tuple, Iterator


def num_iterator(phone_number: str, max_key_size=3) -> Iterator[int]:
    phone_number = phone_number[:1:-1].split("-")

    # итерируемся по номеру
    for n in phone_number[0]:
        yield int(n)

    # итерируемся по городу
    for i, n in enumerate(phone_number[1]):
        yield int(n)
    # лидируещие нули
    for _ in range(i, max_key_size):
        yield 0

    # итерируемся по стране
    for i, n in enumerate(phone_number[2]):
        yield int(n)
    # лидируещие нули
    for _ in range(i, max_key_size):
        yield 0


def counting_sort(arr: List[Tuple[Iterator[int], str]]) -> bool:
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # сохраним индексы, потому что необходимо дважды
    # обращаться к объекту из итератора
    indexes_cached = []
    for i in range(n):
        index = next(arr[i][0], None)
        if index is None:
            return True  # sorted
        indexes_cached.append(index)
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n-1, -1, -1):
        index = indexes_cached[i]
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    return False


def radix_sort_phone_numbers(
    arr: List[Tuple[str, str]]
) -> List[Tuple[str, str]]:
    if len(arr) == 0:
        return arr

    arr = [(num_iterator(a[0]), a) for a in arr]
    sort_complete = False
    while not sort_complete:
        # выполняем каунт сорт, потому что она идеально подходит для задачи
        sort_complete = counting_sort(arr)

    return [a[1] for a in arr]
