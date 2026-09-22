<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?  

<br><br>

Problem-Solving Approach

“Let me first restate the problem to make sure I understand it correctly.

We’re given an integer array nums and a target value, and we need to return the indices of two different elements whose sum equals the target.

A straightforward solution would be to check every pair of numbers. That would take O(n squared) time and O(1) extra space.

We can improve this to O(n) time using a hash map.

The key observation is that when I’m looking at a number x, I know exactly what number I need: target - x.

So as I iterate through the array, I’ll check whether this complement has already appeared in the hash map.

If it has, then I’ve found the answer, and I can return the stored index together with the current index.

Otherwise, I store the current number and its index in the hash map and continue.”

Coding Walkthrough

“I’ll use a dictionary called seen to map each number to its index.

For every number, I calculate the complement.

Importantly, I check the complement before inserting the current number. This guarantees that I don’t accidentally use the same element twice.

If the complement already exists, I return its index and the current index.

Otherwise, I store the current number and continue.”

Time and Space Complexity

“The time complexity is O(n), because we scan the array once, and hash map lookup and insertion are O(1) on average.

The space complexity is O(n) in the worst case because we may store every element in the hash map.”
