def get_indices_of_item_weights(weights, length, limit):
    # create a dictionary of the weights
    w_dict = dict()

    # iterate over the list
    for i in range(length):
        # if a k:v pair is in the dictionary and == the remainder minus the curr el from limit
        x = w_dict.get(limit - weights[i])
        # if value found at index in the dict

        if x is not None:
            # return tuple with corresponding indices
            return (i, x)

        else:
            # !found, then set key as the curr val from list and val as the found index
            w_dict[weights[i]] = i

    print(w_dict)

    # for when the sum of the num in the list != limit, return none
    return None
