from runtimeManager import runtimeManager
from inputManager import inputManager
from sympy import *
from sympy.plotting.plot import plot3d

def main () :
    x, t=  symbols('x t')
    u, dict = runtimeManager(inputManager())
    
    print(f'Answer : {u}')

    if (dict['task'] % 2 == 1) : plot3d(u, (x, 0, dict['l']), (t, 0, 5))
    else : plot3d(u.diff(x), (x, 0, dict['l']), (t, 0, 5))

if (__name__ == '__main__') : 
    main()