class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        hash1 = {}
        for i in range(n):
            if arr[i] in hash1:
                hash1[arr[i]] += 1
            else:
                hash1[arr[i]] = 1
        print(hash1)
        for i in range(n):
            if hash1[arr[i]]>=2:
                return i+1
        return -1