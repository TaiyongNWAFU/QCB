#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author @caominghao
# Description @ hka_v2.py
# CreateTime @ 2024-06-13 16:36:49

import numpy as np
import pandas as pd
from scipy.stats import chi2

# 从CSV文件中读取数据
data = pd.read_csv('data.csv')

# 提取基因名称、多态性和分化数据
genes = data['gene'].values
polymorphism = data['polymorphism'].values
divergence = data['divergence'].values

# 初始化结果列表
p_values = []

# 计算总体期望值
mean_poly = np.mean(polymorphism)
mean_div = np.mean(divergence)
overall_exp = mean_poly / mean_div

# 对每个基因单独进行HKA检验
for i in range(len(polymorphism)):
    obs = polymorphism[i] / divergence[i]
    exp = overall_exp
    chi_square = ((obs - exp) ** 2) / exp
    p_value = chi2.sf(chi_square, df=1)  # 自由度为1
    p_values.append(p_value)

# 将P值结果写入新的CSV文件
result = pd.DataFrame({
    'gene': genes,
    'p_value': p_values
})

result.to_csv('p_values_with_genes.csv', index=False)

print('P值已成功计算并保存到 p_values_with_genes.csv 文件中')
# 注释
"""
解释
读取数据：

使用pandas库读取CSV文件中的数据。
提取基因名称、多态性和分化数据到genes、polymorphism和divergence数组中。
计算总体期望值：

计算所有基因的平均多态性和分化数据，并求得总体期望值。
逐基因计算P值：

对每个基因，计算其多态性与分化的比例（观察值）。
使用总体期望值作为期望值。
计算每个基因的卡方统计量和P值，并将结果存储在p_values列表中。
写入结果：

将结果写入一个新的CSV文件p_values_with_genes.csv，其中包含基因名称和对应的P值。
"""
