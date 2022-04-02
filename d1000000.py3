
def straight(L,l): #Function that returns the length of the straight
    
    m = max(L)
    temp = [0] * (m+1)
    for i in range(l):
        temp[L[i]] += 1
    result = 0
    left = 0
    for i in range(m, 0, -1):
        left += temp[i]
        if left > 0:
            left -= 1
            result += 1
    return result

#main program
T = int(input())
for i in range(T):
    l=int(input())
    if l>1:
        L=input().split(' ')
        L=[int(i) for i in L]
        L.sort()
        print('Case #'+str(i+1)+': '+str(straight(L,l)))
    else:
        print('Case #'+str(i+1)+': '+str(1))
