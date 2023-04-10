import thermalConductivity as tc
import waveEquation as we

def runtimeManager(dict) :
    match dict['task'] :
        case 1 :
            return tc.solveLinearCombinationDirichlet(dict['start1'], dict['a'], dict['nonuniformity']), dict
        case 2 :
            return tc.solveLinearCombinationNeiman(dict['start1'], dict['a'], dict['nonuniformity']), dict
        case 3 :
            return we.solveLinearCombinationDirichlet(dict['start1'], dict['start2'], dict['a'], dict['nonuniformity']), dict
        case 4 :
            return we.solveLinearCombinationNeiman(dict['start1'], dict['start2'], dict['a'], dict['nonuniformity']), dict
