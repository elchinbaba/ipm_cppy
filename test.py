from ipm.optimize import linprog as ipm_linprog, goal
from sci.optimize import linprog as sci_linprog
import statistics
import json


def has_huge_difference(solutions):
    if abs(statistics.fmean(solutions[0] - solutions[1])) > 10:
        return True

    return False


def read_problems(json_file):
    with open("problems/" + json_file + ".json", 'r') as openfile:
        json_object = json.load(openfile)
    problems = json_object["problems"]
    for problem in problems:
        problem["bounds"] = [(0, None) for i in problem["bounds"]]
    return problems


def test_ordinary_problems(problems_file_name):
    problems = read_problems(problems_file_name)

    sum = 0
    count = 0
    for i in range(len(problems)):
        problem = problems[i]
        try:
            solutions = (
                sci_linprog(
                c=problem["c"],
                A_ub=problem["A_ub"],
                b_ub=problem["b_ub"],
                A_eq=problem["A_eq"],
                b_eq=problem["b_eq"],
                bounds=problem["bounds"],
                method="interior-point"
            ).x,
            ipm_linprog(
                c=problem["c"],
                A_ub=problem["A_ub"],
                b_ub=problem["b_ub"],
                A_eq=problem["A_eq"],
                b_eq=problem["b_eq"],
                bounds=problem["bounds"],
                method="interior-point"
            ).x)

            if has_huge_difference(solutions):
                continue

            sum += abs(statistics.fmean(solutions[0] - solutions[1]))
            count += 1

            print("iteration: " + str(count) + " over " + str(i + 1),
                ", average difference between solutions: " + str(sum / count))
        except BaseException as error:
            print(i, error)
            continue

def test_goal_problems(problems_file_name):
    problems = [
        # {
        #     "A_eq":  [
        #         [0, 0.33, 0.67, 1, 1, 0.5, 0],
        #         [1, 1, 1, 1, 1, 1, 1],
        #         [1.5, 1.83, 2.17, 2.5, 3, 3.5, 4]
        #     ],
        #     "b_eq": [0.5, 1, 2.66]
        # },
        {
            "A_eq":  [
                [0.0, 0.33, 0.67, 1.0, 1.0, 0.5, 0.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [2.0, 2.33, 2.67, 3.0, 4.0, 4.5, 5.0]
            ],
            "b_eq": [0.05, 1.0, 3.37]
        }
    ]

    problems = read_problems(problems_file_name)

    count = 0
    for i in range(len(problems)):
        problem = problems[i]

        A = problem["A_eq"]
        b = problem["b_eq"]

        result = goal(A, b).x
        
        summes = [0 for _ in range(len(b))]
        for j in range(len(b)):
            for k in range(len(result)):
                summes[j] += A[j][k] * result[k]
            if (abs(summes[j] - b[j]) > 0.01):
                count += 1
                # print(i)
                # print(*summes[:j+1])
                # print(*b)
                # print()
                break
        
        print(*summes)
        print(*b)
        print()

        # print([sum[i] - b[i] for i in range(len(b) - len(A[0]))])
        # if abs(sum([[sum([A[o][l]*result[l] for l in range(len(result))]) for o in range(len(A))][k] - b[k] for k in range(len(b))]))/len(b) < 0.1:
        #     count += 1
        
        # print(result)
    
    print(count)

problemsFileName = "problems_goal_01-16-2023_03-38-09"

test_goal_problems(problemsFileName)