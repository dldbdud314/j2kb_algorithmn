def numIdenticalPairs(nums) -> int:
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                cnt += 1
    return cnt

print(numIdenticalPairs([1,2,3,1,1,3]))