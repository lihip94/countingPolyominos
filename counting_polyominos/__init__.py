import random


def add_neighbors(item, untried_set, occupied_set):
    old_points = untried_set | occupied_set
    neighbors_set = set()

    if add_left(item, old_points):
        neighbors_set = neighbors_set | add_left(item, old_points)
    if add_right(item, old_points):
        neighbors_set = neighbors_set | add_right(item, old_points)
    if add_up(item, old_points):
        neighbors_set = neighbors_set | add_up(item, old_points)
    if add_down(item, old_points):
        neighbors_set = neighbors_set | add_down(item, old_points)
    return neighbors_set


def add_left(item, old_points):
    if (item[0] > 0 and item[1] >= 0) or (item[0] <= 0 and item[1] >=1):
        new_item = (item[0]-1, item[1])
        if new_item not in old_points:
            return {new_item}


def add_right(item, old_points):
    if (item[0] >= 0 and item[1] >= 0) or (item[0] <= 0 and item[1] >= 1):
        new_item = (item[0] + 1, item[1])
        if new_item not in old_points:
            return {new_item}


def add_up(item, old_points):
    new_item = (item[0], item[1]+1)
    if new_item not in old_points:
        return {new_item}


def add_down(item, old_points):
    if (item[0] >= 0 and item[1] > 0) or (item[0] <= 0 and item[1] > 1):
        new_item = (item[0], item[1]-1)
        if new_item not in old_points:
            return {new_item}


def remove_neighbors(untried_set, new_neighbors):
    for new_neighbor in new_neighbors:
        untried_set.remove(new_neighbor)
    return untried_set


def counting_poly(untried_set, occupied_set, polyomino, n):
    count = 0
    while len(untried_set) != 0:
        random_item = random.choice(tuple(untried_set))
        untried_set.remove(random_item)
        polyomino.append(random_item)
        occupied_set = occupied_set | {random_item}
        count = count + 1
        if len(polyomino) < n:
            new_neighbors = add_neighbors(random_item, untried_set, occupied_set)
            untried_set = untried_set | new_neighbors
            untried_copy = untried_set.copy()
            count = count + counting_poly(untried_copy, occupied_set, polyomino, n)
            untried_set = remove_neighbors(untried_set, new_neighbors)
        polyomino.pop()
    occupied_set.clear()
    return count


def main():
    n = int(input("Enter the max size of the polyomino "))
    print("fixed(n) for n up to specified limit " + str(n))
    print(counting_poly({(0, 0)}, set(), [], n))


if __name__ == '__main__':
  main()


