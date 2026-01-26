def unique_pair_sum(numbers: list[int], target: int) -> set[tuple[int, int]]:
    seen = set()
    pairs = set()

    for x in numbers:
        y = target - x
        if y in seen:
            a, b = (x, y) if x <= y else (y, x)
            pairs.add((a, b))
        seen.add(x)

    return pairs


# exemplu
numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))
