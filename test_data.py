import pandas as pd

#准备一个字典（类似于excel的列名和数据）
data = {
    '月份': ['1月', '2月', '3月'],
    '产品A销售额': [10000, 15000, 12000],
    '产品B销售额': [8000, 9000, 11000]
}

#把字典变成pandas的dataframe
df = pd.DataFrame(data)

#打印出来
print(df)

#1.基础数据分析
#查看数据的基本信息（行列，列数，数据类型）

print(df.info())

#查看数据的统计描述（平均值，最大值，最小值，仅对数字列）
print(df.describe())

#查看前五行或者后五行的数据
print(df.head())
print(df.tail())

#计算每个月的总销售额（新增一列）
#2.简单的数据计算
df['总销售额']= df['产品A销售额'] + df['产品B销售额']

#计算所有月份的总销售额
total_sales = df['总销售额'].sum()
print (f'这三个月总销售额:{total_sales}')

#找出哪个月销售额最高
max_sales_month = df.loc[df['总销售额'].idxmax()]
print(f'销售额最高月份{max_sales_month["月份"]}')

#3.数据可视化
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# --- 数据准备（保持不变）---
# 先计算各个产品总销售额占比
sum_a = df['产品A销售额'].sum()
sum_b = df['产品B销售额'].sum()

# --- 开始拼图 ---
# 1. 创建一个大的画布，大小可以设大一点，比如宽18，高6
plt.figure(figsize=(18, 6))

# 2. 第一张图：折线图
# subplot(1, 3, 1) 的意思是：把画布分成 (1行, 3列)，我们要画在第 1 个位置
plt.subplot(1, 3, 1)
df.plot(x='月份', y=['产品A销售额', '产品B销售额','总销售额'], kind='line', title='3.1 趋势图',ax=plt.gca())
# 注意：pandas自带的plot会自动调用plt，所以这里不需要写plt.plot
# 注意：这里加了 ax=plt.gca() 是为了确保 Pandas 画在当前的 subplot 里，更加保险

# 3. 第二张图：柱状图
# subplot(1, 3, 2) 的意思是：在 (1行, 3列) 的第 2 个位置画
plt.subplot(1, 3, 2)
df.plot(x='月份', y=['产品A销售额', '产品B销售额','总销售额'], kind='bar', title='3.2 对比图',ax=plt.gca())

# 4. 第三张图：饼图
# subplot(1, 3, 3) 的意思是：在 (1行, 3列) 的第 3 个位置画
plt.subplot(1, 3, 3)
plt.pie([sum_a, sum_b], labels=['产品A', '产品B'], autopct='%1.1f%%', startangle=90)
plt.title('3.3 占比图')
plt.axis('equal')

# 5. 自动调整间距（防止标题重叠）
plt.tight_layout()

# 6. 最后只显示一次！
plt.show()
