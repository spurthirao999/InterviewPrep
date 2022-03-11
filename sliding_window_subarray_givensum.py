"""
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right.

 
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N and S as input parameters and returns a list containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return an array consisting only one element that is -1.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 105
1 <= Ai <= 109
"""

 

#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
"""
Inpurt: arr(list), n(int), s(int)
output: (list) indices of start and end computing the sum
Algorithm:
(Optimal)
1. Read the elements(0, len(arr))
    a. add to sum
    b. while(sum >= req_sum)
        1. see if sum = req_sum, break
        2. subtract first element from sum
        3. Increment the start pointer
        
    c. res.append(window_end+1, window_start+1)
    
Time complexity:
O(N)
Space complexity: 
O(1)
"""
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        window_start = 0
        window_sum = 0
        res = []
       
        for window_end in range(0, n):
           window_sum += arr[window_end]
           while window_sum >= s:
               if window_sum==s:
                   res.extend([window_start+1, window_end+1])
                   return res
               window_sum -= arr[window_start]
               window_start += 1
               
        return [-1]
        
        
            
               
           
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
