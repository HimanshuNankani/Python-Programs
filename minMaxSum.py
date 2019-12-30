# The miniMaxSum function.
def miniMaxSum(arr):
    arr.sort()
    print("{} {}".format(sum(arr[:4]),sum(arr[1:5])))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
