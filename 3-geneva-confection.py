'''
Problem S3 

The Geneva Confection 
'''
def geneva(): 
    #ex1 = ['2','4','2','3','1','4','4','4','1','3','2']
    ex1 = [] 
    while 1: 
        x = input() 
        if not x: 
            break 
        ex1.append(x)
    
    lake = [] 
    br = [] 
    
    ex2 = ex1[:] 
    ex2.pop(0)
    for i in ex2: 
        if i == '1': 
            lake.append(i)
        else: 
            br.append(i) 
        if len(lake)>=1 and len(br)>=1: 
            while int(br[-1]) == int(lake[-1])+1: 
                lake.append(br[-1])
                br.pop()
    
    import re 
    conf = '1234' # you can make some codes to adjust the max value 
    res = ''.join(lake)
    for i in range(0,int(ex1[0])): 
        if bool(re.search(conf,res)): 
            print('Y')
            res = res.replace(conf,'')
        else: 
            print('N')
geneva() 
