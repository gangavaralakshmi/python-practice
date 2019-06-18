def toggelstring(s):
    #convert the string intpo a list
    s=list(s)
    t = []
    for c in s:
        if c.islower():
            t.append(c.upper())
        else:
            t.append(c.lower())
    return " ".join(t)
toggelstring("Abc")

###perfect number

def perfectnumber(N):
    sum = 0
    for i in range (1,N):
        if N % i == 0:
            sum=sum+i
    if sum == N:
        print ("YES")
    else:
        print ("NO")
T = int(input ())    
for i in range(T):
    N=int(input())
    perfectnumber(N)

perfectnumber(N)
    
def isPRIME(n):
    flag = 1
    if n == 2:
        return True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=0
            return  False
    if flag == 1:
            return True


def numberPrimeFactors(n): #at P means >= P means either P or more than P
    if isPRIME(n):
        return 1
    count = 0
    for i in range (2,n//2+1):
        if isPRIME(i) and n % i == 0:
            count +=1
    return count
isSpecialnumber(6,3)

