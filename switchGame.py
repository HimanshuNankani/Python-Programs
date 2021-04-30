def switchBulb(testList,n):
    for i in range(1,n+1):
        for m in range(1,n+1):
            if m%i==0:
                testList[m-1] = False if testList[m-1] else True
    
    bulbsOn=[]

    for j in range(n):
        if testList[j]:
            bulbsOn.append(j+1)
            
    return bulbsOn    
    
if __name__ == '__main__':
    t = int(input())
    
    testCases = []
    
    for _ in range(t):
        testCase = int(input())
        testCases.append(testCase)
    
    for i in range(t):
        bulbStates = [False]*testCases[i]
        bulbsOn = switchBulb(bulbStates,testCases[i])
        print(*bulbsOn)
    
