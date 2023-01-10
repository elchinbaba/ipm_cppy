import json
from datetime import datetime
import random

problems = [
    {
        "c": [1, 1, 1],
        "A_ub": [[-1, -2, 0], [0, -1, 0], [0, 0, -1], [-1, -1, -2], [-1, 0, 0]],
        "b_ub": [-2, -3, -1, -10, 0],
        "A_eq": [],
        "b_eq": [],
        "bounds": []
    },
    {
        "c": [1, 1, 1],
        "A_ub": [[-1, -2, 0], [-1, -1, -2]],
        "b_ub": [-2, -10],
        "A_eq": [],
        "b_eq": [],
        "bounds": [(0, None), (3, None), (1, None)]
    },
    {
        "c": [1, 2],
        "A_ub": [[-1, 0], [-1, -1]],
        "b_ub": [-2, -3],
        "A_eq": [],
        "b_eq": [],
        "bounds": [(0, None), (0, None)]
    }
]


def generate_problem():
    n = random.randint(2, 5)
    ub = random.randint(1, 2)
    eq = random.randint(0, 1)

    c = [10 * random.random() for i in range(n)]
    A_ub = [[-5 * random.random() for j in range(n)] for i in range(ub)]
    b_ub = [-3 * random.random() for i in range(ub)]
    A_eq = [[3 * random.random() for j in range(n)] for i in range(eq)]
    b_eq = [2 * random.random() for i in range(eq)]
    bounds = [(0, None) for i in range(n)]

    return {
        "c": c,
        "A_ub": A_ub,
        "b_ub": b_ub,
        "A_eq": [],
        "b_eq": [],
        "bounds": bounds
    }


def create_problems():
    probs = []
    for i in range(250):
        probs.append(generate_problem())

    json_object = json.dumps({
        "problems": probs
    }, indent=4)

    with open("problems/problems" + datetime.now().strftime("_%m-%d-%Y_%H-%M-%S") + ".json", "w+") as outfile:
        outfile.write(json_object)


create_problems()
