#Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.

#Check if two arrays are equal or not
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        setA=set(A)
        A.sort()
        B.sort()
        for x in range(len(A)):
            if A[x]!=B[x]:
                return 0
        return 1
