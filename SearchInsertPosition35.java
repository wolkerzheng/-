package java_test;

public class SearchInsertPosition35 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	class Solution {
	    public int searchInsert(int[] nums, int target) {
	        if(nums.length==0){
	        	return 0;
	        }
	        int low = 0,high = nums.length-1;
	        while(low<=high){
	        	int mid = (low+high)/2;
	        	if(nums[mid]==target) return mid;
	        	else if(nums[mid]<target) low = mid+1;
	        	else high = mid-1;
	        	
	        }
	        return low;
	    }
	}
}
