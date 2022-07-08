if __name__ == '__main__':
    """Print students with the second lowest score"""
    # Unclear if dictionaries are faster for small n without timing it
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])

    grades = sorted(grades, key=lambda x: (x[1],x[0]))
    
    # Move pointer to beginning of second lowest
    # Dunno if this is faster than the other solutions.
    # Didn't want to scan past the second lowest scores if possible.
    n = 0
    last = grades[n][1]
    while n < len(grades) and grades[n][1] == last:
        n = n+1
    
    # Set last to second-lowest score
    last = grades[n][1]
    if n == len(grades):
        for x in grades:
            print(x[0])
    else:
        while n < len(grades) and grades[n][1] == last:
            print(grades[n][0])
            n=n+1
