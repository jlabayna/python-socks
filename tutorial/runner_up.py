if __name__ == '__main__':
    """Return the runner up in a list of n items in [-100,100]"""
    n = int(input())
    arr = map(int, input().split())
    maximum = -100
    runnerUp = -100
    
    # O(n)
    for x in arr:
        if x > maximum:
            runnerUp = maximum
            maximum = x
        elif x > runnerUp and x < maximum:
            runnerUp = x
    print(runnerUp)

