package leetcode_test;
import java.util.*;
public class BinaryTreeInorderTraversal94 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
class Solution94 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null)
            return res;
        inorderTraversalHelp(res,root);
        return res;
    }

	private void inorderTraversalHelp(List<Integer> res, TreeNode root) {
		// TODO Auto-generated method stub
		if(root.left!=null) inorderTraversalHelp(res,root.left);
		res.add(root.val);
		if(root.right!=null) inorderTraversalHelp(res,root.right);
	}
	public List<Integer> inorderTraversal1(TreeNode root) {
		List<Integer> list = new ArrayList<Integer>();

	    Stack<TreeNode> stack = new Stack<TreeNode>();
	    TreeNode cur = root;

	    while(cur!=null || !stack.empty()){
	        while(cur!=null){
	            stack.add(cur);
	            cur = cur.left;
	        }
	        cur = stack.pop();
	        list.add(cur.val);
	        cur = cur.right;
	    }

	    return list;
    }
}