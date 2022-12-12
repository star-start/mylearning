# 安装：pip install pandas
# 注意：如果是anaconda则不需要安装
import pandas as pd

# Pandas中有两个比较重要的对象：DataFrame和Series
# DataFrame具体表现为一个二维的数据表；Series一般变现为一维数据列
# 也就是说，一个DataFrame是由一或多个Series构成的
# DataFrame的创建方法
df = pd.DataFrame({
        "Name": ["小明","大熊","张三",],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"]},
    index=['A','B','C']
)  # 键代表列名，列表代表这一列的值
print(df)
"""
  Name  Age     Sex
0   小明   22    male
1   大熊   35    male
2   张三   58  female
"""
# 注意：行索引（行名）在pandas中是 Index label
# 列索引（列名）在pandas中是 Columns label

# 从DataFrame中取出Series，使用属性或者字面量的语法都可以
names = df.Name  # 属性方式调用
print(names)
print(type(names))  # <class 'pandas.core.series.Series'>
"""
0    小明
1    大熊
2    张三
Name: Name, dtype: object
"""
ages = df['Age']
print(ages)
print('--------------------------------------------------')
# 从上面可以看出，Series实际上就是一个类似列表的序列，序列中的数据类型保持统一
# 另外还可以自己创建Series
al = pd.Series(['a','b','c'], index=['A','B','C'])
print(al)
df['alpha'] = al  # 将Series作为df新的一列
# df['alpha'] = ['a','b','c']  # 列表也可以
print(df)

print('--------------------------------------------------')
# Series和DataFrame的常用方法
# drop方法用于删除DataFrame或者Series中的内容
# 关于Axis的概念：表示轴，也就是数据结构有多少个维度
# 轴从0开始算，0轴就是第一个维度，对应DataFrame的行
# 1轴是第二个维度，对应DataFrame的列
# 删除行
# print(df.drop(0))  # DataFrame使用时，注意默认的axis=0
# print(df.drop(0, axis=0))  # 上面的代码就相当于这一行
print(df.drop('A', axis=0))
print(df.drop(['A', 'C']))  # 删除多行可以使用列表
# 删除列
print(df.drop('Name', axis=1))
print(df.drop(['alpha', 'Name'], axis=1))
print(df)  # 可以发现无论drop多少次都不会对原来的DataFrame产生影响
# 如果想要保留执行结果，可以赋值或者使用inplace
df1 = df.drop('A')
print(df1)
# 使用inplace就可以直接作用于原DataFrame
# df.drop('C', inplace=True)
# print(df)

print('--------------------------------------------------')
# 如果想要将Series作为新的一列传入DataFrame中，需要使用insert
al1 = pd.Series(['a','b','c'], index=['A','B','C'])
print(al1)
df.drop('alpha', axis=1, inplace=True)
print(df)
# 参数1：插入的索引
# 参数2：插入后的列名
# 参数3：插入的内容（Series或者是Array类型的数据）
col_len = len(df.columns)
df.insert(col_len, 'alpha', al1)  # insert是直接作用于DataFrame
print(df)
# 注意在为DataFarme添加一列时，无论是insert还是赋值语句，都需要注意
# DataFrame的索引和所添加的Series要保持一致

print('--------------------------------------------------')
# 其他方法
print("columns label：", df.columns)
print("columns label的列表：", df.columns.tolist())
print("index label：", df.index)
print("index label的列表：", df.index.tolist())
print("Series变为列表：", al1.tolist())

print('--------------------------------------------------')
# 统计方法
print("DataFrame的数值列统计信息：\n", df.describe())
print("查看年龄的最大值：", df['Age'].max())
print()
print("DataFrame的概括信息：")
print(df.info())

print('--------------------------------------------------')
# 在Series中还有一个非常重要的统计方法
s1 = pd.Series(['a','b','a','b','A','c','D'])
# 一个非常常见的场景：统计某一列中某个值出现的次数
res = s1.value_counts()
print(res)
print(type(res))  # <class 'pandas.core.series.Series'>