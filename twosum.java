/**
 * @Copyright (C) 2015 Harbin Institute of Technology
 * @Progect: LeetCode
 * @Package twosum
 * @Author 郑桂东
 * @Date 2015年1月27日 上午10:54:15
 */
package twosum;

import java.util.HashMap;

/**
 * @Class: Solution
 * @Date 2015年1月27日 上午10:54:15
 * @Author 郑桂东
 * @Version
 */
public class Solution {
	public static void main(String[] args) {
		int[] numbers = { 7, 75, 25 };
		int target = 100;
		int[] result = twoSum(numbers, target);
		for (int i = 0; i < result.length; i++) {
			System.out.println(result[i]);
		}
	}

	public static int[] twoSum(int[] numbers, int target) {
		HashMap<Integer, Integer> mymap = new HashMap<Integer, Integer>();
		int[] result = new int[2];
		int i, j = 0;
		for (i = 0; i < numbers.length; i++) {
			mymap.put(numbers[i], i);
		}
		for (i = 0; i < numbers.length; i++) {
			if (mymap.containsKey(target - numbers[i]) == true) {
				if (mymap.get(target - numbers[i]) != i) {
					j = mymap.get(target - numbers[i]);
					break;
				}
			}
		}
		result[0] = i + 1;
		result[1] = j + 1;
		return result;
	}
}
