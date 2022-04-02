
def my_output(i1,i2,i3): #Function that generates the desired output
    mins= []
    for i in range(4): #Get the possible colors that each printer can make (the mins)
        mins.append(
            min(
                i1[i],
                i2[i],
                i3[i],
            )
        )
    if sum(mins) < 1e6:
        return ["IMPOSSIBLE"]
    elif sum(mins) == 1e6:
        return mins
    else:
        for i in range(4):
            mins[i] = max(0, mins[i] - int(abs(sum(mins) - 1e6)))
            if sum(mins) == 1e6:
                return mins
    return ["IMPOSSIBLE"] #In case 

T = int(input())
col =[]
for i in range(T):        #Preparing data
    i1 = [int(x) for x in input().split(' ')] 
    i2 = [int(x) for x in input().split(' ')] 
    i3 = [int(x) for x in input().split(' ')] 
    col.append(my_output(i1,i2,i3))

for index, output in enumerate(col, start=1): #Generating the output
    output_str = ' '.join(map(str, output))
    print(f"Case #{index}: {output_str}")