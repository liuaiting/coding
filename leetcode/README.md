[TOC]

# 排序算法

https://www.cnblogs.com/onepixel/articles/7674659.html

| 排序算法 | 时间复杂度(平均) | 时间复杂度(最坏) | 时间复杂度(最好) | 空间复杂度   | 稳定性 | 总结           |
| -------- | ---------------- | ---------------- | ---------------- | ------------ | ------ | -------------- |
| 插入排序 | $O(n^2)$         | $O(n^2)$         | $O( n ) $        | $O(1)$       | 稳定   | 插入排序.ipynb |
| 希尔排序 | $O(n^{1.3})$     | $O(n^2)$         | $O( n ) $        | $O(1)$       | 不稳定 |                |
| 选择排序 | $O(n^2)$         | $O(n^2)$         | $O(n^2)$         | $O(1)$       | 不稳定 | 选择排序.ipynb |
| 堆排序   | $O(nlog_2n)$     | $O(nlog_2n)$     | $O(nlog_2n)$     | $O(1)$       | 不稳定 | 堆排序.ipynb   |
| 冒泡排序 | $O(n^2)$         | $O(n^2)$         | $O( n ) $        | $O(1)$       | 稳定   | 冒泡排序.ipynb |
| 快速排序 | $O(nlog_2n)$     | $O(n^2)$         | $O(nlog_2n)$     | $O(nlog_2n)$ | 不稳定 | 快速排序.ipynb |
| 归并排序 | $O(nlog_2n)$     | $O(nlog_2n)$     | $O(nlog_2n)$     | $O( n ) $    | 稳定   | 归并排序.ipynb |
|          |                  |                  |                  |              |        |                |
| 计数排序 | $O(n+k)$         | $O(n+k)$         | $O(n+k)$         | $O(n+k)$     | 稳定   |                |
| 桶排序   | $O(n+k)$         | $O(n^2)$         | $O( n ) $        | $O(n+k)$     | 稳定   |                |
| 基数排序 | $O(n+k)$         | $O(n\times k)$   | $O(n \times k)$  | $O(n+k)$     | 稳定   |                |



# leetcode分类表

<https://cspiration.com/leetcodeClassification>

## Leetcode 分类顺序

### 1.3.1. Array

| 基础     |                                               |               |
| -------- | --------------------------------------------- | ------------- |
| 27       | Remove Element                                |               |
| 26       | Remove Duplicates from Sorted Array           |               |
| 80       | Remove Duplicates from Sorted Array II        |               |
| 277      | Find the Celebrity                            |               |
| 189      | Rotate Array                                  |               |
| 41       | First Missing Positive                        |               |
| 299      | Bulls and Cows                                |               |
| 134      | Gas Station                                   |               |
| 118      | Pascal's Triangle                             | 很少考        |
| 119      | Pascal's Triangle II                          | 很少考        |
| 169      | Majority Element                              | 很少考        |
| 229      | Majority Element II                           | 很少考        |
| 274      | H-Index                                       |               |
| 275      | H-Index II                                    | Binary Search |
| 243      | Shortest Word Distance                        |               |
| 244      | Shortest Word Distance II                     |               |
| 245      | Shortest Word Distance III                    |               |
| 217      | Contains Duplicate                            |               |
| 219      | Contains Duplicate II                         | 很少考        |
| 220      | Contains Duplicate III                        | 很少考        |
| 55       | Jump Game                                     |               |
| 45       | Jump Game II                                  |               |
| 121      | Best Time to Buy and Sell Stock               |               |
| 122      | Best Time to Buy and Sell Stock II            |               |
| 123      | Best Time to Buy and Sell Stock III           |               |
| 188      | Best Time to Buy and Sell Stock IV            |               |
| 309      | Best Time to Buy and Sell Stock with Cooldown |               |
| 11       | Container With Most Water                     |               |
| 42       | Trapping Rain Water                           |               |
| 334      | Increasing Triplet Subsequence                |               |
| 128      | Longest Consecutive Sequence                  |               |
| 164      | Maximum Gap                                   | Bucket        |
| 287      | Find the Duplicate Number                     |               |
| 135      | Candy                                         | 很少考        |
| 330      | Patching Array                                | 很少考        |
|          |                                               |               |
| 提高     |                                               |               |
| 4        | Median of Two Sorted Arrays                   |               |
| 321      | Create Maximum Number                         | 很少考        |
| 327      | Count of Range Sum                            | 很少考        |
| 289      | Game of Life                                  |               |
|          |                                               |               |
| Interval |                                               |               |
| 57       | Insert Interval                               |               |
| 56       | Merge Intervals                               |               |
| 252      | Meeting Rooms                                 |               |
| 253      | Meeting Rooms II                              |               |
| 352      | Data Stream as Disjoint Intervals             | TreeMap       |
|          |                                               |               |
| Counter  |                                               |               |
| 239      | Sliding Window Maximum                        |               |
| 295      | Find Median from Data Stream                  |               |
| 53       | Maximum Subarray                              |               |
| 325      | Maximum Size Subarray Sum Equals k            |               |
| 209      | Minimum Size Subarray Sum                     |               |
| 238      | Product of Array Except Self                  |               |
| 152      | Maximum Product Subarray                      |               |
| 228      | Summary Ranges                                |               |
| 163      | Missing Ranges                                |               |
|          |                                               |               |
| Sort     |                                               |               |
| 88       | Merge Sorted Array                            |               |
| 75       | Sort Colors                                   |               |
| 283      | Move Zeroes                                   |               |
| 376      | Wiggle Subsequence                            |               |
| 280      | Wiggle Sort                                   |               |
| 324      | Wiggle Sort II                                |               |



