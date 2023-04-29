"""
      Description:
 Write a program in Python to print the number of unique letters in a string. 
 Only new letters from the string should be counted and not duplicates      

Input : string1 = "India"
Output : uniqueLetters = i,n,d,a


Input : string1 = "Dedication"
Output : uniqueLetters = d,e,i,c,a,t,o,n

"""
#code

str=input("string = ")
str=str.lower()
l=[]
res=list(set(str))
for i in str:
    if i in res:
        l.append(i)
        res.remove(i)
print("uniqueLetters = ",end="")
print(",".join(l))

"""
Test case 1:
string = communication 
uniqueLetters = c,o,m,u,n,i,a,t

Test case 2:
string = uniqueletters
uniqueLetters = u,n,i,q,e,l,t,r,s

"""