def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    negative_values = {}

    for x in a:
        negative_values[x] = -x
    
    result = []

    for x in negative_values.keys():
        if x > 0 and negative_values[x] in negative_values:
            result.append(x)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
