
# X & 1 == 1 or == 0 判断奇偶
x = 123
y = 456
print(x & 1, y & 1)

# X = X & (X-1) => 清零最低位的1
x = 7
print(x & (x-1))

# X & -X => 得到最低位的1
x = 9
print(x & -x)

# 将 x 最右边的 n 位清零  x & (~0 << n)
x = 255
n = 4
print(x & (~0 << n))

# 获取 x 的第 n 位值(0或者1)  (x >> n) & 1
x = 9
n = 2
print((x >> n) & 1)

# 获取 x 的第 n 位的冥值  x & (1 << (n - 1)) ??用途
x = 255
n = 1
print(x & (1 << (n - 1)))

# 仅将第 n 位置为 1    x | (1 << n)
x = 0b1110
n = 0
print(bin(x | (1 << n)))    # out 1111

# 仅将第 n 位置为 0    x & (~(1 << n))
x = 0b1110
n = 1
print(bin(x & (~(1 << n))))    # out 1100

# 将 x 最高位到第 n 位(含)清零 x & ((1 << n) - 1)
x = 255
n = 3
print(x & ((1 << n) - 1))   # out 7 0b00000111

# 将第 n 位到第零位(含)清零    x & (~((1 << (n + 1)) - 1))
x = 255
n = 6
print(x & (~((1 << (n + 1)) - 1)))  # out 128 0b10000000

# 高低位交换
x = 0x1234
x = (x >> 4) | (x << 4)
print(hex(y))

# 最后一位取反，例如(101101->101100) ，则为： x ^ 1
x = 0b111
print(bin(x ^ 1))

#②将右数第 n 位取反，例如 (101001->101101, n=2)，则为： x ^ (1 << n))
x = 0b101001
n = 1
print(bin(x ^ (1 << n)))

# 取右边连续的1，例如 (100101111->1111) ，则为：(x ^ (x+1)) >> 1
x = 0b1010011
print(bin((x ^ (x+1)) >> 1))

# 结合and运算，去掉右起第一个1的左边部分，例如(100101000->1000)，则为：x & (x ^ (x-1))
x = 0b100101000
print(bin(x & (x ^ (x-1))))
