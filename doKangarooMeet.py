def kangaroo(x1, v1, x2, v2):
    if(x1>x2 and v1>=v2):
        return 'NO'
    elif(x1<x2 and v1<=v2):
        return 'NO'
    elif((x2-x1)%(v1-v2)==0):
        return 'YES'

    return 'NO'
if __name__ == '__main__':
    kar = input().split()
    x1 = int(kar[0])
    v1 = int(kar[1])
    x2 = int(kar[2])
    v2 = int(kar[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
    
