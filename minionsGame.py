def minion_game(s):
    vowelscore=0
    consscore=0

    for i in range(len(s)):
        if s[i].upper() in ['A','E','I','O','U']:
            vowelscore+= (len(s)-i)
        else:
            consscore += (len(s)-i)
            
    if(vowelscore > consscore):
        print("Kevin",vowelscore)
    elif(vowelscore < consscore):
        print("Stuart",consscore)
    else:
        print("Draw") 

if __name__ == '__main__':
    s = input()
    minion_game(s)
