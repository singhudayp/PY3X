# Prime numbers <= n
def prime_list(n):
    l = [1,]
    for x in range(2, n+1):
        for y in l:
            if y == 1:
                pass
            elif x%y == 0:
                break
        else:
            l.append(x)
    return l
 
#prime number check
def is_prime(n):
    if n in prime_list(n):
         return True
    return False 

#print prime number between range, Assuming m, n > 1 && m >= n
def prime_list_in_range(n, m):
    ml = prime_list(m)
    nl = prime_list(n)
    return ml[len(nl):]
