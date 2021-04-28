if __name__ == '__main__':
    scoreSet = set()
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoreSet.add(score)
        scoreList.append([name, score])
    
    secondLeast = list(sorted(scoreSet))[1]
    scoreList.sort()
    for i in range(len(scoreList)):
        if scoreList[i][1]==secondLeast:
            print(scoreList[i][0])
