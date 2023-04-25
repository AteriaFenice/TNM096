# Lab 3 for the course TNM096
# Authors: Maria & Malva

import random

def resolution(A, B): 

    # & -> intersection
    if not A.p & B.n and not A.n & B.p:
        return False # There is no solution (no intersection)
    
    if (A.p & B.n):
        a = random.choice(A.p & B.n)
        A.p.remove(a) # Removes element a from the set if its in the intersection
        B.n.remove(a)
    else:
        a = random.choice(A.n & B.p)
        A.n.remove(a) 
        B.p.remove(a)

    C = set()
    C.p.add(A.p.union(B.p)) # Adds the union 
    C.n.add(A.n.union(B.n))
    if C.p & C.n: # C is tautology(always true)
        return False

    # C is a set so it should not have any duplicates by default
    return C # Returns resolvent of A & B or false


def solver(KB):

    KB_prim = set()

    while(KB_prim != KB):
        S = set()
        KB_prim = KB 

        for A,B in KB: 
            C = resolution(A, B)
            if C != False:
                S.add(S.union({C}))

        if not S:
            return KB
        
        KB.add(incorporate(S, KB))


def incorporate(S, KB):

    for A in S:
        KB.add(incorporate_clause(A, KB))

    return KB

def incorporate_clause(A, KB):
    for B in KB:
        if B.p.issubset(A.p) and B.n.issubset(A.n):
            return KB
    
    for B in KB: 
        if A.p.issubset(B.p) and A.n.issubset(B.n):
            KB.remove(B)

    KB.add(KB.union(A))
    return 


# Example 1 - Resolution
# 1.

a_p = {'a', 'b'}
b_n = {'c'}

A = 

B.p = {'c', 'b'}
B.n = {}



result = resolution(A,B)

print(result)


