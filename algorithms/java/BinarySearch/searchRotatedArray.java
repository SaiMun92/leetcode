class Solution {
    public int search(int[] nums, int target) {
        //edge cases
        if(nums == null || nums.length == 0) return -1;
        
        //running slightly modified binary search
        //The idea is that for any rotated sorted array splitted at index 'mid' either left or right half is sorted 
        int start = 0;
        int end = nums.length - 1;
        
        while(start <= end) {
            int mid = (start + end) / 2;
            
            //if we're lucky and mid is the answer
            if(nums[mid] == target) return mid;
            
            //if left half is sorted
            if(nums[start] <= nums[mid]) {
                //if target is in left half -> search there
                //else -> search in right half
                if(target >= nums[start] && target < nums[mid]) {
                    end = mid -1;
                } else {
                    start = mid + 1;
                }
                //if the right half is sorte
            } else {
                //if target is in the right half -> search there
                //else -> search in left half
                if(target <= nums[end] && target > nums[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        
        //default -> when we didn't find any solution
        return -1;
    }
}

