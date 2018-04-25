package leetcode_test;

import java.util.*;

public class FindDisappeared448 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int []tmp = new int[5]; ≥ı ºªØ
//		for(int i:tmp)
//			System.out.println(i);
	}

}
class Solution448 {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
    	if(nums==null) return null;
        List<Integer> res = new ArrayList<Integer>();
    	int len = nums.length;
    	int []tmp = new int[len];
    	for(int i=0;i<len;i++){
    		tmp[nums[i]-1] +=1;
    	}
    	for(int i=0;i<len;i++)
    	{
    		if(tmp[i]==0)
    			res.add(i+1);
    	}
        return res;
    }
    public List<Integer> findDisappearedNumbers11(int[] nums) {
        List<Integer> ret = new ArrayList<Integer>();
        
        for(int i = 0; i < nums.length; i++) {
            int val = Math.abs(nums[i]) - 1;
            if(nums[val] > 0) {
                nums[val] = -nums[val];
            }
        }
        
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] > 0) {
                ret.add(i+1);
            }
        }
        return ret;
    }
}