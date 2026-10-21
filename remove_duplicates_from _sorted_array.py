class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # _sort_hash = {}

        # for num in nums:
        #     if _sort_hash.get(num) is None:
        #         _sort_hash[num] = 1
        #     else:
        #         _sort_hash[num] += 1
        
        # respArray = []
        # for key, value in _sort_hash.items():
        #     respArray.append(key)
        
        # return len(respArray)

        #find latest unique checking for the element behind firstRepetition
            #change the firstRepetition to be the current evaluated element
            #advance idx twice (+=1 and for iteration)
            #advance firstRepetition once
                #we need to evaluate the elements placed after the new latest
                #this assumes that there will be a repetition after the lastedUnique
                    #if there is no repetition
                        #we just replace it with the new latest, repeating the process
                    #else
                        #we do nothing and let the pointer iterate till it finds a new one
        #return firstRepetition since it will be the same number of unique elements

        firstRepetition = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[firstRepetition - 1]:
                nums[firstRepetition] = nums[idx]
                firstRepetition += 1
                idx += 1

        return latestUnique
        
