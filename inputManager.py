from sympy import *
import checks


def inputManager () :
    init_printing()

    task = None
    while ( task == None or task <= 0 or task > 4) :
        if (task != None) : print('Please try again')
        task = int(input('Please write what task would you like to solve\n' + \
        '1.Теплопроводность/Дирихле \n2.Теплопроводность/Нейман\n' + \
         '3.Волновое Уравнение/Дирихле\n4.Волновое Уравнение/Нейман\n'))
    
    checkStartInput = False
    while (not checkStartInput) :
        checkStartInput = True
        try :
            start1 = sympify(input('Please write starting condition\n'))
            checks.checkValidity(start1)
        except SympifyError as e :
            print(e.__str__)
            print('Please try again')
            checkStartInput = False
        except NotImplementedError as e :
            print(e)
            print('Please try again')
            checkStartInput = False
    start2 = None
    if (task > 2) : 
        checkStartInput = False
        while (not checkStartInput) :
            checkStartInput = True
            try :
                start2 = sympify(input('Please write starting condition 2\n'))
                checks.checkValidity(start2)
            except SympifyError as e :
                print(e.__str__)
                print('Please try again')
                checkStartInput = False
            except NotImplementedError as e :
                print(e)
                print('Please try again')
                checkStartInput = False

    checkAInput = False
    while (not checkAInput) :
        checkAInput = True
        a = ''
        try :
            a = sympify(input('Please write a\n'))
        except SympifyError as e :
            print(e.__str__)
            print('Please try again')
            checkAInput = False
        except NotImplementedError as e :
            print(e)
            print('Please try again')
            checkAInput = False

    checkBordersInput = False
    while (not checkBordersInput) :
        checkBordersInput = True
        l = ''
        try :
            l = sympify(input('Please write l\n'))
        except SympifyError as e :
            print(e.__str__)
            print('Please try again')
            checkBordersInput = False
        except NotImplementedError as e :
            print(e)
            print('Please try again')
            checkBordersInput = False

    checkNonuniformityInput = False
    while (not checkNonuniformityInput) :
        checkNonuniformityInput = True
        try :
            inputTaken = input('Please write uniformity (just press Enter if none)\n')
            if (inputTaken == '') : nonuniformity = None
            else : nonuniformity = sympify(inputTaken)
        except SympifyError as e :
            print(e.__str__)
            print('Please try again')
            checkNonuniformityInput = False
        except NotImplementedError as e :
            print(e)
            print('Please try again')
            checkNonuniformityInput = False

    return {
        'task' : task,
        'start1' : start1,
        'start2' : start2,
        'l' : l,
        'a' : a,
        'nonuniformity' : nonuniformity
    }


if (__name__ == '__main__') : 
    print(inputManager())