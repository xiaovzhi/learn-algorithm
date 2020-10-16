'''
leecode 70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''


'''
递推，从结果往前推导
第n层的总走法等于(n-1)层的总走法+(n-2)层的总走法
n-1到n，只需走一步，
n-2到n，只需走两步，如果走一步，那就变成了n-1的一种走法
n-1、n-2这样走，相当于各自原来的总走法增加了一步/两步，但走法数量不变，所以二者相加就是n的总走法
'''
def climbStairs(n):
    f = [0 for i in range(n+1)]
    f[1] = 1
    f[2] = 2

    for i in range(1,n+1):
        if i<=2:
            f[i] = i
        else:
            f[i] = f[i-1] + f[i-2]

    print(f[n])

def climbStairs1(n):    # 只使用三个变量完成递推
    first_step=1
    second_step=2

    final_step = 1

    for i in range(1,n+1):
        if i<=2:
            final_step = i
        else:
            final_step = first_step + second_step
            first_step = second_step
            second_step = final_step            

    print(final_step)

if __name__ == '__main__':
    climbStairs1(6)
