from scipy.optimize import linprog as lp

def linprog(c, A_ub, b_ub, A_eq=[], b_eq=[], bounds=[], method=""):
    if len(A_eq) == 0 or len(b_eq) == 0:
        if len(bounds) != 0:
            return lp(c=c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method=method)
        else:
            return lp(c=c, A_ub=A_ub, b_ub=b_ub, method=method)
    elif len(bounds) == 0:
        return lp(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method=method)
    else:
        return lp(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method=method)