def intersection(arrays):
    # instantiate dict for key value - num and count
    itemcount = dict()
    # initialize array to add the intersections
    result = []

    # iteration over the arr list
    for i, nums in enumerate(arrays):
        # then iterate over the list in the larger list
        for num in nums:
            # if item has a count already and index > 1, we increment the count
            if itemcount.get(num) is not None and i > 0:
                # num becomes the key and increment curr val by one
                itemcount[num] = itemcount[num] + 1
            # if no entry with num in dict set index to one
            elif itemcount.get(num) is None and i == 0:
                itemcount[num] = 1
            else:
                continue

    for numb in itemcount:
        # if number count == array.length()
        if itemcount[numb] == len(arrays):
            # append the number to the intersection list
            result.append(numb)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
