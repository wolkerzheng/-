package leetcode_test;

public class MergeKList {

}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution23 {
    public ListNode mergeKLists(ListNode[] lists) {
        int len = lists.length;
        return mergeListHelp(lists,0,len-1);
    }

	private ListNode mergeListHelp(ListNode[] lists, int s, int e) {
		// TODO Auto-generated method stub
		if(s==e) return lists[s];
		if(s<e){
			int mid = s+(e-s)/2;
			ListNode leftlist  = mergeListHelp(lists,s,mid); 
			ListNode rightlist = mergeListHelp(lists,mid+1,e);
			return combinelist(leftlist,rightlist);
		}
		else return null;
		
	}

	private ListNode combinelist(ListNode leftlist, ListNode rightlist) {
		// TODO Auto-generated method stub
		ListNode tmphead = new ListNode(-1);
		ListNode tmp = tmphead;
		
		while(leftlist!=null && rightlist!=null){
			if(leftlist.val<rightlist.val){
				tmphead.next = leftlist;
				leftlist = leftlist.next;
			}else{
				tmphead.next =rightlist;
				rightlist = rightlist.next;
			}
			tmphead = tmphead.next;
		}
		if(leftlist!=null){
			tmphead.next = leftlist;
		}
		if(rightlist!=null){
			tmphead.next = rightlist;
		}
		return tmp.next;
		
	}
	public static ListNode merge(ListNode l1,ListNode l2){
	    if(l1==null) return l2;
	    if(l2==null) return l1;
	    if(l1.val<l2.val){
	        l1.next=merge(l1.next,l2);
	        return l1;
	    }else{
	        l2.next=merge(l1,l2.next);
	        return l2;
	    }
	}
    
}
class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
} 