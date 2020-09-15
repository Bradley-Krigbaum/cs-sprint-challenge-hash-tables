def value_in_dict(value, dicts):
    for dict in dicts:
        if value not in dict:
            return False
    return True


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # result = list(reduce(lambda i, j: i & j, (set(x) for x in arrays)))
    unique_dict = []

    for array in arrays:
        uninque_values = {}

        for value in array:
            uninque_values[value] = True

        unique_dict.append(uninque_values)

    last_dict = unique_dict[-1]
    result = []

    for value in last_dict:
        if value_in_dict(value, unique_dict[:-1]):
            result.append(value)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
