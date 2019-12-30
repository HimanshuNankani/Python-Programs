def sockMerchant(n, ar):
    d = {}
    for x in set(ar):
        d[x] = 0
    for sock in ar:
        d[sock] += 1
    pairs = 0
    for p in d:
        pairs += d[p]//2
    
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
