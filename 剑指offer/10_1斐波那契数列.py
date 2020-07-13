"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：
    输入：n = 2
    输出：1
示例 2：
    输入：n = 5
    输出：5
提示：
    0 <= n <= 100
"""


def fib(n):
    """
    递归
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)


def fib_2(n):
    """
    非递归
    :param n: int
    :return: int
    """
    res_list = [0, 1]
    if n < 2:
        return res_list[n]
    for i in range(2, n+1):
        res_list = [res_list[1], res_list[0]+res_list[1]]
    return res_list[1] % 1000000007

    """
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a % 1000000007
    """


print(fib_2(56))
