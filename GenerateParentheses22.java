package leetcode_test;
import java.util.*;
public class GenerateParentheses22 {
	public static void main(String[] args) {
		int n = 3;
		Solution22 ss = new Solution22();
		System.out.println(ss.generateParenthesis(n));
		
	}
}
class Solution22 {
	 public List<String> generateParenthesis(int n) {
	        List<String> list = new ArrayList<String>();
	        backtrack(list, "", 0, 0, n);
	        return list;
	    }
	    
	    public void backtrack(List<String> list, String str, int open, int close, int max){
	        
	        if(str.length() == max*2){
	            list.add(str);
	            return;
	        }
	        
	        if(open < max)
	            backtrack(list, str+"(", open+1, close, max);
	        if(close < open)
	            backtrack(list, str+")", open, close+1, max);
	    }
}