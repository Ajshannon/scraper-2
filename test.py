import math


def run():
    distance = []
    tuples = [(0, 1), (1, 2), (5, 6), (9, 8)]
    for list in tuples:
        print(list)
        for tuple in list:
            p2 = [tuple[0], tuple[1]]
            distance.append(math.sqrt(((0-p2[0])**2)+((0-p2[1])**2)))
            print(math.sqrt(((0-p2[0])**2)+((0-p2[1])**2)))
