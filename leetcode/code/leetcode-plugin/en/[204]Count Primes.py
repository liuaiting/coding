# coding=utf-8
#Count the number of prime numbers less than a non-negative number, n.
#
# Example: 
#
# 
#Input: 10
#Output: 4
#Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
#

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 厄拉多塞筛法
        # 具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
        # 第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
        # 现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……
        # 依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
        # 其实，当你要画圈的素数的平方大于n时，那么后面没有划去的数都是素数，就不用继续判了。
        # ---------------------
        # 作者：二当家的掌柜
        # 来源：CSDN
        # 原文：https://blog.csdn.net/github_39261590/article/details/73864039
        # 版权声明：本文为博主原创文章，转载请附上博文链接！

        if n < 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)


s = Solution()
print(s.countPrimes(10))
