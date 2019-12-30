import os

# Complete the gridChallenge function below.
def gridChallenge(grid):
    newgrid = []
    for x in grid:
        lst = [y for y in x]
        lst.sort()
        newgrid.append(lst) 
    print(newgrid)
    for x in range(len(newgrid[0])):
        print(x)
        templ =[y[x] for y in newgrid]
        templ2 = templ.copy()
        templ.sort()
        if(templ2 != templ):
            return 'NO'
        del templ
        del templ2
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
