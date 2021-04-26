if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

uniqScoreList = list(set(arr))
uniqScoreList.sort()
print(uniqScoreList[-2])
