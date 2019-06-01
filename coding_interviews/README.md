# 剑指offer

|        | 题目                           | 思路                                                         |
| ------ | ------------------------------ | ------------------------------------------------------------ |
| 3      | 二维数组中的查找               | 从右上角或者左下角开始找                                     |
| 4      | 替换空格                       | 用re.replace()                                               |
| 5      | 从尾到头打印链表               | 遍历存储在一个数组中，再翻转                                 |
| 6      | 重建二叉树                     | 根据前序遍历和中序遍历的结果重建二叉树：前序遍历的第一个是根节点；中序遍历的根节点的左边是左子树，右边是右子树；递归 |
| 7      | 用两个栈实现队列               | stack1入队列用，stack2出队列用；入队列时压入stack1栈顶，出队列时，先把stack1全部出栈到stack2，此时stack2的栈顶就是要出队列的值，pop出栈，然后再把stack2全部出栈到stack1 |
| 8      | 旋转数组的最小数字             | 二分查找；两个指针，第一个指向第一段递增子数组，第二个指向第二个递增子数组，最终第一个指针指向前面子数组的最后一个元素，第二个指针指向后面子数组的第一个元素。也就是它们最终会指向两个相邻的元素，而第二个指针指向的刚好是最小的元素(注意是否有重复数字) |
| 9-1    | 斐波那契数列                   | 动态规划; f(n) = f(n-1) + f(n-2)， f(0) = 0, f(1)=1, f(2) = 1 |
| 9-2    | 跳台阶                         | 动态规划; f(n) = f(n-1) + f(n-2)， f(0) = 0, f(1)=1, f(2)=2  |
| 9-3    | 变态跳台阶                     | 2**(n-1)                                                     |
| 9-4    | 矩形覆盖                       | 动态规划; f(n) = f(n-1) + f(n-2)， f(0) = 0, f(1)=1, f(2)=2  |
| 10     | 二进制中1的个数                | 把一个整数减去1，再和原整数做与运算，会把该整数最右边的一个1变成0。那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。(注意负数的情况：python要使用`n & 0xffffffff`得到一个数的补码) |
| 11     | 数值的整数次方                 |                                                              |
| 14     | 调整数组顺序使奇数位于偶数前面 | 注意是否要求稳定排序                                         |
| 15     | 链表中倒数第k个结点            | 不要用dummy node！！！fast-slow指针法，fast指针先走k-1步，然后同时走，当fast到最后一个结点时，slow指向倒数第k个结点 |
| **16** | **反转链表**                   | 两个指针，prev=None, cur=head, 当cur不为None时循环；cur.next, prev, cur = prev, cur, cur.next，最后prev指向的正好是新的头结点 |
| 17     | 合并两个排序的链表             |                                                              |
| 18     | 树的子结构                     | 遍历 递归                                                    |
| 19     | 二叉树的镜像                   | 递归                                                         |
| 20     | 顺时针打印矩阵                 | 别慌                                                         |
| 21     | 包含min函数的栈                | 最小值辅助栈                                                 |
| 22     | 栈的压入、弹出序列             | 辅助栈                                                       |
| 23     | 从上往下打印二叉树             | 层次遍历，队列                                               |
| 24     | 二叉搜索树的后序遍历序列       | 后序遍历的最后一个数字是根节点的值，数组中前面的数字可以分为两部分：第一部分是左子树结点的值，它们都比根节点小；第二部分是右子树结点的值，它们都比根节点的值大 |
| **25** | **二叉树中和为某一值的路径**   | 前序遍历，保存路径的栈                                       |
| 26     | 复杂链表的复制                 |                                                              |
| 27     | 二叉搜索树与双向链表           | 中序遍历                                                     |
| 28     | 字符串的排列                   | 递归。首先求所有可能出现在第一个位置的字符，即把第一个字符和后面所有的字符交换；第二步固定第一个字符，求后面所有所有字符的排列 |
| 29     | 数组中出现次数超过一半的数字   |                                                              |
| **30** | **最小的K个数**                | 快速排序，时间复杂度O(n)；堆排序，时间复杂度O(nlogk)         |
| 31     | 连续子数组的最大和             |                                                              |
| 32     | 整数中1出现的次数              | 找规律，比较麻烦的题                                         |
| 33     | 把数组排成最小的数             | 先把数组中的整数转换成字符串，在函数cmp中定义比较规则，并根据规则用库函数list.sort()排序。lst = list(map(str, numbers))； lst.sort(cmp=lambda x, y: cmp(x+y, y+x)) |
| 34     | 丑数                           |                                                              |
| 35     | 第一个只出现一次的字符         |                                                              |
| **36** | **数组中的逆序对**             | 归并排序                                                     |
| **37** | **两个链表的第一个公共结点**   | 先遍历两个链表得到各自的长度，然后让长的那个先走一个长度差   |
| 38     | 数字在排序数组中出现的次数     | 二分查找，分别找到第一个k和最后一个k的位置，时间复杂度O(logn) |
| 39-1   | 二叉树的深度                   | 递归                                                         |
| 39-2   | 平衡二叉树                     | 后序遍历                                                     |
| 40     | 数组中只出现一次的数字         | 所有数字异或的结果数字的二进制表示中至少就有一位为1          |
| 41-1   | 和为S的连续正数序列            | 用两个数small和big分别表示序列的最小值和最大值。如果从small到big的序列的和大于s，从序列中去掉小的值，也就是增大small的值；如果从small到big的序列的和小于s，增大big，让这个序列包含更多的数字(small的边界是(1+S)/2) |
| 41-2   | 和为S的两个数字                | 两个指针，分别指向数组的第一个和最后一个，不断往中间移       |
| 42-1   | 左旋转字符串                   |                                                              |
| 42-2   | 翻转单词顺序列                 | 先翻转整个字符串，再翻转每个单词**(python字符串不能修改，要先转成list)** |
| 44     | 扑克牌顺子                     |                                                              |
| 45     | 圆圈中最后剩下的数             | 找规律，f(n,m) = 0, n = 1; f(n,m) = [f(n-1, m) + m] % n, n > 1 |
| 46     | 求1+2+3+...+n                  | 利用逻辑与的短路特性实现递归终止。其中： “or”运算符表示“或”，有一个为真则全部为真；前半部分判断出来是真的，后半部分就不再进行运算了。 “and”运算符表示“与”，前一项为假则整个表达式为假，因此可以利用这个性质进行递归运算或者达到整洁代码的目的。 |
| 47     | 不用加减乘除做加法             | 位运算, **n & 0xffffffff ????**                              |
| 49     | 把字符串转换成整数             |                                                              |
| 51     | 数组中重复的数字               |                                                              |
| 52     | 构建乘积数组                   |                                                              |
| 53     | 正则表达式匹配                 | **动态规划？？？**                                           |
| 54     | 表示数值的字符串               |                                                              |
| 55     | 字符流中第一个不重复的字符     |                                                              |
| **56** | **链表中环的入口结点**         | fast-slow指针，先判断是否有环，如果有，让slow=head           |
| 57     | 删除链表中重复的结点           |                                                              |
| 58     | 二叉树的下一个结点             |                                                              |
| 59     | 对称的二叉树                   |                                                              |
| 61     | 按之字形顺序打印二叉树         |                                                              |
| 60     | 把二叉树打印成多行             |                                                              |
| 62     | 序列化二叉树                   | 前序遍历                                                     |
| 63     | 数据流中的中位数               |                                                              |
| 64     | 数据流中的中位数               | 最大堆和最小堆                                               |
| 65     | 滑动窗口的最大值               |                                                              |
| 66     | 矩阵中的路径                   | 回溯法                                                       |
| 67     | 机器人的运动范围               | 回溯法                                                       |

