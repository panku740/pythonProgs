class Solution:
    def romanToDecimal(self, S): 
        # code here
        dic = {'M': 1000, 'D': 500, 'C':100, 'L':50,
               'X':10, 'V':5, 'I':1}
        n = 0
        l=[]
        s1=[]
        for i in S:
            s1.append(i)
        #print(len(s1))    
        for i in range(len(s1)-1,-1,-1):
            l.append(dic[s1[i]])
            if max(max(l),dic[s1[i]]) <= dic[s1[i]]:
                n = n + dic[s1[i]]
            else:
                n = n - dic[s1[i]]
            #print(l,n)    
        return n  