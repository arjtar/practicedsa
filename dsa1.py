
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

#Single number
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
#coinchange

def coinchange(coins, amount):

    dp = [amount+1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount+1):
        for c in coins:
            if (i - c) >=0:
                dp[i] = min(dp[i], 1 + dp[i -c])
    return dp[amount] if (dp[amount] != amount+1) else -1
print(coinchange([1, 2, 5], 11))






 
