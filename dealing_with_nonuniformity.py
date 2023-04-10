import checks
from sympy import *
from sympy.core.expr import Expr;

# Simple devide into two
# works only on surface expamples
def devideIntoTwo(expression : Expr) :
    F, G = Number(1), Number(1)

    if (checks.justT(expression)) : return expression, G
    elif (checks.justX(expression)) : return F, expression

    if (not expression.func.is_Mul) : raise Exception('Complex nonuniform function')

    for arg in expression.args : 
        if (checks.justT(arg)) : F = F * (arg)
        elif (checks.justX(arg)) : G = G * (arg)
        else : raise Exception('Complex nonuniform function')

    print(f'Devided {expression} into F : {F} and G : {G} \n')

    return F, G


# MUST BE TRUE : G''(x) == -(k**2) * G(x)
def calculatePartialSolution(F : Expr, G : Expr, a : float = 1) :
    
    x, t, k, c1 = symbols('x t k C1')

    kSquared = solveset(                \
        Eq( G.diff(x, x), -(k)**2 * G), \
        k**2).args[0]
    
    
    w = symbols('w', cls=Function)
    w = dsolve(                                 \
        Eq( w(t).diff(t) , (a**2)*(-1)*kSquared*w(t) + F),  \
        w(t)).args[1]

    print(f'Using F and G found w.\n w = {w.subs(c1, 0)}')
    print(f'Adding {w.subs(c1, 0) * G} to our expression\n')

    return w.subs(c1, 0) * G


if (__name__ == '__main__') : 
    t = symbols('t')
    print(calculatePartialSolution(     \
        *devideIntoTwo(                 \
        sympify('2*cos(t)*sin(pi*x)')   \
    ), 9))