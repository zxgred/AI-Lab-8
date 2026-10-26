
warehouse = {
    "Receiving": {
        "Aisle1": 40,
        "Aisle2": 70
    },
    "Aisle1": {
        "Aisle2": 30,
        "Packing Station": 90
    },
    "Aisle2": {
        "Packing Station": 35
    },
    "Packing Station": {}
}

heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}


def a_star(start, goal):
    frontier = [(heuristic[start], start, [start], 0)]
    visited = []

    while frontier:
        frontier.sort()
        f, current, path, cost = frontier.pop(0)

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            print("Path found by A*:", path)
            print("Total cost of this path:", cost)
            return

        for neighbor, distance in warehouse[current].items():
            if neighbor not in visited:
                new_cost = cost + distance
                new_f = new_cost + heuristic[neighbor]

                frontier.append((
                    new_f,
                    neighbor,
                    path + [neighbor],
                    new_cost
                ))

    print("No path found")


a_star("Receiving", "Packing Station")
