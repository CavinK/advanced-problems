'''
Problem S5 

Lazy Fox 
'''
def fox(): 
    x1 = [[0,0]]
    n1 = int(input())
    while 1:
        n2 = input() 
        if not n2: 
            break 
        l = n2.split(' ')
        z = [int(i) for i in l]
        x1.append(z) 
        z = [] 
    
    sub = [] 
    pos = [] 
    for i in range(0,len(x1)): 
        for j in range(0,len(x1)): 
            sub.append(eucDist(x1[i],x1[j]))
        pos.append(sub)
        sub = [] 
        
    import copy 
    pos2 = copy.deepcopy(pos) 
    
    return rec(pos[0].index(max(pos[0])), pos, pos2) # parameter initialisation!!! 
fox()

def eucDist(a,b):
    import math
    return math.sqrt((b[1]-a[1])**2+(b[0]-a[0])**2)

'''
origin = [0,0] 
a,b,c,d,e = [5,8],[4,10],[3,1],[3,2],[3,3]
x = [origin, a, b, c, d, e]
x[1][0]

sub = [] 
pos = [] 
for i in range(0,len(x)): 
    for j in range(0,len(x)): 
        sub.append(eucDist(x[i],x[j]))
    pos.append(sub)
    sub = [] 

import copy 
pos2 = copy.deepcopy(pos)
'''

def rec(x, pos, pos2, y=0, cnt=0):
    if len(pos2[x]) > 2 and len(pos2[y]) > 2:  
        last=pos2[x][y]
    else: 
        return cnt
    
    for i in pos2[x]:
        if i >= last: 
            pos2[x].pop(pos2[x].index(i))
    #print('good!',' ',x)
    return rec(pos[x].index(max(pos2[x])), pos, pos2, x, cnt+1) 
