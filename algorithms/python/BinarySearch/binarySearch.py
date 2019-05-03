def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# nums = [1,3,4,6,7,9,12,15] target = 9
# right = 7
# left = 0
# mid = 3
# nums[3] = 6
# left = 3 + 1 = 4 # reduce the list by half
# right = 7
# mid = 5
# nums[5] = 9