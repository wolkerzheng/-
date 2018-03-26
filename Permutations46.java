package java_test;

import java.util.*;
/**
 * »ØËİÎÊÌâ
 * @author Administrator
 *
 */
public class Permutations46 {
	
	public static void main(String[] args) {
		Solution s = new Solution();
		int[] nums = {1,2,3};
		s.permute(nums);
	}
	
	class Solution {
	    public List<List<Integer>> permute(int[] nums) {
	        ArrayList<List<Integer>> res = new ArrayList<>();
	        
	        backtrack(res, new ArrayList<>(), nums);
	        return res;
	        
//	        return res;
	    }
	    public void backtrack(List<List<Integer>> res,  List<Integer> tempList,int[] nums){
	    	if(tempList.size()==nums.length){
	    		res.add(new ArrayList<>(tempList));
	    	}
	    	else
	    	{
	    		for(int i=0;i<nums.length;i++){
	    			if(tempList.contains(nums[i])) continue; // element already exists, skip
	    	         tempList.add(nums[i]);
	    	         backtrack(res, tempList, nums);
	    	         tempList.remove(tempList.size() - 1);
	    		}
	    	}
	    }
	}
}
