package leetcode_test;

import java.util.*;

public class LetterCombinations {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution17 ss = new Solution17();
		System.out.println(ss.letterCombinations("234"));
	}

}
class Solution17 {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits.length()==0){
        	return res;
        }
        StringBuffer sb = new StringBuffer();
        
        String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(res,sb,digits,mapping,0);
        return res;
    }

	private void backtrack(List<String> res, StringBuffer sb, String digits, String[] mapping, int idx) {
		if(idx==digits.length()){
			res.add(sb.toString());
			return;
		}
		String tmp = mapping[digits.charAt(idx)-'0'];
		for(char cc : tmp.toCharArray() ){
			sb.append(cc);
			backtrack(res,sb,digits,mapping,idx+1);
			sb.deleteCharAt(sb.length()-1);
		}
		
	}
    
}