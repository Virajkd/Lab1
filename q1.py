def vowel(v):    #checking for vowel 
    vowels='aeiouAEIOU'
    if v in vowels:
        return True
    return False
def count(string):    #counting number of vowels in the string
    vowel_count,consonant_count =0,0
    for i in string:
        if ('a'<=i<='z') or ('A'<=i<='Z'):
            if vowel(i):
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count,consonant_count

string=input("Enter a string\n")

vowel_count, cosonant_count= count(string)
print("vowel_count is ",vowel_count)
print("consonant_count is ",cosonant_count)
