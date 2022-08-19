# 659. Split Array into Consecutive Subsequences 
# You are given an integer array nums that is sorted in non-decreasing order.
# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:
# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.
# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        a = []
        i = -1
        j = -1
        n_prev = nums[0]
        nums.append(1001)
        n_list = []
        while nums!=[]:
            n = nums.pop(0)
            if n == n_prev:
                n_list.append(n)
            else:
                if i ==-1:
                    for z in range(len(n_list)):
                        a.append([n_prev])
                    i=0
                    j = len(n_list) -1 
                elif i == j:
                    for z in range(len(n_list)):
                        if (z==0):
                            a[i].append(n_prev)
                        else:
                            a.append([n_prev])
                    j = i + len(n_list) -1
                elif (j - i) > len(n_list) -1:
                    i = j - len(n_list) +1
                    for z in range(len(n_list)):
                        a[i+z].append(n_prev)
                else:
                    for z in range(len(n_list)):
                        if j > (i+z):
                            a[i+z].append(n_prev)
                        elif j == (i+z):
                            a[j].append(n_prev)
                        else:
                            a.append([n_prev])
                    j = i + len(n_list) -1
                    
                if n > (n_prev+1) and n!=1001:
                    j = j + 1
                    i = j
                    a.append([])
                n_prev = n
                n_list = [n]

        for i in range(len(a)):
            print(a[i])
            if len(a[i]) < 3:
                return False
            
        return True
