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
        	res = isSubtree(s.left,t)||isSubtree(s.right,t);
        }
        
        return res;
    }
    public boolean isSubtreeS(TreeNode s, TreeNode t) {
        if (s == null) return false;
        if (isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        
        if (s.val != t.val) return false;
        
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}