# cook your dish here

if __name__ == '__main__':
    N = int(input())
    xList = []
    for _ in range(N):
        tin = str(input())
        xList.append(tin.count('4'))
    
    print(*xList, sep='\n')
