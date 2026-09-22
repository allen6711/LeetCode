<h2><a href="https://leetcode.com/problems/group-anagrams">49. Group Anagrams</a></h2><h3>Medium</h3><hr><p>Given an array of strings <code>strs</code>, group the <span data-keyword="anagram">anagrams</span> together. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;eat&quot;,&quot;tea&quot;,&quot;tan&quot;,&quot;ate&quot;,&quot;nat&quot;,&quot;bat&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;bat&quot;],[&quot;nat&quot;,&quot;tan&quot;],[&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is no string in strs that can be rearranged to form <code>&quot;bat&quot;</code>.</li>
	<li>The strings <code>&quot;nat&quot;</code> and <code>&quot;tan&quot;</code> are anagrams as they can be rearranged to form each other.</li>
	<li>The strings <code>&quot;ate&quot;</code>, <code>&quot;eat&quot;</code>, and <code>&quot;tea&quot;</code> are anagrams as they can be rearranged to form each other.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;&quot;]]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;a&quot;]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

<br><br>
Problem-Solving Approach

“We need to group strings that are anagrams of each other.

Two strings are anagrams if they contain exactly the same characters with exactly the same frequencies, just in a different order.

So what I need is a canonical representation, or a signature, that is identical for all strings belonging to the same anagram group.”

nterview Explanation

“One straightforward way is to sort every string.

For example, eat, tea, and ate all become aet after sorting, so I can use the sorted string as the key in a hash map.”

Coding Walkthrough

“I’ll maintain a dictionary where the key is the sorted version of the string, and the value is a list of original strings that share that key.

For each string, I sort it to generate the key.

If this key hasn’t appeared before, I initialize a new list.

Then I append the original string to its corresponding group.

Finally, I return all the values from the dictionary.”

Time and Space Complexity

Let:

n = number of strings
k = maximum length of a string

“If there are n strings and each string has length up to k, sorting each string costs O(k log k).

Therefore, the total time complexity is O(n times k log k).

The space complexity is O(n times k), including the hash map and the grouped strings.”

Approach 2: Character Frequency Array
Core Idea

Since the problem only contains lowercase English letters, each string can be represented by a fixed-size array of 26 character counts.

For example:

eat
↓
a: 1
e: 1
t: 1

Frequency Signature
↓
(1, 0, 0, 0, 1, ..., 1, ...)

All anagrams produce the same frequency signature.
Interview Explanation

“Since the problem only contains lowercase English letters, we can avoid sorting and use a fixed-size frequency array of length 26 as the signature.

That reduces processing each string from O(k log k) to O(k).”
Coding Walkthrough

“Because the input only contains lowercase English letters, I can represent each string using a frequency array of size 26.

For each character, I increment the corresponding position using ord(char) - ord('a').

All anagrams will produce exactly the same frequency array.

Since Python lists are mutable and cannot be used as dictionary keys, I convert the frequency array into a tuple.

Then I use that tuple as the key and append the original string to the corresponding group.”

Time and Space Complexity

“For each string, I visit each character exactly once.

So if there are n strings with maximum length k, the time complexity is O(n times k).

The extra space for each frequency array is O(26), which is constant, while the overall output and hash map require O(n times k) space.”