### 1.3.2. String

| 基础        |                                                        |                |
| ----------- | ------------------------------------------------------ | -------------- |
| 28          | Implement strStr()                                     |                |
| 14          | Longest Common Prefix                                  |                |
| 58          | Length of Last Word                                    |                |
| 387         | First Unique Character in a String                     |                |
| 383         | Ransom Note                                            |                |
| 344         | Reverse String                                         |                |
| 151         | Reverse Words in a String                              |                |
| 186         | Reverse Words in a String II                           |                |
| 345         | Reverse Vowels of a String                             |                |
| 205         | Isomorphic Strings                                     |                |
| 293         | Flip Game                                              |                |
| 294         | Flip Game II                                           |                |
| 290         | Word Pattern                                           |                |
| 242         | Valid Anagram                                          |                |
| 49          | Group Anagrams                                         |                |
| 249         | Group Shifted Strings                                  |                |
| 87          | Scramble String                                        |                |
| 179         | Largest Number                                         | 很少考         |
| 6           | ZigZag Conversion                                      | 很少考         |
| 161         | One Edit Distance                                      |                |
| 38          | Count and Say                                          |                |
| 358         | Rearrange String k Distance Apart                      |                |
| 316         | Remove Duplicate Letters                               |                |
| 271         | Encode and Decode Strings                              |                |
| 168         | Excel Sheet Column Title                               |                |
| 171         | Excel Sheet Column Number                              |                |
| 13          | Roman to Integer                                       |                |
| 12          | Integer to Roman                                       |                |
| 273         | Integer to English Words                               |                |
| 246         | Strobogrammatic Number                                 |                |
| 247         | Strobogrammatic Number II                              |                |
| 248         | Strobogrammatic Number III                             | 很少考         |
|             |                                                        |                |
| 提高        |                                                        |                |
| 68          | Text Justification                                     |                |
| 65          | Valid Number                                           |                |
| 157         | Read N Characters Given Read4                          |                |
| 158         | Read N Characters Given Read4 II - Call multiple times |                |
|             |                                                        |                |
| Substring   |                                                        |                |
| 76          | Minimum Window Substring                               | Sliding Window |
| 30          | Substring with Concatenation of All Words              | Sliding Window |
| 3           | Longest Substring Without Repeating Characters         | Sliding Window |
| 340         | Longest Substring with At Most K Distinct Characters   | Sliding Window |
| 395         | Longest Substring with At Least K Repeating Characters | Sliding Window |
| 159         | Longest Substring with At Most Two Distinct Characters | Sliding Window |
|             |                                                        |                |
| Palindrome  |                                                        |                |
| 125         | Valid Palindrome                                       |                |
| 266         | Palindrome Permutation                                 |                |
| 5           | Longest Palindromic Substring                          |                |
| 9           | Palindrome Number                                      |                |
| 214         | Shortest Palindrome                                    |                |
| 336         | Palindrome Pairs                                       |                |
| 131         | Palindrome Partitioning                                |                |
| 132         | Palindrome Partitioning II                             |                |
| 267         | Palindrome Permutation II                              |                |
|             |                                                        |                |
| Parentheses |                                                        |                |
| 20          | Valid Parentheses                                      |                |
| 22          | Generate Parentheses                                   |                |
| 32          | Longest Valid Parentheses                              |                |
| 241         | Different Ways to Add Parentheses                      |                |
| 301         | Remove Invalid Parentheses                             |                |
|             |                                                        |                |
| Subsequence |                                                        |                |
| 392         | Is Subsequence                                         |                |
| 115         | Distinct Subsequences                                  |                |
| 187         | Repeated DNA Sequences                                 | 很少考         |



