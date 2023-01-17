from scipy.optimize import linprog

c = [0, 0, 0, 0, 0, 0, 0, 1, 1]

A = [
    [0, 0.33, 0.67, 1, 1, 0.5, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1.5, 1.83, 2.17, 2.5, 3, 3.5, 4, 0, 0]
]

b = [0.5, 1, 2.6]

print(linprog(c=c, A_eq=A, b_eq=b, method='interior-point').x)