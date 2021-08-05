# implementación dppl

import sys
from copy import deepcopy

truth_assignment = []
unit_propa = 0
splitting = -1

def removeLiteral(cnf):
    #remove items
    new_liters = list(set(''.join(cnf)))
    if '!' in new_liters:
        new_liters.remove('!')
    if '\n' in new_liters:
        new_liters.remove('\n')
    if ' ' in new_liters:
        new_liters.remove(' ')
    return new_liters


def preproc(input_cnf):
    #handle back he literals
    liters = list(set(input_cnf))
    if '!' in liters:
        liters.remove('!')
    if '\n' in liters:
        liters.remove('\n')
    if ' ' in liters:
        liters.remove(' ')
    liters = list(liters)
    input_cnf = input_cnf.splitlines()

    return liters, input_cnf


def dpll(cnf, liters):
    global truth_assignment, unit_propa, splitting

    splitting += 1

    while True:
        if len(liters) == 1 and len(cnf) > 1:
            print('--------------------------------------------------')
            print(cnf)
            break

        delete_list = []
        unit_clause = None
        cnf = list(set(cnf))

        # find unit clause
        for i in range(len(cnf)):
            if ' ' not in cnf[i]:
                unit_clause = cnf[i]
                truth_assignment.append(unit_clause)
                del cnf[i]
                break

        # exception handle
        if unit_clause:
            for i in range(len(cnf)):
                if '!' in unit_clause:
                    if unit_clause.replace('!', '') == cnf[i]:
                        return False
                else:
                    if '!' + unit_clause == cnf[i]:
                        return False

        if unit_clause and '!' not in unit_clause:
            unit_propa += 1
            for j in range(len(cnf)):
                if '!' + unit_clause in cnf[j]:
                    if '!' + unit_clause == cnf[j]:
                        delete_list.append(j)
                    else:
                        cnf[j] = cnf[j].replace('!' + unit_clause, ' ')
                        cnf[j] = cnf[j].strip(' ')
                elif unit_clause in cnf[j]:
                    delete_list.append(j)

            for index in sorted(delete_list, reverse=True):
                del cnf[index]
            liters = removeLiteral(cnf)

        elif unit_clause and '!' in unit_clause:
            unit_propa += 1
            for j in range(len(cnf)):
                if unit_clause in cnf[j]:
                    delete_list.append(j)
                elif unit_clause.replace('!', '') in cnf[j]:
                    if unit_clause.replace('!', '') == cnf[j]:
                        delete_list.append(j)
                    else:
                        cnf[j] = cnf[j].replace(unit_clause.replace('!', ''), ' ')
                        cnf[j] = cnf[j].strip(' ')

            for index in sorted(delete_list, reverse=True):
                del cnf[index]
            liters = removeLiteral(cnf)

        else:
            break

    # checking clause
    if cnf == []:
        return True
    elif len(liters) == 1 and len(cnf) > 1:
        return False

    # splitting
    if dpll(cnf + [liters[0]], deepcopy(liters)) or dpll(cnf + ['!' + liters[0]], deepcopy(liters)):
        return True
    else:
        return False


def main():
    global truth_assignment
    input_cnf = open("example.txt", 'r').read()
    liters, cnf = preproc(input_cnf)

    if dpll(cnf, liters):
        print('--------------------------------------------------')
        print('[Resultado] : satisfacible')

        # print truth assignment
        for i in range(len(truth_assignment) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if '!' in truth_assignment[i]:
                    if truth_assignment[i] == truth_assignment[j] or truth_assignment[i].replace('!', '') == \
                            truth_assignment[j]:
                        truth_assignment[j] = ''
                else:
                    if truth_assignment[i] == truth_assignment[j]:
                        truth_assignment[j] = ''

        if '' in truth_assignment:
            truth_assignment = list(set(truth_assignment))
            truth_assignment.remove('')

        #show truth clauses
        print('[Clausula] | ', end='')
        for i in truth_assignment:
            if '!' in i:
                print(i.replace('!', ''), ' : False', end=' | ')
            else:
                print(i, ' : True', end=' | ')
        print('')
    else:
        print('--------------------------------------------------')
        print('[Resultado] : insatisfacible, {}')

if __name__ == '__main__':
    main()