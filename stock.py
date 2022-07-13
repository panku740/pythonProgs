A = [4,2,2,2,4]

prof = 0
curr = A[-1]


for i in range(len(A),0,-1):
    if A[i-1]>=curr:
        curr = A[i-1]
    else:
        prof = max(prof,curr-A[i-1])
print (A.index(curr-prof),prof)        
print (A.index(curr))
