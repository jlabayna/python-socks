if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # List comprehension example:
    # - Permutations except for those that sum to n
    # A list comprehension consists of brackets containing an expression
    # followed by a for clause, then zero or more for or if clauses. 
    print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a + b + c != n)])
