from ipm.optimize import linprog as ipm_linprog
from sci.optimize import linprog as sci_linprog
import statistics
import json


def has_huge_difference(solutions):
    if abs(statistics.fmean(solutions[0] - solutions[1])) > 10:
        return True

    return False


def has_same_value(sol):
    if len(sol) == 1:
        return False

    for value in sol:
        if value != sol[0]:
            return False

    return True


def read_problems(json_file):
    with open("problems/" + json_file + ".json", 'r') as openfile:
        json_object = json.load(openfile)
    problems = json_object["problems"]
    for problem in problems:
        problem["bounds"] = [(0, None) for i in problem["bounds"]]
    return problems


problemsFileName = "problems_01-10-2023_16-59-43"
problems = read_problems(problemsFileName)

sum = 0
count = 0
for i in range(len(problems)):
    problem = problems[i]
    try:
        solution = (sci_linprog(
            c=problem["c"],
            A_ub=problem["A_ub"],
            b_ub=problem["b_ub"],
            A_eq=problem["A_eq"],
            b_eq=problem["b_eq"],
            bounds=problem["bounds"],
            method="interior-point"
        ).x, ipm_linprog(
            c=problem["c"],
            A_ub=problem["A_ub"],
            b_ub=problem["b_ub"],
            A_eq=problem["A_eq"],
            b_eq=problem["b_eq"],
            bounds=problem["bounds"],
            method="interior-point"
        ).x)

        if has_huge_difference(solution) or has_same_value(solution[1]):
            continue

        sum += abs(statistics.fmean(solution[0] - solution[1]))
        count += 1

        print("iteration: " + str(count) + " over " + str(i + 1),
              ", average difference between solutions: " + str(sum / count))
    except BaseException as error:
        print(i, error)
        continue
