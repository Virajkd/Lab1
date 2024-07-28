def matrix_creation(r,c):
    a=[[0]*c for i in range (r)]
    for i in range (r): 
        for j in range (c):
            print("Enter [",i,j,"] element")
            a[i][j]=int(input())
    return a 

def matrix_check(m1,m2):
    if ( len(m2)==len(m1[0])):
        return True
    return False


def matrix_multiplication(m1,m2):
    sum=0
    if (matrix_check(m1,m2)):
        for i in range (len(m1)):
            for j in range (len(m1[i])):
                sum+=m1[i][j]*m2[j][i]
    
    else:
        print("Matrix cant be multiplied")
        return
        
    print("Sum=",sum)

print("Matrix 1")
rows,columns=eval(input("enter the number of rows n columns"))
m1=matrix_creation(rows,columns)
print(m1)
print("Matrix 2")
rows,columns=eval(input("enter the number of rows n columns"))
m2=matrix_creation(rows,columns)
print(m2)
matrix_multiplication(m1,m2)


    
