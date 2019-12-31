import os

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    count = 0
    for x in range(a[-1],b[0]+1):
        for i in a:
            if(x%i!=0):
                break
        else:
            for j in b:
                if(j%x!=0):
                    break
            else:
                count+=1
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
