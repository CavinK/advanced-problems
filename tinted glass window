'''
Problem S4 

Tinted Glass Window 
'''
'''
n1, n2 = 4, 3
x = [[[11,11],[20,15],1],
     [[13,8],[14,17],2],
     [[17,8],[18,17],1],
     [[12,12],[19,13],1]]
'''

def stain(): 
    n1 = int(input()) 
    n2 = int(input()) 
    x = [] 
    a1, a2, a3 = [], [], [] 
    for i in range(0,n1): 
        n3 = input()
        p = n3.split(' ')
        a1.append(int(p[0]))
        a1.append(int(p[1]))
        a2.append(int(p[2]))
        a2.append(int(p[3]))
        a3.append(a1)
        a3.append(a2)
        a3.append(int(p[4]))
        x.append(a3)
        a1, a2, a3 = [], [], []       
    
    tint = {} 
    for i in x: 
        for k in range(i[0][1],i[1][1]): 
            for l in range(i[0][0],i[1][0]): 
                a = str([l,k])
                if a in tint.keys(): 
                    tint[a] += i[2]
                else: 
                    tint[a] = i[2]
    cnt = 0
    for i in tint.keys(): 
        if tint[i]>=n2: 
            cnt += 1 
    
    return cnt
stain() 
