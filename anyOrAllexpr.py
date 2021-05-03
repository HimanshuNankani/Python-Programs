if __name__ == '__main__':
    n = int(input())
    nList = list(map(str, input().split()))
    
    pos = all([int(x)>0 for x in nList])
    pal = any([y==y[::-1] for y in nList])
    print(all([pos,pal]))
