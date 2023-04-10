import checks
import dealing_with_nonuniformity as nonU
from sympy import *
from sympy.core.expr import Expr;

def solveLinearCombinationDirichlet (expression1 : Expr, expression2 : Expr, a : int, nonuniformity : Expr = None) :
    t, x = symbols('t x')

    additional = Number(0) if (nonuniformity == None) else nonU.calculatePartialSolution(     \
        *nonU.devideIntoTwo(                 \
        nonuniformity   \
    ), a)

    expression1 = expression1 + additional.subs(t, 0)

    ans = Number(0)

    # For phi0
    if (expression1.func.is_Mul or expression1.func == sin or expression1.func == cos) : expression1 = Add(0, expression1, evaluate=False);
    elif (not expression1.func.is_Add) : raise Exception('Failed to solve linear Combination')

    logger1 = []

    for component in expression1.args :
        if (component.is_zero) : continue

        coef, n = checks.correctForm(component)

        logger1.append(f'c{len(logger1)} * {cos(a * n * t) * sin(n * x)}')

        ans = ans + coef * cos(a * n * t) * sin(n * x)

    print(f'Base from the first condition : {" + ".join(logger1)}' )

    # For phi1
    if (expression2.func.is_Mul or expression2.func == sin or expression2.func == cos) : expression2 = Add(0, expression2, evaluate=False);
    elif (not expression2.func.is_Add) : raise Exception('Failed to solve linear Combination')

    logger2 = []

    for component in expression2.args :
        if (component.is_zero) : continue

        coef, n = checks.correctForm(component)

        logger2.append(f'c{len(logger1) + len(logger2)} * {sin(a * n * t) * sin(n * x)}')

        ans = ans + coef * sin(a * n * t) * sin(n * x)

    print(f'Base from the second condition : {" + ".join(logger2)}\n' )

    return ans - additional



def solveLinearCombinationNeiman (expression1 : Expr, expression2 : Expr, a : int, nonuniformity : Expr = None) :
    t, x = symbols('t x')

    additional = Number(0) if (nonuniformity == None) else nonU.calculatePartialSolution(     \
        *nonU.devideIntoTwo(                 \
        nonuniformity   \
    ), a)

    expression1 = expression1 + additional.subs(t, 0)

    ans = Number(0)

    # For phi0
    if (expression1.func.is_Mul or expression1.func == sin or expression1.func == cos) : expression1 = Add(0, expression1, evaluate=False);
    elif (not expression1.func.is_Add) : raise Exception('Failed to solve linear Combination')

    logger1 = []

    for component in expression1.args :
        if (component.is_zero) : continue

        coef, n = checks.correctForm(component)

        logger1.append(f'c{len(logger1)} * {cos(a * n * t) * cos(n * x)}')

        ans = ans + coef * cos(a * n * t) * cos(n * x)

    print(f'Base from the first condition : {" + ".join(logger1)}' )

    # For phi1
    if (expression2.func.is_Mul or expression2.func == sin or expression2.func == cos) : expression2 = Add(0, expression2, evaluate=False);
    elif (not expression2.func.is_Add) : raise Exception('Failed to solve linear Combination')

    logger2 = []

    for component in expression2.args :
        if (component.is_zero) : continue

        coef, n = checks.correctForm(component)

        if ( n != 0 ) : logger2.append(f'c{len(logger1) + len(logger2)} * {sin(a * n * t) * cos(n * x)}')
        else : logger2.append(f'c{len(logger1) + len(logger2)} * {t}')

        if ( n != 0 ) : ans = ans + coef * sin(a * n * t) * cos(n * x)
        else : ans = ans + coef * t

    print(f'Base from the second condition : {" + ".join(logger2)}\n' )

    return ans - additional

if (__name__ == '__main__') : 
    print(solveLinearCombinationDirichlet(  \
        sympify('5 * sin(3 * pi * x / 2)'),           \
        3, sympify('2*cos(t) * sin(pi * x)')))