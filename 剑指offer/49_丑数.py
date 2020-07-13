"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
示例:
    输入: n = 10
    输出: 12
    解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  
    1 是丑数。
    n 不超过1690。
"""


def nthUglyNumber(n):
    """
    遍历法
    超时
    :param n: int
    :return: int
    """
    def isUglyNumber(num):
        if num == 0:
            return False
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        if num > 2:
            return False
        else:
            return True

    tag = 0
    i = 1
    while tag < n:
        if isUglyNumber(i):
            tag += 1
        i += 1
    return i-1


def nthUglyNumber_2(n):
    """

    :param n: int
    :return: int
    """
    dp, a, b, c = [1] * n, 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2: a += 1
        if dp[i] == n3: b += 1
        if dp[i] == n5: c += 1
    return dp[-1]


print(nthUglyNumber_2(1069))
