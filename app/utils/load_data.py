import fileinput


def load_flights_to_dict():
    # dict{day = dict{from_city = list{(to_city, price)}}}
    flights_dict = dict()
    destinations = list()
    start_city = None

    print('entering cycle')
    for line in fileinput.input():
        split = line.split()
        if len(split) == 0:
            break
        elif len(split) == 1:
            start_city = split[0]
        else:
            # if there is no dictionary for the day yet, create one
            if split[2] not in flights_dict:
                flights_dict[split[2]] = dict()
            # if there is no dictionary for the departures from this city
            if split[0] not in flights_dict[split[2]]:
                flights_dict[split[2]][split[0]] = list()
            flights_dict[split[2]][split[0]].append((split[1], split[3]))
            if split[1] not in destinations:
                destinations.append(split[1])

    return start_city, flights_dict, destinations
