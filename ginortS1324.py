if __name__ =='__main__':
    input_str = input()
    
    strList = [s for s in input_str]
    strList.sort()
    oddStr = ""
    evenStr = ""
    lowerStr = ""
    upperStr = ""
    for s in strList:
        if s.islower():
            lowerStr += s
        elif s.isupper():
            upperStr += s
        elif s.isdigit() and int(s)%2==0:
          evenStr += s
        else:
            oddStr += s
    print(lowerStr+upperStr+oddStr+evenStr)
