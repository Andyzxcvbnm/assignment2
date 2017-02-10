class Solution(object):
    def majorityElement(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)                                           # the length of nums
        n = a/2                                                 # n is given a value as a standard and a half of the length of nums 
        i = 0                                                   # set up a variable i. start from zero 
        d = {}                                                  # set up a dictionary
        while i < a:                                            # use while as a loop. if the condition is true, it will operate the first part
            number = nums[i]                                    # set up a variable number that is equal to the value of the i element in nums 
            if number not in d:                                 # this if loop is a condition that cannot count majority elements,which means the d is contain all the elements in number. 
                d[number] = 1 
            else:                                               # ANOTHER CONDITION THAT CAN ACHIEVE THE GOAL 
                d[number] += 1                                  # count one more in d 
                if d[number] > n:                               
                    return number
            i += 1
            return number
        else:
            return 0
                