### 1.3.3. Math

| 基础   |                                    |        |
| ------ | ---------------------------------- | ------ |
| 7      | Reverse Integer                    |        |
| 165    | Compare Version Numbers            |        |
| 66     | Plus One                           |        |
| 8      | String to Integer (atoi)           |        |
| 258    | Add Digits                         |        |
| 67     | Add Binary                         |        |
| 43     | Multiply Strings                   |        |
| 29     | Divide Two Integers                |        |
| 69     | Sqrt(x)                            |        |
| 50     | Pow(x, n)                          |        |
| 367    | Valid Perfect Square               |        |
| 365    | Water and Jug Problem              |        |
| 204    | Count Primes                       |        |
|        |                                    |        |
| Sum    |                                    |        |
| 1      | Two Sum                            |        |
| 167    | Two Sum II - Input array is sorted |        |
| 15     | 3Sum                               |        |
| 16     | 3Sum Closest                       | 很少考 |
| 259    | 3Sum Smaller                       | 很少考 |
| 18     | 4Sum                               |        |
|        |                                    |        |
| 很少考 |                                    |        |
| 231    | Power of Two                       |        |
| 326    | Power of Three                     |        |
| 342    | Power of Four                      |        |
| 372    | Super Pow                          |        |
| 233    | Number of Digit One                |        |
| 319    | Bulb Switcher                      |        |
| 292    | Nim Game                           |        |
| 202    | Happy Number                       |        |
| 400    | Nth Digit                          |        |
| 263    | Ugly Number                        |        |
| 264    | Ugly Number II                     |        |
| 306    | Additive Number                    |        |
| 172    | Factorial Trailing Zeroes          |        |
| 343    | Integer Break                      |        |
| 396    | Rotate Function                    |        |
| 390    | Elimination Game                   |        |
| 386    | Lexicographical Numbers            |        |
| 357    | Count Numbers with Unique Digits   |        |
| 360    | Sort Transformed Array             |        |
| 397    | Integer Replacement                |        |
| 368    | Largest Divisible Subset           |        |



### 1.3.4. Tree

| 基础      |                                                            |                      |
| --------- | ---------------------------------------------------------- | -------------------- |
| 144       | Binary Tree Preorder Traversal                             | preorder             |
| 94        | Binary Tree Inorder Traversal                              | Inorder              |
| 145       | Binary Tree Postorder Traversal                            | postorder            |
| 102       | Binary Tree Level Order Traversal                          | DFS + BFS            |
|           |                                                            |                      |
| Preorder  |                                                            |                      |
| 100       | Same Tree                                                  | preorder             |
| 101       | Symmetric Tree                                             | preorder             |
| 226       | Invert Binary Tree                                         | preorder + BFS       |
| 257       | Binary Tree Paths                                          | preorder             |
| 112       | Path Sum                                                   | preorder             |
| 113       | Path Sum II                                                | preorder             |
| 129       | Sum Root to Leaf Numbers                                   | preorder             |
| 298       | Binary Tree Longest Consecutive Sequence                   | preorder             |
| 111       | Minimum Depth of Binary Tree                               | preorder             |
|           |                                                            |                      |
| Postorder |                                                            |                      |
| 104       | Maximum Depth of Binary Tree                               | postorder            |
| 110       | Balanced Binary Tree                                       | postorder            |
| 124       | Binary Tree Maximum Path Sum                               | postorder            |
| 250       | Count Univalue Subtrees                                    | postorder            |
| 366       | Find Leaves of Binary Tree                                 | postorder            |
| 337       | House Robber III                                           | postorder + preorder |
|           |                                                            |                      |
| BFS       |                                                            |                      |
| 107       | Binary Tree Level Order Traversal II                       | BFS                  |
| 103       | Binary Tree Zigzag Level Order Traversal                   | BFS                  |
| 199       | Binary Tree Right Side View                                | BFS + preorder       |
|           |                                                            |                      |
| BST       |                                                            |                      |
| 98        | Validate Binary Search Tree                                | preorder             |
| 235       | Lowest Common Ancestor of a Binary Search Tree             | preorder             |
| 236       | Lowest Common Ancestor of a Binary Tree                    | postorder            |
| 108       | Convert Sorted Array to Binary Search Tree                 | binary search        |
| 109       | Convert Sorted List to Binary Search Tree                  | binary search        |
| 173       | Binary Search Tree Iterator                                | inorder              |
| 230       | Kth Smallest Element in a BST                              | inorder              |
| 297       | Serialize and Deserialize Binary Tree                      | BFS                  |
| 285       | Inorder Successor in BST                                   | inorder              |
| 270       | Closest Binary Search Tree Value                           | preorder             |
| 272       | Closest Binary Search Tree Value II                        | inorder              |
| 99        | Recover Binary Search Tree                                 | inorder              |
|           |                                                            |                      |
| 重要程度  |                                                            |                      |
| 156       | Binary Tree Upside Down                                    | 很少考               |
| 114       | Flatten Binary Tree to Linked List                         | 很少考               |
| 255       | Verify Preorder Sequence in Binary Search Tree             | 很少考               |
| 333       | Largest BST Subtree                                        | 很少考               |
| 222       | Count Complete Tree Nodes                                  | 很少考               |
| 105       | Construct Binary Tree from Preorder and Inorder Traversal  | 很少考               |
| 106       | Construct Binary Tree from Inorder and Postorder Traversal | 很少考               |
| 116       | Populating Next Right Pointers in Each Node                | 重要                 |
| 117       | Populating Next Right Pointers in Each Node II             | 重要                 |
| 314       | Binary Tree Vertical Order Traversal                       | 重要                 |
| 96        | Unique Binary Search Trees                                 | 重要                 |
| 95        | Unique Binary Search Trees II                              | 很少考               |
| 331       | Verify Preorder Serialization of a Binary Tree             | 很少考               |



