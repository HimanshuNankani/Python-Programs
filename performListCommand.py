if __name__ == '__main__':
    N = int(input())
    ar = []
    commandList = []
    for _ in range(N):
        commandList.append(input())
    
    for i in range(N):
        if commandList[i]=="reverse":
            ar.reverse()
        elif commandList[i]=="pop":
            ar.pop()
        elif commandList[i]=="sort":
            ar.sort()
        elif commandList[i]=="print":
            print(ar)
        elif "append" in commandList[i]:
            ar.append(int(commandList[i][7:]))
        elif "remove" in commandList[i]:
            ar.remove(int(commandList[i][7:]))
        elif "insert" in commandList[i]:
            x = commandList[i].split()
            ar.insert(int(x[1]),int(x[2]))
