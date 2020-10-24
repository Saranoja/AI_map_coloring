X1 = ['WA', 'SA', 'NT']
D1 = [{'R', 'G', 'B'}, {'R', 'G'}, {'G'}]
adjacency_dict1 = {
    'WA': {'SA', 'NT'},
    'SA': {'WA', 'NT'},
    'NT': {'WA', 'SA'},
}
# C = [('WA', 'SA'), ('SA', 'WA'), ('WA', 'NT'), ('NT', 'WA'), ('SA', 'NT'), ('NT', 'SA')]

X2 = ['T', 'WA', 'SA', 'NT', 'Q', 'NSW', 'V']
D2 = [{'R', 'B', 'G'}, {'R'}, {'R', 'B', 'G'}, {'R', 'B', 'G'}, {'G'}, {'R', 'B', 'G'}, {'R', 'B', 'G'}]
adjacency_dict2 = {
    'T': {'V'},
    'WA': {'NT', 'SA'},
    'NT': {'WA', 'Q', 'SA'},
    'SA': {'WA', 'NT', 'Q', 'NSW', 'V'},
    'Q': {'NT', 'SA', 'NSW'},
    'NSW': {'Q', 'SA', 'V'},
    'V': {'SA', 'NSW', 'T'}
}
# C = [('T', 'V'), ('WA', 'NT'), ('WA', 'SA'), ('NT', 'Q'), ('NT', 'SA'), ('NT', 'WA'), ('SA', 'V'), ('SA', 'WA'),
# ('SA', 'Q'), ('SA', 'NT'), ('SA', 'NSW'), ('Q', 'NT'), ('Q', 'NSW'), ('Q', 'SA'), ('NSW', 'Q'), ('NSW', 'SA'),
# ('NSW', 'V'), ('V', 'NSW'), ('V', 'SA'), ('V', 'T')]

X = X1
D = D1
adjacency_dict = adjacency_dict1


def get_constraint_queue(d):
    C = []
    for node, l in d.items():
        for neighbour in l:
            C.append((node, neighbour))
    return C


def revise(i, j):
    Di = D[i]
    Dj = D[j]

    revised = False
    for elem1 in Di.copy():
        satisfies = False
        for elem2 in Dj:
            if elem1 != elem2:
                satisfies = True
        if not satisfies:
            Di.remove(elem1)
            revised = True

    return revised


def arc_consistency(X, D, queue: list):
    while queue:
        Xi, Xj = queue.pop()
        i, j = X.index(Xi), X.index(Xj)
        if revise(i, j):
            if not D[i]:
                return False

            neighbours = adjacency_dict[Xi].copy()
            neighbours.remove(Xj)
            for neighbour in neighbours:
                queue.insert(0, (neighbour, Xi))

    return True


if arc_consistency(X, D, get_constraint_queue(adjacency_dict)):
    print(f'Solution found: {D}')
else:
    print('No solution found.')
