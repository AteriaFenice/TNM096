# Lab 3 for the course TNM096
# Authors: Maria & Malva

import random

class Clause: 
    def __init__(self, p, n):
        self.p = p
        self.n = n 
    
    def __str__(self):
        return str(self.p) + " " + str(self.n)

    def __repr__(self):
        return str(self.p) + " " + str(self.n)


def resolution(A, B): 
    #print('A = ', A, ', B = ', B)
    # & -> intersection
    if not (A.p.intersection(B.n)) and not (A.n.intersection(B.p)):
        return False # There is no solution (no intersection)
    
    if (A.p.intersection(B.n)):
        a = random.choice(list(A.p.intersection(B.n)))
        A.p.remove(a) # Removes element a from the set if its in the intersection
        B.n.remove(a)
    else:
        a = random.choice(list(A.n.intersection(B.p)))
        A.n.remove(a) 
        B.p.remove(a)

    C = Clause(p = set(A.p).union(B.p), n = set(A.n).union(B.n))
    #C.p.add(A.p.union(B.p)) # Adds the union 
    #C.n.add(A.n.union(B.n))
    if C.p.intersection(C.n): # C is tautology(always true)
        return False

    # C is a set so it should not have any duplicates by default
    return C # Returns resolvent of A & B or false


def solver(KB):

    KB_prim = set()

    while(KB_prim != KB):
        S = set()
        KB_prim = KB 

        #print('KB: ', KB)

        #for A,B in enumerate(KB): 
        for A in KB: 
            for B in KB:
                #print('A = ', A, ', B = ', B)
                C = resolution(A, B)
                if C != False:
                    S = S.union({C})

        if not S:
            return KB
        
        KB = incorporate(S, KB)

    print("KB: ")
    for C in KB: 
        print(C)
    print("S: ")
    for C in S:
        print(C)
    print()

    return KB


def incorporate(S, KB):
    for A in S:
        KB = incorporate_clause(A, KB)

    return KB

def incorporate_clause(A, KB):

    for B in KB:
        if set(B.p).issubset(A.p) and set(B.n).issubset(A.n):
            return KB
    
    for B in KB: 
        if set(A.p).issubset(B.p) and set(A.n).issubset(B.n):
            KB.remove(B)

    KB = KB.union(A)
    return 


# Example 1 - Resolution
# 1.
A1 = Clause(p = {'a', 'b'}, n ={'c'} )
B1 = Clause(p = {'c', 'b'}, n = {})
result1 = resolution(A1,B1)
print('Ex 1: ', result1)

# 2.
A2 = Clause(p = {'a', 'b'}, n ={'c'}) 
B2 = Clause(p = {'d', 'b'}, n = {'g'})
result2 = resolution(A2,B2)
print('Ex 2: ', result2)

# 3.
A3 = Clause(p = {'c', 't'}, n = {'b'})
B3 = Clause(p = {'z', 'b'}, n = {'c'})
result3 = resolution(A3, B3)
print('Ex 3: ', result3)

# Drawing conclusion
# Bob.
ice = 'a'
sun = 'b'
money = 'c'
movie = 'd'
cry = 'e'
A4 = Clause(p = {'ice'}, n = {'sun', 'money'})
B4 = Clause(p = {'ice', 'movie'}, n = {'money'})
C4 = Clause(p = {'money'}, n = {'movie'})
D4 = Clause(p = {}, n = {'movie', 'ice'})
E4 = Clause(p = {'sun', 'money', 'cry'}, n = {})
F4 = Clause(p = {'movie'}, n = {})

KB = set({A4, B4, C4, D4, E4, F4})
print('KB: ', KB)
result4 = solver(KB)
print('solver finished')
print('KB: ', result4)