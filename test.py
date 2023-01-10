from ipm.optimize import linprog as ipm_linprog
from sci.optimize import linprog as sci_linprog
import statistics
import json

def has_huge_difference(solutions):
    if abs(statistics.fmean(solutions[0]-solutions[1])) > 10:
        return True
    
    return False

def has_same_value(solution):
    if len(solution) == 1:
        return False

    for value in solution:
        if value != solution[0]:
            return False

    return True

def read_problems(json_file):
    with open("problems/"+json_file+".json", 'r') as openfile:
        json_object = json.load(openfile)
    problems = json_object["problems"]
    for problem in problems:
        problem["bounds"] = [(0, None) for i in problem["bounds"]]
    return problems

problemsFileName = "problems_01-10-2023_15-28-03"
problems = read_problems(problemsFileName)

sum = 0
count = 0
solutions = []
for i in range(len(problems)):
    problem = problems[i]
    try:
        solutions.append((sci_linprog(
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
        ).x))

        if has_huge_difference(solutions[count]) or has_same_value(solutions[count][1]):
            solutions.pop()
            continue

        sum += abs(statistics.fmean(solutions[count][0]-solutions[count][1]))
        count += 1

        print("iteration: " + str(count) + ", " + str(i), ", average difference between solutions: " + str(sum / count))
    except BaseException as error:
        print(i, error)
        continue