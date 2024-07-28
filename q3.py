def list_generation ():
    num_a=int(input("Enter the number of elements in List "))
    a=[0]*num_a
    for i in range (len(a)):
        print("Enter",i+1,"th number")
        a[i]=int(input())
    return a
 
def common_elements (a,b):
    count=0
    for i in range (len(a)):
        for j in range (len(b)):
            if a[i]==b[j]:
                count+=1
    return count

a,b=list_generation(),list_generation()
print("Common Elements:",common_elements(a,b))
