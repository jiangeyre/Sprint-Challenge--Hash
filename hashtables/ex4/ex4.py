def has_negatives(a):
    # create dict for numbers and a result array
    numb_dict = {}
    result = []

    # iterate over each num in list
    for num in a:
        # if the number is not in dict
        if num not in numb_dict:
            if num > 0:
                # add the number to the dict
                numb_dict[num] = num
            
            elif num < 0:
                # add number to the dict negative
                numb_dict[-num] = num
        # if the num has corresponding number in the dict
        if num > 0:
            # if number is greater than 8 and if the negative number is in the dict add to the result array
            if -num in numb_dict:
                result.append(num)
            
        if num < 0:
            # if the number in the dict and less than zero, we check for the positive and cancel out the negative number
            if -num in numb_dict:
                result.append(-num)

    # return result array
    # print(numb_dict)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
