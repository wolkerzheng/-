package java_test;
 /*

LCP(S_1... S_n) = LCP(LCP(LCP(S_1, S_2),S_3),...S_n)

  * */
public class LongestCommonPrefix14 {
	
//	System.out.println('hello');
	public static void main(String[] args) {
		Solution s = new Solution();
		String []p = {"a"};
		
		
		String res = s.longestCommonPrefix(p);
//		System.out.println("hello world");
		System.out.println(res);
	}
}
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0){
        	return "";
        }
        String res = strs[0];
        
        for(int i = 1;i<strs.length;i++)
        {	//寻找是否包含res这个的串，如果有，返回串最开始的起点，本题的最长前缀则起点为0的。
        	while(strs[i].indexOf(res)!=0){
        		res = res.substring(0, res.length()-1);
        		if(res.isEmpty()) return "";
        	}
        }
    	return res;
    }
}