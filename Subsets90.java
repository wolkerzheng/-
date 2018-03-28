package java_test;

import java.util.*;

public class Subsets90 {
	public static void main(String[] args) {
		Solution90 s = new Solution90() ;
		int []nums = {1,2,2};
//		s.subsetsWithDup(nums);
		System.out.println(s.subsetsWithDup(nums));
	}
	class Solution90 {
	    public List<List<Integer>> subsetsWithDup(int[] nums) {
	    	List<List<Integer>> res = new ArrayList<>();
	    	
	    	Arrays.sort(nums);
	        backtrack(res,new ArrayList<>(),nums,0);
	        return res;
	    }

		private void backtrack(List<List<Integer>> res, ArrayList tmp, int[] nums, int s) {
			// TODO Auto-generated method stub
			res.add(new ArrayList<>(tmp));
			for(int i=s;i<nums.length;i++){
				if(i>s && nums[i]==nums[i-1]) continue;
				tmp.add(nums[i]);
				backtrack(res, tmp, nums, i+1);
				tmp.remove(tmp.size()-1);
			}
		}
	}
}
