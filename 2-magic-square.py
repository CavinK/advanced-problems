'''
Problem S2 

Introduction: A magic square is a 2D matrix composed of n^2 integers 
where n is the length of one row/column. 
In a magic square each row, 
each column and the two diagonals must sum to the same value (see example below). 

Problem: Given a 2D matrix in the same form as shown and mentioned above your program must determine 
if the square is magic or not magic. It will output “magic” or “not magic” accordingly.

Input: Your program will first take an input n, representing the length of one row of the matrix. 
It will then take n lines of input containing n integers separated by spaces. 

Sample Input/Output:

1.)
Input: 
3
2 2 2
2 2 2
2 2 2
Output: “magic”

2.) 
Input:
4
16 2 3 13
5 11 10 8
9 7 6 12
4 14 15 1
Output: “magic”

3.)
Input:
4
12 3 4 5
5 67 8 9
102 3 4 6
34 2 89 0

Output: “not magic”
'''
def cubeSum(): 
    import numpy as np 
    l1 = []
    while 1:
        x = input()
        if not x:
            break
        e = [int(i) for i in x.split(" ")]
        l1.append(e)
    
    n = np.array(l1)
    l2 = [] 
    a, b = 0, 0
    for i in range(0,n.shape[0]):
        l2.append(n[i].sum())
    for i in range(0,n.shape[1]):
        l2.append(n[:,i].sum())
    for i in range(0,n.shape[0]):
        a += n[i,i]
    for i in range(0,n.shape[1]):
        for j in range(0,n.shape[0]):
            if i+j == n.shape[1]-1:
                b += n[i,j]
    l2.append(a)
    l2.append(b)
    if all(i==l2[0] for i in l2):
        return "magic" 
    else: 
        return "not magic"
cubeSum() 
