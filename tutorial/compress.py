from itertools import groupby

# Take an input whole number and return tuples representing consecutive chars
for group, items in groupby(input()):
    print(f"({len(list(items))}, {group})", end=" ")
