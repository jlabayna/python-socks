if __name__ == '__main__':
    N = int(input())
    # Init list
    items = []
    
    """
    # Dictionary idea
    cmd = {
        'print': (lambda a,b: print(items))
    }
    """

    # The site I was using didn't have match case support
    for _ in range(N):
        command = input().split()
        if command[0] != 'print':
            eval(f"items.{command[0]}({','.join(command[1:])})")
        else:
            print(items)
