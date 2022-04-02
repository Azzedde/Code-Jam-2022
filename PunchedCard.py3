
T = int(input())
for i in range(T):
    print('Case #'+str(i+1)+':')
    R,C = map(int,input().split(' '))
    
    for j in range(2*R+1):
        s=''
        if j == 0 :
            s='..'
            for k in range(C-1):
                s+='+-'
            s+='+'
            print(s)
        elif j == 1:
            s='..'
            for k in range(C-1):
                s+='|.'
            s+='|'
            print(s)
        elif j % 2 ==0:
            for k in range(C):
                s+='+-'
            s+='+'
            print(s)
        else:
            for k in range(C):
                s+='|.'
            s+='|'
            print(s)



