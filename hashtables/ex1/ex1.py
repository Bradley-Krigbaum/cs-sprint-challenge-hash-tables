def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    
    weight_dict = {}

    for i in range(length):
        weight_dict[weights[i]] = i
    
    for i in range(length):
        weight_limit = limit - weights[i]
        if weight_limit in weight_dict:
            if weight_dict[weight_limit] > i:
                return weight_dict[weight_limit], i
            else:
                return i, weight_dict[weight_limit]

    return None
