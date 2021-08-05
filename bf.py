import itertools

exp = input("Ingrese una expresion cnf en este formato [{(p, False), (q, False)}, {(p, True), (r, True)}]:\n")
lista = []

def array(exp):
    a = exp.replace("[",'')
    b = a.replace("]", '')
    c = b.replace("{",'')
    d = c.replace("(",'') 

    s1 = d.split("}, ")
    for d in s1:
        d1 = d.replace("), ","+")
        d2 = d1.replace(")","+")
        e = d2.split('+')
        del e[-1]
        literal = []
        for l in e:
            v = l.split(", ")
            if(v[1] == 'False'):
                v[1] = False
            else:
                v[1] = True
            literal.append(v) 
        lista.append(literal)
    return lista

w = array(exp)

def brute_force(cnf):
    literals = set()
    for conj in cnf:
        for disj in conj:
            literals.add(disj[0])

    literals = list(literals) 
    n = len(literals)
    for seq in itertools.product([True,False], repeat=n):
        a = zip(literals, seq)
        #if all([bool(disj.intersection(a)) for disj in cnf]):
        intersection = []
        for cong in cnf:
            for disj in cong:
                for asg in a:
                    if set(asg) == set(disj):
                        intersection.append(asg)
        if len(intersection) == 0:
            return False, None
        else:
            cont = 0
            r = []
            while (cont < len(literals)):
                r.append(str(literals[cont]) +" = " + str(seq[cont]))
                cont = cont +1
            return True, r

print(brute_force(w))