def matrix_transpose (a):
    r=len(a)
    c=len(a[0])
    t=[[0]*r for i in range (c)]
    
    for i in range (r):
        for j in range(c):
            t[j][i]=a[i][j]
    return t

def matrix_creation (r,c):
    a=[[0]*c for i in range (r)]
    for i in range (r):
        for j in range (c):
            print("Enter[",i,j,"]th element")
            a[i][j]=int(input())
    return a

def matrix_display (a):
    for i in a :
        print(" ".join(map(str, i)))
    


r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
a=matrix_creation(r,c)
t=matrix_transpose(a)
print("Original matrix")
matrix_display(a)
print("Transpose matrix")
matrix_display(t)


