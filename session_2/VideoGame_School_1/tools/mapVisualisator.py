import json

with open("room1.json", "r") as f:
    data = json.load(f)

size = data["size"] + 1


def print_map(size, walls):
    for y in range(size):
        for x in range(size):
            wall_found = False
            for wall in walls:
                if (x, y) == tuple(wall["0"].values()) or (x, y) == tuple(wall["1"].values()):
                    print("O", end=" ")
                    wall_found = True
                    break
            if not wall_found:
                print(" ", end=" ")
        print("")


print_map(size, data["walls"].values())
