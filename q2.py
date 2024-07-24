def matrix_creation(rows,columns):
    for i in range (rows):
        for j in range (columns):
            mi[i][j]=int(input("enter at position ({i},{j})"))
    return mi


def matrix_check(m1,m2):
    r_m1,r_m2,c_m1,c_m2=0
    for i in m1:
        r_m1+=1
        for j in i:
            c_m1+=1
    for i in m2:
        r_m2+=1
        for j in i:
            c_m2+=1
    if (r_m1==c_m2) and (r_m2==c_m1):
        return True
    return False

def matrix_multiplication(m1,m2):
    if (matrix_check()):
        for i in m1:
            for j in i:
                sum=m1[i][j]*m2[j][i]
    return sum


print("Matrix 1(m1)")
rows,columns=eval(input("enter the number of rows n columns"))
m1=matrix_creation(rows,columns)
print("Matrix 2(m2)")
rows,columns=eval(input("enter the number of rows n columns"))
m2=matrix_creation(rows,columns)
sum=matrix_multiplication(m1,m2)
print("Sum=",sum)

    