### 1.3.5. Backtracking

| 基础        |                                       |                     |
| ----------- | ------------------------------------- | ------------------- |
| 78          | Subsets                               |                     |
| 90          | Subsets II                            |                     |
| 77          | Combinations                          |                     |
| 39          | Combination Sum                       |                     |
| 40          | Combination Sum II                    |                     |
| 216         | Combination Sum III                   |                     |
| 377         | Combination Sum IV                    | Dynamic Programming |
| 254         | Factor Combinations                   |                     |
| 46          | Permutations                          |                     |
| 47          | Permutations II                       |                     |
| 31          | Next Permutation                      | String              |
| 60          | Permutation Sequence                  | String              |
| 291         | Word Pattern II                       |                     |
|             |                                       |                     |
| Enumeration |                                       |                     |
| 17          | Letter Combinations of a Phone Number |                     |
| 320         | Generalized Abbreviation              | 要重录              |
| 93          | Restore IP Addresses                  | 很少考              |
| 282         | Expression Add Operators              |                     |
| 140         | Word Break II                         |                     |
| 351         | Android Unlock Patterns               |                     |



### 1.3.6. Dynamic Programming

blog: 

连续子序列 https://www.jianshu.com/p/b26773acfe18

| 一维 |                                       |         |      |
| ---- | ------------------------------------- | ------- | ---- |
| 70   | Climbing Stairs                       |         |      |
| 62   | Unique Paths                          |         |      |
| 63   | Unique Paths II                       |         |      |
| 120  | Triangle                              | 很少考  |      |
| 279  | Perfect Squares                       |         |      |
| 139  | Word Break                            |         |      |
| 375  | Guess Number Higher or Lower II       |         |      |
| 312  | Burst Balloons                        |         |      |
| 322  | Coin Change                           |         |      |
|      |                                       |         |      |
| 二维 |                                       |         |      |
| 256  | Paint House                           |         |      |
| 265  | Paint House II                        |         |      |
| 64   | Minimum Path Sum                      |         |      |
| 72   | Edit Distance                         |         |      |
| 97   | Interleaving String                   |         |      |
| 174  | Dungeon Game                          |         |      |
| 221  | Maximal Square                        |         |      |
| 85   | Maximal Rectangle                     |         |      |
| 363  | Max Sum of Rectangle No Larger Than K | TreeSet |      |
| 718  | Maximum Length of Repeated Subarray | $ dp[i][j]=\left\{\begin{aligned}dp[i-1][j-1] + 1 & &  if s1[i-1]==s2[j-1]\\ & & else\\\end{aligned}\right.$ |                                                              |
| 583  | Delete Operation for Two Strings    | $ dp[i][j]=\left\{\begin{aligned}dp[i-1][j-1] + 1 & &  if s1[i-1]==s2[j-1]\\max(dp[i][j-1], dp[i-1][j]) & & else\\\end{aligned}\right.$ |                                                              |
| 72   | Edit Distance                       | $ dp[i][j]=\left\{\begin{aligned} dp[i-1][j-1] & &  if s1[i-1]==s2[j-1]\\min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1 & & else\\ \end{aligned} \right.$ | [blog1](https://blog.csdn.net/zxzxzx0119/article/details/82054807) |
|      |                                       |         |      |
| 化简 |                                       |         |      |
| 198  | House Robber                          |         |      |
| 213  | House Robber II                       |         |      |
| 276  | Paint Fence                           |         |      |
| 91   | Decode Ways                           |         |      |
| 10   | Regular Expression Matching           |         |      |
| 44   | Wildcard Matching                     |         |      |



### 1.3.7. LinkedList

| 基础 |                                       |
| ---- | ------------------------------------- |
| 206  | Reverse Linked List                   |
| 141  | Linked List Cycle                     |
| 24   | Swap Nodes in Pairs                   |
| 328  | Odd Even Linked List                  |
| 92   | Reverse Linked List II                |
| 237  | Delete Node in a Linked List          |
| 19   | Remove Nth Node From End of List      |
| 83   | Remove Duplicates from Sorted List    |
| 203  | Remove Linked List Elements           |
| 82   | Remove Duplicates from Sorted List II |
| 369  | Plus One Linked List                  |
| 2    | Add Two Numbers                       |
| 160  | Intersection of Two Linked Lists      |
| 21   | Merge Two Sorted Lists                |
| 提高 |                                       |
| 234  | Palindrome Linked List                |
| 143  | Reorder List                          |
| 142  | Linked List Cycle II                  |
| 148  | Sort List                             |
| 25   | Reverse Nodes in k-Group              |
| 61   | Rotate List                           |
| 86   | Partition List                        |
| 23   | Merge k Sorted Lists                  |
| 147  | Insertion Sort List                   |
| 382  | Linked List Random Node               |



### 1.3.8. Binary Search

| 基础 |                                         |
| ---- | --------------------------------------- |
| 278  | First Bad Version                       |
| 35   | Search Insert Position                  |
| 33   | Search in Rotated Sorted Array          |
| 81   | Search in Rotated Sorted Array II       |
| 153  | Find Minimum in Rotated Sorted Array    |
| 154  | Find Minimum in Rotated Sorted Array II |
| 162  | Find Peak Element                       |
| 374  | Guess Number Higher or Lower            |
| 34   | Search for a Range                      |
| 349  | Intersection of Two Arrays              |
| 350  | Intersection of Two Arrays II           |
| 315  | Count of Smaller Numbers After Self     |
| 300  | Longest Increasing Subsequence          |
| 354  | Russian Doll Envelopes                  |



### 1.3.9. Matrix

| 48   | Rotate Image                              |
| ---- | ----------------------------------------- |
| 54   | Spiral Matrix                             |
| 59   | Spiral Matrix II                          |
| 73   | Set Matrix Zeroes                         |
| 311  | Sparse Matrix Multiplication              |
| 329  | Longest Increasing Path in a Matrix       |
| 378  | Kth Smallest Element in a Sorted Matrix   |
| 74   | Search a 2D Matrix                        |
| 240  | Search a 2D Matrix II                     |
| 370  | Range Addition                            |
| 79   | Word Search                               |
| 296  | Best Meeting Point                        |
| 361  | Bomb Enemy                                |
| 317  | Shortest Distance from All Buildings      |
| 302  | Smallest Rectangle Enclosing Black Pixels |
| 36   | Valid Sudoku                              |
| 37   | Sudoku Solver                             |



### 1.3.10. DFS & BFS

| 基础 |                           |      |
| ---- | ------------------------- | ---- |
| 200  | Number of Islands         |      |
| 286  | Walls and Gates           |      |
| 130  | Surrounded Regions        |      |
| 339  | Nested List Weight Sum    |      |
| 364  | Nested List Weight Sum II |      |
| 127  | Word Ladder               |      |
| 51   | N-Queens                  |      |
| 52   | N-Queens II               |      |
| 126  | Word Ladder II            |      |



### 1.3.11. Stack & PriorityQueue

| Stack         |                                  |        |
| ------------- | -------------------------------- | ------ |
| 155           | Min Stack                        |        |
| 232           | Implement Queue using Stacks     |        |
| 225           | Implement Stack using Queues     |        |
| 150           | Evaluate Reverse Polish Notation |        |
| 71            | Simplify Path                    |        |
| 388           | Longest Absolute File Path       |        |
| 394           | Decode String                    |        |
| 224           | Basic Calculator                 |        |
| 227           | Basic Calculator II              |        |
| 385           | Mini Parser                      |        |
| 84            | Largest Rectangle in Histogram   |        |
|               |                                  |        |
| PriorityQueue |                                  |        |
| 215           | Kth Largest Element in an Array  |        |
| 347           | Top K Frequent Elements          |        |
| 313           | Super Ugly Number                | 很少考 |
| 373           | Find K Pairs with Smallest Sums  | 很少考 |
| 218           | The Skyline Problem              |        |
| 332           | Reconstruct Itinerary            |        |
| 341           | Flatten Nested List Iterator     |        |



### 1.3.12. Bit Manipulation

| 基础   |                                 |
| ------ | ------------------------------- |
| 389    | Find the Difference             |
| 136    | Single Number                   |
| 318    | Maximum Product of Word Lengths |
|        |                                 |
| 很少考 |                                 |
| 393    | UTF-8 Validation                |
| 201    | Bitwise AND of Numbers Range    |
| 371    | Sum of Two Integers             |
| 338    | Counting Bits                   |
| 89     | Gray Code                       |
| 268    | Missing Number                  |
| 191    | Number of 1 Bits                |
| 190    | Reverse Bits                    |
| 137    | Single Number II                |
| 260    | Single Number III               |



### 1.3.13. Topological Sort

| 基础 |                    |
| ---- | ------------------ |
| 207  | Course Schedule    |
| 210  | Course Schedule II |
| 269  | Alien Dictionary   |



### 1.3.14. Random

| 基础 |                                                   |
| ---- | ------------------------------------------------- |
| 模板 | Reservoir Sampling                                |
| 384  | Shuffle an Array                                  |
| 398  | Random Pick Index                                 |
| 382  | Linked List Random Node                           |
| 380  | Insert Delete GetRandom O(1)                      |
| 381  | Insert Delete GetRandom O(1) - Duplicates allowed |
| 138  | Copy List with Random Pointer                     |



### 1.3.15. Graph

| 基础   |                      |        |
| ------ | -------------------- | ------ |
| 133    | Clone Graph          |        |
| 399    | Evaluate Division    |        |
| 310    | Minimum Height Trees |        |
|        |                      |        |
| 图形学 |                      |        |
| 335    | Self Crossing        | 很少考 |
| 149    | Max Points on a Line |        |
| 356    | Line Reflection      | 很少考 |
| 391    | Perfect Rectangle    | 很少考 |
| 223    | Rectangle Area       | 很少考 |



### 1.3.16. Union FInd

| 基础 |                                                       |
| ---- | ----------------------------------------------------- |
| 261  | Graph Valid Tree                                      |
| 323  | Number of Connected Components in an Undirected Graph |
| 305  | Number of Islands II                                  |



### 1.3.17. Trie

| 基础 |                                             |
| ---- | ------------------------------------------- |
| 211  | Add and Search Word - Data structure design |
| 208  | Implement Trie (Prefix Tree)                |
| 212  | Word Search II                              |



### 1.3.18. Design

| 基础 |                                     |                   |
| ---- | ----------------------------------- | ----------------- |
| 359  | Logger Rate Limiter                 |                   |
| 346  | Moving Average from Data Stream     | Sliding Window    |
| 362  | Design Hit Counter                  |                   |
| 281  | Zigzag Iterator                     |                   |
| 284  | Peeking Iterator                    |                   |
| 251  | Flatten 2D Vector                   |                   |
| 288  | Unique Word Abbreviation            |                   |
| 170  | Two Sum III - Data structure design |                   |
| 348  | Design Tic-Tac-Toe                  |                   |
| 379  | Design Phone Directory              |                   |
| 353  | Design Snake Game                   |                   |
| 146  | LRU Cache                           |                   |
| 355  | Design Twitter                      |                   |
| 303  | Range Sum Query - Immutable         |                   |
| 304  | Range Sum Query 2D - Immutable      |                   |
| 307  | Range Sum Query - Mutable           | Binary Index Tree |
| 308  | Range Sum Query 2D - Mutable        | Binary Index Tree |