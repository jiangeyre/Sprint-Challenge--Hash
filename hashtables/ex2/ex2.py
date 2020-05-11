#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    trip_dict = dict()

    route = list()

    # iteration
    for t in tickets:
        # set source as the key and destination is value for the dict
        trip_dict[t.source] = t.destination

    # set index
    ind = 0

    # initialize curr destination
    curr_destiny = "NONE"

    while ind < length:
        # curr == new source
        curr_destiny = trip_dict.get(curr_destiny)
        # append to ordered list
        route.append(curr_destiny)

        ind += 1

    return route
