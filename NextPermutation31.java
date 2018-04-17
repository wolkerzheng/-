package leetcode_test;

public class NextPermutation31 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
class Solution31 {
    public void nextPermutation(int[] nums) {
        if(nums.length<=1){
        	return ;
        }
        int idx = nums.length-1;
        while(idx>0){
        	 if(nums[idx]>nums[idx-1]){ //find first number which is smaller than it's after number
                 break;
             }
        	 idx--;
        }
        if(idx==0){
        	reverse(nums,0,nums.length-1);
        }else{
        	int val=nums[idx-1];
            int j=nums.length-1;
            while(j>=idx){
                if(nums[j]>val)
                    break;
                j--;
            }
            swap(nums,j,idx-1);
            reverse(nums,idx,nums.length-1);
            return;
        }
    }

	private void reverse(int[] nums, int start, int end) {
		// TODO Auto-generated method stub
		if(start>end) return;
		for(int i=start;i<=start+(end-start)/2;i++){
			swap(nums,i,start+end-i);
		}
	}

	private void swap(int[] nums, int i, int j) {
		// TODO Auto-generated method stub
	    int temp=nums[i];
	    nums[i]=nums[j];
	    nums[j]=temp;
	}
}