# Complete the staircase function below.
def staircase(n):
    s = ' '
    h = '#'
    for i in range(1,n+1):
        print("{}{}".format(s*(n-i),h*i))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
