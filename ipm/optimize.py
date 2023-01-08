from ipm.source import optimize

class OptimizeResult:
    def __init__(self, result):
        self.x = result

def linprog(c, A_ub, b_ub, A_eq=[], b_eq=[], bounds=[], method=""):
    if method == 'interior-point':
        for i in range(len(A_ub)):
            for j in range(len(A_ub[i])):
                A_ub[i][j] *= -1
        for i in range(len(b_ub)):
            b_ub[i] *= -1

        for eq in A_eq:
            A_ub.append(eq)
            A_ub.append([-x for x in eq])
        for eq in b_eq:
            b_ub.append(eq)
            b_ub.append(-eq)

        for index, bound in enumerate(bounds):
            if bound[0] is not None:
                A_ub.append([0 if i != index else 1 for i in range(len(c))])
                b_ub.append(bound[0])
            if bound[1] is not None:
                A_ub.append([0 if i != index else -1 for i in range(len(c))])
                b_ub.append(-bound[0])

        return OptimizeResult(optimize.linprog(c, A_ub, b_ub))
    else:
        print("Currently only Interior Point Method is supported.")
        return None