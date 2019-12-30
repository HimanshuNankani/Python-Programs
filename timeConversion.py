def timeConversion(s):
    
    # Write your code here.
    
    hour = int(s[:2])
    if(s[-2].lower() == 'p' and hour != 12):
        hour += 12
    if(hour == 12 and s[-2].lower() == 'a'):
        hour = 0
    if(hour < 10):
        hour = '0'+str(hour)
    
    return str(hour)+s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
