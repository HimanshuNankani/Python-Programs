if __name__ == '__main__':
    n = int(input())
    s=0
    m=10
for i in range(1,n+1):
    if i==m:
        m = m*10
    s = s*m + i        
print(s)
