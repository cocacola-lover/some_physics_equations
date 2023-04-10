from sympy import *
from sympy.core.expr import Expr
from sympy.functions.elementary.trigonometric import cos, sin

def checkValidity(expression : Expr) :
    for arg in expression.args : 
        if (len(arg.args) == 0) :
            if (not arg.is_number and \
                arg != Symbol('x') and \
                arg != Symbol('t') ) :
                raise NotImplementedError('Wrong input function')
        else :
            checkValidity(arg)

def justX(expression : Expr) :
    for arg in expression.args : 
        if (len(arg.args) == 0) :
            if (not arg.is_number and \
                arg != Symbol('x')) :
                return False
        else :
            if (not justX(arg)) : return False
    return True

def justT(expression : Expr) :
    for arg in expression.args : 
        if (len(arg.args) == 0) :
            if (not arg.is_number and \
                arg != Symbol('t')) :
                return False
        else :
            if (not justT(arg)) : return False
    return True

def correctForm (expression : Expr) : 

    if (expression.is_constant()) : return expression, 0

    coef, trig, n = Number(1), Number(1), Number(1)

    if (expression.func.is_Mul) :
        for arg in expression.args :
            if (arg.is_constant()) :
                coef = coef * arg
            elif (arg.func == sin or arg.func == cos) :
                trig = trig * arg
            else :
                raise NotImplementedError('Unexpected expression')

    elif (expression.func == sin or expression.func == cos) :
        trig = expression

    else : 
        raise NotImplementedError('Unexpected expression')
    
    for arg in trig.args[0].args :
        if (arg.is_constant()) :
            n = n * arg

    return coef, n

    

        
if (__name__ == '__main__') : 
    print(correctForm(sympify('cos(5*pi * x)')))