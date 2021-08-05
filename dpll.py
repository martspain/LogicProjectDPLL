# implementación dppl

import sys
from copy import deepcopy

assign_true = set()
assign_false = set()
n_props, n_splits = 0, 0

    
def solveDPLL(clause, I):
    trueAssigned = []
    falseAssigned = []

    global assign_true, assign_false, n_props, n_splits
    assign_true = set(assign_true)
    assign_false = set(assign_false)
    n_splits += 1

    clause = list(set(clause))
    units = [i for i in clause if len(i)<3]
    units = list(set(units))
    if len(units):
        for unit in units:
            n_props += 1
            if '!' in unit:
                assign_false.add(unit[-1])
                falseAssigned.append(unit[-1])
                i = 0
                while True:
                    if unit in clause[i]:
                        clause.remove(clause[i])
                        i -= 1
                    elif unit[-1] in clause[i]:
                        clause[i] = clause[i].replace(unit[-1], '').strip()
                    i += 1
                    if i >= len(clause):
                        break
            else:
                assign_true.add(unit)
                trueAssigned.append(unit)
                i = 0
                while True:
                    if '!'+unit in clause[i]:
                        clause[i] = clause[i].replace('!'+unit, '').strip()
                        if '  ' in clause[i]:
                            clause[i] = clause[i].replace('  ', ' ')
                    elif unit in clause[i]:
                        clause.remove(clause[i])
                        i -= 1
                    i += 1
                    if i >= len(clause):
                        break

    if len(clause) == 0:
        return True

    if sum(len(clause)==0 for clause in clause):
        for i in trueAssigned:
            assign_true.remove(i)
        for i in falseAssigned:
            assign_false.remove(i)
        return False
    I = [k for k in list(set(''.join(clause))) if k.isalpha()]

    x = I[0]
    if solveDPLL(deepcopy(clause)+[x], deepcopy(I)):
        return True
    elif solveDPLL(deepcopy(clause)+['!'+x], deepcopy(I)):
        return True
    else:
        for i in trueAssigned:
            assign_true.remove(i)
        for i in falseAssigned:
            assign_false.remove(i)
        return False

clauses = [
    [{"p"}, {"!p"}],
    [{"q", "p", "!p"}],
    [{"!p", "!r", "!s"}, {"!q", "!p", "!s"}],
    [{"!p", "!q"}, {"q", "!s"}, {"!p", "s"}, {"!q", "s"}],
    [{"!p", "!q", "!r"}, {"q", "!r", "p"}, {"!p", "q", "r"}],
    [{"r"}, {"!q", "!r"}, {"!p", "q", "!r"}, {"q"}]
]

