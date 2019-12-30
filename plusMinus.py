#!/bin/python3
# Complete the plusMinus function below.
def plusMinus(arr):
    countp = 0
    countn = 0
    countz = 0
    
    for x in arr:
        if x >0:
            countp += 1
        elif x < 0:
            countn += 1
        else:
            countz += 1
    
    l = len(arr)
    print("{0:.6f}".format(countp/l))
    print("{0:.6f}".format(countn/l))
    print("{0:.6f}".format(countz/l))
 
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
