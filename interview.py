#pattern = input()
pattern = 'xxx-xxx-xxxx'

#prod = list(map(str,input().split()))
prod = ['c-24-vvd-11g4','22x-r2x-vv33','ddxx-fsw-xdx','ccx-fd-f3','ghx-02c-c4hh','111-r2x-vss','s-r-4cxc','ss2-dff-xsd','33-df-vg-12-87']
print(pattern,prod) 

prodSepCount = 0
outList = []
for i in range(len(prod)):
    err = 0
    if len(prod[i]) != len(pattern):
        continue
    for j in range(len(prod[i])):
        if prod[i][j] == "-" and pattern[j] != "-":
            err = 1
        if prod[i][j] != "-" and pattern[j] == "-":
            err = 1    
    if err == 0:
        outList.append(prod[i])

print(outList)        
            



