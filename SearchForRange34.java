package leetcode_test;

import javax.net.ssl.SSLContext;

public class SearchForRange34 {
	
	public static void main(String[] args) {
		Solution34 ss = new Solution34();
		int []nums = {5, 7, 7, 8, 10};
		int target = 8;
		int []res = ss.searchRange(nums,target);
		for(int i :res)
			System.out.println(i);
	}
}
class Solution34 {
    public int[] searchRange(int[] nums, int target) {
    	int[]res = {-1,-1};
    	if(nums.length==0) return res;
    	int start=0,end=nums.length-1;
    	while(start<=end){
    		int mid = start + (end-start)/2;
    		if(nums[mid]==target){
    			res[0]=mid;
    			res[1]=mid;
    			while(res[0]-1>=start && nums[res[0]-1]==target)res[0] = res[0]-1;
    			while(res[1]+1<=end &&  nums[res[1]+1]==target) res[1]= res[1]+1;
    			break;
    			
    		}else if(nums[mid]<target)
    			start = mid+1;
    		else
    			end = mid-1;
    	}
    	return res;
    }
    public int[] searchRange2(int[] A, int target) {
		int start = firstGreaterEqual(A, target);
		if (start == A.length || A[start] != target) {
			return new int[]{-1, -1};
		}
		return new int[]{start, firstGreaterEqual(A, target + 1) - 1};
	}

	//find the first number that is greater than or equal to target.
	//could return A.length if target is greater than A[A.length-1].
	//actually this is the same as lower_bound in C++ STL.
	private  int firstGreaterEqual(int[] A, int target) {
		int low = 0, high = A.length;
		while (low < high) {
			int mid = low + ((high - low) >> 1);
			//low <= mid < high
			if (A[mid] < target) {
				low = mid + 1;
			} else {
				//should not be mid-1 when A[mid]==target.
				//could be mid even if A[mid]>target because mid<high.
				high = mid;
			}
		}
		return low;
	}
}