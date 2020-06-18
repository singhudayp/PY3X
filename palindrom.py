#Palindrom check as string
def palindrom_string(s):
    l = len(s)
    for i in range(0, l):
        if s[i] != s[l-i-1]:
            return False
    return True

#Palindrom check as integer
def palindrom_number(n):
    if n // 10 == 0:
        return False
    tmp = n
    rtmp = 0

    while tmp != 0:
        rtmp = (rtmp * 10) + (tmp % 10)
        tmp = tmp // 10

    if n == rtmp:
        return True
    else:
        return False    
