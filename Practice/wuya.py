"""
d,h=map(int,input().split())
s=3*(d/2)**2
num=(h+1)*s
print(int(num/8))




def num_stones(D, H):
    S = (D / 2) ** 2 * 3 * (H - 2)
    num = int(S / 8)
    # 返回石子个数
    return num

print(num_stones(10, 9))

def num_stones(D, H):
    # 根据圆的面积公式，计算容器底面积
    S1 = (D / 2) ** 2 * 3
    # 根据圆柱表面积公式，计算容器侧面积
    S2 = D / 2 * (H - 1.99) * 3
    # 根据圆柱侧面积公式，计算容器表面积
    S3 = 2 * S1 + S2
    # 根据石子体积为8，除以容器表面积的立方，向上取整，算出石子个数
    num = int(S3 / (8 ** (1)))
    # 返回石子个数
    return num

print(num_stones(10, 9))

"""





import math

d, depth = map(int, input().split())
r = d / 2
flag = depth - 1.99
v = r * r * 3 * flag
n = v / 8
# print(n)

print(math.ceil(n))