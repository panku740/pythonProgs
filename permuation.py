from itertools import permutations

print(list(permutations("ABC")))

s = "ABC"
ans = ""
def permut(s,ans):
    if len(s)==0:
        print(ans,end=' ')
        return

    for i in range(len(s)):
        ch = s[i]
        lt = s[0:i]
        rt = s[i+1:]
        permut(lt+rt,ans+ch)

permut(s,ans)               