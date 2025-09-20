
#1 Duplicate values
   # finding the duplicate number

def has_duplicate(nums):
    if len(set(nums)) == len(nums):
     return False
    else:
        return True

nums = [1, 2, 3, 1]
print(has_duplicate(nums))


#---------------------------------------------


# 2.Finding all number disappeared in an Array

def findDisappearedNumbers(nums):
    set_nums = set(nums)
    arr = []

    for i in range(1,len(nums)+1):

        if i not in set_nums:
            arr.append(i)
    return arr
nums = [4, 3, 2, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))  


#---------------------------------------------


# 3. Two sum number

# #Hash  map

class Solution(object):
    def twoSum(self, nums, target):

        hashMap = {} #val: index

        for index, val in enumerate(nums):
            diff = target - val

            if diff in hashMap:
                return[index, hashMap[diff]]
            hashMap[val] = index
s=Solution()
print(s.twoSum([2,7,11,15], 9))  



#---------------------------------------------

# 4. How many number are smaller than the current number

def smallerNumbersThanCurrent(nums):
    temp = sorted(nums)
    d={}

    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i
    ret = []
    for i in nums:
        ret.append(d[i])
    return ret

nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))   


#---------------------------------------------

# 5 Single number
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor^= num
        return xor

s = Solution()
nums = [4, 1, 2, 1, 2,4,6]
print(s.singleNumber(nums))

#---------------------------------------------
# 6 coinchange

def coinchange(coins, amount):

    dp = [amount+1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount+1):
        for c in coins:
            if (i - c) >=0:
                dp[i] = min(dp[i], 1 + dp[i -c])
    return dp[amount] if (dp[amount] != amount+1) else -1
print(coinchange([1, 2, 5], 11))



#---------------------------------------------
# 7 climbing stairs

def steps(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range (3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
print(steps(4))

#---------------------------------------------
#8 Maxsum subarray

def maxSubArray(arr):
    maxSum = arr[0]
    currentSum = 0

    for n in arr:
        if currentSum < 0:
            currentSum = 0

        currentSum += n
        maxSum = max(maxSum, currentSum)
    return maxSum

arr = [-2, 1, -3, -1, 2, 1, -5]
print(maxSubArray(arr))


#---------------------------------------------
#9. counting bits

def countingBits(n):

    dp = [0] * (n+1)
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp
print(countingBits(5))  


#---------------------------------------------
#10.subset 

def subsets(nums):
    def backtrack(start, path):

        result.append(path[:])
        for i in range(start, len(nums)):

            path.append(nums[i])
            backtrack(i +1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result
nums = [1, 2, 3]
print(subsets(nums))


#---------------------------------------------
#11.combination

def combine(n,k):
    def backtrack(start, path):

        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()

    result = []
    backtrack(1, [])
    return result 
print(combine(4,2))