package leetcode_test;

public class MergeTwoBinaryTrees617 {
	public static void main(String[] args) {
		
	}
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x){
		val = x;
	}
}
class Solution617 {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if(t1 == null && t2 == null)
        	return null;
        else if(t1 != null && t2 != null){
        	t1.val = t1.val+t2.val;
        	t1.left = mergeTrees(t1.left,t2.left);
        	t1.right = mergeTrees(t1.right,t2.right);
        	return t1;
        }
        else if(t1 == null && t2 != null){
        	return t2;
        }
        else{
        	return t1;
        }
    }
    public TreeNode mergeTreesSolution(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return null;
        
        int val = (t1 == null ? 0 : t1.val) + (t2 == null ? 0 : t2.val);
        TreeNode newNode = new TreeNode(val);
        
        newNode.left = mergeTrees(t1 == null ? null : t1.left, t2 == null ? null : t2.left);
        newNode.right = mergeTrees(t1 == null ? null : t1.right, t2 == null ? null : t2.right);
        
        return newNode;
    }

}