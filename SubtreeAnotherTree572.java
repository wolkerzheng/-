package leetcode_test;

public class SubtreeAnotherTree572 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
class Solution572 {
    public boolean isSubtree(TreeNode s, TreeNode t) {
    	boolean res = false;
        if(s==null && t== null)
        	return true;
        else if (s!=null && t!=null){
        	if(s.val==t.val)
        		res =isSubtree(s.left,t.left)&&isSubtree(s.right,t.right);
        	if(res==true)
        		return res;
        	res = res || isSubtree(s.left,t)||isSubtree(s.right,t);
        }

        return res;
    }
}