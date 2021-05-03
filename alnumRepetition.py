if __name__ == '__main__':
    S = input()
    x = ""
    j=-1
    for s in S:
        if s.isalnum() and s == x:
            j = s
            break
        x = s
    print(j)
