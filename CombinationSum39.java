package leetcode_test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CombinationSum39 {
	public static void main(String[] args) {
		int nums[]={10, 1, 2, 7, 6, 1, 5};
		Solution s = new Solution();
		System.out.println(s.combinationSum2(nums, 8));
	}
}
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
    	List<List<Integer>> res = new  ArrayList<>();
    	Arrays.sort(candidates);
    	backtrack(res,new ArrayList<>(),candidates,target,0);
    	return res;
    }

	private void backtrack(List<List<Integer>> res, ArrayList tmp, int[] candidates, int target, int s) {
		// TODO Auto-generated method stub
		if(target<0) return;
		if(tmp.size()!=0 && target == 0){
			res.add(new ArrayList<>(tmp));
		}
		for(int i=s;i<candidates.length;i++){
			 if(i > s && candidates[i] == candidates[i-1]) continue; 
			 
				tmp.add(candidates[i]);
				backtrack(res, tmp, candidates, target-candidates[i], i+1);
				tmp.remove(tmp.size()-1);
			
		}
	}
    
}