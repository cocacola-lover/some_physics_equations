import checks
import dealing_with_nonuniformity as nonU
from sympy import *
from sympy.core.expr import Expr;

def solveLinearCombinationDirichlet (expression : Expr, a : int, nonuniformity : Expr = None) :
    t, x = symbols('t x')

    additional = Number(0) if (nonuniformity == None) else nonU.calculatePartialSolution(     \
        *nonU.devideIntoTwo(                 \
        nonuniformity   \
    ), a)

    expression = expression + additional.subs(t, 0)

    ans = Number(0)

    if (expression.func.is_Mul or expression.func == sin or expression.func == cos or expression.func == sin or expression.func == cos) : expression = Add(0, expression, evaluate=False);
    elif (not expression.func.is_Add) : raise Exception('Failed to solve linear Combination')

    logger = []

    for component in expression.args :
        if (component.is_zero) : continue

        coef, n = checks.correctForm(component)

        logger.append(f'c{len(logger)} * {exp(-a**2 * n**2 * t) * sin(n * x)}')

        ans = ans + coef * exp(-a**2 * n**2 * t) * sin(n * x)

    print(f'Our base : {" + ".join(logger)}\n' )

    return ans - additional

def solveLinearCombinationNeiman (expression : Expr, a : int, nonuniformity : Expr = None) :
    t, x = symbols('t x')

    additional = Number(0) if (nonuniformity == None) else nonU.calculatePartialSolution(     \
        *nonU.devideIntoTwo(                 \
        nonuniformity   \
    ), a)

    expression = expression + additional.subs(t, 0)

    ans = Number(0)

    if (expression.func.is_Mul or expression.func == sin or expression.func == cos) : expression = Add(0, expression, evaluate=False);
    elif (not expression.func.is_Add) : raise Exception('Failed to solve linear Combination')

    logger = []

    for component in expression.args :
        if (component.is_zero) : continue

        coef, n = checks.correctForm(component)

        logger.append(f'c{len(logger)} * {exp(-a**2 * n**2 * t) * cos(n * x)}')

        ans = ans + coef * exp(-a**2 * n**2 * t) * cos(n * x)

    print(f'Our base : {" + ".join(logger)}\n' )

    return ans - additional





if (__name__ == '__main__') : 
    print(solveLinearCombinationDirichlet(  \
        sympify('5 * sin(3 * pi * x / 2)'),           \
        3, sympify('2*cos(t) * sin(pi * x)')))